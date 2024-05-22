
import matplotlib.pyplot as plt
import pandas as pd
import random
import csv

# Read in Titanic data
titanic_df = pd.read_csv("titanic_dataset.csv", index_col="PassengerId")

# SCATTERPLOT OF AGE VS FARE PAID
# Create figure and axes objects
figure_1, ax_scat = plt.subplots()

# Set axis labels
ax_scat.set_xlabel("Age")
ax_scat.set_ylabel("Fare Paid")

# Generate scatterplot of age (x-axis) vs fare paid (y-axis)
ax_scat.scatter(titanic_df["Age"], titanic_df["Fare"])

# Show the plot
figure_1.show()

# HISTOGRAM OF AGES
# Create figure and axes objects
figure_2, ax_hist = plt.subplots()

# Set axis labels
ax_hist.set_xlabel("Age")
ax_hist.set_ylabel("Fare Paid")

# Variable to store number of bins
bins = 50

# Generate histogram
ax_hist.hist(titanic_df["Age"], bins=bins)

# Show the plot
figure_2.show()

# LINE PLOT OF MEDICATIONS USED
# Read in medications data
meds_df = pd.read_csv("meds_used_per_day.csv")

# Create figure and axes objects
figure_3, ax_line = plt.subplots()

# Set axis labels
ax_line.set_xlabel("Day")
ax_line.set_ylabel("Total Medications Used")

# Create list of day numbers
day_numbers = [x+1 for x in range(28)]

# Plot each line with a different colour and style
# Don't forget the cheatsheets here : https://matplotlib.org/cheatsheets/
ax_line.plot(day_numbers, meds_df["Run 1"], color="red", linestyle="-",
             label="Run 1")
ax_line.plot(day_numbers, meds_df["Run 2"], color="black", linestyle=":",
             label="Run 2")
ax_line.plot(day_numbers, meds_df["Run 3"], color="blueviolet", 
             linestyle="-.", label="Run 3")

# Create and set up a legend
ax_line.legend(loc="upper right")

# Show the plot
figure_3.show()

