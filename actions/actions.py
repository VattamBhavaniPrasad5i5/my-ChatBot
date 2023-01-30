# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class CollageInfo(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link = "https://gmrit.edu.in/"
        # Link1 = "https://github.com/VattamBhavaniPrasad5i5"
        # dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_template("utter_collage_info", tracker, link=Link)
        # dispatcher.utter_template("utter_gmritan", tracker, link1=Link1)
        return []


class OnlinePayments(Action):

    def name(self) -> Text:
        return "action_online_payments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link1 = "https://gmrit.edu.in/payments/"
        dispatcher.utter_template(
            "utter_online_payments", tracker, link1=Link1)
        return []


class FacultyDetails(Action):

    def name(self) -> Text:
        return "action_faculty_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link2 = "https://gmrit.edu.in/facultydirectory.php"
        dispatcher.utter_template(
            "utter_Faculty_details", tracker, link2=Link2)
        return []


class HODDetails(Action):

    def name(self) -> Text:
        return "action_hod_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link3 = "https://gmrit.edu.in/facultydirectory.php?dept=hod"
        dispatcher.utter_template("utter_HOD_details", tracker, link3=Link3)
        return []


class AcademicCalendar(Action):

    def name(self) -> Text:
        return "action_academic_calendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link4 = "https://gmrit.edu.in/examination/academic_calendars.php"
        dispatcher.utter_template(
            "utter_Academic_calendar", tracker, link4=Link4)
        return []


class Results(Action):

    def name(self) -> Text:
        return "action_results"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link5 = "https://gmrit.edu.in/examination/results.php"
        dispatcher.utter_template(
            "utter_Results", tracker, link5=Link5)
        return []


class Timetable(Action):

    def name(self) -> Text:
        return "action_timetable"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link6 = "https://gmrit.edu.in/examination/timetables.php"
        dispatcher.utter_template(
            "utter_Timetables", tracker, link6=Link6)
        return []


class all360view(Action):

    def name(self) -> Text:
        return "action_360view"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link7 = "https://www.google.com/maps/@18.4665112,83.6608295,3a,75y,269.47h,90.74t/data=!3m6!1e1!3m4!1sAF1QipOWSKxx3t5p0_Ju8V-GeoxU8Nu-4YmbSN3LpT4O!2e10!7i14000!8i7000"
        dispatcher.utter_template(
            "utter_360view", tracker, link7=Link7)
        return []


class cse_faculty(Action):

    def name(self) -> Text:
        return "action_Faculty_details_CSE"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link8 = "https://gmrit.edu.in/facultydirectory.php?dept=cse"
        dispatcher.utter_template(
            "utter_Faculty_details_CSE", tracker, link8=Link8)
        return []


class cse_faculty(Action):

    def name(self) -> Text:
        return "action_Faculty_details_CSE"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link8 = "https://gmrit.edu.in/facultydirectory.php?dept=cse"
        dispatcher.utter_template(
            "utter_Faculty_details_CSE", tracker, link8=Link8)
        return []


class civil_faculty(Action):

    def name(self) -> Text:
        return "action_Faculty_details_civil"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link9 = "https://gmrit.edu.in/facultydirectory.php?dept=civil"
        dispatcher.utter_template(
            "utter_Faculty_details_civil", tracker, link9=Link9)
        return []


class ece_faculty(Action):

    def name(self) -> Text:
        return "action_Faculty_details_ece"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link10 = "https://gmrit.edu.in/facultydirectory.php?dept=ece"
        dispatcher.utter_template(
            "utter_Faculty_details_ece", tracker, link10=Link10)
        return []


class eee_faculty(Action):

    def name(self) -> Text:
        return "action_Faculty_details_eee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link11 = "https://gmrit.edu.in/facultydirectory.php?dept=eee"
        dispatcher.utter_template(
            "utter_Faculty_details_eee", tracker, link11=Link11)
        return []


class it_faculty(Action):

    def name(self) -> Text:
        return "action_Faculty_details_it"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link12 = "https://gmrit.edu.in/facultydirectory.php?dept=it"
        dispatcher.utter_template(
            "utter_Faculty_details_It", tracker, link12=Link12)
        return []


class mech_faculty(Action):

    def name(self) -> Text:
        return "action_Faculty_details_mech"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link13 = "https://gmrit.edu.in/facultydirectory.php?dept=mech"
        dispatcher.utter_template(
            "utter_Faculty_details_mech", tracker, link13=Link13)
        return []


class bsh_faculty(Action):

    def name(self) -> Text:
        return "action_Faculty_details_bsh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link14 = "https://gmrit.edu.in/facultydirectory.php?dept=bsh"
        dispatcher.utter_template(
            "utter_Faculty_details_bsh", tracker, link14=Link14)
        return []


class ActionCarousel_departmentInfo(Action):
    def name(self) -> Text:
        return "action_carousels"

    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "CSE",
                        "subtitle": "Computer Science and engineering",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBHbY88KcbdQCtoPvX8d-QTwUq2y1hJTclKU_0GsHvHmC1BuXUiScVG9MNBJaO_gfS2r4&usqp=CAU",
                        "buttons": [
                            {
                                "title": "Happy",
                                "payload": "Happy",
                                "type": "postback"
                            },
                            {
                                "title": "sad",
                                "payload": "sad",
                                "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "ECE",
                        "subtitle": "Electronic Communication and engineering",
                        "image_url": "data:image/jpeg;base64,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",
                        "buttons": [
                            {
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=ece",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return []
