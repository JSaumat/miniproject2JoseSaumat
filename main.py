### INF601 - Advanced Programming in Python
### Jose Saumat
### Mini Project 2

# Imported packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import requests

# Create the charts folder to hold the charts created by the program
os.makedirs("charts", exist_ok=True)

# List of the 10 breeds to include
breeds_to_include = [
    "Boxer", "Beagle", "Alaskan Husky", "Basset Hound", "Border Collie",
    "Chow Chow", "German Shepherd Dog", "Golden Retriever", "Great Dane", "Greyhound"
]

# API url
url = "https://api.thedogapi.com/v1/breeds"

# Gets data from API url
response = requests.get(url, headers=headers)
data = response.json()

# Converts data pulled to DataFrame
df = pd.DataFrame(data)

# Extracts the relevant columns (name and life span)
df = df[['name', 'life_span']]

# Filters information based on the information in list of breeds_to_include
df = df[df['name'].isin(breeds_to_include)]

# Function to extract min and max life expectancy from the API
def extract_lifespan(life_span):
    if not isinstance(life_span, str):
        return None, None
    numbers = [int(s) for s in life_span.split() if s.isdigit()]
    if len(numbers) == 2:
        return numbers[0], numbers[1]  # min and max
    return None, None  # If there's no range or invalid data

df[['min_life_span', 'max_life_span']] = pd.DataFrame(df['life_span'].apply(extract_lifespan).tolist(), index=df.index)

# Drops NaN values
df = df.dropna()

# Create the "charts" folder if it doesn't exist
if not os.path.exists('charts'):
    os.makedirs('charts')

# Plot for the min and max life expectancy side by side
plt.figure(figsize=(12, 8))

# Stem plot for the min and max values
plt.stem(df['name'], df['min_life_span'], basefmt=" ", linefmt='-g', markerfmt='og', label='Min Life Expectancy')
plt.stem(df['name'], df['max_life_span'], basefmt=" ", linefmt='-r', markerfmt='or', label='Max Life Expectancy')

# Labeling for the plot
plt.xlabel('Dog Breed', fontsize=12)
plt.ylabel('Life Expectancy (Years)', fontsize=12)
plt.title('Dog Breeds Min & Max Life Expectancy', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=8)  # Slanted labels on x-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adds a legend to differentiate min and max
plt.legend()

# Saves the plot to the "charts" folder
plt.tight_layout()
plt.savefig('charts/dog_life_expectancy_min_max_stem_plot.png')

# Shows the plot
plt.show()

# Prints out the min and max life expectancy for each breed I chose
print(df[['name', 'min_life_span', 'max_life_span']])