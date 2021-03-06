# Week 3 Exercises: Statistics for Data Science

### Part 1:  Binomial Distribution
According to Forbes [(https://www.forbes.com/sites/zackfriedman/2019/01/11/live-paycheck-to-paycheck-government-shutdown/#4693b2194f10)](https://www.forbes.com/sites/zackfriedman/2019/01/11/live-paycheck-to-paycheck-government-shutdown/#4693b2194f10), 78% of American workers live paycheck-to-paycheck.

1. You take a random sample of 10 American workers.


	a. What is the probability that between 6 and 9 people (inclusive) in your sample are living paycheck-to-paycheck?

	b. What is the probability that at least 9 people in your sample are living paycheck-to-paycheck?

	c. What is the probability that fewer that 75% of people in your sample are living paycheck-to-paycheck?

	d. What is the probability that fewer than 50% of people in your sample are living paycheck-to-paycheck?

2. You take a random sample of 25 American workers.
	a. What is the probability that fewer than 75% of people in your sample are living paycheck-to-paycheck?
	b. What is the probability that fewer than 50% of people in your sample are living paycheck-to-paycheck?

3. You take a random sample of 100 American workers. 
	a. What is the probability that fewer than 75% of people in your sample are living paycheck-to-paycheck?
	b. What is the probability that fewer than 50% of people in your sample are living paycheck-to-paycheck?

4. You take a random sample of 1000 American workers. 
	a. What is the probability that fewer than 75% of people in your sample are living paycheck-to-paycheck?
	b. What is the probability that fewer than 50% of people in your sample are living paycheck-to-paycheck?

5. What do you notice happens as the size of your sample increases?

### Part 2: The Newton Problem 
Now, you will attempt to outdo Isaac Newton. See this video by Vsauce 2 for an entertaining description and analysis of the problem: [https://www.youtube.com/watch?v=RFlTawWwLZc](https://www.youtube.com/watch?v=RFlTawWwLZc). As described in the video, this is a problem which Isaac Newton got wrong. More precisely, he got the correct calculations, but his explanation was off. To be fair to Newton, the machinery of probability theory had not been developed yet in his time.

Use the binomial distribution to answer this question.
Which of the following three propositions has the greatest chance of success?
A. Six fair dice are tossed independently and at least one “6” appears.
B. Twelve fair dice are tossed independently and at least two “6”s appear.
C. Eighteen fair dice are tossed independently and at least three “6”s appear.


### Part 3: Normal Distribution - Pulse Rates 
The file nhanes_pulse_sample.csv contains a sample of 100 men between the ages of 30 and 40 from the 2015 National Health and Nutrition Examination Survey.

Read in this dataset as a dataframe named *nhanes*.

1. Plot the histogram and Q-Q plot for the pulse rate from this sample. Does it appear that pulse rates are normally distributed?

2. Use a normal approximation to answer the following questions:
  a) Approximately what  proportion of men between the age of 30 and 40 will have a pulse less than 60?
  b) Approximately what proportion of men between the age of 30 and 40 will have a pulse greater than 100?

### Part 4: Normal Distribution - Appraisal Values
The file appraisal_2017.csv includes the appraised values for 1000 Davidson County homes in 2017.

Read in this dataset as a dataframe named *appraisal*.

1. Plot a histogram and Q-Q plot for the appraisal values. Does the distribution of the appraisal values appear to be approximately normal?

2. Apply a transformation to the appraisal values and then repeat the above step.

3. Use what you have found to approximate the proportion of total houses in Davidson County with appraisal value at least $1,000,000.
