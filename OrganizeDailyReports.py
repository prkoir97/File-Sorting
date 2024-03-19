# Renames and organizes daily report CSV files into folders by corresponding year and month

import os
import shutil
import calendar

# Define the source directory containing the reports
source_directory = "/Users/priya/PycharmProjects/FileSorting/Daily_Reports_CSV"

# Change working directory to the source directory
os.chdir(source_directory)

# List files in the directory
files = os.listdir()

# Create a dictionary to map month names to their respective numbers
month_mapping = {
    'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06',
    'july': '07', 'august': '08', 'september': '09', 'october': '10', 'november': '11', 'december': '12'
}

# Create a dictionary to store file names grouped by year and month
files_by_year_month = {}

# Group files by year and month
for file in files:
    if file.lower().endswith(".csv"):  # Change to CSV extension
        # Parse the month, day, and year from the filename
        parts = file.split("_")
        month_str, day_str, year_str, *_ = parts[0].split("_") + parts[1:]

        try:
            # Convert to YYMMDD format
            new_filename = f"{year_str[-2:]}{month_mapping[month_str.lower()]}{day_str.zfill(2)}_report.csv"  # Change to CSV extension

            # Add the file to the corresponding year and month's list
            year = int(year_str)
            month_num = int(month_mapping[month_str.lower()])
            key = (year, month_num)
            if key not in files_by_year_month:
                files_by_year_month[key] = []
            files_by_year_month[key].append((file, new_filename))

        except KeyError:
            print(f"Error parsing month from filename '{file}'")

# Create directories for each year and month, then move files
for (year, month), files_in_month in files_by_year_month.items():
    year_directory = os.path.join(source_directory, str(year))
    if not os.path.exists(year_directory):
        os.mkdir(year_directory)
        print(f"Created directory '{year_directory}' for year {year}")

    month_directory = os.path.join(year_directory, calendar.month_name[month])
    if not os.path.exists(month_directory):
        os.mkdir(month_directory)
        print(f"Created directory '{month_directory}' for {calendar.month_name[month]}")

    for file, new_filename in files_in_month:
        destination_path = os.path.join(month_directory, new_filename)
        source_path = os.path.join(source_directory, file)
        shutil.move(source_path, destination_path)

print("Moved daily reports to designated folders.")
