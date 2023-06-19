import csv
import re
import os




input_folder_path = '/Users/Admin/Desktop/Usernames/instacomm_csvs'


# Initialize a dictionary to keep track of unique usernames and their corresponding comments
usernames = {}


# Initialize a set to keep track of usernames without comments
usernames_without_comments = set()
import csv
import re
import os




input_folder_path = '/Users/Admin/Desktop/Names/reddit_csvs'


# Initialize a dictionary to keep track of unique usernames and their corresponding comments
usernames = {}


# Initialize a set to keep track of usernames without comments
usernames_without_comments = set()


# Get the list of CSV files in the input folder
csv_files = [filename for filename in os.listdir(input_folder_path) if filename.endswith('.csv')]


# # Loop through each CSV file in the current directory
# for filename in os.listdir(input_folder_path):
#     if filename.endswith('.csv'):


# Loop through each CSV file in the input folder
for file_count, filename in enumerate(csv_files, 1):
   # Open the input CSV file for reading
   with open(os.path.join(input_folder_path, filename), 'r', encoding='utf-8') as input_file:
       # Create CSV reader object
       reader = csv.reader(input_file)
      
       # Get the rows of the CSV file in a list
       rows = list(reader)


       # Get the total number of rows in the CSV file
       total_rows = len(rows)


       # Reset the reader to the beginning of the file
       input_file.seek(0)


       # Loop through each row in the input CSV file
       for row_count, row in enumerate(reader, 1):
           # Extract the username and comment from the current row
           username, comment = row[0], row[1]


           # If the comment is empty or contains only URLs, emojis, digits, or non-text characters, skip the row
           if not comment or all(char in '\n\t\x0b\x0c\r 0123456789' or ord(char) > 127 for char in comment):
               # Add the username to the set of usernames without comments
               usernames_without_comments.add(username)
               continue


           # Remove URLs, emojis, and digits from the comment
           comment = re.sub(r'http\S+', '', comment)
           comment = re.sub(r'[^\w\s]+|_', '', comment)
           comment = comment.encode('ascii', 'ignore').decode('ascii')
           comment = re.sub(r'\d+', '', comment)
           comment = comment.lower()


           # Trim the comment to 15 words if it's too long
           comment_words = comment.split()
           if len(comment_words) > 15:
               comment = ' '.join(comment_words[:15])


           # Add the username and comment to the dictionary
           if username in usernames:
               # If the username is already in the dictionary, update the comment
               if comment:
                   usernames[username] = comment
                   # Remove the username from the set of usernames without comments if it was in there
                   if username in usernames_without_comments:
                       usernames_without_comments.remove(username)
               else:
                   # Add the username to the set of usernames without comments if the comment is empty
                   usernames_without_comments.add(username)
           else:
               # If the username is not in the dictionary, add it with the current comment
               usernames[username] = comment


           # Print the progress message
           # print(f"We are processing {row_count}/{total_rows} rows for {filename}...", end='\r')
           print(f"We are processing file {file_count}/{len(csv_files)} - row {row_count}/{total_rows} for {filename}...", end='\r')


# Write the cleaned rows to the output CSV file
with open('cleaned_reddit_com/output.csv', 'w', encoding='utf-8', newline='') as output_file:
   # Create CSV writer object
   writer = csv.writer(output_file)
   for username, comment in usernames.items():
       # If the comment is empty or contains only URLs, emojis, digits, or non-text characters, skip writing to the output CSV file
       if not comment or all(char in '\n\t\x0b\x0c\r 0123456789' or ord(char) > 127 for char in comment):
           continue
       # Otherwise, write the cleaned row to the output CSV file
       writer.writerow([username, comment])


# Write the usernames without comments to the text file
with open('cleaned_reddit_com/usernames_without_comments.txt', 'w', encoding='utf-8') as no_comment_file:
   for username in usernames_without_comments:
       no_comment_file.write(username + '\n')
