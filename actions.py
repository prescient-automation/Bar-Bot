# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#
class ActionSaveName(Action):
#
    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import datetime
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("BAR").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        date = datetime.date.today()
        time = datetime.datetime.now()
        date = str(date)
        hour = time.hour
        hour = str(hour)
        minu = time.minute
        minu = str(minu)
        time_1 = str(hour) + str(minu)
        to_save = [date, hour, minu]
        sheet.insert_row(to_save, 3)
        name = tracker.get_slot("PERSON")
        sheet.update_cell(3,4, name)
        dispatcher.utter_message("Okay")

        return []

class ActionSaveEmail(Action):
#
    def name(self) -> Text:
        return "action_save_email"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("BAR").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        email = tracker.get_slot("email")
        
        sheet.update_cell(3, 5, email) 
        dispatcher.utter_message("Okay. Your details are saved.")

        return []


class ActionSaveTable(Action):
#
    def name(self) -> Text:
        return "action_save_table_no"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("BAR").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        table = tracker.get_slot("table")
        
        sheet.update_cell(3, 8, table) 
        dispatcher.utter_message("Okay. Your details are saved.")

        return []