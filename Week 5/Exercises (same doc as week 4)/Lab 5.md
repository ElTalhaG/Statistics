# Lab 5 - Hypothesis testing

Exercises: 3.4(a)-(d) and 3.12(a)-(e). Based on [[statistics_exercises_ch3_solution.pdf|the uploaded Chapter 3 solutions]], printed pages 13-15 and 48-52.

For a two-sided one-sample test of a normal population with unknown standard deviation:

$$H_0:\mu=\mu_0,\qquad H_1:\mu\ne\mu_0,$$
$$SE=\frac{s}{\sqrt n},\qquad t_{\mathrm{obs}}=\frac{\bar{x}-\mu_0}{SE},\qquad df=n-1.$$

Under $H_0$, compare the observed statistic with a $t$ distribution:

$$p=2P(T_{df}\ge |t_{\mathrm{obs}}|).$$

Reject $H_0$ when $p\le\alpha$. A large p-value means the data do not provide enough evidence to reject $H_0$; it does not prove that $H_0$ is true. The p-value is calculated assuming $H_0$ and is not the probability that $H_0$ is true.

**TI-30XB:** use the calculator for sample statistics, square roots, standard errors, and test statistics. For $t$ probabilities and quantiles, use the supplied values, a statistical table, or the short Python commands below. They cannot conveniently be obtained directly on the TI-30XB. Python snippets use `import numpy as np` and `from scipy import stats`.

## Exercise 3.4 - Aluminum profile

Given $n=16$, $\bar{x}=180.05$ mm, and $s=0.0959$ mm. Assume independent observations from a normal population. The target population mean is 180 mm.

### 3.4 a) Test statistic, p-value, and interpretation

**1. State the hypotheses.** The question asks whether the mean differs from 180 mm in either direction:

$$H_0:\mu=180,\qquad H_1:\mu\ne180.$$

**2. Calculate the standard error.**

$$SE=\frac{0.0959}{\sqrt{16}}=\frac{0.0959}{4}=0.023975\text{ mm}.$$

**3. Calculate the test statistic.**

$$t_{\mathrm{obs}}=\frac{180.05-180}{0.023975}
=\frac{0.05}{0.023975}\approx2.085.$$

The observed sample mean is about 2.085 estimated standard errors above the null value.

**4. Find the two-sided p-value using $df=16-1=15$.**

$$p=P(T_{15}\le-2.085)+P(T_{15}\ge2.085)
=2P(T_{15}\ge2.085)\approx0.0546.$$

Python: `2 * stats.t.sf(abs(2.085), df=15)`.

**Answer:** $\boxed{t_{\mathrm{obs}}\approx2.085,\quad p\approx0.0546}$. If the true mean is 180 mm, a statistic this far from zero or farther in either direction occurs with probability about 5.46%. The source describes this as weak evidence against $H_0$.

The exercise also asks for a direct test from the raw data:

```python
x = np.array([180.02, 180.00, 180.01, 179.97, 179.92, 180.05,
              179.94, 180.10, 180.24, 180.12, 180.13, 180.22,
              179.96, 180.10, 179.96, 180.06])
stats.ttest_1samp(x, popmean=180)
# t = 2.0851; two-sided p = 0.05456
```

### 3.4 b) Critical values at the 1% significance level

For a two-sided test with $\alpha=0.01$, each rejection tail has probability $\alpha/2=0.005$. The critical values are:

$$\pm t_{0.995,15}=\boxed{\pm2.94671}.$$

Python: `stats.t.ppf(0.995, df=15)`; the lower critical value is its negative.

Reject $H_0$ if $t_{\mathrm{obs}}<-2.94671$ or $t_{\mathrm{obs}}>2.94671$. Here $2.085$ is between the critical values, so **do not reject $H_0$ at 1%**. This also follows from $p=0.0546>0.01$.

### 3.4 c) 99% confidence interval for the mean

Use the critical value from part (b):

$$\bar{x}\pm t_{0.995,15}\frac{s}{\sqrt n}
=180.05\pm2.94671(0.023975).$$

The margin of error is about $0.07066$ mm, giving:

$$\boxed{\mu\in[179.9793,\ 180.1207]\text{ mm}}
\approx[179.98,\ 180.12]\text{ mm}.$$

The interval contains 180 mm, consistent with not rejecting that mean at the 1% level. Over repeated sampling, 99% of intervals constructed this way would contain the population mean.

### 3.4 d) Carry out the test at the 5% significance level

