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
            "utter_faculty_details", tracker, link2=Link2)
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
            "utter_Faculty_details_eees", tracker, link11=Link11)
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


class Notifications(Action):

    def name(self) -> Text:
        return "action_Notifications"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link15 = "https://gmrit.edu.in/index.php#notifications"
        dispatcher.utter_template(
            "utter_Notifications", tracker, link15=Link15)
        return []


class Exam_Notifications(Action):

    def name(self) -> Text:
        return "action_Exam_Notifications"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link16 = "https://gmrit.edu.in/examination/notifications.php"
        dispatcher.utter_template(
            "utter_Exam_Notifications", tracker, link16=Link16)
        return []


class Placements(Action):

    def name(self) -> Text:
        return "action_Placements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link17 = "https://gmrit.edu.in/placements.php"
        dispatcher.utter_template(
            "utter_Placements", tracker, link17=Link17)
        return []


class Autonomy_Governance(Action):

    def name(self) -> Text:
        return "action_Autonomy_Governance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link18 = "https://gmrit.edu.in/autonomy.php"
        dispatcher.utter_template(
            "utter_Autonomy_Governance", tracker, link18=Link18)
        return []


class Academic_Regulations(Action):

    def name(self) -> Text:
        return "action_Academic_Regulations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link19 = "https://gmrit.edu.in/academic_regulations.php"
        dispatcher.utter_template(
            "utter_Academic_Regulations", tracker, link19=Link19)
        return []


class PG_Programs(Action):

    def name(self) -> Text:
        return "action_PG_Programs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link20 = "http://www.gmrit.org/pgcourses.html"
        dispatcher.utter_template(
            "utter_PG_Programs", tracker, link20=Link20)
        return []


class LAN_Based_courses(Action):

    def name(self) -> Text:
        return "action_LAN-Based_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link21 = "http://117.239.50.211/wbc/index.aspx"
        dispatcher.utter_template(
            "utter_LAN-Based_courses", tracker, link21=Link21)
        return []


class Lecture_capturing_system(Action):

    def name(self) -> Text:
        return "action_Lecture_capturing_system"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link22 = "https://lcs.gmrit.edu.in/login/#/"
        dispatcher.utter_template(
            "utter_Lecture_capturing_system", tracker, link22=Link22)
        return []


class Labs(Action):

    def name(self) -> Text:
        return "action_Labs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link23 = "https://gmrit.edu.in/labs.php"
        dispatcher.utter_template(
            "utter_Labs", tracker, link23=Link23)
        return []


class Library(Action):

    def name(self) -> Text:
        return "action_Library"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link24 = "https://gmrit.edu.in/library.php"
        dispatcher.utter_template(
            "utter_Library", tracker, link24=Link24)
        return []


class Sports(Action):

    def name(self) -> Text:
        return "action_Sports"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link25 = "https://gmrit.edu.in/sports.php"
        dispatcher.utter_template(
            "utter_Sports", tracker, link25=Link25)
        return []


class studentlogin(Action):

    def name(self) -> Text:
        return "action_student_parent_login"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link26 = "http://115.241.205.4/spflogin/Login.aspx"
        dispatcher.utter_template(
            "utter_student_parent_login", tracker, link26=Link26)
        return []


class Cyber_Security(Action):

    def name(self) -> Text:
        return "action_Cyber_Security"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link27 = "http://www.gmrit.org/pgcourses_Cyper_Security.html"
        dispatcher.utter_template(
            "utter_Cyber_Security", tracker, link27=Link27)
        return []


class Environmental(Action):

    def name(self) -> Text:
        return "action_Environmental"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link28 = "http://www.gmrit.org/pgcourses_environmental_engineering.html"
        dispatcher.utter_template(
            "utter_Environmental", tracker, link28=Link28)
        return []


class power_and_industrial_drives(Action):

    def name(self) -> Text:
        return "action_power_and_industrial_drives"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link29 = "http://www.gmrit.org/pgcourses_power_and_industrial_drives.html"
        dispatcher.utter_template(
            "utter_power_and_industrial_drives", tracker, link29=Link29)
        return []


