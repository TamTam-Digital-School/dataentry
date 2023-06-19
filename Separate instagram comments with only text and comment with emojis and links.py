import csv
import re
import os




input_folder_path = '/Users/Admin/Desktop/Usernames/instacomm_csvs'


# Initialize a dictionary to keep track of unique usernames and their corresponding comments
usernames = {}


# Initialize a set to keep track of usernames without comments
usernames_without_comments = set()