import os
import shutil
import sqlite3

# Define input and output paths
input_path = r"C:\YOUR PATH\repositoryR2.db" # edit with your path, leave repositoryR2.db
output_path = r"C:\YOUR PATH" # edit with your path

# Connect to input database
input_conn = sqlite3.connect(input_path)
input_c = input_conn.cursor()

# Define output folders
studio_folder = os.path.join(output_path, "Studio")
direct_folder = os.path.join(output_path, "Direct")

# Create output folders if they don't already exist
if not os.path.exists(studio_folder):
    os.makedirs(studio_folder)
if not os.path.exists(direct_folder):
    os.makedirs(direct_folder)

# Select all rigs from input database
input_c.execute("SELECT * FROM Rigs")
rigs = input_c.fetchall()

# Loop through each rig
for rig in rigs:
    # Extract relevant columns
    source_amp = rig[11]
    amp_name = rig[9]
    source_cabinet = rig[21]

    # Determine destination folder based on source cabinet value
    if source_cabinet in ["N/A", ""]:
        dest_folder = direct_folder
    else:
        dest_folder = studio_folder

    # Create manufacturer folder if it doesn't already exist
    manufacturer_folder = os.path.join(dest_folder, source_amp)
    if not os.path.exists(manufacturer_folder):
        os.makedirs(manufacturer_folder)

    # Create rig folder if it doesn't already exist
    rig_folder = os.path.join(manufacturer_folder, amp_name)
    if not os.path.exists(rig_folder):
        os.makedirs(rig_folder)

   

# Close input database connection
input_conn.close()
