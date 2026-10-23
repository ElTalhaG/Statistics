# Lab 6 - Comparing two samples and paired measurements

Exercises: 3.5(a)-(e), 3.6(a), 3.7(a)-(b), 3.8(a)-(b), and 3.9(a)-(c). Based on [[statistics_exercises_ch3_solution.pdf|the uploaded Chapter 3 solutions]], printed pages 17-21 and 24-35. Results below follow the source's rounding where appropriate; direct calculation from raw data can change the last decimal.

| Exercise | Setting | Method |
|---|---|---|
| 3.5: transport firms | Two independent groups | Welch two-sample $t$ test and interval; two-sample power calculations |
| 3.6: cholesterol | Same patients before and after | Paired $t$ test on patient differences |
| 3.7: pulse | Same runners at two times | Mean-drop interval on paired differences; standard-deviation interval on end pulses |
| 3.8: foil | Maximum and minimum on the same foil | One-sample inference on paired thickness differences |
| 3.9: course project | Two different student groups | Welch test and interval; standard-deviation interval for the after group |

**TI-30XB:** use it for averages, sample standard deviations, square roots, standard errors, test statistics, and interval arithmetic. Use the statistical quantiles/probabilities shown here, a statistical table, or Python for $t$ and chi-square distribution values. Exact power calculations require statistical software.

Optional Python setup for the snippets:

```python
import numpy as np
from scipy import stats
from statsmodels.stats.power import TTestIndPower
```

## Exercise 3.5 - Transport times

Given independent samples of 9 deliveries from each firm:

$$\bar{x}_A=1.93,\quad s_A=0.45,\qquad
\bar{x}_B=1.49,\quad s_B=0.58\quad\text{(days)}.$$

Assume normal populations. Define the difference as $\delta=\mu_A-\mu_B$; a positive difference means Firm A takes longer.

### 3.5 a) Welch test of equal mean delivery times

**1. State the hypotheses.**

$$H_0:\mu_A-\mu_B=0,\qquad H_1:\mu_A-\mu_B\ne0.$$

**2. Find the estimated difference and its standard error.**

$$\hat{\delta}=\bar{x}_A-\bar{x}_B=1.93-1.49=0.44\text{ days},$$
$$SE=\sqrt{\frac{s_A^2}{n_A}+\frac{s_B^2}{n_B}}
=\sqrt{\frac{0.45^2}{9}+\frac{0.58^2}{9}}
\approx0.2447\text{ days}.$$

**3. Calculate the statistic.**

$$t_{\mathrm{obs}}=\frac{\hat{\delta}-0}{SE}
=\frac{0.44}{0.2447}\approx1.80.$$

**4. Calculate Welch's degrees of freedom.** We do not need to assume equal population variances:

$$\nu=
\frac{(s_A^2/n_A+s_B^2/n_B)^2}
{(s_A^2/n_A)^2/(n_A-1)+(s_B^2/n_B)^2/(n_B-1)}
$$
$$=
\frac{(0.45^2/9+0.58^2/9)^2}
{(0.45^2/9)^2/8+(0.58^2/9)^2/8}
\approx15.07.$$

The source rounds this to about 15 degrees of freedom.

**5. Find the two-sided p-value and compare with $\alpha=0.05$.**

$$p=2P(T_\nu\ge|1.80|)\approx0.092.$$

Python with the source's rounded inputs: `2 * stats.t.sf(1.8, df=15)`.

Since $0.092>0.05$, $\boxed{\text{do not reject }H_0}$. The observed mean for A is 0.44 days longer, but the source describes the evidence as weak, and the data do not establish a population mean difference at the 5% level. This does not prove that the firms have equal mean delivery times.

For the direct test requested in the exercise:

```python
A = np.array([2.20, 1.58, 2.41, 2.49, 1.15, 1.46, 2.12, 1.91, 2.05])
B = np.array([0.97, 1.07, 1.02, 1.34, 2.33, 0.88, 2.09, 2.24, 1.47])
stats.ttest_ind(A, B, equal_var=False)
# t = 1.79829; p = 0.09219; df = 15.0693
```

`equal_var=False` selects Welch's test.

### 3.5 b) 95% confidence interval for $\mu_A-\mu_B$

Use the difference, standard error, and degrees of freedom from part (a):

$$\hat{\delta}\pm t_{0.975,\nu}SE.$$

The source uses $t_{0.975,15}=2.131$:

$$0.44\pm2.131\sqrt{0.45^2/9+0.58^2/9}
\approx0.44\pm0.522.$$

**Source-rounded answer:** $\boxed{[-0.082,\ 0.962]\text{ days}}$. Using unrounded statistics from the raw data gives approximately $[-0.0813,0.9613]$ days.

Zero lies inside the interval, agreeing with the test decision. A negative possible difference means A could be faster; a positive difference means A could be slower.

