"""Reproducible computations and plots for Statistics 02323 Lab 8."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf


HERE = Path(__file__).resolve().parent
ASSET_DIR = HERE / "Lab assets" if HERE.name == "3. Lab" else HERE
ASSET_DIR.mkdir(parents=True, exist_ok=True)


def summarize_fit(name, fit):
    print(f"\n=== {name} ===")
    print(fit.summary(slim=True))
    print(f"Residual SD s: {np.sqrt(fit.mse_resid):.6f}")


def save_scatter(data, x, y, title, filename):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.scatter(data[x], data[y], color="steelblue", edgecolor="black")
    fit = smf.ols(f"{y} ~ {x}", data=data).fit()
    x_line = np.linspace(data[x].min(), data[x].max(), 200)
    ax.plot(x_line, fit.params.iloc[0] + fit.params.iloc[1] * x_line, color="darkorange")
    labels = {
        "temperature": "Temperature (°C)",
        "lifetime": "Lifetime (hours)",
        "pressure": "Pressure",
        "flux": "Flux",
    }
    ax.set(title=title, xlabel=labels.get(x, x), ylabel=labels.get(y, y))
    ax.grid(alpha=0.2)
    fig.tight_layout()
    path = ASSET_DIR / filename
    fig.savefig(path, dpi=180)
    plt.close(fig)
    print(f"Plot saved: {path}")
    return fit


def print_prediction(fit, predictor, x0, alpha=0.05):
    result = fit.get_prediction(pd.DataFrame({predictor: [x0]})).summary_frame(alpha=alpha)
    print(f"Prediction at {predictor}={x0}:")
    print(result.to_string(index=False))
    return result


def exercise_5_1():
    print("\n=== Exercise 5.1: plastic film folding machine ===")
    print("(a) Choice 3: beta0=252, beta1=-0.9, sigma=3.6")
    print("(b) Choice 5: R-squared=0.96 and r=-0.98")
    print("Reason: downward, strong but not perfect linear trend; small residual scatter.")


def exercise_5_2():
    data = pd.DataFrame(
        {
            "temperature": [10, 20, 30, 40, 50, 60, 70, 80, 90],
            "lifetime": [420, 365, 285, 220, 176, 117, 69, 34, 5],
        }
    )
    fit = save_scatter(
        data,
        "temperature",
        "lifetime",
        "Device lifetime versus temperature",
        "lab_8_exercise_5_2.png",
    )
    summarize_fit("Exercise 5.2: lifetime model", fit)
    print("Slope 95% CI:", fit.conf_int(alpha=0.05).loc["temperature"].to_list())
    print("Slope p-value:", f"{fit.pvalues['temperature']:.9g}")


def exercise_5_3():
    data = pd.DataFrame(
        {"temperature": [0, 25, 50, 75, 100], "chemical_yield": [14, 38, 54, 76, 95]}
    )
    fit = smf.ols("chemical_yield ~ temperature", data=data).fit()
    summarize_fit("Exercise 5.3: chemical process yield", fit)
    print("95% CI for mean yield at 80 C:")
    print_prediction(fit, "temperature", 80)
    residuals = np.sort(fit.resid.to_numpy())
    rank = int(np.ceil(0.75 * len(residuals)))
    print("Sorted residuals:", residuals)
    print(f"Upper quartile using exercise rank rule (rank {rank}): {residuals[rank - 1]:.6f}")


def exercise_5_4():
    data = pd.DataFrame(
        {"cooling_time": [15, 25, 35, 40], "impact_strength": [42.1, 36.0, 31.8, 28.7]}
    )
    fit = smf.ols("impact_strength ~ cooling_time", data=data).fit()
    summarize_fit("Exercise 5.4: plastic material", fit)
    print("Slope 95% CI:", fit.conf_int(alpha=0.05).loc["cooling_time"].to_list())
    print("Slope p-value for H0: beta1=0:", f"{fit.pvalues['cooling_time']:.9g}")
    critical = stats.t.ppf(0.975, df=int(fit.df_resid))
    print(f"Acceptance range for the stated two-sided 5% test statistic: [{-critical:.6f}, {critical:.6f}]")


def exercise_5_5():
    data = pd.DataFrame(
        {"distance": [2, 4, 6, 8, 10], "concentration": [11.5, 10.2, 10.3, 9.68, 9.32]}
    )
    fit = smf.ols("concentration ~ distance", data=data).fit()
    summarize_fit("Exercise 5.5: water pollution", fit)
    print(f"Explained variation R-squared: {fit.rsquared:.6%}")
    print("95% CI for mean concentration at 7 km:")
    print_prediction(fit, "distance", 7)


def exercise_5_6():
    data = pd.DataFrame(
        {
            "pressure": [1.02, 2.08, 2.89, 4.01, 5.32, 5.83, 7.26, 7.96, 9.11, 9.99],
            "flux": [1.15, 0.85, 1.56, 1.72, 4.32, 5.07, 5.00, 5.31, 6.17, 7.04],
        }
    )
    fit = save_scatter(
        data,
        "pressure",
        "flux",
        "Membrane flux versus pressure",
        "lab_8_exercise_5_6.png",
    )
    summarize_fit("Exercise 5.6: membrane pressure drop", fit)
    print(f"Pearson correlation r: {data['pressure'].corr(data['flux']):.9f}")
    print("90% CI for slope:", fit.conf_int(alpha=0.10).loc["pressure"].to_list())
    print(f"Unexplained variation 1-R-squared: {1 - fit.rsquared:.6%}")
    print(f"Intercept p-value for H0: beta0=0: {fit.pvalues['Intercept']:.9f}")
    print("95% CI for mean flux at pressure 5:")
    print_prediction(fit, "pressure", 5)
    print("95% prediction interval for one new flux at pressure 5:")
    prediction = print_prediction(fit, "pressure", 5)
    print(
        f"[{prediction['obs_ci_lower'].iloc[0]:.6f}, "
        f"{prediction['obs_ci_upper'].iloc[0]:.6f}]"
    )


if __name__ == "__main__":
    exercise_5_1()
    exercise_5_2()
    exercise_5_3()
    exercise_5_4()
    exercise_5_5()
    exercise_5_6()
