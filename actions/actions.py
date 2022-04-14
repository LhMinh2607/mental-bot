# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from urllib.request import urlopen
import json
import random
url = ["https://api.pushshift.io/reddit/search/submission/?subreddit=crappydesign&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true", 
"https://api.pushshift.io/reddit/search/submission/?subreddit=programmerhumor&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=memes&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=artbreeder&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=wholesomememes&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true"]


  



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionSendPicture(Action):
        

    def name(self) -> Text:
        return "action_send_picture"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        urlIndex = random.randint(0, 4)
        response = urlopen(url[urlIndex])
        reddit_post = json.loads(response.read())
        index = random.randint(0, 100)
        print(index)
        print(reddit_post['data'][index]['full_link'])
        print(reddit_post['data'][index]['url'])

        
        
        if(reddit_post['data'][index]['is_video']=='true'):
            dispatcher.utter_message(response="utter_send_picture")
            dispatcher.utter_message(text=f"Video: "+reddit_post['data'][index]['full_link'])
        else:
            dispatcher.utter_message(response="utter_send_picture")
            dispatcher.utter_message(image=reddit_post['data'][index]['url'])
            dispatcher.utter_message(text=f"Nguồn: "+reddit_post['data'][index]['full_link'])

        return[]
