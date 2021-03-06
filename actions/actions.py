# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from __future__ import annotations
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
import http.client

from decouple import config

from googletrans import Translator


url = ["https://api.pushshift.io/reddit/search/submission/?subreddit=crappydesign&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true", 
"https://api.pushshift.io/reddit/search/submission/?subreddit=programmerhumor&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=memes&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=artbreeder&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true",
"https://api.pushshift.io/reddit/search/submission/?subreddit=wholesomememes&sort=desc&sort_type=score&size=100&user_removed=false&mod_removed=false&over_18=false&is_video=false&is_original_content=true"]

mentalBotDB = pymongo.MongoClient("mongodb://localhost:27017/")
mentalBot = mentalBotDB["mentalBotDB"]

usersCollection = mentalBot["users"]

remindersCollection = mentalBot["reminders"]

userlogs = mentalBot["userlogs"]

feedbacksCollection = mentalBot["feedbacks"]

imageSearchLogsCollection = mentalBot["imageSearchLogs"]

userId = ""

RAPID_API_KEY = config("RAPID_API_KEY")
RAPID_API_HOST = config("RAPID_API_KEY")





class ActionInitialGreeting(Action):

    def name(self) -> Text:
        return "action_initial_greeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SlotSet("userId", None)

        
        entities = tracker.latest_message.get("entities")

        if entities:
            userId = entities[0]['value']

            print(userId)

            usersCollection = mentalBot["users"]

            user = usersCollection.find_one({"_id": ObjectId(str(userId))})

            print(user['username'])

            print("action_initial_greeting get called")

            dispatcher.utter_message(response="utter_greet")

            return[SlotSet("user", str(user['username'])), SlotSet("userId", str(user['_id']))]
        
        else:
            dispatcher.utter_message(response="utter_ask_to_repeat")
            return []


class ActionSendPicture(Action):
        

    def name(self) -> Text:
        return "action_send_picture"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            query = tracker.latest_message.get('text')
            query = query.replace("g???i", "")
            query = query.replace("h??nh", "")
            query = query.replace("xin", "")
            query = query.replace("G???i", "")
            query = query.replace("H??nh", "")
            query = query.replace("Xin", "")
            query = query.replace("???nh", "")   
            query = query.replace("???nh", "")
            query = query.replace("N???a", "")
            query = query.replace("n???a", "")
            query = query.replace("??i", "")
            query = query.replace("??i", "")
            query = query.replace(" ","%20")
            translator = Translator()
            enQuery = translator.translate(query, dest='en')
            enQuery = str(enQuery.text).replace("2017", " ")
            print(enQuery)
            if enQuery:
                headers = {
                    'X-RapidAPI-Host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
                    'X-RapidAPI-Key': "15b3fa1d8cmsh1ae9b5162464c82p17fba9jsn8e709fcfccf1"
                }
                null = None

                conn = http.client.HTTPSConnection("contextualwebsearch-websearch-v1.p.rapidapi.com")

                conn.request("GET", "/api/Search/ImageSearchAPI?q="+enQuery+"&pageNumber=1&pageSize=1&autoCorrect=true&base64Encoding=false", headers=headers)

                res = conn.getresponse()
                data = res.read()
                dataObj = eval(data.decode("utf-8"))
                # dataObj = {"_type":"images","totalCount":970,"value":[{"url":"http://tokusiro.com/anime/wp-content/uploads/2016/04/naruto.jpg","height":450,"width":301,"thumbnail":"https://rapidapi.usearch.com/api/thumbnail/get?value=8313506348614855164","thumbnailHeight":224,"thumbnailWidth":150,"base64Encoding":null,"name":"","title":"Naruto: Shippuuden Sub Indo - Tokusiro Anime","provider":{"name":"tokusiro","favIcon":"","favIconBase64Encoding":""},"imageWebSearchUrl":"https://usearch.com/search/naruto%20anime/images","webpageUrl":"http://tokusiro.com/anime/naruto-shippuuden/"}]}
                dispatcher.utter_message(response="utter_send_picture_per_request")
                dispatcher.utter_message("Link h??nh: "+dataObj["value"][0]["url"])
                dispatcher.utter_message(image=dataObj["value"][0]["url"])
                dispatcher.utter_message("Ngu???n: "+dataObj["value"][0]["webpageUrl"])
                print(dataObj["value"][0]["url"])
                print(dataObj["value"][0]["webpageUrl"])
                return[]
            else:
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
                    dispatcher.utter_message(text=f"Link h??nh: "+reddit_post['data'][index]['url'])
                    dispatcher.utter_message(image=reddit_post['data'][index]['url'])
                    dispatcher.utter_message(text=f"Ngu???n: "+reddit_post['data'][index]['full_link'])

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