class Transportation(Action):

    def name(self) -> Text:
        return "action_Transportation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link30 = "http://www.gmrit.org/pgcourses_transportation_engineering.html"
        dispatcher.utter_template(
            "utter_Transportation", tracker, link30=Link30)
        return []


class VLSI_and_embedded_systems_design(Action):

    def name(self) -> Text:
        return "action_VLSI_and_embedded_systems_design"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link31 = "http://www.gmrit.org/pgcourses_vlsi_and_embedded_system_design.html"
        dispatcher.utter_template(
            "utter_VLSI_and_embedded_systems_design", tracker, link31=Link31)
        return []


class Thermal(Action):

    def name(self) -> Text:
        return "action_Thermal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link32 = "http://www.gmrit.org/pgcourses_Thermal_Engineering.html"
        dispatcher.utter_template(
            "utter_Thermal", tracker, link32=Link32)
        return []


class admission_form(Action):

    def name(self) -> Text:
        return "action_admission_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link33 = "https://gmrit.edu.in/PDFs/Downloads/gmrit_admission_form.doc"
        dispatcher.utter_template(
            "utter_admission_form", tracker, link33=Link33)
        return []


class ActionCarousel_departmentInfo(Action):
    def name(self) -> Text:
        return "action_carousels"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
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
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=cse",
                                "type": "web_url"
                            },
                            {
                                "title": "faculty",
                                "url": "https://gmrit.edu.in/facultydirectory.php?dept=cse",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "AI & DS",
                        "subtitle": "CSE (Artificial Intelligence & Data Science)",
                        "image_url": "https://gmrit.edu.in/images/department/CSE.jpeg",
                        "buttons": [
                            {
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=AIDS",
                                "type": "web_url"
                            },
                            {
                                "title": "faculty",
                                "url": "https://gmrit.edu.in/facultydirectory.php?dept=cse",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "AI & ML",
                        "subtitle": "CSE (Artificial Intelligence & Machine Learning)",
                        "image_url": "https://gmrit.edu.in/images/department/CSE.jpeg",
                        "buttons": [
                            {
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=AIML",
                                "type": "web_url"
                            },
                            {
                                "title": "faculty",
                                "url": "https://gmrit.edu.in/facultydirectory.php?dept=cse",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "ECE",
                        "subtitle": "Electronic Communication and engineering",
                        "image_url": "https://gmrit.edu.in/images/blocks/Block-5.jpeg",
                        "buttons": [
                            {
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=ece",
                                "type": "web_url"
                            },
                            {
                                "title": "faculty",
                                "url": "https://gmrit.edu.in/facultydirectory.php?dept=ece",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "IT",
                        "subtitle": "Information Technology",
                        "image_url": "https://gmrit.edu.in/images/blocks/Landing.png",
                        "buttons": [
                            {
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=it",
                                "type": "web_url"
                            },
                            {
                                "title": "faculty",
                                "url": "https://gmrit.edu.in/facultydirectory.php?dept=it",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "EEE",
                        "subtitle": "Electrical and Electronics Engineering",
                        "image_url": "https://gmrit.edu.in/images/blocks/Block-3.jpeg",
                        "buttons": [
                            {
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=eee",
                                "type": "web_url"
                            },
                            {
                                "title": "faculty",
                                "url": "https://gmrit.edu.in/facultydirectory.php?dept=eee",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "MECH",
                        "subtitle": "Mechanical Engineering",
                        "image_url": "https://gmrit.edu.in/images/blocks/Block-2.jpeg",
                        "buttons": [
                            {
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=mech",
                                "type": "web_url"
                            },
                            {
                                "title": "faculty",
                                "url": "https://gmrit.edu.in/facultydirectory.php?dept=mech",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "CIVIL",
                        "subtitle": "Civil Engineering",
                        "image_url": "https://gmrit.edu.in/images/blocks/Block-2.jpeg",
                        "buttons": [
                            {
                                "title": "Click here",
                                "url": "https://gmrit.edu.in/department.php?code=civil",
                                "type": "web_url"
                            },
                            {
                                "title": "faculty",
                                "url": "https://gmrit.edu.in/facultydirectory.php?dept=civil",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return []
