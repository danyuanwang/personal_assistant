# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

class AskDiseaseDataForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "ask_disease_data_form" 

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["disease",  "treatment"]


#    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#        """A dictionary to map required slots to
#            - an extracted entity
#            - intent: value pairs
#            - a whole message
#            or a list of them, where a first match will be picked"""

#        return {
#            "cuisine": self.from_entity(entity="cuisine", not_intent="chitchat"),
#            "num_people": [
#                self.from_entity(
#                    entity="number", intent=["inform", "request_restaurant"]
#                ),
#            ],
#            "outdoor_seating": [
#                self.from_entity(entity="seating"),
#                self.from_intent(intent="affirm", value=True),
#                self.from_intent(intent="deny", value=False),
#            ],
#            "preferences": [
#                self.from_intent(intent="deny", value="no additional preferences"),
#                self.from_text(not_intent="affirm"),
#            ],
#            "feedback": [self.from_entity(entity="feedback"), self.from_text()],
#        }

    # USED FOR DOCS: do not rename without updating in docs
#    @staticmethod
#    def cuisine_db() -> List[Text]:
#        """Database of supported cuisines"""
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
            ) -> List[Dict]:
        """Define what the form has to do after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="uutter_report_amount")
        return [SlotSet("amount", 10)]