#         dispatcher.utter_message("M??nh s??? nh???n l???i cho b???n trong 5s. (??ang test)")
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
        if entities and entities[0] and entities[1]:
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

            dispatcher.utter_message("M??nh s??? nh???n l???i cho b???n trong " + entities[1]['value'] + " (Beta)")


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
        else:
            dispatcher.utter_message(response="utter_ask_to_repeat")

            return []

            


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
        if userId:
            for obj in remindersCollection.find().sort([('createdAt', -1)]):
                if obj['userId'] == str(userId):
                    # activity = next(tracker.get_slot("activity"), None)
                    if obj["reminder"] is not "" and obj["reminder"]["value"] is not "":
                        activity = obj["reminder"]["value"]
                        print(activity)
                        dispatcher.utter_message(response="utter_reminder_message")
                        break
            return []
        else:
            dispatcher.utter_message(response="utter_ask_to_repeat")
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
        if userId:
            dispatcher.utter_message(response="utter_respond_to_user_info_req")

            usersCollection = mentalBot["users"]

            user = usersCollection.find_one({"_id": ObjectId(str(userId))})

            # dispatcher.utter_message(text=f"T??n ?????y ????? c???a b???n l?? "+user['name'])
            # dispatcher.utter_message(text=f"Username c???a b???n l?? "+user['username'])
            # dispatcher.utter_message(text=f"Ngh??? nghi???p c???a b???n l?? "+user['occupation'])
            # dispatcher.utter_message(text=f"S??? ??i???n tho???i c???a b???n l?? "+user['phoneNumber'])
            # dispatcher.utter_message(text=f"Email c???a b???n l?? "+user['email'])
            # dispatcher.utter_message(text=f"Ng??y th??ng n??m sinh c???a b???n l?? "+str(user['dob'])[:10])
            # # dispatcher.utter_message(text=f"B???n "+datetime.today().year - user['dob'][:4]+" tu???i")
            # dispatcher.utter_message(text=f"T??m tr???ng hi???n t???i c???a b???n do b???n cung c???p l?? ??ang "+user['mood'])
            # dispatcher.utter_message(text=f"Ti???n ????? c???a b???n l?? "+user['progress'])

            print(user['name'])
            print(user['username'])
            print(user['occupation'])
            print(user['phoneNumber'])
            print(user['email'])
            print(user['dob'])
            print(user['mood'])
            print(user['progress'])

            # dispatcher.utter_message(text=f"T??n ?????y ????? c???a b???n l?? "+str(user['name'])+"\n"+
            # "Username c???a b???n l?? "+str(user['username'])+"\n"+
            # "Ngh??? nghi???p c???a b???n l?? "+str(user['occupation'])+"\n"+
            # "S??? ??i???n tho???i c???a b???n l?? "+str(user['phoneNumber'])+"\n"+
            # "Email c???a b???n l?? "+str(user['email'])+"\n"+
            # "Ng??y th??ng n??m sinh c???a b???n l?? "+str(user['dob'])[:10]+"\n"+
            # "T??m tr???ng hi???n t???i c???a b???n do b???n cung c???p l?? ??ang "+str(user['mood'])+"\n"
            # "Ti???n ????? c???a b???n l?? "+str(user['progress'])+"\n")


            dispatcher.utter_message(text=f"T??n ?????y ????? c???a b???n l?? "+str(user['name']))
            dispatcher.utter_message(text=f"Username c???a b???n l?? "+str(user['username']))
            dispatcher.utter_message(text=f"Ngh??? nghi???p c???a b???n l?? "+str(user['occupation']))
            dispatcher.utter_message(text=f"S??? ??i???n tho???i c???a b???n l?? "+str(user['phoneNumber']))
            dispatcher.utter_message(text=f"Email c???a b???n l?? "+str(user['email']))
            dispatcher.utter_message(text=f"Ng??y th??ng n??m sinh c???a b???n l?? "+str(user['dob'])[:10])
            dispatcher.utter_message(text=f"T??m tr???ng hi???n t???i c???a b???n do b???n cung c???p l?? ??ang "+str(user['mood']))
            dispatcher.utter_message(text=f"Ti???n ????? c???a b???n l?? "+str(user['progress']))

            return[]
        else:
            dispatcher.utter_message(response="utter_ask_to_repeat")
            return []


