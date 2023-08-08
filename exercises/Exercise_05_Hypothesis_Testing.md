# Week 5 Exercises: Statistics for Data Science

### Part 1: Pulse Rates
The file nhanes_pulse_sample.csv contains a sample of 100 men between the ages of 30 and 40 from the 2015 National Health and Nutrition Examination Survey.

Read in this dataset as a dataframe named *nhanes*.

You suspect that the average pulse rate for men between the ages of 30 and 40 is greater than 70 and want to use this data to test this hypothesis.

1. What are your null and alternative hypotheses? Is this is one-tailed test or a two-tailed test?

2. Find the mean and standard deviation of the pulse rate in your sample.

3. Conduct a t-test to test your hypothesis.

4. What p-value did you get?

5. State your conclusion at the 0.05 significance level.

### Part 2: Russia Constitutional Referendum

A 2016 paper published in the Annals of Applied Statistics [(https://projecteuclid.org/euclid.aoas/1458909907)](https://projecteuclid.org/euclid.aoas/1458909907)  suggests that election falsification can be indicated by the presence of higher-than-usual reported number of integer results. The paper suggests that this may be due to the well-known psychological phenomenon of attraction to round numbers.

Recently in Russia, a [constitutional referendum](https://en.wikipedia.org/wiki/2020_Russian_constitutional_referendum) passed, which included provisions allowing President Vladimir Putin to run again for two more six-year presidential terms.

The file results_2020_clean.csv contains a cleaned up version of these refenendum vote results by polling location. Note that 11 polling locations were dropped for having zero reported votes. The source for this data is [https://github.com/khakhalin/Sketches/tree/master/ru_vote_2020](https://github.com/khakhalin/Sketches/tree/master/ru_vote_2020).

The first three columns (region, tik, and uik) together identify the polling location.

The next three columns (yes, no, and total_votes) give the number of yes votes, number of no votes, and total number of votes cast for that location.

The winning_pct column is equal to yes / (yes + no), and the winning_pct_rounded column is the winning percentage rounded to one decimal place.

The final column, which is what we are most interested in, is the decimal value of the rounded winning percentage.

1. What proportion of the time would you expect the decimal part of random number rounded in the manner as above to be 0?
2. Create a bar chart showing the distribution of the occurences of each digit in the decimal column of the dataset. That is, you should have a bar for 0, 1, 2, 3, ..., 9. What do you notice from your bar plot?
3. Assume, as a null hypothesis that each digit is equally likely to appear as the decimal for any polling location (i.e., the probability of the decimal being 0 is 0.1). Under the assumption of this null hypothesis, what is the probability of seeing as extreme a proportion of 0's in the decimal position as was observed in the referendum?
4. Does the result of this hypothesis test call into question to reported results of this referendum? Use the 0.05 significance level.

### Part 3: Differences in Means
1. In this question, we'll use the penguins dataset. Read this into a DataFrame named `penguins`. We're only going to focus on two of the species, adelie and chinstrap, so filter down to these two using the following code:
```
penguins = penguins[penguins['species'].isin(['Adelie', 'Chinstrap'])]
```
a. Take a look at the distribution of body mass for these two species. What do you notice?

b. Test the hypothesis that the distribution of body masses is different for these two species. What conclusion do you reach? Use the 0.05 significance level.

c. Now, instead of using the difference in means, test whether there is a difference in the standard deviation of body mass between the two species (Hint: You'll need to run a permutation test for this.) What conclusion do you reach now? Use the 0.05 significance level.


### Part 4: Tests for Dependence
1. In this question and the next, you'll be looking at shooting data from NBA games that took place during the 2014/2015 NBA season. We'll be working with data from one particular player, Steph Curry, who is widely regarded as one of the greatest shooters in NBA history. You have been provided a dataset, curry_shooting.csv, which contains all shots that Steph Curry took during the 2014/2015 NBA season. Read this dataset into a DataFrame named `shots`.

The SHOT_RESULT column indicates whether a particular shot was successful, and the PERIOD column shows which quarter (1-4) or overtime period (5) the shot took place. In this question, we'll explore whether the PERIOD and SHOT_RESULT columns are independent or dependent.

a. Create a cross-tabulation to look at Curry's makes/misses vs. game period. What do you notice?

b. Run a hypothesis test for whether Curry's makes/misses and game period are dependent.

c. In the NBA players can earn more points for a successful basket that is made from behind the 3-point line. The type of shot (2-pointer vs 3-pointer) is indicated by the PTS_TYPE column. Test whether PTS_TYPE and SHOT_RESULT are dependent for Steph Curry.

2. In the week 3 exercises, we examined the relationship between rain_today, rain_yesterday, and day_of week. Now, let's perform hypothesis tests to see if the observed dependence we saw holds up to a statistical test. Read in the data from bna_rain.csv into a DataFrame named bna_rain.

a. Test whether rained_today and rained_yesterday are dependent.

b. Test whether rained_today and day_of_week are dependent.

### Part 5: Test for Correlation
Read in the file shifted_BNA_temps.csv into a DataFrame named bna. 

1. In week 2, we saw that there was a moderate positive correlation between TMAX and TMAX_LY. Run a hypothesis test to see if this correlation is statistically significant.

2. In week 2, we saw that there was a very small positive correlation between TMAX and TMAX_3MO. Run a hypothesis test to see if this correlation is statistically significant.