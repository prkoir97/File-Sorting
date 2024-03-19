# Merges daily report CSV files into monthly CSV files, and moves them to a separate directory, then deletes Daily_Reports_CSV directory

import os
import shutil
import csv
from collections import defaultdict

# Source and destination directories
source = "/Users/priya/PycharmProjects/FileSorting/Daily_Reports_CSV"
destination = "/Users/priya/PycharmProjects/FileSorting/Monthly_Reports_CSV"

# Function to merge daily reports into one monthly CSV
def merge_daily_reports(year_directory):
    # Dictionary to store merged file paths for each month
    month_files = defaultdict(list)

    # Loop through month folders in the year directory
    for month_folder in sorted(os.listdir(year_directory)):  # Sort month folders chronologically
        month_path = os.path.join(year_directory, month_folder)
        if os.path.isdir(month_path):
            merged_data = []

            # Get list of daily report files and sort them
            daily_reports = [report for report in os.listdir(month_path) if report.endswith(".csv")]
            daily_reports.sort()  # Sort daily report files

            # Merge daily reports into one monthly CSV
            for daily_report in daily_reports:
                daily_report_path = os.path.join(month_path, daily_report)
                with open(daily_report_path, "r", newline="") as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header row
                    merged_data.extend(reader)

            # Define the filename for the merged CSV
            merged_filename = f"{year_directory[-4:]}_{month_folder}.csv"
            merged_path = os.path.join(destination, year_directory[-4:], merged_filename)

            # Ensure the directory structure exists before writing the merged file
            os.makedirs(os.path.dirname(merged_path), exist_ok=True)

            # Write the merged CSV to the destination directory
            with open(merged_path, "w", newline="") as merged_file:
                writer = csv.writer(merged_file)
                writer.writerows(merged_data)

            # Store the merged file paths for sorting
            month_files[month_folder] = merged_path

    # Move the merged CSVs to year folders
    for month_folder, merged_path in month_files.items():
        year_month_directory = os.path.join(destination, year_directory[-4:])
        if not os.path.exists(year_month_directory):
            os.makedirs(year_month_directory)
        new_merged_path = os.path.join(year_month_directory, os.path.basename(merged_path))
        shutil.move(merged_path, new_merged_path)

# Merge daily reports for each year
for year_folder in os.listdir(source):
    year_path = os.path.join(source, year_folder)
    if os.path.isdir(year_path):
        merge_daily_reports(year_path)

print("Daily reports merged into monthly CSVs.")

# Delete the Daily_Reports_CSV folder
try:
    shutil.rmtree(source)
    print("Daily_Reports_CSV folder deleted successfully.")
except Exception as e:
    print(f"Error deleting Daily_Reports_CSV folder: {e}")
