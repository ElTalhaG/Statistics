## Exercise 2.9 - Continuous random variable

For `stats.norm`, Python uses `cdf(x, loc, scale)`, where `loc` is the mean $\mu$ and `scale` is the standard deviation $\sigma$ (not the variance). If omitted, the defaults are $\mu=0$ and $\sigma=1$.

### 2.9 a) Interpret the three normal CDF expressions

A CDF gives the probability to the left of a value: $F(x)=P(X\le x)$.

1. `stats.norm.cdf(2)` uses the standard normal distribution, $X\sim N(0,1)$:
   $$P(X\le2)=0.9772.$$
   In words, about 97.72% of the standard normal curve is to the left of 2.

2. `stats.norm.cdf(2, 1, 1)` uses $X\sim N(1,1^2)$:
   $$P(X\le2)=0.8413.$$

3. `stats.norm.cdf(2, 1, 2)` uses $X\sim N(1,2^2)$:
   $$P(X\le2)=0.6915.$$

The last argument is the standard deviation. Thus `2` means variance $2^2=4$, and this wider curve puts a smaller fraction of its area below 2 than the first two curves.

### 2.9 b) Apply `ppf` to a CDF result

The CDF at 2 gives the cumulative probability up to 2. The `ppf` (percent-point function) reverses that operation and returns the value at that cumulative probability:

$$\operatorname{ppf}(\operatorname{cdf}(2))=2.$$

Therefore `stats.norm.ppf(stats.norm.cdf(2))` returns **2** (up to numerical rounding).

### 2.9 c) Interpret the 97.5th percentiles

The standard normal 97.5th percentile is $z_{0.975}=1.960$. For a normal variable with mean $\mu$ and standard deviation $\sigma$, convert the standard normal percentile back to the original scale using:

$$x_{0.975}=\mu+\sigma z_{0.975}.$$

1. For $N(0,1^2)$:
   $$x_{0.975}=0+1(1.960)=1.960.$$

2. For $N(1,1^2)$:
   $$x_{0.975}=1+1(1.960)=2.960.$$

3. For $N(1,2^2)$:
   $$x_{0.975}=1+2(1.960)=4.920.$$

Each answer is the value with 97.5% of that distribution to its left. Python checks: `stats.norm.ppf(0.975)`, `stats.norm.ppf(0.975, 1, 1)`, and `stats.norm.ppf(0.975, 1, 2)`.

**TI-30XB note:** use the standard normal table for $z$ probabilities and quantiles; the TI-30XB does not conveniently calculate normal CDFs or inverse CDFs directly. The calculator can do the arithmetic in $\mu+\sigma z$.

---

## Exercise 2.10 - The normal PDF

### 2.10 a) Find the false statement

The notation is $N(1,2^2)$, so the mean is $\mu=1$ and the standard deviation is $\sigma=2$. The variance is the square of the standard deviation:

$$\sigma^2=2^2=4.$$

Check each claim: a probability density has total area 1; the mean is 1; a normal curve is symmetric about its mean; and its tails extend indefinitely in both directions. Statement 3 says the variance is 2, but it is 4.

**Answer: statement 3 is false.**

### 2.10 b) Probabilities for $X\sim N(24,16)$

Here $\mu=24$ and the given variance is 16, so:

$$\sigma=\sqrt{16}=4.$$

For normal probabilities, first standardize with $Z=(X-\mu)/\sigma$ and then use a standard normal table or CDF.

1. For $P(X\le20)$:
   $$z=\frac{20-24}{4}=-1,$$
   so $P(X\le20)=P(Z\le-1)=0.1587$.

2. For $P(X>29.5)$:
   $$z=\frac{29.5-24}{4}=1.375.$$
   Use the upper tail, or subtract the CDF from 1:
   $$P(X>29.5)=1-P(Z\le1.375)=0.0845.$$

3. A continuous random variable has probability zero at any one exact point:
   $$P(X=23.8)=0.$$

**Answers:** $\boxed{0.1587}$, $\boxed{0.0845}$, and $\boxed{0}$, respectively.

**TI-30XB note:** use the standard normal table after calculating each $z$ score. Python checks from the source are `stats.norm.cdf(20, 24, 4)` and `1 - stats.norm.cdf(29.5, 24, 4)`. The exact-point probability is 0 because the normal distribution is continuous.

---

## Exercise 2.11 - Computer chip control

The old checking time has mean 65 ms and standard deviation 4 ms. The new machine has mean 54 ms and standard deviation 3 ms. The two checking times are assumed independent and normally distributed.

### 2.11 a) Probability the time saving is less than 10 ms

Define the saving as old time minus new time:

$$U=X_{\text{old}}-X_{\text{new}}.$$

Its mean is the difference of the means:

$$\mu_U=65-54=11\text{ ms}.$$

For independent variables, variances add even when one variable is subtracted:

$$\sigma_U^2=4^2+3^2=16+9=25,$$
$$\sigma_U=\sqrt{25}=5\text{ ms}.$$

Therefore $U\sim N(11,5^2)$. Standardize 10 ms:

$$z=\frac{10-11}{5}=-0.2.$$

