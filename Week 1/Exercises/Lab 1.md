**E1.1 — Infant birth weight**.
The data are:

| Group        | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| ------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Females\(x\) | 2474 | 2547 | 2830 | 3219 | 3429 | 3448 | 3677 | 3872 | 4001 | 4116 |
| Males \(y\)  | 2844 | 2863 | 2963 | 3239 | 3379 | 3449 | 3582 | 3926 | 4151 | 4356 |

**1.1(a)**:

> Find the "**sample mean**, **sample variance**, and **sample standard deviation**" for the female birth weights. Do it both by hand/calculator and with Python. Then explain what the numbers mean in words.

The three formulas we need are:

Sample average/mean:                     $\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$

Sample variance:                   $s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2$

Sample standard deviation:   $s=\sqrt{s^2}$

Here $(n=10)$.

For Python, we’ll eventually use:

```
import numpy as np

x = np.array([2474, 2547, 2830, 3219, 3429,
              3448, 3677, 3872, 4001, 4116])
```

The relevant Week 1 functions are:

```
np.mean(x)
np.var(x, ddof=1)
np.std(x, ddof=1)
```

The `ddof=1` matters because we are calculating the **sample variance** and **sample standard deviation**, so the variance formula divides by $(n-1)$ instead of $(n)$.

### Sample average/mean

We calculate and get:
$$ \bar{x} = \frac{ 2474+2547+2830+3219+3429+3448+3677+3872+4001+4116 }{10}\approx3361,3\text{ g}$$
So the average female birth weight in this sample is about 3361.3 g.

### Sample variance
For our data:
 $n=10$
 $\bar{x}=3361.3$

We calculate and get:
$$
s^2=
\frac{1}{9}
\left[
(2474-3361.3)^2+
(2547-3361.3)^2+
\cdots+
(4116-3361.3)^2
\right]
\approx 344920,5\text{ g}^2
$$

### Sample standard deviation
For this one we basically square root the answer from sample variance and get:

$$
s=\sqrt{344920,5}\approx587,29 \text{ g}

$$

**1.1(b)**:
>Compute the same summary statistics for the male births, and compare the mean and standard deviation to the results for the female births. Based on these ten observations alone, would you say the difference is large?

The same 3 summary statistics for the **male birth weights**:
`2844, 2863, 2963, 3239, 3379, 3449, 3582, 3926, 4151, 4356`

We get:
$$
\bar{y}=\frac{1}{n}\sum_{i=1}^{n}y_i \approx 3475,2 \text{ g}
$$
$$
s_y^2=\frac{1}{n-1}\sum_{i=1}^{n}(y_i-\bar{y})^2 \approx 283158,1778 \text{ g}^2
$$
$$
s_y=\sqrt{s_y^2}\approx 532.126092 \text{ g}
$$
So for the male births we now have:
- Mean: $3475.2 \text{ g}$
- Sample variance: $283158 g²$
- Sample standard deviation: 532.13 g

Now compare that with the females:
- Female mean: 3361.3 g
- Male mean: 3475.2 g
- Female SD: 587.3 g
- Male SD: 532.13 g

The difference in means is: $3475.2-3361.3=113,9\text{ g}$
This shows that the males are on avg. about 113,9 g heavier in this sample, while the male birth weights are also a bit less spread out because their standard deviation is smaller.




---

E1.2



E1.3

E1.4
