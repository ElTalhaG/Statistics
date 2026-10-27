"""Runnable Python work for Statistics 02323 Lab 7 (Chapter 4)."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

try:
    import pandas as pd
except ModuleNotFoundError:
    pd = None


def exercise_4_1():
    print("\n=== Exercise 4.1: reliability / system lifetime ===")
    # The seed and draw order match the supplied solution PDF.
    np.random.seed(82719)
    k = 10_000
    component_data = {
        "Lifetime_A": stats.expon.rvs(scale=2, size=k),
        "Lifetime_B": stats.expon.rvs(scale=3, size=k),
        "Lifetime_C": stats.expon.rvs(scale=5, size=k),
    }
    if pd is not None:
        # The exercise asks for a DataFrame; use it whenever pandas is installed.
        df = pd.DataFrame(component_data)
        print("First three component lifetimes (months):")
        print(df.head(3).round(6))
        print("Component means (months):")
        print(df.mean().round(6))
        # A series system fails as soon as any component fails.
        df["Lifetime"] = df[["Lifetime_A", "Lifetime_B", "Lifetime_C"]].min(axis=1)
        lifetime = df["Lifetime"].to_numpy()
    else:
        # This fallback keeps the calculations runnable without pandas.
        component_matrix = np.column_stack(list(component_data.values()))
        print("First three component lifetimes (A, B, C; months):")
        print(np.round(component_matrix[:3], 6))
        print("Component means (A, B, C; months):")
        print(np.round(component_matrix.mean(axis=0), 6))
        lifetime = component_matrix.min(axis=1)

    figure, axis = plt.subplots(figsize=(8, 5))
    axis.hist(lifetime, bins=30, color="steelblue", edgecolor="black")
    axis.set(title="Simulated system lifetimes", xlabel="Lifetime (months)", ylabel="Devices")
    figure.tight_layout()
    image_path = Path(__file__).with_name("lab_7_system_lifetime_histogram.png")
    figure.savefig(image_path, dpi=180)
    plt.close(figure)

    print(f"System mean (months): {lifetime.mean():.6f}")
    print(f"System sample SD (months): {lifetime.std(ddof=1):.6f}")
    print(f"Estimated P(lifetime <= 1 month): {(lifetime <= 1).mean():.6f}")
    print(f"System median (months): {np.median(lifetime):.6f}")
    print(
        "System 10th percentile (months): "
        f"{np.quantile(lifetime, 0.1, method='averaged_inverted_cdf'):.6f}"
    )
    print(f"Histogram saved to: {image_path}")


def exercise_4_3():
    print("\n=== Exercise 4.3: bootstrap confidence intervals ===")
    x = np.array([38.43, 38.43, 38.39, 38.83, 38.45, 38.35, 38.43, 38.31, 38.32, 38.48, 38.50])
    n = len(x)
    k = 10_000
    np.random.seed(6287)
    print(f"n={n}, mean={x.mean():.6f}, sample SD={x.std(ddof=1):.6f}")

    # (a) Non-parametric bootstrap: resample observed values with replacement.
    bootstrap_means = np.array(
        [np.random.choice(x, n, replace=True).mean() for _ in range(k)]
    )
    print("(a) Non-parametric bootstrap 95% CI for mean:", np.quantile(bootstrap_means, [0.025, 0.975]))

    # (b) Parametric bootstrap under a fitted normal model.
    normal_means = np.array(
        [np.random.normal(x.mean(), x.std(ddof=1), n).mean() for _ in range(k)]
    )
    print("(b) Normal parametric bootstrap 95% CI for mean:", np.quantile(normal_means, [0.025, 0.975]))
    classical_t_ci = stats.t.interval(
        0.95,
        df=n - 1,
        loc=x.mean(),
        scale=x.std(ddof=1) / np.sqrt(n),
    )
    print("    Classical t-based 95% CI for comparison:", classical_t_ci)

    # (c) Parametric bootstrap under a fitted log-normal model.
    log_x = np.log(x)
    lognormal_means = np.array(
        [np.random.lognormal(log_x.mean(), log_x.std(ddof=1), n).mean() for _ in range(k)]
    )
    print("(c) Log-normal parametric bootstrap 95% CI for mean:", np.quantile(lognormal_means, [0.025, 0.975]))

    # (d) Simulate from the fitted normal model and record each sample's Q1.
    normal_q1 = np.array(
        [np.percentile(np.random.normal(x.mean(), x.std(ddof=1), n), 25) for _ in range(k)]
    )
    print("(d) Normal parametric bootstrap 95% CI for Q1:", np.quantile(normal_q1, [0.025, 0.975]))

    # (e) Resample the observed values and record each sample's Q1.
    nonparametric_q1 = np.array(
        [np.percentile(np.random.choice(x, n, replace=True), 25) for _ in range(k)]
    )
    print("(e) Non-parametric bootstrap 95% CI for Q1:", np.quantile(nonparametric_q1, [0.025, 0.975]))


def exercise_4_4():
    print("\n=== Exercise 4.4: two independent TV-rating samples ===")
    tv1 = np.array([1, 2, 1, 3, 2, 1, 2, 3, 1, 1])
    tv2 = np.array([3, 4, 2, 4, 2, 3, 2, 4, 3, 2])
    n1, n2 = len(tv1), len(tv2)
    difference = tv1.mean() - tv2.mean()
    k = 10_000
    print(f"Mean TV 1={tv1.mean():.3f}; mean TV 2={tv2.mean():.3f}; difference={difference:.3f}")

    # (a) Resample independently within each group; preserve group sizes.
    np.random.seed(98273)
    bootstrap_differences = np.array(
        [
            np.random.choice(tv1, n1, replace=True).mean()
            - np.random.choice(tv2, n2, replace=True).mean()
            for _ in range(k)
        ]
    )
    print("(a) Non-parametric bootstrap 95% CI for mean difference:", np.quantile(bootstrap_differences, [0.025, 0.975]))

    # (b) Welch allows the two population variances to differ.
    welch = stats.ttest_ind(tv1, tv2, equal_var=False)
    pooled = stats.ttest_ind(tv1, tv2)  # SciPy's default is equal_var=True.
    print("(b) Welch test:", welch)
    print("    Pooled test (SciPy default, shown to identify the distinction):", pooled)

    # (c) Parametric bootstrap from separately fitted normal distributions.
    parametric_differences = np.array(
        [
            np.random.normal(tv1.mean(), tv1.std(ddof=1), n1).mean()
            - np.random.normal(tv2.mean(), tv2.std(ddof=1), n2).mean()
            for _ in range(k)
        ]
    )
    print("(c) Normal parametric bootstrap 95% CI for mean difference:", np.quantile(parametric_differences, [0.025, 0.975]))


def exercise_4_5():
    print("\n=== Exercise 4.5: nonlinear error propagation ===")
    gas_constant = 8.31

    # (a) T = P*V/R; assume independent measurement errors.
    P, V = 240.48, 9.987
    sigma_P, sigma_V = 0.03, 0.002
    temperature = P * V / gas_constant
    sigma_temperature = np.sqrt(
        (V / gas_constant) ** 2 * sigma_P**2
        + (P / gas_constant) ** 2 * sigma_V**2
    )
    print(f"(a) T estimate={temperature:.6f} K; propagated SD={sigma_temperature:.6f} K")

    # (b) V = R*T/P; the minus sign in dV/dP disappears when squared.
    P, T = 240.48, 289.12
    sigma_P, sigma_T = 0.03, 0.02
    volume = gas_constant * T / P
    sigma_volume = np.sqrt(
        (gas_constant / P) ** 2 * sigma_T**2
        + (-gas_constant * T / P**2) ** 2 * sigma_P**2
    )
    print(f"(b) V estimate={volume:.6f} L; propagated SD={sigma_volume:.6f} L")

    # (c) P = R*T/V.
    V, T = 9.987, 289.12
    sigma_V, sigma_T = 0.002, 0.02
    pressure = gas_constant * T / V
    sigma_pressure = np.sqrt(
        (gas_constant / V) ** 2 * sigma_T**2
        + (-gas_constant * T / V**2) ** 2 * sigma_V**2
    )
    print(f"(c) P estimate={pressure:.6f} kPa; propagated SD={sigma_pressure:.6f} kPa")

    # (d) Simulate the independent normal measurement errors in part (c).
    np.random.seed(28973)
    k = 10_000
    simulated_V = np.random.normal(9.987, 0.002, k)
    simulated_T = np.random.normal(289.12, 0.02, k)
    simulated_P = gas_constant * simulated_T / simulated_V
    print(f"(d) Simulated P mean={simulated_P.mean():.6f} kPa")
    print(f"    Simulated P sample SD={simulated_P.std(ddof=1):.6f} kPa")
    print("    Compare the simulated SD with part (c)'s first-order estimate above.")


if __name__ == "__main__":
    exercise_4_1()
    exercise_4_3()
    exercise_4_4()
    exercise_4_5()