Thus:

$$P(U<10)=P(Z<-0.2)=0.4207.$$

**Answer:** $\boxed{0.4207}$, or about 42.1%.

**TI-30XB note:** calculate $z=-0.2$ on the calculator and read $P(Z<-0.2)$ from the standard normal table. Python check: `stats.norm.cdf(10, 11, 5)`.

### 2.11 b) Total time to check 100 chips on the new machine

Let $T=X_1+\cdots+X_{100}$, where each time has mean 54 ms and standard deviation 3 ms. Add the means:

$$\mu_T=100(54)=5400\text{ ms}.$$

For independent check times, add variances (not standard deviations):

$$\sigma_T^2=100(3^2)=100(9)=900\text{ ms}^2.$$

Take the square root to obtain the standard deviation:

$$\sigma_T=\sqrt{900}=30\text{ ms}.$$

**Answer:** the total has mean $\boxed{5400\text{ ms}}$ and standard deviation $\boxed{30\text{ ms}}$.

---

## Exercise 2.12 - Concrete items

Item length is normally distributed with $\mu_L=3000$ mm and $\sigma_L=3$ mm.

### 2.12 a) Expected error rate

The acceptable range, 2993 to 3007 mm, is symmetric about the mean 3000 mm. Therefore the two failure tails have equal probabilities:

$$P(\text{error})=P(L<2993)+P(L>3007)=2P(L<2993).$$

Standardize the lower limit:

$$z=\frac{2993-3000}{3}=-\frac{7}{3}\approx-2.333.$$

Using the standard normal CDF:

$$P(\text{error})=2P(Z<-2.333)=0.0196.$$

**Answer:** the expected error rate is $\boxed{0.0196}$, about 2.0% of items.

**TI-30XB note:** calculate the $z$ score and use a standard normal table. Python check: `2 * stats.norm.cdf(2993, 3000, 3)`. Doubling one tail works here because the specification limits are equally far from the mean.

### 2.12 b) Required precision for the beam spacing

Assume the item length $L$ and beam spacing $L_{\text{beam}}$ are independent, as in the source solution. Define the gap:

$$D=L-L_{\text{beam}}.$$

The mean gap is:

$$\mu_D=3000-2900=100\text{ mm}.$$

Because the measurements are independent, their variances add even though we subtract one measurement:

$$\sigma_D^2=3^2+\sigma_{\text{beam}}^2=9+\sigma_{\text{beam}}^2.$$

The required interval $90<D<110$ is centered at 100 mm with half-width 10 mm. For a symmetric central 99% of a normal distribution, 0.5% is in each tail, so the given standard normal quantile is $z_{0.995}=2.576$. Therefore:

$$\frac{10}{\sigma_D}=2.576,\qquad \sigma_D=\frac{10}{2.576}.$$

Solve for the beam-spacing standard deviation:

$$9+\sigma_{\text{beam}}^2=\left(\frac{10}{2.576}\right)^2,$$
$$\sigma_{\text{beam}}=\sqrt{\left(\frac{10}{2.576}\right)^2-9}=2.464\text{ mm}.$$

**Answer:** the beam spacing standard deviation must be no larger than $\boxed{2.464\text{ mm}}$.

**TI-30XB note:** enter the supplied quantile into the formula and use the square root key. No distribution function is needed because $z_{0.995}$ is given.

---

## Exercise 2.13 - Online statistics video views

Model views as a Poisson process with 110,000 views per 365-day year. Convert that yearly average to the time interval asked about.

### 2.13 a) No views in a half-hour

There are $365\cdot24\cdot2$ half-hour periods in a year. Thus the mean number of views per half-hour is:

$$\lambda_{30\text{ min}}=\frac{110000}{365\cdot24\cdot2}=6.28.$$

For a Poisson random variable, the probability of zero events is $P(X=0)=e^{-\lambda}$:

$$P(X=0)=e^{-6.28}=0.00187.$$

**Answer:** $\boxed{0.00187}$, or about 0.187%.

TI-30XB: calculate the rate above and use the $e^x$ function with exponent $-6.28$. Python check: `lam = 110000 / (365*24*2)` followed by `stats.poisson.pmf(0, lam)`.

### 2.13 b) Waiting more than 15 minutes for the next view

There are half as many expected views in 15 minutes as in 30 minutes:

$$\lambda_{15\text{ min}}=\frac{6.28}{2}=3.14.$$

Waiting more than 15 minutes means there are no views during those 15 minutes. For a Poisson process, the zero-event probability is $e^{-\lambda}$:

$$P(T>15)=P(X_{15\text{ min}}=0)=e^{-3.14}=0.043.$$

Equivalently, the mean waiting time is $\beta=365\cdot24\cdot60/110000=4.778$ minutes, and the exponential survival probability is $P(T>15)=e^{-15/\beta}=0.043$.

**Answer:** $\boxed{0.043}$, or about 4.3%.

TI-30XB: calculate $e^{-3.14}$ using the $e^x$ function. Python check from the source: `beta = 365*24*60/110000` and `1 - stats.expon.cdf(15, scale=beta)`.
