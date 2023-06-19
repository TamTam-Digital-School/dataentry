import pandas as pd
import os
from tqdm import tqdm
import time
# import chardet




def process_csv_files(csv_files, output_folder):
   language_file_prefixes = {
       "en": "english", 'hi': "english", 'sw': "english", 'mt': "english", 'ur': "english",
       'af': "english", 'zu': "english", 'xh': "english", 'tn': "english",
       'st': "english", 'ts': "english", 'sn': "english", 'nd': "english",
       "fr": "french", 'crs': "french", 'fr': "french", 'ki': "french", 'ln': "french",
       'mg': "french", 'rn': "french", 'sg': "french", 'wo': "french",
       'ay': "spanish", 'ca': "spanish", 'es': "spanish", 'gl': "spanish",
       'gn': "spanish", 'oc': "spanish", 'qu': "spanish",
       'chk': "chinese", 'id': "chinese", 'km': "chinese", 'kos': "chinese",
       'ms': "chinese", 'pon': "chinese", 'ta': "chinese",
       'vi': "chinese", 'yap': "chinese", 'zh': "chinese",
       "ja": "japanese",
       "ko": "korean",
       "nl": "dutch",
       "pt": "portuguese",
       'be': "russian", 'et': "russian", 'ka': "russian", 'kk': "russian", 'ky': "russian",
       'lt': "russian", 'lv': "russian", 'ro': "russian", 'ru': "russian", 'tg': "russian",
       'tk': "russian", 'uk': "russian", 'uz': "russian",
       'de': "german",'it': "german", 'lb': "german", 'rm': "german"
       }
   users = {"influencers": set(), "simple_users": set()}
   start_time = time.time()




   for i, csv_file in enumerate(tqdm(csv_files)):
       # print(f"Processing file {i+1} of {len(os.listdir(input_folder))}: {csv_file}", end='\r')
       with open(csv_file, 'rb') as f:
           data = f.read()
           for encoding in ['utf-8', 'iso-8859-1', 'utf-16']:
               try:
                   # Check that the required columns are present in the CSV file
                   df = pd.read_csv(csv_file, usecols=["username", "language", "follower_count"], on_bad_lines='skip', encoding=encoding, engine='c')
                   assert all(col in df.columns for col in ["username", "language", "follower_count"])
                   break
               except (UnicodeDecodeError, AssertionError):
                   pass
       df['follower_count'] = pd.to_numeric(df['follower_count'], errors='coerce').fillna(0)
       df["username"] = df["username"].astype(str)
       for _, row in df.iterrows():
           username = row["username"].lower()
           language = row["language"]
           # follower_count = int(float(row["follower_count"]))
           follower_count = int(float(row["follower_count"])) if isinstance(row["follower_count"], str) else int(row["follower_count"])
           # check if the Twitter user is a celebrity by searching for their name on Google
           if follower_count >= 10000 and username not in users["influencers"]:
               users["influencers"].add(username)
               file_prefix = language_file_prefixes.get(language, "unknown")
               output_file_name = os.path.join(output_folder, f"{file_prefix}_influencers.txt")
               with open(output_file_name, "a") as outfile:
                   outfile.write(f"@{username}\n")
           else:
               if username not in users["simple_users"]:
                   users["simple_users"].add(username)
                   file_prefix = language_file_prefixes.get(language, "unknown")
                   output_file_name = os.path.join(output_folder, f"{file_prefix}_simple_user.txt")
                   with open(output_file_name, "a") as outfile:
                       outfile.write(f"@{username}\n")


      
       # Move the processed CSV file to the csv_processed folder
       csv_file_name = os.path.basename(csv_file)
       csv_processed_folder = os.path.join(output_folder, "csv_processed")
       if not os.path.exists(csv_processed_folder):
           os.makedirs(csv_processed_folder)
       os.rename(csv_file, os.path.join(csv_processed_folder, csv_file_name))




       elapsed_time = time.time() - start_time
       rest_time = (elapsed_time / (i + 1)) * (len(csv_files) - (i + 1))
       progress_percentage = (i + 1) / len(csv_files) * 100
   print(f"Progress: {progress_percentage:.2f}% - Elapsed time: {elapsed_time:.2f}s - Estimated rest time: {rest_time:.2f}s", end='\r')
   return users




# Set the input and output folder paths
input_folder = '/Users/Admin/Desktop/twitter_treatment/tweets_csvs_with_followers_count_to_do'
output_folder = '/Users/Admin/Desktop/twitter_treatment/final_result'


# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
   os.makedirs(output_folder)


# List all CSV files in the input folder
csv_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.csv')]


# Process the CSV files and output the results to the output folder
users = process_csv_files(csv_files, output_folder)