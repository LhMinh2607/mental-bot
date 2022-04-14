from urllib.request import urlopen

import json
import random
url = ["https://api.pushshift.io/reddit/search/submission/?subreddit=crappydesign&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true", 
"https://api.pushshift.io/reddit/search/submission/?subreddit=programmerhumor&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=memes&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=artbreeder&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=softwaregore&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true"]
  
urlIndex = random.randint(0, 4)
response = urlopen(url[urlIndex])
  

reddit_post = json.loads(response.read())
  

# print(random.choice(reddit_post).full_link)

# for each in reddit_post['data']:
#     if each['author'] == "the_Diva":
#         print(each['full_link'])
#         print(each['preview']['images'][0]['source']['url'])


index = random.randint(0, 100)
print(index)
print(reddit_post['data'][index]['full_link'])
# print(reddit_post['data'][index]['preview']['images'][0]['source']['url'])
if(reddit_post['data'][index]['is_video']=='false'):
    print(reddit_post['data'][index]['url'])


# print(reddit_post[0])