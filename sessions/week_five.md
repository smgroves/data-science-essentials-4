##### Week 5:
Building a Classifier
- Overview of Machine Learning
- Feature Engineering
- One hot encoding to encode categorical variables for use in a model
- Creating training and test data

Coding tasks:
The file brfss.csv contains a subset of the responses and variables from the [2019 Behavioral Risk Factor Surveillance System (BRFSS)](https://www.cdc.gov/brfss/). This dataset can be downloaded using this link: [https://drive.google.com/file/d/1acJKmT2aFf2nZl_VYLE897yx0LPNajoY/view?usp=sharing](https://drive.google.com/file/d/1acJKmT2aFf2nZl_VYLE897yx0LPNajoY/view?usp=sharing).

A detailed Codebook can be found [here](https://www.cdc.gov/brfss/annual_data/2019/pdf/codebook19_llcp-v2-508.HTML).

Our target variable is the CHECKUP1 column, which contains the responses to the question "About how long has it been since you last visited a doctor for a routine checkup?   [A routine checkup is a general physical exam, not an exam for a specific injury, illness, or condition.]" Specifically, we want to try and predict if someone gives an answer besides "Within past year (anytime less than 12 months ago)".

First, create a new coumn, "target" by converting this to a binary outcome. After you do this, drop the CHECKUP1 column from your dataframe so that you don't accidentally make predictions based off of it.

Then, experiment with making a logistic regression model to predict the target variable using one or more of the other columns. Note that you will need to convert the precictor columns into dummy variable prior to fitting a model. What do you find?