from math import inf
import pandas as pd
import os

# Set base folder path
base_folder = "../input"


def combine_files_in_folder(folder_path, max_files=inf):
    combined_data = pd.DataFrame()
    file_count = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_count += 1
            if file_count > max_files:
                break
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)

            # Extract month from filename and year from folder path
            month = file_name.split("_")[-1]
            year = os.path.basename(folder_path)  # Extract year from folder name

            # Create the "period" column with month and year
            df["period"] = f"{month} {year}"

            print(f"Entries from {file_name}:")
            print(df)  # Display entries for each file

            combined_data = pd.concat([combined_data, df], ignore_index=True)
            print("Total files combined: ", file_count)

    return combined_data


# Process folders in specified order and combine data
folders = ["2018", "2017", "2016"]
all_data = pd.DataFrame()
for folder in folders:
    folder_loc = os.path.join(base_folder, folder)
    folder_data = combine_files_in_folder(folder_loc, 6 if folder == "2016" else inf)
    all_data = pd.concat([all_data, folder_data], ignore_index=True)

# Write final integrated file
all_data.to_csv("../input/Integrated_Data.csv", index=False)
