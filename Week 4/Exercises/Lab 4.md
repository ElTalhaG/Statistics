## Exercise 3.1 - Concrete items

The sample of 9 lengths is 3003, 3005, 2997, 3006, 2999, 2998, 3007, 3005, 3001 mm. The sum is 27021 mm. The sum of squared deviations from 3000 is 159 mm², but sample variance requires deviations from the sample mean:

$$\sum(x_i-\bar{x})^2=159-9(3002.3333-3000)^2=159-49=110\text{ mm}^2.$$

### 3.1 a) Sample mean, standard deviation, and standard error

The sample mean is the total divided by the number of items:

$$\bar{x}=\frac{27021}{9}=3002.333\text{ mm}.$$

It estimates the population mean item length.

The sample variance divides the squared deviations by $n-1$; the sample standard deviation is its square root:

$$s^2=\frac{110}{9-1}=13.75\text{ mm}^2,\qquad s=\sqrt{13.75}=3.708\text{ mm}.$$

$s$ describes the spread of individual item lengths around the sample mean.

The standard error estimates how much the sample mean would typically vary across repeated samples of 9 items:

$$SE_{\bar{x}}=\frac{s}{\sqrt{n}}=\frac{3.708}{\sqrt{9}}=1.236\text{ mm}.$$

**Answers:** $\boxed{\bar{x}=3002.333\text{ mm}}$, $\boxed{s=3.708\text{ mm}}$, and $\boxed{SE_{\bar{x}}=1.236\text{ mm}}$. The standard error describes sample-to-sample variation in the mean, not the variation of individual lengths.

**TI-30XB:** enter the nine measurements in 1-variable statistics to find $\bar{x}$ and sample standard deviation $S_x$ (not population $\sigma_x$), then calculate $S_x/\sqrt{9}$.

### 3.1 b) Error probability for a 5-item construction

Assume the 5 item lengths are independent, each with mean 3000 mm and standard deviation 3 mm. For the total length $T$, add means and add independent variances:

$$\mu_T=5(3000)=15000\text{ mm},$$
$$\sigma_T^2=5(3^2)=45\text{ mm}^2,\qquad \sigma_T=\sqrt{45}=6.708\text{ mm}.$$

The total is normally distributed. More than 1 cm away means outside $15000\pm10$ mm. The limits are symmetric, so calculate one tail and double it:

$$P(|T-15000|>10)=2P\left(Z>\frac{10}{6.708}\right)
=2P(Z>1.491)\approx0.1360.$$

**Answer:** about $\boxed{0.136}$, or 13.6% of constructions, will miss the target by more than 1 cm. Python check: `2 * (1 - stats.norm.cdf(10, loc=0, scale=(5*3**2)**0.5))`.

### 3.1 c) 95% confidence interval for the mean

The population standard deviation is unknown, so use a $t$ interval with $n-1=8$ degrees of freedom:

$$\bar{x}\pm t_{0.975,8}\frac{s}{\sqrt{n}}.$$

Using the supplied $t_{0.975,8}=2.306$ and $SE=1.236$:

$$3002.333\pm2.306(1.236)\approx3002.333\pm2.850,$$
$$\boxed{[2999.48,\ 3005.18]\text{ mm}}.$$

In repeated sampling, 95% of intervals constructed this way would contain the true population mean. Here, the target 3000 mm lies inside the interval.

### 3.1 d) 99% confidence interval for the mean

Use the same formula with the supplied $t_{0.995,8}=3.355$:

$$3002.333\pm3.355(1.236)\approx3002.333\pm4.147,$$
$$\boxed{[2998.19,\ 3006.48]\text{ mm}}.$$

This interval is wider than the 95% interval because greater confidence requires a larger range of plausible values. Both intervals contain 3000 mm.

### 3.1 e) 95% confidence intervals for variance and standard deviation

For normal data, the chi-square interval for population variance is:

$$\left[\frac{(n-1)s^2}{\chi^2_{0.975,8}},\ \frac{(n-1)s^2}{\chi^2_{0.025,8}}\right].$$

Here $(n-1)s^2=110$, with supplied quantiles 17.535 and 2.180:

$$\sigma^2\in\left[\frac{110}{17.535},\frac{110}{2.180}\right]
\approx[6.273,\ 50.459]\text{ mm}^2.$$

