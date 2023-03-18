import os
import sqlite3

# Define input and output paths
input_path = os.path.normpath(r"C:\YOUR PATH\repositoryR2.db") #edit with your path, leave repositoryR2.db 
output_path = os.path.normpath (r"C:\YOUR PATH") # edit with your path

# Connect to input database
input_conn = sqlite3.connect(input_path)
input_c = input_conn.cursor()

# Define output folders
studio_folder = os.path.join(output_path, "Studio")
direct_folder = os.path.join(output_path, "Direct")

# Verify output folders exist
if not os.path.exists(studio_folder):
    print("studio folder does not exist")
    exit()
if not os.path.exists(direct_folder):
    print("direct folder does not exist")
    exit()

# Select all rigs from input database
input_c.execute("SELECT * FROM Rigs")
rigs = input_c.fetchall()

# Loop through each rig
for rig in rigs:

    # Extract relevant columns
    source_amp = rig[11]
    amp_name = rig[9]
    source_cabinet = rig[21]
    rig_id = rig[0]
        
    # Select the blob    
    input_c.execute("SELECT id, data FROM Rigs_blobs WHERE id = ?",(rig_id,))
    the_blob = input_c.fetchone()
        
    # Determine destination folder based on source cabinet value
    if source_cabinet in ["N/A", ""]:
        dest_folder = direct_folder
    else:
        dest_folder = studio_folder

    # Verify manufacturer folder exists
    manufacturer_folder = os.path.join(dest_folder, source_amp)
    if not os.path.exists(manufacturer_folder):
        print("manf folder does not exist")
        exit()

    # Verify rig folder exists
    rig_folder = os.path.join(manufacturer_folder, amp_name)
    if not os.path.exists(rig_folder):
        print("rig folder does not exist")
        exit()
    
    # Sets path to output database
    final_destination = os.path.join(rig_folder, "repositoryR2.db")
    if not os.path.exists(final_destination):
        print("no output database")
        exit()
    
    # Connect to output daatabase
    output_conn = sqlite3.connect(final_destination)    
    output_c = output_conn.cursor()

    # Write the data
    output_c.execute("INSERT OR REPLACE INTO Rigs ('id', 'Filename', 'File', 'Name', 'Date', 'Author', 'Comment', 'Favourite', 'Gain', 'Amp Name', 'Amp Author', 'Source Amp', 'Amp Comment', 'Amp Creation Artist', 'Amp Model', 'Amp Channel', 'Amp Pickup', 'Amp Model Year', 'Cabinet Name', 'Cabinet Author', 'source Cabinet', 'Mic Type', 'Cabinet Comment', 'Mic Position', 'Cabinet Configuration', 'Source Cabinet Model', 'Cabinet Creation Artist', 'Amp Location', 'Cabinet Location', 'Kind', 'Vote', 'Speaker Manufacturer', 'Speaker Model', 'Cabinet Type') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(rig))
    output_c.execute("INSERT OR REPLACE INTO Rigs_blobs ('id', 'data') VALUES (?, ?)", (the_blob))
    output_conn.commit()

    # Close the output database
    output_conn.close()

    
# Close input database connection
input_conn.close()
