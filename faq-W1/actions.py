# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class faq(Action):

 def name(self) -> Text:
     return "faq"

 def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

     df = pd.read_excel (r'faq.xlsx')
     g=df.set_index('Intent').to_dict()
     print ("**********************************")
     if (len(tracker.latest_message['entities'])>0):
         print (tracker.latest_message)
         print (tracker.latest_message['entities'][0])
         print (tracker.latest_message['entities'][0]['value'])
     else:
         print ("ERROR")
         print (len(tracker.latest_message['entities'])==0)
         print (tracker.latest_message)
     print ("**********************************")

     if (len(tracker.latest_message['entities'])==0):
         res = "Sorry I did not understand, please rephrase"
     else:
         res=g.get("Answer").get(tracker.latest_message['entities'][0]['entity'])

     resp = {"message":res}

     dispatcher.utter_message(text=res)
     return []