class ActionNoteMood(Action):
    def name(self):
        return "action_note_mood"

    def run(self, dispatcher, tracker, domain):
        userId = tracker.get_slot("userId") 
        mood = tracker.latest_message.get("entities") 


        print("action_node_mood is called")
        if mood and userId:
            print(mood[0]["value"])
            usersCollection.find_one_and_update({'_id': ObjectId(str(userId))}, update={"$set": {'mood': mood[0]["value"]}})
            userlogs.insert_one({'userId': ObjectId(str(userId)), "mood": mood[0]["value"], "happyThing": "", "issues": [], "createdAt": datetime.datetime.now(), "updatedAt": datetime.datetime.now()})


        # dispatcher.utter_message(response="utter_ask_for_issue")

        ####some code or no code here SlotSet("activity", None)
        return[]

class ActionFollowUpMood(Action):
    def name(self):
        return "action_follow_up_mood"

    def run(self, dispatcher, tracker, domain):
        #follow up to user, ask them about their previous mood log
        for obj in userlogs.find().sort([('createdAt', -1)]):
            if obj['userId'] == str(userId):
                # activity = next(tracker.get_slot("activity"), None)
                if obj["mood"] and obj["mood"] is not "":
                    mood = obj["mood"]
                    print(mood)
                    dispatcher.utter_message(response="utter_follow_up"+mood)
                    break
        return[]

class ActionNoteIssue(Action):
    def name(self):
        return "action_note_issue"

    def run(self, dispatcher, tracker, domain):
        userId = tracker.get_slot("userId") 
        issue = tracker.latest_message.get("entities") 

        if issue and userId:
            print("action_note_issue is called")
            print(issue[0]["value"])
            usersCollection.update({'_id': ObjectId(str(userId))}, {'$addToSet': {'issues': issue[0]["value"]}})

            for obj in userlogs.find().sort([('createdAt', -1)]):   
                if obj['userId'] == str(userId):
                    print(obj)
                    userlogs.update_one({"_id": ObjectId(obj['_id'])}, {'$addToSet': {'issues': issue[0]["value"]}, '$set': {"updatedAt": datetime.datetime.now()}})
                    print(obj)
                    break

            # dispatcher.utter_message(response="utter_note_issue")

            return[]
            

# class ActionConsultWithGenericAnxiety(Action):
#     def name(self):
#         return "action_consult_with_generic_anxiety"

#     def run(self, dispatcher, tracker, domain):
#         userId = tracker.get_slot("userId") 
#         issue = tracker.latest_message.get("entities") 

#         if issue and userId:
#             print("action_note_issue is called")
#             print(issue[0]["value"])
#             usersCollection.update({'_id': ObjectId(str(userId))}, {'$addToSet': {'issues': issue[0]["value"]}})

#             for obj in userlogs.find().sort([('createdAt', -1)]):   
#                 if obj['userId'] == str(userId):
#                     print(obj)
#                     userlogs.update_one({"_id": ObjectId(obj['_id'])}, {'$addToSet': {'issues': issue[0]["value"]}, '$set': {"updatedAt": datetime.datetime.now()}})
#                     print(obj)
#                     break 
#         print("action_consult_with_generic_anxiety is called")
#         dispatcher.utter_message(response="utter_help_with_ways_to_reduce_anxiety")
#         dispatcher.utter_message(response="utter_comment_on_help_with_ways_to_reduce_anxiety")
#         dispatcher.utter_message(response="utter_ask_if_bot_can_continue")

# class ActionSetLoopForConsultingAnxiety(Action):
#     def name(self):
#         return "action_set_loop_for_consultinng_anxiety"

#     def run(self, dispatcher, tracker, domain):
        
#         print("action_set_loop_for_consultinng_anxiety is called")
#         dispatcher.utter_message(response="utter_help_with_ways_to_reduce_anxiety")
#         dispatcher.utter_message(response="utter_comment_on_help_with_ways_to_reduce_anxiety")
#         dispatcher.utter_message(response="utter_ask_if_bot_can_continue")

#         return[SlotSet("loop", "consult_anxiety")]

# class ActionClearLoop(Action):
#     def name(self):
#         return "action_clear_loop"

#     def run(self, dispatcher, tracker, domain):
#         print("action_clear_loop is called")

#         return[SlotSet("loop", None)]

class NoteFeedback(Action):
    def name(self):
        return "action_note_feedback"

    def run(self, dispatcher, tracker, domain):
        print("action_note_feedback is called")
        userId = tracker.get_slot("userId") 
        username = tracker.get_slot("user")
        feedback = tracker.latest_message.get('text')
        formatedFeedback = str(feedback).replace("content", "")
        formatedFeedback = str(feedback).replace("Content", "")

        print("action_note_feedback is called")
        print(feedback)
        feedbacksCollection.insert_one({'content': formatedFeedback,'userId': ObjectId(str(userId)), 'username': username,"createdAt": datetime.datetime.now(), "updatedAt": datetime.datetime.now()})

        dispatcher.utter_message(response="utter_receive_feedback")

        return[]

    