Take square roots of both endpoints:

$$\sigma\in[\sqrt{6.273},\sqrt{50.459}]\approx[2.505,\ 7.103]\text{ mm}.$$

**Answers:** $\boxed{\sigma^2\in[6.273,50.459]\text{ mm}^2}$ and $\boxed{\sigma\in[2.505,7.103]\text{ mm}}$.

### 3.1 f) 99% confidence intervals for variance and standard deviation

Use the same formula with supplied quantiles $\chi^2_{0.995,8}=21.955$ and $\chi^2_{0.005,8}=1.344$:

$$\sigma^2\in\left[\frac{110}{21.955},\frac{110}{1.344}\right]
\approx[5.010,\ 81.845]\text{ mm}^2,$$
$$\sigma\in[\sqrt{5.010},\sqrt{81.845}]\approx[2.238,\ 9.047]\text{ mm}.$$

**Answers:** $\boxed{\sigma^2\in[5.010,81.845]\text{ mm}^2}$ and $\boxed{\sigma\in[2.238,9.047]\text{ mm}}$. These 99% intervals are wider than the 95% intervals because they are designed to capture the true value more often. Using unrounded chi-square quantiles gives slightly different last decimals.

**TI-30XB note for parts (c)-(f):** the calculator can do the arithmetic, but it does not conveniently supply $t$ or chi-square quantiles. The exercise gives these values; otherwise use a statistical table or Python.

---

## Exercise 3.2 - Aluminum profile

Given $n=16$, $\bar{x}=180.05$ mm, and $s=0.0959$ mm. Assume the population is normal.

### 3.2 a) 90% confidence interval for the mean

The population standard deviation is unknown, so use a $t$ interval with $15$ degrees of freedom:

$$\bar{x}\pm t_{0.95,15}\frac{s}{\sqrt{n}}.$$

The standard error is $0.0959/\sqrt{16}=0.023975$ mm. Python gives $t_{0.95,15}=1.7531$ (`stats.t.ppf(0.95, df=15)`). Therefore:

$$180.05\pm1.7531(0.023975)=180.05\pm0.04203,$$
$$\boxed{[180.0080,\ 180.0920]\text{ mm}}.$$

### 3.2 b) 99% confidence interval for the standard deviation

First form the chi-square interval for variance and then take square roots. With $df=15$:

$$\sigma\in\left[\sqrt{\frac{(n-1)s^2}{\chi^2_{0.995,15}}},\ \sqrt{\frac{(n-1)s^2}{\chi^2_{0.005,15}}}\right].$$

Python gives $\chi^2_{0.995,15}=32.8013$ and $\chi^2_{0.005,15}=4.6009$ (use `stats.chi2.ppf(0.995, df=15)` and `stats.chi2.ppf(0.005, df=15)`). Also, $(n-1)s^2=15(0.0959)^2=0.137952$ mm$^2$. Substitute:

$$\sigma\in\left[\sqrt{\frac{0.137952}{32.8013}},\sqrt{\frac{0.137952}{4.6009}}\right]
=[0.06485,\ 0.17316]\text{ mm}.$$

**Answer:** $\boxed{\sigma\in[0.0649,\ 0.1732]\text{ mm}}$ (99% confidence).

**TI-30XB note:** use it for standard errors, square roots, and arithmetic. Get the $t$ and chi-square quantiles from Python or a table; those distribution functions are not conveniently available on the TI-30XB.

---

## Exercise 3.11 - Concrete items 2

Parts (b)-(f) use the same nine measurements as Exercise 3.1. Their sample statistics are:

$$\bar{x}=3002.333\text{ mm},\quad s^2=13.75\text{ mm}^2,\quad s=3.708\text{ mm},\quad SE_{\bar{x}}=1.236\text{ mm}.$$

### 3.11 a) Error probability for a 5-item construction

Let $T$ be the total length of 5 independent items. Then:

$$\mu_T=5(3000)=15000\text{ mm},\qquad
\sigma_T=\sqrt{5(3^2)}=\sqrt{45}=6.708\text{ mm}.$$

The tolerance is 15 m plus or minus 2 cm, or $15000\pm20$ mm. A miss is more than 20 mm from the target. By symmetry:

