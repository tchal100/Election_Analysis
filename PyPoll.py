# The data we need to retrieve.
# 1.The totl number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes eachcandidate won
# 4. The total number of votes each candidate won
# 5. The winner of the elections based on popular vote.

# Assign a variable for the file to lload and the path.
file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')

# Open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)
    
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#  Open the elction results and reaf the file.
with open(file_to_load) as election_data:
    print(election_data)    

# Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")

# Create  filenme variable to a direct or indirect pth to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the width statement opent he file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
#close the file
outfile.close()


# Create  filenme variable to a direct or indirect pth to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the width statement opent he file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    txt_file.write("Counties in the Election"),
    txt_file.write("\n-----------------------")
# Write some data to the file.
    txt_file.write("\nArapahoe\nDenver\nJefferson")

 # Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Aaign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#  Open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)    

    # read and print the header row
    headers = next(file_reader)
    print(headers)
    
