### Problem Statement: Temperature Data Analysis
### You have a list of daily average temperatures for a week. You need to analyze this data to provide insights:

### Calculate the average temperature for the week.
### Find the maximum and minimum temperatures recorded.
### Count how many days were above the weekly average temperature.

temperatures = [22, 25, 19, 24, 28, 21, 23]

# Task Breakdown
# - Calculate the average temperature for the week.
# - Find the maximum and minimum temperatures.
# - Count the number of days above the weekly average temperature.

# Hints:
# - You can use sum() and len() functions to calculate the average.
# - Python has built-in functions max() and min() for finding the maximum and minimum.
# - A for loop can be used to iterate over the list and count the days above the average.

# Exercise: Implement the Solution
# Write a Python script that processes the temperatures list according to the tasks outlined. You can break the problem into parts, and I'll guide you through each step. Let's start by calculating the average temperature for the week. Write the code to find this average and let me know what you get!

### Step 1: Calculate the Average Temperature

temperatures = [22, 25, 19, 24, 28, 21, 23]

# Calculate the sum of all temperatures
total_sum = sum(temperatures)

# Find the number of temperature entries
number_of_entries = len(temperatures)

# Calculate the average temperature
average_temperature = total_sum / number_of_entries

print(f"The average temperature for the week is {average_temperature}")


### Step 2: Find the Maximum and Minimum Temperatures
### Python provides built-in functions called max() and min() that make it easy to find the highest and lowest values in a list.

# Find the maximum temperature
max_temperature = max(temperatures)

# Find the minimum temperature
min_temperature = min(temperatures)

print(f"The maximum temperature for the week is {max_temperature}")
print(f"The minimum temperature for the week is {min_temperature}")

### Step 3: Count Days Above the Weekly Average Temperature
### To determine how many days had temperatures above the average, you’ll need to iterate over the temperatures list and count each day that exceeds the calculated average temperature.

# Initialize a counter for days above average temperature
days_above_average = 0

# Loop through each temperature in the list
for temperature in temperatures:
    # Check if the temperature is above the average
    if temperature > average_temperature:
        # Increment the counter
        days_above_average += 1

print(f"There are {days_above_average} days above the average temperature.")