The hypotheses, statistic, and p-value are the same as in part (a). Compare the p-value with the new significance level:

$$0.0546>0.05.$$

**Conclusion:** $\boxed{\text{Do not reject }H_0\text{ at }5\%.}$ There is insufficient evidence that the population mean differs from 180 mm. Being close to 0.05 does not change the rule, and failure to reject does not establish that the mean is exactly 180 mm.

---

## Exercise 3.12 - Concrete items 2: hypothesis testing

The nine observed lengths, in mm, are:

$$3003,\ 3005,\ 2997,\ 3006,\ 2999,\ 2998,\ 3007,\ 3005,\ 3001.$$

Use the statistics calculated from these actual measurements:

$$n=9,\qquad \bar{x}=3002.3333,\qquad s^2=13.75,$$
$$s=\sqrt{13.75}=3.70810,\qquad SE=\frac{3.70810}{3}=1.23603\text{ mm}.$$

For clarity, $\sum(x_i-\bar{x})^2=110$, so $s^2=110/8$. The stated 3 mm standard deviation is a target; this test estimates the unknown standard deviation using $s$.

### 3.12 a) Test the mean at the 5% significance level

**1. State the hypotheses.**

$$H_0:\mu=3000,\qquad H_1:\mu\ne3000.$$

**2. Calculate the statistic.**

$$t_{\mathrm{obs}}=\frac{3002.3333-3000}{3.70810/\sqrt9}
=\frac{2.3333}{1.23603}\approx1.88776.$$

**3. Use a two-sided $t$ probability with $df=8$.**

$$p=2P(T_8\ge1.88776)\approx0.09576.$$

The source's rounded calculation uses $t=1.885$ and reports $p=0.0961$; using all raw measurements gives $t\approx1.88776$ and $p\approx0.09576$. Both lead to the same conclusion.

```python
x = np.array([3003, 3005, 2997, 3006, 2999, 2998, 3007, 3005, 3001])
stats.ttest_1samp(x, popmean=3000)
# t = 1.88776; p = 0.09576
```

**4. Decide and interpret.** Since $0.09576>0.05$, $\boxed{\text{do not reject }H_0}$. The source describes the evidence as weak. The sample mean is above 3000 mm, but the data do not provide sufficient evidence of a population mean difference at the 5% level.

### 3.12 b) Critical values at the 1% significance level

With $df=8$ and a two-sided test:

$$\pm t_{0.995,8}=\boxed{\pm3.355}.$$

Python: `stats.t.ppf(0.995, df=8)`.

Reject $H_0$ only if $|t_{\mathrm{obs}}|>3.355$. Since $1.88776<3.355$, do not reject at 1%.

### 3.12 c) Critical values at the 5% significance level

With $df=8$:

$$\pm t_{0.975,8}=\boxed{\pm2.306}.$$

Python: `stats.t.ppf(0.975, df=8)`.

Reject $H_0$ if $|t_{\mathrm{obs}}|>2.306$. Here $1.88776<2.306$, so do not reject at 5% either.

The 1% critical values are farther from zero than the 5% values. A smaller significance level allows fewer false rejections when $H_0$ is true, so it requires a more extreme statistic to reject.

### 3.12 d) Why is the normality assumption important?

For independent observations from a normal population, the statistic

$$T=\frac{\bar X-\mu_0}{S/\sqrt n}$$

has a $t$ distribution with $n-1$ degrees of freedom under $H_0$. That distribution is what gives the p-values and critical values above.

With only $n=9$, we cannot rely on a large sample to smooth out strong skewness or outliers. Normality is therefore important for the validity of these calculations. Independence and representative sampling are also required.

### 3.12 e) Interpret the QQ plots

The source compares the real data (the central panel with a red border) with eight simulated normal samples of the same size:

![[lab-5-exercise-3-12-qq.png]]

**How to read the plot:** the horizontal axis contains theoretical normal quantiles, and the vertical axis contains ordered sample values. If a normal model is reasonable, the points should approximately follow a straight line. With only nine observations, even genuinely normal samples show visible departures from a line.

The real-data panel follows its reference line about as well as the simulated normal samples. There is no striking outlier or systematic curvature beyond the variation visible in the simulations.

**Answer:** $\boxed{\text{The plot gives no clear reason to doubt normality.}}$ This supports using the normal model here; nine observations cannot establish normality with certainty.

**Exam procedure:** identify the actual-data panel, compare its departures from a straight line with the normal simulations, and state whether those departures look unusually large.