$$P(|T-15000|>20)=2P\left(Z>\frac{20}{6.708}\right)
=2P(Z>2.981)\approx0.00287.$$

**Answer:** about $\boxed{0.00287}$, or 0.287% of constructions, miss the tolerance. Python check: `2 * (1 - stats.norm.cdf(20, loc=0, scale=(5*3**2)**0.5))`.

### 3.11 b) Sample mean, standard deviation, and standard error

Using the calculations from Exercise 3.1(a):

$$\bar{x}=3002.333\text{ mm},\qquad s=3.708\text{ mm},\qquad
SE_{\bar{x}}=\frac{s}{\sqrt{9}}=1.236\text{ mm}.$$

The sample standard deviation describes variation in individual item lengths. The standard error describes estimated sample-to-sample variation of the mean for samples of 9; it is smaller because it divides $s$ by $\sqrt{n}$.

### 3.11 c) 95% confidence interval for the mean

Use a $t$ interval with 8 degrees of freedom and $t_{0.975,8}=2.306$:

$$3002.333\pm2.306(1.236)\approx3002.333\pm2.850,$$
$$\boxed{[2999.48,\ 3005.18]\text{ mm}}.$$

The target mean 3000 mm is inside the interval.

### 3.11 d) 99% confidence interval for the mean

Use $t_{0.995,8}=3.355$:

$$3002.333\pm3.355(1.236)\approx3002.333\pm4.147,$$
$$\boxed{[2998.19,\ 3006.48]\text{ mm}}.$$

It is wider than the 95% interval because 99% confidence requires a larger range of plausible values.

### 3.11 e) 95% confidence intervals for variance and standard deviation

With $df=8$, $(n-1)s^2=110$, $\chi^2_{0.975,8}=17.535$, and $\chi^2_{0.025,8}=2.180$:

$$\sigma^2\in\left[\frac{110}{17.535},\frac{110}{2.180}\right]
\approx[6.273,\ 50.459]\text{ mm}^2,$$
$$\sigma\in[\sqrt{6.273},\sqrt{50.459}]\approx[2.505,\ 7.103]\text{ mm}.$$

**Answers:** $\boxed{\sigma^2\in[6.273,50.459]\text{ mm}^2}$ and $\boxed{\sigma\in[2.505,7.103]\text{ mm}}$.

### 3.11 f) Can the company trust the target mean and standard deviation?

Compare the targets to their 95% confidence intervals:

- The target mean 3000 mm is inside $[2999.48,3005.18]$ mm.
- The target standard deviation 3 mm is inside $[2.505,7.103]$ mm.

**Conclusion:** both target values are consistent with their respective 95% confidence intervals. The sample gives insufficient evidence to reject either target. This does not certify that the parameters equal those targets; with only 9 items, the intervals are relatively wide.

### 3.11 g) Repeat the assessment with 100 items

Now $n=100$, $\bar{x}=3002.3$ mm, and $s=3.7$ mm. For the mean, $SE=3.7/\sqrt{100}=0.37$ mm and $t_{0.975,99}=1.9842$:

$$3002.3\pm1.9842(0.37)=3002.3\pm0.7342,$$
$$\boxed{\mu\in[3001.566,\ 3003.034]\text{ mm}}.$$

This interval is entirely above 3000 mm, so it gives evidence that the mean length exceeds the target.

For the standard deviation, use $df=99$, $\chi^2_{0.975,99}=128.422$, and $\chi^2_{0.025,99}=73.361$:

$$\sigma\in\left[\sqrt{\frac{99(3.7)^2}{128.422}},\sqrt{\frac{99(3.7)^2}{73.361}}\right]
=[3.249,\ 4.298]\text{ mm}.$$

This interval is also entirely above 3 mm. With 100 items, both target values (mean 3000 mm and standard deviation 3 mm) are excluded from their respective 95% confidence intervals.

Python critical values if needed: `stats.t.ppf(0.975, df=99)`, `stats.chi2.ppf(0.975, df=99)`, and `stats.chi2.ppf(0.025, df=99)`.

**TI-30XB note:** use the calculator for standard errors, interval arithmetic, and square roots. Obtain $t$ and chi-square quantiles from a statistical table or Python when the exercise does not supply them.
