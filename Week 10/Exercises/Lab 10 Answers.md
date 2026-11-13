# Lab 10 Answers - Chapter 7: Categorical and Count Data

Exercises: 7.1, 7.2, 7.3(a,b), 7.4(a,b), and 7.5. This write-up follows the data and wording in the [DTU Chapter 7 exercise sheet](https://02323.compute.dtu.dk/enotes/exercises7-Python.pdf). A runnable calculation script is in [lab_10_categorical_counts.py](<lab_10_categorical_counts.py>).

## Useful ideas and notation

- A **sample proportion** is $\hat p=x/n$, where $x$ counts observations in the category of interest and $n$ is the sample size.
- To compare two independent proportions with a confidence interval, use the two separate sample estimates in the standard error.
- To test $H_0:p_1=p_2$, pool the counts because the null assumes one common proportion.
- For a contingency table, expected counts under independence are

$$
E_{ij}=\frac{(\text{row }i\text{ total})(\text{column }j\text{ total})}{\text{grand total}}.
$$

- A chi-square statistic sums $(O-E)^2/E$ over table cells. For a $r\times c$ table, $df=(r-1)(c-1)$.

## Exercise 7.1 - Passing proportions

The counts are $82/108$ passed in Course 1 and $104/143$ passed in Course 2. Define the difference in the order asked, $p_1-p_2$.

### (a) 95% confidence interval for $p_1-p_2$

First calculate the sample proportions:

$$
\hat p_1=\frac{82}{108}=0.7593,\qquad
\hat p_2=\frac{104}{143}=0.7273,
\qquad \hat p_1-\hat p_2=0.0320.
$$

For a confidence interval, estimate the standard error from each sample separately:

$$
SE=\sqrt{\frac{\hat p_1(1-\hat p_1)}{108}+\frac{\hat p_2(1-\hat p_2)}{143}}
=0.05549.
$$

For 95% confidence, $z^*=1.96$. Therefore

$$
(\hat p_1-\hat p_2)\pm z^*SE
=0.03199\pm1.96(0.05549)
=\boxed{(-0.0768,\ 0.1408)}.
$$

The interval contains zero, so these data do not establish a difference in the courses' passing proportions at the 5% level. Course 1's observed passing proportion is about 3.2 percentage points higher, but the estimate is uncertain.

### (b) Critical value for the chi-square test at $\alpha=0.01$

The pass/fail by course table has 2 rows and 2 columns, so

$$
df=(2-1)(2-1)=1.
$$

The chi-square test is right-tailed. At $\alpha=0.01$ and $df=1$, the critical value is

$$
\boxed{\chi^2_{0.99,1}=6.635\text{ (approximately)}}.
$$

Reject the equality hypothesis only if the observed $\chi^2$ statistic exceeds 6.635.

### (c) Expected number and standard deviation of students who do not pass

If a student's probability of not passing is $q=1-0.80=0.20$, the number $X$ of non-passing students among 250 is binomial:

$$
X\sim\operatorname{Binomial}(n=250,q=0.20).
$$

For a binomial count, $\mu=nq$ and $\sigma=\sqrt{nq(1-q)}$:

$$
\mu=250(0.20)=\boxed{50\text{ students}},\qquad
\sigma=\sqrt{250(0.20)(0.80)}=\sqrt{40}=\boxed{6.32\text{ students}}.
$$

## Exercise 7.2 - Outdoor lighting

There were 250 lamps. Convert each percentage to a count by multiplying by 250:

| Variant | Denmark | Export | Total |
|---|---:|---:|---:|
| Copper | $0.072(250)=18$ | $0.064(250)=16$ | 34 |
| Painted | $0.280(250)=70$ | $0.348(250)=87$ | 157 |
| Stainless steel | $0.088(250)=22$ | $0.148(250)=37$ | 59 |
| **Total** | **110** | **140** | **250** |

### (a) Compare the overall proportions sold in Denmark and exported

The observed proportions are

$$
\hat p_{DK}=\frac{110}{250}=0.44,\qquad
\hat p_{export}=\frac{140}{250}=0.56.
$$

Under the null of equal proportions, each country group would account for half the lamps: expected counts are 125 and 125. The one-degree-of-freedom chi-square statistic is

$$
\chi^2=\frac{(110-125)^2}{125}+\frac{(140-125)^2}{125}=3.60.
$$

The 5% critical value is 3.841 (equivalently, the two-sided normal test has $|z|=\sqrt{3.60}=1.897$). Since $3.60<3.841$, do not reject equality at $\alpha=0.05$. The two-sided p-value is approximately 0.058; the observed 44% versus 56% split is not statistically significant at 5%.

### (b) Critical value for comparing the variant mix between Denmark and export

This is a $3\times2$ contingency table: three lamp variants and two destinations. Therefore

$$
df=(3-1)(2-1)=2.
$$

At $\alpha=0.05$, the right-tail critical value is

$$
\boxed{\chi^2_{0.95,2}=5.991\text{ (approximately)}}.
$$

For context, the table's independence/homogeneity statistic is approximately $2.204$, below 5.991 (p-value $\approx0.332$). Thus the data do not show a significant difference in the variant mix by destination.

## Exercise 7.3 - Local elections

The exit poll had $x=168$ respondents reporting a vote for A out of $n=740$:

$$
\hat p=\frac{168}{740}=0.2270.
$$

### (a) Test $H_0:p=0.295$ against $H_1:p\ne0.295$ at $\alpha=0.001$

Under the null, the standard error uses $p_0=0.295$:

$$
SE_0=\sqrt{\frac{p_0(1-p_0)}{n}}
=\sqrt{\frac{0.295(0.705)}{740}}=0.01677.
$$

The observed z statistic is

$$
z_{obs}=\frac{\hat p-p_0}{SE_0}
=\frac{0.2270-0.295}{0.01677}=\boxed{-4.055}.
$$

For a two-sided test, the p-value is $2P(Z\le-4.055)\approx\boxed{0.0000502}$. Since this is below $0.001$, reject $H_0$. The exit poll provides strong evidence that the population proportion differs from 29.5%; the sample estimate is lower.

### (b) 95% confidence interval for $p$

For the interval, use the sample proportion in the estimated standard error:

$$
SE=\sqrt{\frac{\hat p(1-\hat p)}{n}}
=\sqrt{\frac{0.2270(0.7730)}{740}}=0.01540.
$$

Then

$$
\hat p\pm1.96SE
=0.2270\pm1.96(0.01540)
=\boxed{(0.1968,\ 0.2572)}.
$$

As percentages, the interval is approximately **19.7% to 25.7%**.

## Exercise 7.4 - Sugar quality

Supplier A has 6 defective bags out of 50, and Supplier B has 12 out of 50.

### (a) Compare the defective proportions at the 5% significance level

The sample proportions are

$$
\hat p_A=\frac{6}{50}=0.12,\qquad
\hat p_B=\frac{12}{50}=0.24.
$$

The hypotheses are $H_0:p_A=p_B$ versus $H_1:p_A\ne p_B$. Under $H_0$, pool the observed defective bags:

$$
\hat p=\frac{6+12}{50+50}=0.18.
$$

The pooled standard error and z statistic are

$$
SE_0=\sqrt{\hat p(1-\hat p)\left(\frac1{50}+\frac1{50}\right)}
=\sqrt{0.18(0.82)(0.04)}=0.07684,
$$

$$
z_{obs}=\frac{0.12-0.24}{0.07684}=\boxed{-1.562}.
$$

The two-sided p-value is $2P(Z\le-1.562)\approx\boxed{0.118}$. Because $0.118>0.05$, do not reject $H_0$. The sample has a lower defective percentage for A, but the evidence is not statistically significant at 5%.

### (b) 99% confidence interval for a supplier with 36 defective bags out of 200

Here $\hat p=36/200=0.18$. For a 99% interval, $z^*=2.576$:

$$
SE=\sqrt{\frac{0.18(1-0.18)}{200}}=0.02716,
$$

$$
0.18\pm2.576(0.02716)
=\boxed{(0.1100,\ 0.2500)}.
$$

We estimate that 11.0% to 25.0% of this supplier's bags are defective, with 99% confidence using the normal-approximation interval.

## Exercise 7.5 - Physical training

The observed table has 3 job-success categories and 3 physical-training categories. The row totals are 53, 84, and 63; column totals are 30, 90, and 80; the grand total is 200.

### (a) Expected count for above-average training and good job success

Assuming independence, the expected count is row total times column total divided by the grand total:

$$
E=\frac{(63)(80)}{200}=\boxed{25.2}.
$$

### (b) Number of contributions and cell (1,1) contribution

There are $3\times3=\boxed{9}$ cells, so there are nine contributions to the Pearson chi-square statistic.

Cell $(1,1)$ is Bad job success and Below-average training. Its expected count is

$$
E_{11}=\frac{(53)(30)}{200}=7.95.
$$

Its contribution is

$$
\frac{(O_{11}-E_{11})^2}{E_{11}}
=\frac{(11-7.95)^2}{7.95}
=\boxed{1.170\text{ (approximately)}}.
$$

### (c) p-value and conclusion using the supplied statistic $\chi^2=10.985$

For a $3\times3$ table,

$$
df=(3-1)(3-1)=4.
$$

The right-tail p-value is

$$
P(\chi^2_4\ge10.985)\approx\boxed{0.0267}.
$$

At the usual $\alpha=0.05$ level, reject independence: the data provide evidence that job success and physical-training condition are associated. At $\alpha=0.01$, the result would not be significant.

## TI-30XB calculator notes

- The TI-30XB MultiView has **Normalcdf** and **invNorm**. For a two-sided z-test, evaluate the one-tail area and double it; for 95% and 99% intervals, use $z^*=1.96$ and $2.576$ (or obtain them with **invNorm**).
- Use the calculator for the arithmetic in proportions, standard errors, and $(O-E)^2/E$. For chi-square critical values and right-tail p-values, use a chi-square table or the provided Python script; the TI-30XB distribution menu does not provide chi-square CDF/inverse functions.
- For E7.1(c), enter $250(0.20)$ for the mean and $\sqrt{250(0.20)(0.80)}$ for the standard deviation.

## Python analysis

Run `python3 lab_10_categorical_counts.py` from the Week 10 Exercises folder. It reproduces the numerical results, including normal and chi-square tail probabilities and critical values. This is useful for checking arithmetic; the formulas above are the exam-ready method.

## Sources

- Exercise statements and data: [DTU Chapter 7 exercise sheet](https://02323.compute.dtu.dk/enotes/exercises7-Python.pdf).
- Chapter methods: `Week 10/Exercises/chapter7-Exercises.pdf` in this repository.
- Calculator functions: [TI-30XS / TI-30XB MultiView Guidebook](https://education.ti.com/en/guidebook/details/en/50BE24C84836434485BD2E8D49374AF7/30x_mv).
