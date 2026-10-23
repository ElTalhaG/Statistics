#### E2.1. Discrete random variable

**2.1 a)**
We are given:

```c
stats.binom.pmf(4, 10, 0.6)
```

and Python returns:

```c
0.1115
```

The question is:

> What distribution is applied, and what does `0.1115` represent?

So we can read the Python command like this:

```
stats.binom.pmf(k, n, p)
```

So here:
- $k=4$
- $n=10$
- $p=0.6$

`binom` tells us this is a **binomial distribution**, and `pmf` asks for the probability of **exactly one specific number of successes**.

So the the binomial distribution is used with $n=10$ and $p=0.6$. The value $0.1115$ is the probability of getting exactly $4$ successes out of $10$ independent trials.
In formula form: $P(X=4)=0.1115$

---

**2.1 b)**

### 2.1 b) Using cumulative probabilities

Given:

- $P(X \le 4)=0.1662$
- $P(X \le 5)=0.3669$

Because $X$ is discrete, $X<5$ means $X\le4$.

1. **Directly given:**
   $$P(X\le5)=0.3669.$$

2. **Less than 5:**
   $$P(X<5)=P(X\le4)=0.1662.$$

3. **More than 4:** use the complement rule, because either $X\le4$ or $X>4$ must happen:
   $$P(X>4)=1-P(X\le4)=1-0.1662=0.8338.$$

4. **Exactly 5:** subtract the probability up to 4 from the probability up to 5. This leaves only the probability at 5:
   $$P(X=5)=P(X\le5)-P(X\le4)=0.3669-0.1662=0.2007.$$

**Final answers:**

$$P(X\le5)=0.3669,\qquad P(X<5)=0.1662,$$
$$P(X>4)=0.8338,\qquad P(X=5)=0.2007.$$

**TI-30XB note:** the calculator is useful for the subtraction and complement, but it does not conveniently provide the binomial CDF. Use the given CDF values and the probability rules above. Python commands: `stats.binom.cdf(5, 10, 0.6)`, `stats.binom.cdf(4, 10, 0.6)`, and `stats.binom.pmf(5, 10, 0.6)`.

---

## Exercise 2.4 - Consumer survey

There are 20 groceries in total: 6 have discrepancies and 14 do not. Three different groceries are selected without replacement.

### 2.4 a) Probability that no discrepancies occur

Let $X$ be the number of discrepancies. Since sampling is **without replacement**, use the hypergeometric distribution:

$$X\sim H(N=20, a=6, n=3).$$

We want no discrepancies, so $X=0$.

1. Choose 0 of the 6 discrepancy products.
2. Choose all 3 products from the 14 without discrepancies.
3. Divide by the number of ways to choose any 3 products from 20.

$$P(X=0)=\frac{\binom{6}{0}\binom{14}{3}}{\binom{20}{3}}.$$

Substitute and calculate:

$$P(X=0)=\frac{1\cdot364}{1140}=0.3193\approx0.319.$$

**Answer:** the probability that none of the 3 groceries has a discrepancy is $\boxed{0.319}$.

**TI-30XB:** use the combinations function `nCr`:

`(6 nCr 0) * (14 nCr 3) / (20 nCr 3)` $\approx0.319$.

Python check: `stats.hypergeom.pmf(0, M=20, n=6, N=3)`.

### 2.4 b) Mean and variance

For a hypergeometric variable:

$$\mu_X=n\frac{a}{N},$$
$$\sigma_X^2=n\frac{a}{N}\left(1-\frac{a}{N}\right)\frac{N-n}{N-1}.$$

Mean:

$$\mu_X=3\cdot\frac{6}{20}=0.90.$$

Variance:

$$\sigma_X^2=3\cdot\frac{6}{20}\cdot\frac{14}{20}\cdot\frac{20-3}{20-1}$$
$$=3\cdot0.30\cdot0.70\cdot\frac{17}{19}=0.564\approx0.56.$$

**Answer:** $\boxed{\mu_X=0.90}$ and $\boxed{\sigma_X^2\approx0.56}$.

TI-30XB can evaluate the arithmetic directly. Python checks are `stats.hypergeom.mean(M=20, n=6, N=3)` and `stats.hypergeom.var(M=20, n=6, N=3)`.

---

## Exercise 2.5 - Hay delivery quality

There are 20 bales, 2 infected and 18 not infected. Three bales are selected without replacement.

### 2.5 a) Mean, variance, and probability of at least one infected bale

Let $X$ be the number of infected bales. Use the hypergeometric distribution:

$$X\sim H(N=20, a=2, n=3).$$

**Mean:**

$$\mu_X=n\frac{a}{N}=3\cdot\frac{2}{20}=0.3.$$

**Variance:**

$$\sigma_X^2=n\frac{a}{N}\left(1-\frac{a}{N}\right)\frac{N-n}{N-1}$$
$$=3\cdot\frac{2}{20}\cdot\frac{18}{20}\cdot\frac{17}{19}=0.2416\approx0.242.$$

**At least one infected bale:** use the complement. “At least one” is the opposite of “none”:

$$P(X\ge1)=1-P(X=0).$$

