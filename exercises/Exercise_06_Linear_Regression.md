# Week 6 Exercises: Statistics for Data Science

### Question 1: Sea Level Rise

The file key_west.csv contains Mean Sea Level values monthly for Key West, Florida.
Use this data to fit a linear regression model with target value the Monthly_MSL column and predictor variable the Year.

a. What coefficient do you obain for the Year variable? Is it statistically significant?

b. How can we interpret the meaning of this coefficient?

c. It might be possible that adding the Month variable to our model could capture seasonality. Perform a hypothesis test to determine if adding Month to the model is statistically significant. Warning: Make sure that you add it as a categorical variable, even though it is a numeric one. Remember that this is done by surrounding it with C.

### Question 2: Penguins

For these questions, you'll be working with the penguins dataset.

a. Fit a linear regression model with target variable body_mass_g and predictor flipper_length_mm. Interpret the meaning of the coefficients you get.

b. Test whether adding bill length to this model gives a statistically significant coefficient, after controlling for flipper length.

c. Test whether adding sex to this model gives a statistically significant coefficient, after controlling for flipper length.

d. Test whether adding species to this model gives a statistically significant coefficient, after controlling for flipper length and sex.

e. Finally, test whether the coefficients for interaction terms between flipper length and species are statistically significant.

f. Take the model that uses flipper length, sex, and species. What does this model estimate for the average body mass of a male Gentoo penguin with flipper length of 210 mm? Also, find a confidence interval for this estimate and a prediction interval.

g. Take the model that uses flipper length, sex, and species. What does this model estimate for the average body mass of a female Adelie penguin with flipper length of 190 mm? Also, find a confidence interval for this estimate and a prediction interval.

### Question 3: King County Home Prices
The file kc_sample.csv contains a sample of 1000 homes that were sold in King County, Washington. 

a. Build a linear regression model with target variable `price` and predictor variable `sqft_living`. How well does this model perform? Plot confidence intervals and prediction intervals against your dataset. Check the residuals. What problems might be present in this model?

b. Modify your model so that your target variable is the log of the price. How does this model compare to your previous one.

c. Add the `bedrooms` variable to your model. Look at the coefficient of the result. Do they make sense?