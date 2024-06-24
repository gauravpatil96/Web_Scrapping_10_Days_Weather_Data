# Web_Scrapping_10_Days_Weather_Data

This Python program scrapes weather data for a 10-day forecast from the specified URL on weather.com and saves the data into a CSV file.
Here’s a detailed description of what the program does:

Imports and Setup:
Imports required libraries: requests, BeautifulSoup from bs4, and pandas as pd.
Defines the URL for the 10-day weather forecast from weather.com.

Fetching the Web Page:
Uses requests.get(url).text to fetch the HTML content of the web page.

Parsing the HTML:
Creates a BeautifulSoup object to parse the HTML content using the 'html.parser'.

Extracting Weather Data:
Uses soup.find_all to find all relevant weather data elements:
ht: High temperatures.
lt: Low temperatures.
wc: Weather conditions.
rainp: Rain percentages.
wd: Wind speeds and directions.

Processing and Storing Data:
Initializes an empty list lis to store the weather data for each day.
Iterates over the length of the ht (high temperatures) list.

For each day, extracts the relevant data and stores it in a dictionary d1 with keys:
"Day High Temperature"
"Day Low Temperature"
"Weather Condition"
"Rain Percentage" (trims the first 4 characters)
"Wind Speed" (extracts text after the first space)
"Wind Direction" (extracts text before the first space)
Appends the dictionary d1 to the list lis.

Creating and Saving DataFrame:
Converts the list lis to a pandas DataFrame df.
Saves the DataFrame df to a CSV file named 'Weather_Data.csv'.
