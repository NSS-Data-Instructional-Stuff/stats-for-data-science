# Week 1 Exercises: Statistics for Data Science

### Part 1: Library Circulation 

The file physical_circulation.csv contains the total physical circulation (checkouts and renewals) at each branch of the Nashville Public Library.

Read in this file as a dataframe named *circulation*.

1. Find the following:
* mean circulation
* median circulation
* min, max, and range
* the 10% trimmed mean
* standard deviation
* 25th and 75th percentile and the interquartile range

2. Plot the distribution of circulation numbers. Describe the shape of the distribution. Is is symmetric? left-skewed? right-skewed? How many modes does it have?

3. Would you consider any branches to be outliers?

### Part 2: Metro Government Salaries

The file General_Government_Employees_Titles_and_Base_Annual_Salaries.csv contains the base annual salary of all Metro Government employees.

Read in this dataset as a dataframe named *salaries*.

1. What are the mean and median salaries?

2. Plot the distribution of the dataset via both a histogram and boxplot. Is the data symmetric? skewed? How many modes does it have?

3. Create a KDE for the distribution. Experiment with different bandwidths until you think that you have a good representation of the dataset.

4. Create a boxplot showing the distribution of salaries across the different categories of employment status. What do you notice? Which employment statuses have higher salaries on average? What can you say about the variability of salaries across employment statuses?

5. Find the standard deviation of salaries, and use this to compute z-scores for each observation.

6. Find the interquartile range of salaries.

7. Which observations would you consider to be outliers?

### Part 3: Conceptual 
1. In what scenarios might the mean of a dataset be significantly lower than the median? Can you come up with any examples of such a distribution?

2. Consider the distribution of number of Twitter followers per Twitter account. Would you expect the interquartile range of the number of Twitter followers to be (a) about half as large as the range (b) almost as large as the range (c) much smaller than the range? 

3. You are analyzing the housing market in Davidson County. You notice that there are some very expensive homes and are afraid that including these homes might skew your analysis. You are considering dropping the top 1% and bottom 1% of the observations prior to your analysis. What impacts might this have on your analysis? What alternatives do you have is you do not wish to drop any observations?

4. You are analyzing daily stock market returns. You are considering dropping the top 1% and bottom 1% of the observations prior to your analysis. What impacts might this have on your analysis?

5. Say you are interested in studying commute times. You are looking at the daily commute times for two different people. Person A commutes from Murfreesboro into Nashville. Person B commutes in the opposite direction, from Nashville to Murfreesboro. If you look at the distribution of their daily commute times over a one-year period, which would you expect to have a larger standard deviation and why? Assume that they both leave for work around rush hour every morning.
