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

# 1. Initialize a total vote counter.
total_votes = 0 

# Candidate_options
candidate_options =[] 
#1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#  Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)    

    # read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count. 
        total_votes += 1 

        # Print the candidate name for each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentageof votes for each candidate by looping through the counts.
    # 1. Interate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #4. Print the candidate name and the percentage of votes.
        candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)  
        # Determine the winning vote count and candidate
        # Determine if the votes are greter than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes 
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
                
    # print out the winning candidate,vote count and percentage to terminal.
    winning_candidate_summary = (
        f"------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count:{winning_count:,}\n"
        f"winning Percentage:{winning_percentage:.1f}%\n"
        f"-------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

 


    
