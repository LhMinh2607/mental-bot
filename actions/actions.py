# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from psycopg2 import Date

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ReminderScheduled, ReminderCancelled, SlotSet, AllSlotsReset

from urllib.request import urlopen
import json
import random

import pymongo 
import datetime

from bson.objectid import ObjectId

url = ["https://api.pushshift.io/reddit/search/submission/?subreddit=crappydesign&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true", 
"https://api.pushshift.io/reddit/search/submission/?subreddit=programmerhumor&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=memes&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=artbreeder&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=wholesomememes&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true"]

mentalBotDB = pymongo.MongoClient("mongodb://localhost:27017/")
mentalBot = mentalBotDB["mentalBotDB"]

usersCollection = mentalBot["users"]

remindersCollection = mentalBot["reminders"]

userId = ""


class ActionInitialGreeting(Action):

    def name(self) -> Text:
        return "action_initial_greeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SlotSet("userId", None)

        entities = tracker.latest_message.get("entities")

        userId = entities[0]['value']

        print(userId)

        usersCollection = mentalBot["users"]

        user = usersCollection.find_one({"_id": ObjectId(str(userId))})

        print(user['username'])

        print("action_initial_greeting get called")

        dispatcher.utter_message(response="utter_greet")

        return[SlotSet("user", str(user['username'])), SlotSet("userId", str(user['_id']))]


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

# class ActionAskForTimer(Action):
#     """Schedules a reminder, supplied with the last message's entities."""

#     def name(self) -> Text:
#         return "action_ask_for_timer"

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         # next(tracker.get_latest_entity_values(entity_type="timer", entity_role="hours"))

#         dispatcher.utter_message("Mình sẽ nhắn lại cho bạn trong 5s. (Đang test)")
#         date = datetime.datetime.now() + datetime.timedelta(hours=1)

#         entities = tracker.latest_message.get("entities")

#         print(tracker.latest_message)
#         print(tracker.latest_message.get("entities"))
#         print(entities)


#         mydict = { "userId": "6258e2b0ee1e676f8626d4bd", "username": "LhMinh2607", "reminder": entities, "createdAt": datetime.datetime.now(), "duration": 3600}

#         remindersCollection.insert_one(mydict)

#         # SlotSet("activity", None) #reset "activity" slot
#         # AllSlotsReset()

#         reminder = ReminderScheduled(
#             "EXTERNAL_reminder",
#             trigger_date_time=date,
#             entities=entities,
#             name="my_reminder",
#             kill_on_user_message=False,
#         )

#         return [reminder]


class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # next(tracker.get_latest_entity_values(entity_type="timer", entity_role="hours"))

        userId = tracker.get_slot("userId")
        
        entities = tracker.latest_message.get("entities")

        print(tracker.latest_message)
        print(tracker.latest_message.get("entities"))
        print(entities[0]["value"])
        print(entities[1]["value"])


        if entities[1] != "None":
            duration = entities[1]['value']
        else:
            duration="1h00m00s"
        print(duration)

        splitTimerHour = duration.split('h')
        splitTimerMinute = splitTimerHour[1].split('m')
        splitTimerSecond = splitTimerMinute[1].split('s')

        print(splitTimerHour)
        print(splitTimerMinute)
        print(splitTimerSecond)

        date = datetime.datetime.now() + datetime.timedelta(hours= int(splitTimerHour[0]), minutes=int(splitTimerMinute[0]), seconds=int(splitTimerSecond[0]))


        mydict = { "userId": str(userId), "username": "Nam", "reminder": entities[0], "createdAt": datetime.datetime.now(), "duration": entities[1]}

        remindersCollection.insert_one(mydict)

        dispatcher.utter_message("Mình sẽ nhắn lại cho bạn trong " + entities[1]['value'] + " (Beta)")


        # SlotSet("activity", None) #reset "activity" slot
        # AllSlotsReset()

        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities=entities[0],
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]


