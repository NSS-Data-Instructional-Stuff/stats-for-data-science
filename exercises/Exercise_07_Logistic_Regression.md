# Week 6 Exercises: Statistics for Data Science

### Part 1: Steph Curry Shooting
Read in the data from curry_shooting.csv into a dataframe named *shots*.

The statsmodels library expects our target to be encoded as 0/1, so let's convert the shot result to this by using 
```
shots['SHOT_RESULT'] = (shots['SHOT_RESULT'] == 'made').astype(int)
```

a. Fit a logistic regression model with target variable SHOT_RESULT and predictor variable SHOT_DIST. Is the coefficient you obtain statistically significant? Interpret the coefficient on SHOT_DIST.

b. Now, fit a logistic regression model with target variable SHOT_RESULT and predictor variable PTS_TYPE. NOTE: Make sure that you treat PTS_TYPE as a categorical variable. Is the coefficient you obtain statistically significant? Interpret the coefficient you get.

c. Test whether PTS_TYPE is statistically significant, once you control for SHOT_DIST.

### Part 2: Breast Cancer
The dataset breast_cancer.csv comes from [https://www.kaggle.com/uciml/breast-cancer-wisconsin-data](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data).

Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.
n the 3-dimensional space is that described in: [K. P. Bennett and O. L. Mangasarian: "Robust Linear Programming Discrimination of Two Linearly Inseparable Sets", Optimization Methods and Software 1, 1992, 23-34].

The columns are as follows:

* id: ID number of the patient 
* diagnosis: Diagnosis, where 0 = benign and 1 = malignant
* radius_mean: mean of distances from center to points on the perimeter
* texture_mean: standard deviation of gray-scale values 
* perimeter_mean: perimeter
* area_mean: area
* smoothness_mean: local variation in radius lengths 
* compactness_mean: perimeter^2 / area - 1.0
* concavity_mean: severity of concave portions of the contour
* concave_points_mean: number of concave portions of the contour
* symmetry_mean: symmetry
* fractal_dimension_mean: "coastline approximation" - 1

The mean, standard error and "worst" or largest (mean of the three
largest values) of these features were computed for each image,
resulting in 30 features. For instance, field 3 is Mean Radius, field
13 is Radius SE, field 23 is Worst Radius.

All feature values are recoded with four significant digits.

We will consider the following set of features: 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean','fractal_dimension_mean'

Read in this data as a dataframe named *bc*.

1. Create a logistic regression model with response being diagnosis and predictor being the mean radius. Is the coefficient you get statistically significant. Interpret the meaning of this coefficient.

2. Now, run a hypothesis test to see if the relationship between either of the perimeter_mean and area_mean is statistically significant after controlling for radius mean. Look at the coefficients of the model using radius, perimeter, and area. Interpret the meaning of the radius coefficient. Also, look at the boxplot showing diagnosis vs. radius_mean. Does the coefficient you got make sense? What might explain what is going on?

3. Fit a logistic regression model with response being diagnosis, using all of the "mean" variables as predictors. Look at the p-values associated with each coefficient and note which are larger than 0.05. Run a hypothesis test to determine if any of those coefficients are statistically significantly different from zero.

4. Finally, let's see how well your model predicts on new data. Perform a train/test split and train a model using the reduced model from question 3. Inspect the confusion matrix for the test data. How well did you model do?