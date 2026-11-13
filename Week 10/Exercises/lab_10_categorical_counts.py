"""Reproduce the numerical calculations for Statistics 02323 Lab 10.

Run with: python3 lab_10_categorical_counts.py
Dependencies: NumPy and SciPy.
"""

import math

import numpy as np
from scipy import stats


def show(label: str, value: object) -> None:
    print(f"{label}: {value}")


def main() -> None:
    print("E7.1 - Passing proportions")
    x1, n1 = 82, 108
    x2, n2 = 104, 143
    p1, p2 = x1 / n1, x2 / n2
    difference = p1 - p2
    se_difference = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    ci_difference = (
        difference - stats.norm.ppf(0.975) * se_difference,
        difference + stats.norm.ppf(0.975) * se_difference,
    )
    show("  p1, p2", (p1, p2))
    show("  95% CI for p1-p2", ci_difference)
    show("  chi-square critical, df=1, alpha=.01", stats.chi2.ppf(0.99, 1))
    show("  failed-count mean, SD", (250 * 0.20, math.sqrt(250 * 0.20 * 0.80)))

    print("\nE7.2 - Outdoor lighting")
    observed = np.array([[18, 16], [70, 87], [22, 37]])
    country_totals = observed.sum(axis=0)
    equal_share = stats.chisquare(country_totals)
    homogeneity = stats.chi2_contingency(observed, correction=False)
    show("  Denmark/export totals", country_totals.tolist())
    show("  equal-share chi-square, p-value", (equal_share.statistic, equal_share.pvalue))
    show("  chi-square critical, df=2, alpha=.05", stats.chi2.ppf(0.95, 2))
    show("  variant-by-destination chi-square, p-value", (homogeneity.statistic, homogeneity.pvalue))

    print("\nE7.3 - Local elections")
    x, n, p0 = 168, 740, 0.295
    phat = x / n
    se_null = math.sqrt(p0 * (1 - p0) / n)
    z = (phat - p0) / se_null
    p_value = 2 * stats.norm.sf(abs(z))
    se_ci = math.sqrt(phat * (1 - phat) / n)
    ci = (phat - stats.norm.ppf(0.975) * se_ci, phat + stats.norm.ppf(0.975) * se_ci)
    show("  sample proportion, z statistic, two-sided p-value", (phat, z, p_value))
    show("  95% CI", ci)

    print("\nE7.4 - Sugar quality")
    xa, xb, na, nb = 6, 12, 50, 50
    pa, pb = xa / na, xb / nb
    pooled = (xa + xb) / (na + nb)
    se_pooled = math.sqrt(pooled * (1 - pooled) * (1 / na + 1 / nb))
    z = (pa - pb) / se_pooled
    p_value = 2 * stats.norm.sf(abs(z))
    show("  pA, pB, pooled proportion", (pa, pb, pooled))
    show("  z statistic, two-sided p-value", (z, p_value))
    phat = 36 / 200
    se_ci = math.sqrt(phat * (1 - phat) / 200)
    ci_99 = (phat - stats.norm.ppf(0.995) * se_ci, phat + stats.norm.ppf(0.995) * se_ci)
    show("  99% CI for 36/200", ci_99)

    print("\nE7.5 - Physical training")
    observed = np.array([[11, 27, 15], [14, 40, 30], [5, 23, 35]])
    expected = np.outer(observed.sum(axis=1), observed.sum(axis=0)) / observed.sum()
    contributions = (observed - expected) ** 2 / expected
    p_value = stats.chi2.sf(10.985, df=4)
    show("  expected count, Good job / Above-average training", expected[2, 2])
    show("  number of cells", observed.size)
    show("  cell (1,1) expected count and contribution", (expected[0, 0], contributions[0, 0]))
    show("  supplied chi-square statistic, df, p-value", (10.985, 4, p_value))


if __name__ == "__main__":
    main()
