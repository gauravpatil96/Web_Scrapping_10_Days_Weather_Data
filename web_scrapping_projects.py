
# **Weather Data Collection**


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for 10-day weather forecast
url = "https://weather.com/en-IN/weather/tenday/l/a5f0fe2ff9a40acc9ce62d67cd99439a71cde78cc0c5c1fbf6da052bef4cdba9"

# Fetch the web page content
re = requests.get(url).text

# Initialize an empty list to store weather data
lis = []

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(re, 'html.parser')

# Find all elements for high temperatures, low temperatures, weather conditions, rain percentages, and wind data
ht = soup.find_all('span', class_="DetailsSummary--highTempValue--3PjlX")
lt = soup.find_all('span', class_="DetailsSummary--lowTempValue--2tesQ")
wc = soup.find_all('span', class_="DetailsSummary--extendedData--307Ax")
rainp = soup.find_all('div', class_='DetailsSummary--precip--1a98O')
wd = soup.find_all('span', class_="Wind--windWrapper--3Ly7c DailyContent--value--1Jers DailyContent--windValue--JPpmk")

# Print the number of high temperature elements found
print(len(ht))

# Loop through each day's data and store it in a dictionary
for i in range(len(ht)):
    d1 = {
        "Day High Temperature": ht[i].text,
        "Day Low Temperature": lt[i].text,
        "Weather Condition": wc[i].text,
        "Rain Percentage": rainp[i].text[4:],  # Trim the first 4 characters
        "Wind Speed": wd[i].text[wd[i].text.find(" "):],  # Extract text after the first space
        "Wind Direction": wd[i].text[:wd[i].text.find(" ")]  # Extract text before the first space
    }
    lis.append(d1)

# Print an empty line for separation
print()

# Print the list of dictionaries containing weather data
print(lis)

# Convert the list to a pandas DataFrame
df = pd.DataFrame(lis)

# Save the DataFrame to a CSV file
df.to_csv('Weather_Data.csv', index=True)