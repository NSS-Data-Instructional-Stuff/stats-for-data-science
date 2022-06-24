# Week 1 Exercises: Statistics for Data Science

### Part 1: Metro Government Salaries

The file General_Government_Employees_Titles_and_Base_Annual_Salaries.csv contains the base annual salary of all Metro Government employees.

Read in this dataset as a dataframe named *salaries*.

1. What percentage of employees are full time?

2. Create a bar chart showing the number of employees per department. Which has the largest number of employees?

3. What is the most common job title for metro employees?

4. What are the mean and median salaries?

5. Plot the distribution of the dataset via a histogram. Is the data symmetric? skewed? How many modes does it have?

6. Find the standard deviation of salaries, and use this to compute z-scores for each observation. Inspect the results. Do you find anything interesting?

### Part 2: Temperatures 

The files BNA_temps.csv and LAX_temps.csv contain the daily high (TMAX) and low (TMIN) temperatures recorded at BNA and LAX airports, respectively, for the years 2012 through 2018.

Read in these file as dataframes named *bna* and *lax*.

1. How do the mean high temperatures compare for BNA and LAX? What about the medians?

2. Inspect the histograms for TMAX for both BNA and LAX. How would you describe these distributions (are they symmetric? are they skewed?) How do the distributions compare?

3. Before doing any computations, think about whether you expect the high temperatures for BNA or LAX to have the same standard deviation or whether you expect one to have higher standard deviation than the other. Then, compute the standard deviations and see if you were correct.

4. Look at the boxplot of high temperatures by month for each airport. What do you notice?

### Part 3: Conceptual 
1. In what scenarios might the mean of a dataset be significantly lower than the median? Can you come up with any examples of such a distribution?

2. Can you come up with an example of a distribution that has a median of 0 but a nonzero mean?

3. You are analyzing the housing market in Davidson County. You notice that there are some very expensive homes and are afraid that including these homes might skew your analysis. You are considering dropping the top 1% and bottom 1% of the observations prior to your analysis. What impacts might this have? What alternatives do you have if you do not wish to drop any observations?

4. You are analyzing daily stock market returns. You are considering dropping the top 1% and bottom 1% of the observations prior to your analysis. What impacts might this have on your analysis?

5. Say you are interested in studying commute times. You are looking at the daily commute times for two different people. Person A commutes from Murfreesboro into Nashville. Person B commutes in the opposite direction, from Nashville to Murfreesboro. If you look at the distribution of their daily commute times over a one-year period, which would you expect to have a larger standard deviation and why? Assume that they both leave for work around rush hour every morning.