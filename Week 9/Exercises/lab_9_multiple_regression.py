"""Reproducible Statistics 02323 Lab 9 (Chapter 6) regression work."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf


HERE = Path(__file__).resolve().parent
ASSET_DIR = HERE / "Lab assets" if HERE.name == "3. Lab" else HERE
ASSET_DIR.mkdir(parents=True, exist_ok=True)


def nitrate_model():
    print("\n=== Exercise 6.1: nitrate concentration ===")
    print("Published model output: n=240, df=237, R-squared=0.3438")
    print("beta0=-2.365 (SE 0.222), beta1=0.4762 (SE 0.062), beta2=0.0827 (SE 0.070)")
    print("95% CIs: beta0 [-2.802,-1.928], beta1 [0.354,0.598], beta2 [-0.055,0.221]")
    print("p-values: intercept <0.0005, loading <0.0005, runoff 0.237")
    print("The source provides only the summary table, not the 240-row dataset; no refit or residual diagnostics are possible here.")


def exercise_6_2():
    data = pd.DataFrame(
        {
            "x1": [0.58, 0.86, 0.29, 0.20, 0.56, 0.28, 0.08, 0.41, 0.22, 0.35, 0.59, 0.22, 0.26, 0.12, 0.65, 0.70, 0.30, 0.70, 0.39, 0.72, 0.45, 0.81, 0.04, 0.20, 0.95],
            "x2": [0.71, 0.13, 0.79, 0.20, 0.56, 0.92, 0.01, 0.60, 0.70, 0.73, 0.13, 0.96, 0.27, 0.21, 0.88, 0.30, 0.15, 0.09, 0.17, 0.25, 0.30, 0.32, 0.82, 0.98, 0.00],
            "y": [1.45, 1.93, 0.81, 0.61, 1.55, 0.95, 0.45, 1.14, 0.74, 0.98, 1.41, 0.81, 0.89, 0.68, 1.39, 1.53, 0.91, 1.49, 1.38, 1.73, 1.11, 1.68, 0.66, 0.69, 1.98],
        }
    )
    full = smf.ols("y ~ x1 + x2", data=data).fit()
    reduced = smf.ols("y ~ x1", data=data).fit()
    print("\n=== Exercise 6.2(a): full model ===")
    print(full.summary(slim=True))
    print(f"Residual variance estimate: {full.scale:.8f}")
    print("95% coefficient intervals:\n", full.conf_int())
    print("\n=== Exercise 6.2(b): reduced model after removing x2 ===")
    print(reduced.summary(slim=True))
    print(f"Reduced-model residual SD: {np.sqrt(reduced.mse_resid):.6f}")

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    sm.qqplot(reduced.resid, line="q", ax=axes[0])
    axes[0].set_title("Reduced model: normal Q-Q")
    axes[1].scatter(reduced.fittedvalues, reduced.resid, edgecolor="black", alpha=0.85)
    axes[1].axhline(0, color="firebrick", linestyle="--")
    axes[1].set(title="Residuals versus fitted", xlabel="Fitted response", ylabel="Residual")
    fig.tight_layout()
    diagnostics_path = ASSET_DIR / "lab_9_exercise_6_2_diagnostics.png"
    fig.savefig(diagnostics_path, dpi=180)
    plt.close(fig)
    print(f"Diagnostic plots saved: {diagnostics_path}")

    x_grid = np.linspace(0, 1, 200)
    prediction = reduced.get_prediction(pd.DataFrame({"x1": x_grid})).summary_frame(alpha=0.05)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(data["x1"], data["y"], color="steelblue", edgecolor="black", label="Observed data")
    ax.plot(x_grid, prediction["mean"], color="firebrick", label="Reduced-model fitted mean")
    ax.fill_between(x_grid, prediction["mean_ci_lower"], prediction["mean_ci_upper"], color="firebrick", alpha=0.22, label="95% CI for mean")
    ax.fill_between(x_grid, prediction["obs_ci_lower"], prediction["obs_ci_upper"], color="seagreen", alpha=0.16, label="95% prediction interval")
    ax.set(xlabel="$x_1$", ylabel="$y$", title="Reduced model with 95% intervals")
    ax.legend()
    ax.grid(alpha=0.2)
    fig.tight_layout()
    interval_path = ASSET_DIR / "lab_9_exercise_6_2_intervals.png"
    fig.savefig(interval_path, dpi=180)
    plt.close(fig)
    print(f"Line and intervals plot saved: {interval_path}")
    print("Exam item 6.2(e): statement 3 is false; prediction intervals vary in width with x1.")


if __name__ == "__main__":
    nitrate_model()
    exercise_6_2()
