
import snscrape.modules.twitter as sntwitter
import csv


limit = 1500000
tweets_list = []
counter = 0


with open('me zh.csv', 'w', encoding='utf-8', newline='') as f:
   writer = csv.writer(f, escapechar='\\')
   writer.writerow(["username", "tweet", "language", "follower_count"]) # write header row
   for tweet in sntwitter.TwitterSearchScraper('me lang:zh').get_items():
       if len(tweets_list) == limit:
           break
       else:
           tweets_list.append([tweet.user.username, tweet.rawContent, tweet.lang, tweet.user.followersCount])
           writer.writerow([tweet.user.username, tweet.rawContent, tweet.lang, tweet.user.followersCount]) # write row to CSV
           counter += 1
           print(f"{counter} tweets extracted.", end="\r")


print("Extraction complete!")