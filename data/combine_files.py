import pandas as pd
import os

# Specify the directory containing your CSV files
directory = '/home/szymon/Git/sandbox/data'  # Replace with the actual path to your CSV files

# Initialize a list to hold dataframes
all_dataframes = []

# Loop over all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # Check if the file is a CSV
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame
        df = df.drop(columns=['Id'])  # Drop the 'Id' column
        all_dataframes.append(df)  # Append the DataFrame to the list

# Concatenate all dataframes into one
combined_df = pd.concat(all_dataframes, ignore_index=True)

# Create a new 'Id' column starting from 1
combined_df.insert(0, 'Id', range(1, len(combined_df) + 1))

# Save the combined dataframe to a new CSV file
combined_df.to_csv('combined_output.csv', index=False)

print("CSV files have been successfully merged into 'combined_output.csv'")