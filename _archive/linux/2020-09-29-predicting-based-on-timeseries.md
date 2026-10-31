---
title: "Predicting based on timeseries"
category: linux
---

- Suppose we have a dataset of phone pickups and timestamps, and we want to know if the chance of pickup varies with time. A question on the Internet asks whether to use linear regression, and whether 1-hot encoding would be useful.
- Linear regression finds the best fit line between the input and the target variable. It works when the target is proportional to the input. But the probability of picking up a phone call is not proportional to the hour of day on a 24 hour basis - 8am might have high rate, 9am not, and 12 again have a high rate.
- We can think about 1-hot encoding. We have timestamps and 0/1 for pickup or no pickup. If we 1-hot encode the hour, we'll get 24 independent variables that take on values of 0 or 1 . For the regression problem we'll be fitting 24 coefficients for these 24 variables to predict call pickup. Each coefficient could be interpreted as the probability of pickup during the corresponding hour. Time is the independent variable, the 1-hot encoding represents the hour of that timestamp, and the prediction of the regression is just the probability of pickup based on the dataset.
- To find out if this is a good approach, we need to think about what we're trying to do - the objective. If the objective is to know whether the probability of pickup varies over the hours, then the variation in the coefficients tells us how the hour predicts the probability of pickup.
- But using linear regression here is overly complex - we get the same result by grouping your data by hour and then finding the fraction of pickups over total calls.
