# Daily Reports Organizer

This Python script suite is designed for practice purposes. It demonstrates how to generate, organize, and merge daily report CSV files using Python scripts. It serves as a learning exercise to understand file manipulation, CSV generation, and basic automation techniques in Python.

## File Structure

- **SampleReports.py**:  This script automates the generation of sample daily report CSV files covering the years 2018 to 2023. It utilizes the `csv` library to create CSV files, with each file representing a daily report for a specific date. The reports are named based on the date and saved in the "Daily_Reports_CSV" directory.
- **OrganizeDailyReports.py**: This script facilitates the efficient organization of daily report CSV files by renaming and categorizing them into folders based on their corresponding year and month. It parses the filenames to extract the date information, then creates directories for each year and month if they don't exist already, and moves the files accordingly, ensuring a structured and easily navigable file hierarchy.
- **MonthlyMerge.py**: This script automates the process of merging individual daily report CSV files into monthly CSV files, ensuring a more manageable and organized structure for the data. It follows a clear workflow of processing files by year and month, merging them into larger units, and then cleaning up the workspace by deleting redundant directories.
## Dependencies

Ensure you have the following dependencies installed:

- **csv**: A Python library for creating and manipulating CSV files.
- **calendar**: A module to work with dates and calendars.
- **os**: A module to interact with the operating system, such as file operations.
- **shutil**: A module for high-level file operations.
- **collections.defaultdict**: A subclass of dictionary that provides default values for keys.

## Usage

1. Clone the repository or download the script files.
2. Ensure you have Python installed on your system.
3. Install the required dependencies as mentioned above.
4. Run each script in the following order:

    ```
    python SampleReports.py
    python OrganizeDailyReports.py
    python MonthlyMerge.py
    ```

## Note

- This code is provided for educational and practice purposes only. It may not be suitable for production environments without further modifications and testing.
- Ensure that the file paths specified in the scripts are correct and correspond to your system's directory structure.
- Customize the scripts as per your requirements, such as changing the source and destination directories.
- These scripts are designed to work with Python 3.x. Make sure you have a compatible version installed.