For $X=0$, choose all 3 bales from the 18 uninfected bales:

$$P(X=0)=\frac{\binom{2}{0}\binom{18}{3}}{\binom{20}{3}}=\frac{816}{1140}.$$

Therefore:

$$P(X\ge1)=1-\frac{816}{1140}=0.2842.$$

**Answers:**

$$\boxed{\mu_X=0.30},\qquad \boxed{\sigma_X^2\approx0.242},\qquad \boxed{P(X\ge1)=0.2842}.$$

TI-30XB: use `nCr` for the combinations in $P(X=0)$, then subtract from 1. Python check: `1 - stats.hypergeom.pmf(0, M=20, n=2, N=3)`.

### 2.5 b) Probability that all 10 purchased bales are error-free

The supplier has a very large stock, so model the purchases as independent binomial trials. “Error-free” means “not infected”, with probability $1-p$ on each bale.

For all 10 bales to be error-free:

$$P(X=0)=(1-p)^{10}.$$

**(a) If 1% are infected:** $p=0.01$.

$$P(X=0)=(1-0.01)^{10}=0.99^{10}=0.9044.$$

**(b) If 10% are infected:** $p=0.10$.

$$P(X=0)=(1-0.10)^{10}=0.90^{10}=0.3487.$$

**Answers:**

$$\boxed{0.9044\text{ when }p=0.01},\qquad \boxed{0.3487\text{ when }p=0.10}.$$

TI-30XB: enter `0.99 ^ 10` and `0.90 ^ 10`. Python check: `stats.binom.pmf(0, 10, 0.01)` and `stats.binom.pmf(0, 10, 0.10)`.

---

## Exercise 2.7 - A fully automated production

The average rate is 1.6 items per minute, so $X\sim\operatorname{Poisson}(\lambda=1.6)$ for one minute.

### 2.7 a) Probability of more than 5 items in one minute

“More than 5” means $X>5$, which is the complement of $X\le5$:

$$P(X>5)=1-P(X\le5).$$

For a Poisson variable:

$$P(X\le5)=\sum_{x=0}^{5}\frac{e^{-1.6}(1.6)^x}{x!}.$$

Evaluating this Poisson CDF gives:

$$P(X>5)=1-P(X\le5)=0.00604\approx0.006.$$

**Answer:** about $\boxed{0.006}$, i.e. about 0.6% of minutes.

**TI-30XB note:** a Poisson CDF is not convenient to compute directly on this calculator. Use the complement and the Poisson sum above, or the Python result `1 - stats.poisson.cdf(5, 1.6)`.

### 2.7 b) Probability of no more than 8 items in 5 minutes

The Poisson rate scales with the length of the time interval:

$$\lambda_{5\text{ min}}=5\cdot1.6=8.$$

“No more than 8” means $X\le8$:

$$P(X\le8)=\sum_{x=0}^{8}\frac{e^{-8}8^x}{x!}=0.5925\approx0.593.$$

**Answer:** $\boxed{P(X\le8)\approx0.593}$.

**TI-30XB note:** use the scaled rate $\lambda=8$; do not use 1.6 for the 5-minute period. The Poisson CDF is more conveniently obtained from the exercise’s Python calculation: `stats.poisson.cdf(8, 8)`.

---

## Exercise 2.8 - Call center staff

The call rate is 180 calls per hour. A 5-minute period is $5/60=1/12$ of an hour, so:

$$\lambda_{5\text{ min}}=180\cdot\frac{5}{60}=15.$$

Thus $X\sim\operatorname{Poisson}(15)$ for a random 5-minute period.

### 2.8 a) Probability that capacity is exceeded

Capacity is exceeded when there are 20 or more calls, so we want $P(X\ge20)$.

Use the complement:

$$P(X\ge20)=1-P(X\le19).$$

The Poisson CDF calculation gives:

$$P(X\ge20)=0.1248\approx0.125.$$

**Answer:** there is a $\boxed{0.125}$ probability, or 12.5% chance, that the capacity is exceeded in a random 5-minute period.

**TI-30XB note:** the Poisson CDF is not convenient directly. Use the complement formula and the Python result `1 - stats.poisson.cdf(19, 15)`.

### 2.8 b) Capacity needed for at least 99% service without waiting

We need the **smallest** integer capacity $c$ satisfying:

$$P(X\le c)\ge0.99,$$

where $X\sim\operatorname{Poisson}(15)$.

Evaluate the CDF around the current capacity:

| Capacity $c$ | $P(X\le c)$ |
|---:|---:|
| 22 | 0.9615 |
| 23 | 0.9762 |
| 24 | 0.9857 |
| 25 | 0.9915 |
| 26 | 0.9950 |

The first value reaching at least 0.99 is $c=25$. Therefore:

$$\boxed{\text{Capacity must be at least 25 calls per 5 minutes.}}$$

**TI-30XB note:** there is no convenient Poisson inverse-CDF function, so use a small table of CDF values. The source also gives Python `stats.poisson.ppf(q=0.99, mu=15)`, which returns 25.0. The check is that $P(X\le24)=0.9857<0.99$ but $P(X\le25)=0.9915\ge0.99$.
