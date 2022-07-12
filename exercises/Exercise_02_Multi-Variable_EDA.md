# Week 2 Exercises: Statistics for Data Science

### Part 1: 2017 Appraisal Values 

The file appraisal_2017.csv contains the 2017 appraised value (total_appr) and square footage (finished_area) for a random sample of 1000 houses in Davidson County.

Read this data into a dataframe named *appraisal*.

1. Create a scatterplot of total_appr vs finished_area. 

2. By inspecting the scatterplot, describe the relationship between total_appr and finished_area. Is the direction of association positive or negative? Is the relationship linear? How strong is the relationship?

3. Do you see any points which might be considered outliers? Investigate those points.

4. Find the correlation between total_appr and finished_area. How strong is the relationship between the two variables?

### Part 2: Temperatures 

You have been provided two datasets, shifted_BNA_temps.csv and shifted_LAX_temps.csv. These contain the following columns:
* NAME: Location of temperature readings
* DATE: Date of the measurements
* TMIN: minimum temperature
* TMAX: maximum temperature
* TMAX_YESTERDAY: the maximum temerature for the previous day
* TMAX_3MO: the maximum temperature three months in the past. For example, for 2013-01-01, the TMAX_3MO column contains the maximum temperature on 2012-10-01.
* TMAX_6MO: the maximum temperature six months in the past. For example, for 2013-01-01, the TMAX_6MO column contains the maximum temperature on 2012-06-01.
* TMAX_LY: the maximum temperature for the same day of the previous year. For example, for 2013-01-01, the TMAX_LY column contains the maximum temperature on 2012-01-01.

1. Read in the file shifted_BNA_temps.csv into a DataFrame named bna.   
    a. Before doing any calculations, which columns do you think will have a positive correlation with TMAX? Which do you think will have a negative correlation? Which do you think will have the strongest relationship?  the weakest?
    b. Calculate the correlation between TMAX and all other temperature columns. Were your guesses correct?  
    c. Create a scatterplot of TMAX vs. TMIN. (There is an alpha argument for the plot method which sets the opacity of the points in your scatterplot. This argument takes a number between 0 and 1, where 0 is fully transparent and 1 is fully opaque. If you have a large number of points, like you have on this exercise, it can be useful to set the opacity lower in order to more easily identiy high density areas.) 
    d. You will notice that TMAX_6MO has a strong negative correlation with TMAX. Can you explain why this is?  
    e. You will notice that TMAX_3MO has a very weak correlation with TMAX. Can you explain why this is?  

2. Read in the file shifted_LAX_temps.csv into a DataFrame named lax.   
    a. Before doing any calculations, how do you think that the correlations for LAX will compare to those that you saw for BNA? Will the correlations be stronger than what you saw for BNA? weaker? about the same?
    b. Calculate the correlation between TMAX and all other temperature columns. Were you guesses from the previous question correct?
    c. You'll notice that the correlation between TMAX and TMIN is much smaller for LAX compared to BNA. Create a scatterplot showing TMAX vs TMIN for LAX. What would explain the lower correlation?

### Part 3: Penguins 

The file pengiuns.csv contains the [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/articles/intro.html), which contains size measurements for three penguin species observed on three islands in the Palmer Archipelago of Antarctica.

Read this dataset into a dataframe named *penguins*.

1. How many missing values are in this dataset? After checking this, use the dropna() method to remove any missing values.

2. Examine the distribution of penguin species by island. What do you find? (You might want to create a plot or two to aid in your analysis)

3. What do you find if you examine the distribution of weights by species? 

4. Create a scatterplot of bill depth vs. bill length. What do you notice from the scatterplot? What is the correlation between bill depth and bill length?

5. Color the scatterplot from the previous question by species. What do you notice now? 

6. Are there major differences in the distribution of species observed across the three years that the data was collected?

7. Inspect the relationship between body mass and flipper length. How is the relationship between these variables different than the one between bill length and bill depth that we observed above?

8. How does the distribution of body mass differ between male and female observations?

9. You can group by multiple variables simultaneously by passing a list into your groupby method. What do the differences in body mass between male and female penguins look like at a species level?