Python: `stats.ttest_ind(A, B, equal_var=False).confidence_interval(0.95)`.

### 3.5 c) Power with 9 observations per firm

Power is the probability of rejecting the equal-means hypothesis when the specified true mean difference actually exists. Here the assumed true difference is 0.4 days and the planning standard deviation is 0.5 days for each population:

$$d=\frac{|\mu_A-\mu_B|}{\sigma}=\frac{0.4}{0.5}=0.8.$$

For a two-sided test with 9 observations per firm and $\alpha=0.05$, use:

```python
TTestIndPower().solve_power(
    effect_size=0.8, nobs1=9, alpha=0.05,
    ratio=1, alternative="two-sided"
)
# 0.35794895
```

**Answer:** $\boxed{\text{power}\approx0.358}$, or about 36%. If the true mean difference is 0.4 days under these planning assumptions, this study detects it only about 36% of the time; it misses it about 64% of the time.

**TI-30XB:** calculating $d=0.8$ is straightforward, but the power calculation involves a noncentral $t$ distribution and is not convenient on this calculator. Use the supplied Python result.

### 3.5 d) Effect size detectable with 80% power

Keep $n_A=n_B=9$ and $\alpha=0.05$, but now ask the software to solve for the effect size:

```python
d = TTestIndPower().solve_power(
    nobs1=9, alpha=0.05, power=0.80,
    ratio=1, alternative="two-sided"
)
# d = 1.40692
```

**Standardized effect-size answer:** $\boxed{d\approx1.40692}$.

Convert this to an actual mean difference using $\sigma=0.5$:

$$|\mu_A-\mu_B|=d\sigma=1.40692(0.5)
=0.70346\text{ days}.$$

**Interpretation:** with 9 deliveries per firm, a true difference of about $\boxed{0.70\text{ days}}$ is needed for 80% power under these assumptions.

### 3.5 e) Sample size needed for 90% power

The question asks for a 0.4-day difference, $\sigma=0.5$, $\alpha=0.05$, and power 0.90. Again, $d=0.8$. Solve for the number in one group:

```python
n = TTestIndPower().solve_power(
    effect_size=0.8, alpha=0.05, power=0.90,
    ratio=1, alternative="two-sided"
)
# 33.8255
```

A sample size must be an integer, and rounding down would not reach the requested power:

$$n_A=n_B=\lceil33.8255\rceil=\boxed{34}.$$

**Answer:** collect at least $\boxed{34\text{ deliveries from each firm}}$, or 68 in total.

**Source correction:** the PDF's printed command says `power=0.80`, although the question and the displayed result 33.8255 correspond to 90% power. Use `power=0.90` as above. With 80% power the result would instead be about 25.52, rounded up to 26 per firm.

---

## Exercise 3.6 - Cholesterol

The same 15 patients are measured before treatment and three weeks later. Therefore the measurements are paired by patient.

### 3.6 a) Choose the correct calculation and assess the decrease

**1. Choose the paired test.** Calculation 3, `stats.ttest_rel(x1, x2)`, is appropriate. Calculations 1 and 2 treat the two sets of measurements as independent groups, which does not match these data.

**2. Define a positive drop.**

$$D_i=\text{Before}_i-\text{After}_i.$$

The differences are:

$$0.9,\ 1.6,\ 1.1,\ 1.5,\ 1.6,\ 2.1,\ 1.2,\ -0.1,\ 1.6,\ -0.2,\ 1.1,\ 1.5,\ 1.3,\ 1.9,\ 1.1.$$

The paired test is a one-sample test on these 15 differences. From the data:

$$\bar D=1.21333,\quad s_D=0.64016,\quad
SE_D=\frac{0.64016}{\sqrt{15}}=0.16529
\quad\text{(mmol/L)}.$$

**3. Compute the statistic for a zero mean change.**

$$t_{\mathrm{obs}}=\frac{\bar D-0}{s_D/\sqrt{15}}
=\frac{1.21333}{0.16529}=7.34065,\qquad df=14.$$

**4. Use the p-value given by calculation 3.** The source uses a two-sided paired test of $H_0:\mu_D=0$ versus $H_1:\mu_D\ne0$:

$$p=3.67225\times10^{-6}\approx0.0000037.$$

Since this is much smaller than $\alpha=0.001$, reject the zero-change hypothesis. The estimated change is positive under our before-minus-after definition.

**Answer:** $\boxed{\text{Calculation 3 is correct; the mean cholesterol level decreased significantly.}}$ The estimated decrease is about 1.213 mmol/L, and the source describes the evidence as very strong.

If a one-sided decrease test is specified in advance, use $H_1:\mu_D>0$; its p-value is half the source's two-sided p-value, about $1.836\times10^{-6}$, with the same conclusion:

`stats.ttest_rel(x1, x2, alternative="greater")`, where `x1` is before and `x2` is after.

**TI-30XB:** first calculate each patient's difference, then use 1-variable statistics on the differences to get $\bar D$ and sample $s_D$. Do not combine the separate before and after standard deviations as if the measurements were independent.

---

## Exercise 3.7 - Pulse

The same 13 runners are measured at the end of exercise and one minute later. A drop is $D_i=\text{Pulse end}_i-\text{Pulse 1 minute}_i$.

Given:

$$n=13,\quad\bar D=54.46,\quad s_D=5.768,\quad
s_{\mathrm{end}}=5.190\quad\text{(beats/minute)}.$$

### 3.7 a) 99% confidence interval for the mean pulse drop

**1. Use the paired differences.** Their mean and standard deviation give:

$$SE_D=\frac{s_D}{\sqrt n}=\frac{5.768}{\sqrt{13}}
\approx1.5998\text{ beats/minute}.$$

**2. Choose the correct supplied quantile.** For 99% confidence, $\alpha=0.01$, so each tail contains 0.005 and the upper quantile is $0.995$, not $0.99$:

$$t_{0.995,12}=3.055.$$

**3. Substitute into the interval.**

$$\bar D\pm t_{0.995,12}\frac{s_D}{\sqrt n}
=54.46\pm3.055\frac{5.768}{\sqrt{13}}
\approx54.46\pm4.887.$$

**Source-rounded answer:** $\boxed{[49.57,\ 59.35]\text{ beats/minute}}$. This estimates the population mean drop over that minute. It is not an interval containing 99% of individual runners' drops.

**TI-30XB:** all needed values are supplied. Calculate `5.768 / sqrt(13)`, multiply by `3.055`, then subtract from and add to `54.46`.

### 3.7 b) 95% confidence interval for the standard deviation of end pulses

This question concerns the first row of measurements, so use $s_{\mathrm{end}}=5.190$, not $s_D$.

For normal observations:

$$CI_\sigma=
\left[\sqrt{\frac{(n-1)s_{\mathrm{end}}^2}{\chi^2_{0.975,n-1}}},
\sqrt{\frac{(n-1)s_{\mathrm{end}}^2}{\chi^2_{0.025,n-1}}}\right].$$

Here $df=12$ and the numerator is:

$$12(5.190)^2\approx323.2.$$

The source gives $\chi^2_{0.975,12}\approx23.34$ and $\chi^2_{0.025,12}\approx4.404$. Therefore:

$$CI_\sigma=
\left[\sqrt{\frac{323.2}{23.34}},\
\sqrt{\frac{323.2}{4.404}}\right]
\approx\boxed{[3.72,\ 8.57]\text{ beats/minute}}.$$

Python quantiles: `stats.chi2.ppf(0.975, df=12)` and `stats.chi2.ppf(0.025, df=12)`.

**Exam reminder:** the larger chi-square quantile is used in the denominator of the lower endpoint. Take square roots because the question asks for standard deviation, not variance.

---

## Exercise 3.8 - Foil production

For each of 10 foils, maximum and minimum thickness are measured on the same foil. Define:

$$D_i=\text{Maximum}_i-\text{Minimum}_i.$$

The observed differences, in mm, are:

$$0.48,\ 0.32,\ 0.32,\ 0.33,\ 0.39,\ 0.34,\ 0.38,\ 0.36,\ 0.57,\ 0.56.$$

Given $\bar D=0.405$ mm and $s_D=0.09664$ mm. Model the differences as independent normal observations across foils.

### 3.8 a) 95% confidence interval for the mean difference

Calculate the standard error:

$$SE_D=\frac{0.09664}{\sqrt{10}}\approx0.03056\text{ mm}.$$

With $df=9$, the upper critical value is $t_{0.975,9}=2.262$. Then:

$$\bar D\pm t_{0.975,9}SE_D
=0.405\pm2.262(0.03056)
\approx0.405\pm0.06913.$$

**Answer:** $\boxed{[0.3359,\ 0.4741]\text{ mm}}$, or about $[0.336,0.474]$ mm.

The requested direct Python interval can be computed from the differences or from paired maximum/minimum arrays:

```python
D = np.array([0.48, 0.32, 0.32, 0.33, 0.39, 0.34, 0.38, 0.36, 0.57, 0.56])
stats.ttest_1samp(D, popmean=0).confidence_interval(0.95)
# low = 0.335869; high = 0.474131
# Equivalent: stats.ttest_rel(maximum, minimum).confidence_interval(0.95)
```

### 3.8 b) Test whether the mean difference differs from 0.35 mm

The question asks for a difference in either direction, so use:

$$H_0:\mu_D=0.35,\qquad H_1:\mu_D\ne0.35.$$

The test statistic is:

$$t_{\mathrm{obs}}=\frac{0.405-0.35}{0.09664/\sqrt{10}}
=\frac{0.055}{0.03056}\approx1.80.$$

With $df=9$, the two-sided p-value is:

$$p=2P(T_9\ge1.80)\approx0.105.$$

Python: `stats.ttest_1samp(D, popmean=0.35)` gives $t\approx1.79976$ and $p\approx0.10543$.

Since $0.10543>0.05$, $\boxed{\text{do not reject }H_0}$. The source concludes there is little or no evidence that the population mean difference differs from 0.35 mm. This agrees with the 95% interval containing 0.35.

Use a one-sample test on the paired differences with `popmean=0.35`, because the ordinary paired-test command tests a mean difference of zero.

**Interpretation:** this test does not demonstrate that the stability requirement $\mu_D\le0.35$ is satisfied. It says the sample does not establish a difference from 0.35 in the two-sided test asked for.

---

## Exercise 3.9 - Course project

The before and after groups contain different students, so treat them as independent samples. The data for mean-grade inference are:

| Group | $n$ | Sample mean | Sample standard deviation |
|---|---:|---:|---:|
| Before | 50 | 6.420 | 2.205 |
| After | 24 | 7.375 | 1.813 |

Assume approximately normal grades within each group. Define $\delta=\mu_{\mathrm{Before}}-\mu_{\mathrm{After}}$. The failed-student counts are not needed for the mean-grade questions below.

### 3.9 a) Welch test for a population mean-grade difference

**1. State the hypotheses.**

$$H_0:\mu_{\mathrm{Before}}-\mu_{\mathrm{After}}=0,\qquad
H_1:\mu_{\mathrm{Before}}-\mu_{\mathrm{After}}\ne0.$$

**2. Find the estimated difference and its standard error.**

$$\hat{\delta}=6.420-7.375=-0.955,$$
$$SE=\sqrt{\frac{2.205^2}{50}+\frac{1.813^2}{24}}
=\sqrt{0.0972405+0.1369570}
\approx0.48394.$$

**3. Calculate the statistic and Welch degrees of freedom.**

$$t_{\mathrm{obs}}=\frac{-0.955}{0.48394}\approx-1.9734,$$
$$\nu=
\frac{(0.0972405+0.1369570)^2}
{0.0972405^2/49+0.1369570^2/23}
\approx54.386.$$

**4. Calculate the two-sided p-value.**

$$p=2P(T_{54.386}\ge1.9734)\approx0.0535.$$

The source reports about 0.0536 using rounded inputs. Since $p>0.05$, $\boxed{\text{do not reject }H_0}$. The observed after-group mean is 0.955 grade points higher, but the data do not establish a population mean difference at the 5% level.

A direct calculation from the provided summaries is:

```python
stats.ttest_ind_from_stats(
    mean1=6.420, std1=2.205, nobs1=50,
    mean2=7.375, std2=1.813, nobs2=24,
    equal_var=False
)
# t = -1.97339; p = 0.05354
```

### 3.9 b) 99% confidence interval for the mean-grade difference

Use the same difference, standard error, and Welch degrees of freedom:

$$CI_\delta=\hat{\delta}\pm t_{0.995,\nu}SE.$$

Python gives $t_{0.995,54.386}\approx2.6693$:

$$-0.955\pm2.6693(0.48394)
\approx-0.955\pm1.2918.$$

**Answer:** $\boxed{[-2.247,\ 0.337]\text{ grade points}}$ for $\mu_{\mathrm{Before}}-\mu_{\mathrm{After}}$.

The interval contains zero. It allows either a higher population mean after introduction (negative before-minus-after difference) or a slightly higher mean before introduction (positive difference). Do not reverse the signs without also changing the defined order of the difference.

Python quantile: `stats.t.ppf(0.995, df=54.3859)`.

### 3.9 c) 95% confidence interval for the after-group standard deviation

Use only the after group: $n=24$, $s=1.813$, and $df=23$. The chi-square numerator is:

$$ (n-1)s^2=23(1.813)^2\approx75.6007.$$

The source gives $\chi^2_{0.975,23}\approx38.076$ and $\chi^2_{0.025,23}\approx11.689$. Thus:

$$CI_\sigma=
\left[\sqrt{\frac{75.6007}{38.076}},\
\sqrt{\frac{75.6007}{11.689}}\right]
\approx\boxed{[1.41,\ 2.54]\text{ grade points}}.$$

This interval estimates the population standard deviation of grades after introducing the project. It concerns the spread of individual grades, whereas the standard error in parts (a)-(b) concerns uncertainty in the difference of group means.

Python quantiles: `stats.chi2.ppf(0.975, df=23)` and `stats.chi2.ppf(0.025, df=23)`.

**TI-30XB:** square 1.813, multiply by 23, divide separately by each supplied quantile, and take the square root of each result.
