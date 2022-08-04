# Week 5 Exercises: Statistics for Data Science

### Part 1: Pulse Rates
The file nhanes_pulse_sample.csv contains a sample of 100 men between the ages of 30 and 40 from the 2015 National Health and Nutrition Examination Survey.

Read in this dataset as a dataframe named *nhanes*.

You suspect that the average pulse rate for men between the ages of 30 and 40 is greater than 70 and want to use this data to test this hypothesis.

1. What are your null and alternative hypotheses? Is this is one-tailed test or a two-tailed test?

2. Find the mean and standard deviation of the pulse rate in your sample.

3. Conduct a t-test to test your hypothesis.

4. What p-value did you get?

5. State your conclusion.

### Part 2: Crashes on Weekend vs Weekday 
We are interested in studying the difference between weekends and weekdays in terms of number of reported crashes in Davidson County. We speculate that there are a larger number of reported crashes on average on weekdays compared to weekends.

The file crashes_sample.csv contains a random sample of 65 randomly selected days.

Read in this data as a dataframe named *crashes*.

1. Look at the distribution of Accident_Number for weekends vs non-weekends. Do this distributions appear to be approximately normal?

2. What are your null and alternative hypotheses?

3. What is the observed difference in the average number of crashes on weekends vs. weekdays?

4. Conduct a t-test to test your hypotheses.

5. What p-value did you get?

6. State your conclusion at the 0.05 significance level.

7. Repeat this test, but use a permutation test this time. How do your results compare to the t-test?

### Part 3: Russia Constitutional Referendum

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

### Part 4: Permutation Testing
1. In this question, we'll use the penguins dataset. Read this into a DataFrame named `penguins`. We're only going to focus on two of the species, adelie and chinstrap, so filter down to these two using the following code:
```
penguins = penguins[penguins['species'].isin(['Adelie', 'Chinstrap'])]
```
a. Take a look at the distribution of body mass for these two species. What do you notice?

b. Let's test the hypothesis that the distribution of body masses is different for these two species using a permutation test. Use as your test statistic the difference between means. What conclusion do you reach?

c. Now, instead of using the difference in means, use the difference in standard deviations. What conclusion do you reach now?

2. In this question and the next, you'll be looking at shooting data from NBA games that took place during the 2014/2015 NBA season. We'll be working with data from one particular player, Steph Curry, who is widely regarded as one of the greatest shooters in NBA history. You have been provided a dataset, curry_shooting.csv, which contains all shots that Steph Curry took during the 2014/2015 NBA season. Read this dataset into a DataFrame named `shots`.

The SHOT_RESULT column indicates whether a particular shot was successful, and the PERIOD column shows which quarter (1-4) or overtime period (5) the shot took place. In this question, we'll explore whether the PERIOD and SHOT_RESULT columns are independent or dependent.

a. Create a cross-tabulation to look at Curry's makes/misses vs. game period. What do you notice?

b. One method of determining if two variables are dependent is using the [mutual information](https://en.wikipedia.org/wiki/Mutual_information) metric. For two random variables, the mutual information of these variables is zero if they are independent and positive otherwise. This metric can be imported from scikit-learn:
```
from sklearn.metrics import mutual_info_score
```
Calculate the observed mutual information score for PERIOD versus SHOT_RESULT. This can be accomplished using
```
mutual_info_score(labels_true = None, labels_pred = None, 
                             contingency = pd.crosstab(shots['PERIOD'], shots['SHOT_RESULT']))
```

c. The mutual information score does not have to land in a particular range like the correlation does. Because of this, if we want to use the mutual information score to determine dependence or independence, it can be useful to do a hypothesis test. If we assume a null hypothesis that shooting and period are independent, then we can permute one of the variables and still have a valid sample. Perform a permutation test of dependence for these variables using the mutual information score. What conclusion can you reach?

d. In the NBA players can earn more points for a successful basket that is made from behind the 3-point line. The type of shot (2-pointer vs 3-pointer) is indicated by the PTS_TYPE column. Run a permutation test to test if the PTS_TYPE and SHOT_RESULT are dependent.

**Challenge Question:** In the game of basketball there is a concept of the "hot hand" effect where it is believed that a player will occasionally go on a streak of shooting success. A recent [article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0261890) examined the hot hand phenomenon to try and determine if the hot hand effect can be detected in real NBA games. For this question, you'll be doing a limited analysis of the hot hand phenomenon, focusing just on Steph Curry.

a. What was the overall percentage of shots that Steph Curry made in this season?

b. For this question, we want to examine whether he tends to make more shots after a miss or after a make. In order to do this, we need to be able to identify which shots occurred after a make and which occurred after a miss. The `shift` function will give the result of the previous row. We'll assume that the hot hand effect won't carry over across games, so we'll only look at the second or later shot of a game. Create a new column, Previous", using the following code:  
```
shots['Previous'] = shots.groupby('MATCHUP')['SHOT_RESULT'].shift()
```
Take a look at the results and make sure that they look correct.

c. What percentage of the time did Steph Curry make a shot after making the previous shot?

d. What percentage of the time did Steph Curry miss a shot after missing the previous shot?

e. We might wonder whether this observed difference can be explained by random chance or if there is actually a different make percentage after missing. Run a permutation test with the null that the difference in proportions is zero and alternative that the rate of makes is smaller after a make than after a miss. What conclusion can you reach?