class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_remind"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
    
        userId = tracker.get_slot("userId")
        # for obj in remindersCollection.find().sort([('createdAt', -1)]):
        #     if obj['userId'] == "6258e2b0ee1e676f8626d4bd":
        #         # activity = next(tracker.get_slot("activity"), None)
        #         activity = obj["reminder"][0]["value"]
        #         print(activity)
        #         dispatcher.utter_message(response="utter_reminder_message")

        for obj in remindersCollection.find().sort([('createdAt', -1)]):
            if obj['userId'] == str(userId):
                # activity = next(tracker.get_slot("activity"), None)
                activity = obj["reminder"]["value"]
                print(activity)
                dispatcher.utter_message(response="utter_reminder_message")
                break
        return []


class ActionCancelReminder(Action):
    def name(self):
        return "action_cancel_reminder"

    def run(self, dispatcher, tracker, domain):  
        ####some code or no code hereSlotSet("activity", None)
        return[ReminderCancelled]


class ActionShowUserInfo(Action):

    def name(self) -> Text:
        return "action_show_user_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        userId = tracker.get_slot("userId")

        dispatcher.utter_message(response="utter_respond_to_user_info_req")

        usersCollection = mentalBot["users"]

        user = usersCollection.find_one({"_id": ObjectId(str(userId))})

        # dispatcher.utter_message(text=f"Tên đầy đủ của bạn là "+user['name'])
        # dispatcher.utter_message(text=f"Username của bạn là "+user['username'])
        # dispatcher.utter_message(text=f"Nghề nghiệp của bạn là "+user['occupation'])
        # dispatcher.utter_message(text=f"Số điện thoại của bạn là "+user['phoneNumber'])
        # dispatcher.utter_message(text=f"Email của bạn là "+user['email'])
        # dispatcher.utter_message(text=f"Ngày tháng năm sinh của bạn là "+str(user['dob'])[:10])
        # # dispatcher.utter_message(text=f"Bạn "+datetime.today().year - user['dob'][:4]+" tuổi")
        # dispatcher.utter_message(text=f"Tâm trạng hiện tại của bạn do bạn cung cấp là đang "+user['mood'])
        # dispatcher.utter_message(text=f"Tiến độ của bạn là "+user['progress'])

        print(user['name'])
        print(user['username'])
        print(user['occupation'])
        print(user['phoneNumber'])
        print(user['email'])
        print(user['dob'])
        print(user['mood'])
        print(user['progress'])

        dispatcher.utter_message(text=f"Tên đầy đủ của bạn là "+str(user['name'])+"\n"+
        "Username của bạn là "+str(user['username'])+"\n"+
        "Nghề nghiệp của bạn là "+str(user['occupation'])+"\n"+
        "Số điện thoại của bạn là "+str(user['phoneNumber'])+"\n"+
        "Email của bạn là "+str(user['email'])+"\n"+
        "Ngày tháng năm sinh của bạn là "+str(user['dob'])[:10]+"\n"+
        "Tâm trạng hiện tại của bạn do bạn cung cấp là đang "+str(user['mood'])+"\n"
        "Tiến độ của bạn là "+str(user['progress'])+"\n")

        return[]


class ActionNoteMood(Action):
    def name(self):
        return "action_note_mood"

    def run(self, dispatcher, tracker, domain):
        userId = tracker.get_slot("userId") 
        mood = tracker.latest_message.get("entities") 


        print("action_node_mood is called")
        print(mood[0]["value"])
        usersCollection.find_one_and_update({'_id': ObjectId(str(userId))}, update={"$set": {'mood': mood[0]["value"]}})

        dispatcher.utter_message(response="action_note_mood")

        ####some code or no code here SlotSet("activity", None)
        return[]

class FollowUpMood(Action):
    def name(self):
        return "action_follow_up_mood"

    def run(self, dispatcher, tracker, domain):
        #follow up to user, ask them about their previous mood log

        return[]