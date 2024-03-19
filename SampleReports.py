# Generates sample daily report CSV files for the years 2018 to 2023.

import csv
import os
import calendar

# Define the directory path
directory_path = "/Users/priya/PycharmProjects/FileSorting/Daily_Reports_CSV"

# Creating the Daily_Reports_CSV directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

# Change working directory to the specified path
os.chdir(directory_path)

# Generating Sample CSV Files
def generate_sample_csv(year, month, day):
    """
       Generates a sample CSV file for a specific date.

       Args:
       - year (int): The year of the date.
       - month (int): The month of the date.
       - day (int): The day of the date.
       """
    month_name = calendar.month_name[month]         # get month, corresponding month number

    filename = f"{month_name.lower()}_{day:02d}_{year}_daily_report.csv"   # file name

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Title", "Content"])
        writer.writerow([f"{year}-{month:02d}-{day:02d}", f"{month_name} {day} {year} Daily Report", "Sample content"])

# Generate daily sample CSV files for years 2018 to 2023
for year in range(2018, 2024):
    for month in range(1, 13):
        num_days = calendar.monthrange(year, month)[1]

        for day in range(1, num_days + 1):
            generate_sample_csv(year, month, day)
