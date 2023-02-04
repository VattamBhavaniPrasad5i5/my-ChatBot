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
                        "image_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBQVFBcUFBQXFxcXGyAeGhsbGBshHR0bGxcbGCEbGyEcICwkGx0pHhsbJjYlKS4wMzMzGiI5PjkyPSwyMzABCwsLEA4QHRISHjIpJCoyMDIyMjIyMjIyNDIyMjIyMjIyMjIyMjQyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIALcBEwMBIgACEQEDEQH/xAAbAAAABwEAAAAAAAAAAAAAAAAAAQIDBAUGB//EAEcQAAIBAgQDBQQGBgkDBAMAAAECEQADBBIhMQVBUQYTImFxMkKBkVKhscHR8BQVI2Jy4QczQ1OCkrLC0hai8SRUk+Jjo7P/xAAZAQADAQEBAAAAAAAAAAAAAAABAgMEAAX/xAAnEQACAgICAgICAgMBAAAAAAAAAQIRAyESMUFRBBMigWFxFKHRsf/aAAwDAQACEQMRAD8AiWbpQ9VO4PP+dSEdrbLctsRBlTznofOs9wbiouDu3Pi5Hr6/vfbVxYcpKscynf8APUVn/hlu9o6dwDjC3kziA40dfvHkauSOY2Nck4fi7mHuLcRs3nydehA/M103hePS7bFxDKtuOYPQ+YqsJWTkqKfj/D8jd4o8Le15N19D9vrVQK3d60CCjCVYQfMGsbjsIbVwodt1PUda9T42bkuL7R5+fFxfJdEahQo61mYKhQoVxwKFChXHAoUKFccHRiipQrjg6MUVGKUIYpQpIpQoBFijFEKMVwRQpxaQKcFKwoMU4tIFOLSsdChS1pIpaikYULFFcfKPPlRzFRycx/OmlSyTrRWEbDUbk7fyqo7Q8Y7lcqn9q3sj6I2zfh/KpfFuIpZtl231CL9Jvw61z3EX2uublwyzGT+A6CsWSdaRohG9hJJJLGSdSaczU3NM4/FC0mZtWPsr956CszZdEvWhT2Au2+6tl2GYqpOo3IB++jqX5DaG+2fY04dnv2QTbZdVA2bMrTptsfnVVwniguDu3Pj5Hr/9vtruDWwwysJBEEHauS9vuxbWc2JwykpJLKN11mRHKtUoWSUqDtOB4W9k/Ueoq34FxZsNcg6229sDpyYVQKxCKd/CJ+Q1p+zilYZSR+6enkfL7KlGRRo7Hhb6uoIIIYSp9aj8UwIupHvrqp8+nofwrD9luO90/cXDCMdCfcY/7T/OuiI2YeY+sVphNp2uyM4JqmYXKQYIgjcedCKue0uBmLiKCG0fUgxHtCAZMacuVU9etiyqa0edlxPHTfm/9BRRUqiirERNHRxQiuOCoUcUIrjghS6KjrjgUYoqMUpwYpQohShQCKFKFEKMVwwpacFJUUsClYyFLTgpCinFFIxkKUU4opKiiuNGnP7qnKSSHirCuPJgbfzFMYrEJaQu5hVGv4DqackKJJjSZPIRuem1YTj/ABU33ypPdIdP3jtmP5++sWSdbNMIXoicTx737huNouyryA/POorClhaYxWLS0uZ9T7q8z+A86yNmhKheJxC2kzsJb3V68pPQedROz3ALmPuG5cJFoHxNtmj3E8vOnuznAbmOdrt6RZJALDQtDg5E6LpBPrz26rhsMltAltQqrAAA0AAFUx4/LJylYeFwNm2ioqKAogaUKfmhVxC2vWY1G32UyygiCJBo7OIK6HVfrH8qee2CMyag/nSkHOddpezpszctAm1uyje35jqnly9NsqMMg3J66bfZXaSNIPSsJ2n7M93mu2Vm3u6AapzLJ+71HLlUZwraKwn4ZnDhbbgeJs40336axvW27IcdmLFxvEvsMeYHunz6fLpXPrR1ANwy2YrGXUK0aadCKmopOouOHBn3ZPn7O9CMvIZR8HVePKzWWKNlGpfQHQK3h12kxrWfxmCa0VDHMGUEMBAOgnSTGvKTuKe4Xxzv8NcRiO9W22YfSEEBx99aHFYIXLQQ/RGU9CBvWz4+XhK/DM+fHygl5tmRoUboVJVhBBgiir1bPLoFChQrgAoUKFMcChQo4pTgUdCKOK4IBSxRAUoCgEMUoUQFLUUGFC1FKUUQpaikY6FKKcFJWlrSsdDWLeE2mSoIiZBYSPiJHxpnABcgKpkB1C5cu5nYbU3xdv2YnYXLX/8AVKqO1HGu6Xurf9Yw1IBORTz05msWXIrs1Y4vil/LKzth2hGY4e2Z/vCOZ+jWWGPj3alWrsaQf8j/AIU+l0ucoHzUj7axTne2aYwrSI+AutdYgCAN/WrSx2U/S763HMWbaQetxgT4QfojmfhVtwHgveeJhFqdTsXPRfLqfgPLXIgVQqgABQABsB0pscG3yYs5LpCbVhUUIihVWAABoAIgCnQsz6/cKMLvPX8KQ1zWBWggLzCiqvucRtKcrXLYIiQWAI0560KHJBop+B9pWSEuSybDmyjy+kvkdRynatngsUCqvbYMrDkdDED4GuQYbFW7qypB+7+IcjVvwvi1zDtIMqdwdmHn+I19dqzQyeGXlD0dV8LjMu/MUydDH52qq4TxW3eAa2crgCVO49PpL5/OKu0uB9Do321ZOxGc07c9j2IGIwgjISxtjqxBZk6aiY9etZfhmPF0AN4bg5bTBIJjqCPhXbmQjQ1zztz2MLE4vBiLi6ui841JUdd9KSUPQVKmVmBWbiMpKtmCmCR4WOU6TB0JkeddN4BxVL9sMNCNGX6Lfga5ThHIvWoEg3E1HLxj6ql8L4xcsXO8S2+WcrrBgifT4ikhMrONxR0bj+AzDvFHiX2h1Xr6j7PSs8K2WAxiXba3EMhhp18wRyI6VneL4HunlR4G28jzX8P5V6nxstri/wBHmfIxU+S/ZAoUdHWwyiYoRSooRROCijijihQOBFGBS7Vh29lGb0BNHcsuntKy+oIpeSuhuLqxIFGBQFKFMcGBSwKJRSwKRsKDUU4opKinAKVsdIUoonPKgTFRuIY1LNtrjmAPmTyUeZrPlyVotjheyu7T4wW7UAjOWBQbzkYNJ8tKw+ZyS7klmJJJOupp/FY1rtxrjsJOwnRVkaComJxS27ZuHUDQdJO0npXnTnbN8Y1FfsLF4oWkzNufZXmfXoB1rS9mODtdS3duCEKKSNQXaCT6Lr8ag9ley73mXFYsGN0tkb6iCw5L0X4muhKNIH50oxx+WTc34DUAAACANAByAWIFHsNaS7xoNT+RVbxXituwua42pmFHtNryHTz2qzaRNInX7ogliAoWSSYA8yTWN432pLTbwxIGxucz/AOXrv6VS8Y43cxB8XhQbWxt6t9I/kRVa7qurEDoOcnYfGs88nhFow9geyhJLAEncmZPrQp3IelCoc2U4meFi7YueIFYDHMJjRGOvy2O/nV1w/jymFuQP3vdP/E/VV7Fu6kgq6HZgZHpI2PkazvFOzJEtZMfu8j8OXw+Qp7Uu9MHFro0OGulSHttBGog6+o/lW04J2mW5Fu9Cv8AS2B9fonz29Nq5/gE/ZINiqgHyI0o8tzlyO860IZGnQZQtHa7d8EQ/wA6N0IrnHAe0V20AlxS9saGCMyjqv0lHNflW9wGPR0DIwdD05eXUehrTGSZJxaM5x3s0O8W/ZEQ6s6bCAwJdehiSRz9d8MMUBcZA2vtR1UsR8dRXWuN4fNaZlZgFBbwmJ8DCD5a/VWK7T9jzet28VhpF9bakj+88M+mfX40koW7Q6lUV/Y32c433DySTac+Ic1P0h+dR5iui3raXbcSCrCQR8wwrieDxhyB3UqZKsCDupIII5aitl2R7SpbZbLv+zc/syfdYn2D5E/WfPQ450xZxtE29ZZGKNuPr8x5UkCtHxnA94udR4128xzX16fzrOoa9jFl5xvyeXlhxlQcUcUdCKpYgqzazuqTGYgT61pcNwm0nu5j1bX5DYVmVJGqmGGx6Hkah2u1184JbngFwXO6LRJOW0GzGdMxPlHlWL5c5JpJmv40E02zoJ8jFDcQYPXTT5Vy1+02KYf1rT5QP9IFCz2mxS73TPQgH4eL86Vh5mvib7GcGRtU8DdPdPw5fCqELrHSgnam6cOj5V7x7vdgjYaIc0GZ9qImnI1Nb/jZJSTTfRj+RBRpoAFKUUSinFFaGyCQailiiAozUsk+KKQjbG7txVUuxAAEknYAc659xvHfpTy0i2vsLP8A3HzNTO0vGhdbu0b9kp1M+2w/2jl86z2IxSIAd5MIo946CPrHzrzcmTkzdCHFWx63gLZzZUiRBMnYsBWv4H2bTIhupKqQyIRzXZmn5gH1qBwDg9+1aW7dC97cuKwRtkECAYnXw7cp5mtnYzZAXjNGsbTAmPKaWEN2xpz/ABpDlIL8h+fzFRsbjEtoblxgiLuSfzJrn/HO2BuzbtZktbE7M/r9FfL51WU1EnGLZoeN9qEtTbsw9zm3uqf9x8tvsrF3Lly65d2LMd2P50HlUbC3e82WANPj5VV8WvXXutZWcoA8KiJETLHp6wKzObm6K0oomYziqWxFuHbYn3Qfv+FVOH729dVzLZWUk+6IIOUeemw1q74Z2ZLKDciJmNcv3FvqGu5rTYTBpbgIu2gMfUANAPIUOUY9dhUXLsiolyB+yPxIH3UVXP6M1FU6HLvifYewzm7hybF2DOT2GkEeNeepn1FZXiFvE4WBibRKxrctglNzuOXhAJ6TGtdUnf0o3AIIIBB3B2rVKCl2RjJx6OSKqXFW4pjMJVhpIO0g/fTTkrpcGn0ht8Ry+yuh8Q7L231t/s26e78uVY3i2DuYbW6jZZ0dVLLtzygx8azzxtF4zUv7KV8cEZQ7nKxMEZSBCoZ1BPvb1d8M4hcssLlq4WU7qYKsPOB9Yqibh1rEIWDR4pRhpqUWdOs71U3TiMGZ9pOZGqnU7gbGI1oxXrsErT2jtOD49bv2XCnLcyNNsnU6GSv0h+TV3gk/Z28vJFny8IrkdhpuWzlMlhqJ2JEzHKtjwPtYM3dXgUKnKtyPDA0Gfptvt161aGS+xZwqKr2SO0/ZzvJu2RFzdl5P5jo/28+tYKzixne3zQwykQfXWuzqwfURP1HzFZLtT2SS+64i2Mt9NwNO8WCMrfvdDRlDyhIy8EjsjxzOBZuN4gPAx95Ry/iH1j0qTxrBZGzqPCx18m/A1za0zW3ym46upBG2ZSGiYOo1H1V07gHFkxVs27kd4BDj6Q+mvkfqPwqmDLwZPNjUkVQoxU1+D3gSAuYTocyiR11OlD9U3/7v/uX8a9L7YezB9UvREArJ40i1gnDe7jGHr+yFbc8LvD+z/wC5f+VUmM4JcxFm5btoGZcTnIJURNm3rqY51k+U4ySaZp+MnFtNGa7P30a9aBIJZ1HoJFFxC+gu3ACBDuPk7VouFdkMTbu2nNpQFYFiGTSGJ0gztG1Z7jvYbHXbly4uEUl9RL2ZkszEeJvMbk1kir7NTZa4Vpw+HC7nFmP8NtG+6tLUbhnZ+7atIrW/Etx3AWDGe2iT4dOTVPGDu/Qf5Gtvxqim2+zJnuTSSELTi0oYS59B/wDKaWMO43VgPMGrucfZJQl6ExWZ7TcV3sWzvpcYcgfcBGx6nltU/tHxbul7u2R3rjSdlH0jH1CsTbt3GIVcrEkTAYmSfPc15+bLyZsx46RE/V9ksLaW5Y/vPsI5TruPmK3HA+zNu33dy4gNy2D3YPuZok/x6b8qb7K9me4PfXiHvsI8rakzlXqep+XU6O64UEkxAkk7COZpIQp2xpStUROJvAtH/wDIv2NUPjfHreHEHxXI8KA+kFj7orOdou1ttwUsvrbIY3IkbhPCI19rf7ayWJxioneOWfOdCd2LS2pOw9aEslaQ6hpNk7ifEbt8l7pSBsCfAg8gR9e9R7VosYyqAP3Rzjy86q1wmIxZEDLbj/CN/wDMdtT8K1mGwMs2fWCPCPZ2G/0vjp5VCdjQ34I2Gsja2s767KNev4TU7DcPUEtAZ2MkxAnrH3mT0q1weBZ/ZEjy2GtWidnULTdYuv8Ad7Jt70av6GR5V0MbkdKSRQ2Ea4QLam6ZIJUjIpETmb1PKTodKusBwIyrXXJ5hElVEERPNvjp5VdWkVQqqAABoAI6UFbb0/41ojjjElKbYdqykDwj5ChSbZ0HoPso6cU0T2lPL5U02GPLWoiuw2JH2fKn0xh5ifSgMJII3oEAiCJB5HapK4lG0JHx0o2w4O2lccZPiXZO08m0e6YnMQACrGI1HLlqOlZbivDL1gQ9uVPvRKfHoK6e1hh5+lNkaQRI5iklBMdTaOSYFfFbK7BllSZjxD2TvtyP1VC4hxfur2R1ORp1gyGzNMcjoBt9ddL4p2bsENctju3HiOX2TlloI5c9qx3FuHNbUG9bJtOM3eAZkE6wxGqGOZAHnUHBxZXknH9kzs/2la0BDd7aPKdV65eh8q6FgOIW7yB0YMOvMHow5Vx/C4RLahbcPbkkQZIn/UPTWhwLtF3dyEPdXQYKmcr67EHr0Pwp4Ta/onKCN/2t7JLiSt634L6cxoLi80b1GxrCcPxVzD3dLmS7aOqMpG+6tpsRXSuB9ord8BDC3Buk/Wh5jyqH2u7KrilNy2RbxAWEuRIIkHKw57aHlPSnavaFTrTLLBdsMIyKXuBHI1UhjB9QsEedSh2owf8Afp8m/CuK2eH4lLuW5dLFCVZCiiTqN1JgAx8vOlYrD3ncd3c7sLowyBgSNdztpXc3dB4KrOvcQ7TYUoVW+knTntz3Hw+NU1/idgWO8NtcQrXogMRlYWxroDyA+dc6sYa4iEXG7xpnNAWBA0gfH51osIQMAJAH/qW8/wCxXyrubeqBxRcLxbCkgfoIltv2jf8AGi/XeDkqcIQQSDFx9xp0qp4WUa9bBIgsBMVT8atOLj5Llu2O8fxPBDAMdpiOtB2go6l2f4rhhZzgCwrOwAe5uwVZILHpGnlVp+u8L/7i1/8AIv41yy2SuAtd49tyb1whlgLGRIiJFVOODsFFl7atOuaWkRsBG9dzrR3C1Z2j9e4X/wBza/8AkX8aou0Paiwiyly3cIHhVXUyx6wdFA51yy0l1WZbzoxPsBRl6yPM7VCOHxFy53dt7RZj4EOrx567ee1Hm+gcS47y5euakXLlxtcpkn0A2A+qtl2W4AcOpe4we8+rH3U0jInkBz569aV2a7OJhQXaGvOAHbkAB7FvosyfMn4BXG+PpalEGe505L/ERz/dH1V0UltnN3pFjj+IW7S5naBy6seijnWB45xt7wOeLdoe6Tof4/pHy2+2q3F4wXr2W5ddrrTMN4VA1jTQegpd/s6Lz2yzMLaLGX3mJ5mfZ0570ksluvAYwpWMYI27iKyqIdioAUZmCmdukgVLxGCt+AXV8KnMByGhEsdj6CaucLwcJ3K20CL3h2G8WrjanmauOH9mLSnvLhN15kZ/ZXT3V206mTU1jlJ2ikpJJWV/DMCbiqUUhSJAgCAddeQqywfZm2rd5dPePM7kKDttzGuxq8OggaD/AM0IJ/PnWiGNRJPI30JEAQAANYA9aBOvx/20rIOZ/MzRG6o/l1/8VUmIVDp/D+H4Ua2wPMgR8dP5U22J8uf2UybhMa8z9hoHEvvFGkbUKrmIk6jc/bQrrBRzDAdqMdYZF729lLBYuLnXUge04mPQ1f8AD/6TrmnfWbbjm1typ/yvM/MVXKlwbXAf4l/A0xfwSP7di2x6qQD9xrEs5f6/R0jhfa3CXkV8zW83K4sc+qyo+dX+FvKwzW7gYdUYEfVpXGsOEtoECOqjYEExJnfWpOHvrMpchuqtB+rWu/yWn1o7gdmXFsNxPppTgvI2+nrp9dchftTjbSTbZrsPBDLn8OQHl4jr586nYT+k5QB+kWCp55DB0/deP9VaIZFJWJJUzovF8AHtOJ2GYeqgnlTXC0ixakaG2u5ncTuaqU7SYa5bOW7kLocquCsyug+iTqNJq64fePdWxoRkXbqFAoqSb0M0+P7KnHdl7Dybai0xJPgAyknUkrtqekVjePdnHtlXuW8wVgVuJ7sEGTGoHkdK6rnQ7+GiNk8jIrpQT2BTaOKYi/dt3FKqpt6BmU6o0yG01A9n7Zrbdnu1+1u+QdouDXf6YH+ofHrU/i/Y3DXXa4oNq6whmSQr6R402b6joNaxfFuzNyw5utbDrlILqSVyggjNpKnTmOutSdwH/GZ2S04KggyCNKaxl7IhPPYep/M/CuL8P4uzE27N5oTkl1gonoBtzpi7jcTcIf8ATMSimCEzmNh9IyCfvp1k9oVw9HU3cxUHimAN/DFO8t2ouzmdoEhV0nrE1zS3xO9anPi8U+bbVzGXcjJO88+lazgXGnXBFrireJxJUi6rMBFpToHjUfeabnfgHGiXw7gC27iM+LwzBTJHeDXU9aYxvAWuM04nBBO8Zl/amcpzaNymCNulOJx0FgoweF1O/dDT66h4jtWiE58Jg1AYqCyKoMEjSTXcqO42bfsxg1SwEY2rkMSCniSDpoSNxEH0q2GHT6C/5R+Fc04xxvNg7N5MtpM7giySE9z6B1Mn66zR4niLtstbxdxFVj41cnwhdmzsIImdKV5N9BUDsHF1QBUCLJ1PhGgHw5n7KqWW2njYIoAktAED15CuUWOIXznY4u7dnRYuRlidsrmR+FJxuJuMMty47DQwxcjyOrR1oSzVpI5Y73ZreNdqWuE27EquxubE/wAPNR57+lZzhdrvkZ+6NvNIRm0YqV9v1kn5b1J7P9lr1zO4BXOB43zARyyLoToSfU710Ph/CbdsCfGw3Yjn1A2FLTkG1EyXZ3swigd2hAjW4w9r0O5G/s6eda7C8Kt24nxHz2+VWGU89KauuoHX0qkYJbYjm3oquM4cObKSwlnHhYrANm5tB3/PM1aJb01P5iqri+KCPhyzKii4ZLGBHdXNydBVfxbtjhbQ1uG4TsLakzA66LzHOn5JAl0jStcUfn8+dNvePL86xXN8T/SKzOtuzYAzECXaSA3PKg6H6VRsT2ixFwkG8QJIy2/DzP0fFy60s8iidGNnRMZjEQTcuKo19pgBv571m8d26wdskKz3GB2RD0jdoH11j0Ric2RmJ5nf45taiJ2eJJZydTMTpr6AH66ms196C8b8FxxH+kO5p3VlEkEguxY+0R7Kx06mqfDdo8VfuEPfbLlJyoMijYe7BPPepicFtrEgGBA0B5k+9J3J51I/QrexXN6yftoSzJqgrGytJXmR8xQq1/Rk+gPlRVmHomEjYqflSlRfOow4jiCUyragxMoZ35ZWFLfG3s7p3diFMf2g0kx728Uzws5ZES1T96nDhlbcK3wFSeDWjctZ2ABzEQCSNDGk0OI3bdlZuGBH2dPOk+uSY6kmVWHwqy8Ajx+6SPcXzinnwRYQTmHR1DD7qYwnE7QttdAcg3FEQAYZDB1MR+zYfCnv15ZjNluAa+6vL/FR4S7OlUXTF27TgqIQgEDQkQPQj76bxlm53neW7l2yykjwCQ3iJ1yNPOrq3hyVV40IB+YmomMxFtHAe4qFpKydxNCKknod04b9krhHaTFW1C3byXWk+2seHl0afWanYXt7Dhb2Fu25bKHTxKZaAdQAAdOZqvwuS4ma2wuLMSNRpvSEsW5gZR/CYP8A2matHJJdifXFrRu7PabDMwRrtsMdlfwE6xpm0OvSrNSh1BiduY+dcxxPC0JVj7S+ySASNeRYE/XUbDLet3C9u86mNgzBeWsBomnWbWxXi9HSl7K4IMzjDIGcyxWRmPU5SBzPzoDstgtP/Tr83/5VjB2mxqKB3imCN0XmesUq72pxo17xR5ZUj60mmWWLFcJIs7vBsLCxZWQomC25+P5mq3tFh0tYEG0gUDETAndkAJ19ap27QYoe+p9VX7lFXGFs38bgineW0fviZLZPCET2SFOubnHWm5xlpA4NbZQ8GxDNiLUqWm4ukxOu08qoeK461fxFyw2dGW9ciFDey7EiZ8t63nCuyWJt3LbNftOqMC37ViTBJ08AB5b1Hv8AYq/3924LtqHuMyg3WBAZmMGFjZvqoxXs6T9F32S4PhcTw+0ly0txAW0YES0iSQDvIHyqbjuzWBt2sq4ZBmMBfFGo1JE9B9lUuMxmJwGGs2ke2XL3M5HiHuldSNDv8qpcV2oxtyM1xRG0KvP1Suc4xdM5RbVo0Fjs1g0ELh0UdBm/GpGH4Lh0YOtpQyxBJJiNozEifOsh/wBRYwA/tFb1VNPkgpF/j+MYR3gHoqg/PLSyzROWOR0VriqCWMAc50+JNVGL7V4S2jutxXCAk934/ZEkSPDMedYXB4R7pZrly5cLH3mkLuIWdtDVthuD27awiAKOXKeuuk7Un3ehvrFDt61x8tuwyrlnPcneRoFXQnXk3KqninEeI3mi3cNu3l1yqE8Wu2mbp71XmHwyttHoI5GKVcNpGyvcRWiYZgDBmNCZ5H5UrySb0H60lsywwNwLbW6+dpMu5ZifC51zSefWnn4Orx3nijYZRGvrNaA2ldrLIQytmII2IyaEfOpF7C5epgTpAGlI+VjtKkZ5OHKNAmnnt8tqLCYIgGAB42+01pbWGmQQQR5+VQLT2kTMzjVzt4teY023HzFDYEvRFGD6mjGFXmamYfFWXAIdf8XhM9IaDVXY4i7f2CHxMJNwgEABgQAOc8j+A5QbFckh/uU9aWLQ5AUjF4q6qAi3aBJAAlzyckGW6LUHg2Oe5jL9piMlsHKoVQAQ6DeMx3PPn6Et9TBzRY9yelCrfuaFDgw8kc1HFLxZQG0kaADrU7F27fem493QO0wu0XGI56yNPONK0mI7M2ApNtCGAME3GEGDrO2/URWb4nwi7ZLNnOkSZXI0mCSDtt0k61okn4Mv5I0XCu0WHs2xbbPqzEGN8xmk8Vu4TEsGZyAFZI6szKRlAmTAPnptWHXFEEeGNoAOVRGUZgVgHQTpBqXcv3BDPLFjBAPiKzIluYHTeNTvUpcgxnJO0aLiXDrdnBrlYsWuL7TKWCBLkCF0AlmP+I1SEju/i3+kVa9nFuXLyaBkUmDljTLBnlImN428627IF0LIP8Q+6a6OaMVUmkWk3N8mMXif0ZRbIz5E08vDP1TWQ7XnvMRZNtWIVCG8DCDM8xWsuYywCVN1c0bBWJ+z19KbTiNoyF71oE6WyJ/hnQ6UF8jHdr/wLpw4/wAkLsbbT9DFu4GWWaQQwME+lSltqHGmgM/AMPup2xfe4Tkw7EDm9xVG0mQASCNdPKlthbxP9XaUfvNcJ3jqBHnSy+VC+n/oMdLRTcds58bZuKjFEC5mjQRcYnfyNNfp6ozHKCW3mcoytB0nQSd/TStI3CrmmZ7QM6gKTpE7k6nQ8uflSW4IhBUZSxmdEAMCRMKZ1kxO1QyfJjNUjndaM+vFlIVe7WDlMJuNd5UkEactNd+dMY5FuEkDwnkfKK0OD4AEEXMrQWiQugLFlEFYMeGTzy8uTrcGEyGBEkR3dsADrOWSfjQx5Ywu9/v/AKLGeqbM3wzhpuXFtqWzOYERHmWnWANdOnwrsPD8Gtm2lpBCoIHn1J8yZPxrDcPwdyy73FYqdkZVt6qdWDaaHQVb4bjVxWRWurczNGqqNCZ90clFV/zccZJNbfrZzuQv+kG+lvCh7j3FC3FgWwCzEggLqwAHOSfdp7sLdR8Ily2zsrsx8YhlIbKVIkjQiJBM1Ox96zdQ27tvvEO6lQRIMjfz50zb4hYsWsqILVtBCiAFHwHn863ckDix/jvDFxFlrZ33U9GGx+741yPF4QZisMGWQytGhBiN/WtkvanvbYf9KFskTAUaHaDp61Q8QwF/EEvaxFssZzbZmM6Eyo5QN68//Nxyl01/eg8uKKq1YVA0g6jSBO0+dZ3H8UuZzKCRpAA03AmQZq1xWGvW2yXLl0MOUKJ9N5FQrmGctnLEkfSCEdOY6U/2wbsjPOmqLDs9i7jpd7xfaWFgb+B/huQJq47L4fJh2t3FZXNwkDrIUaxy3rOWmvJJFwAkaTk+vw6c6mW8fjFAIa24PUAHTrtrpTLIqKRyxpdmzwBVWJbQQRsfpfyrMdpkLYrMisVCIJCmN38qZ/6hxABBtIYO8HLzn3vzNScP2tQjxpBkwFOY6b6ddKdZEmM5xkqsf4RiwRgrSyGt24uhkYAL3QEAsILSUMDkav8AE5ERirFgqsxIEncsdBE86zeH4/auXUfLcUIrg5kO7FI9mfotVm/EbTpcUXAM6ldVYakEcwOvWnVvaHbXFUzM8S7UXSzC2yoCdNQSQAdiIIn+XOqHF4928bs50lc23xk6eQ+2omLs+MqwJKnlBgA7E/L8xUTEzOZwSW11IO3Wemv2V0cd7Zmpy7JBuPlOa5p5Gdz706DQ89vjFE2JZD4XIOhPiJjWI0G+nWkpZaChtifEZn2eUZYM8wB1nzqx/VzKihEQ3E0InMc5geLL75OoAOg12BJfijuAu1xe86ZMzaEZWIIg5Lhy6zrqfkd60PZFM2NxZ38TD/8AafwqfhOAW1RVuIGKkHQuNQGAOjbw7AnnoTrUnB8Lt23uXEzTcbM0kRMk6aTz5k7ULVFYwaNF3flQqpk9T86FAbiZK52nxDCBt1CqIjTUNMehqtxK3GVmLKs6ksVEqx8Q2A16emnVlnvzq1tACSIOozbiADr50zduE6F7jLpAQcgIgFp0+ApPxvtv92ZhprLjM3eLmEkCd9NtOY10PQ9ZpbIgLMWbXXYkgQNTOmtEGXVUV5+kTuJmDlABHLrHSrLgtu+VCW7VsOseIopYa6asCQIO1CUklYdl1wXBl7Yhbt0SICZo3kiQCoI5kkDlNaKzwW+x/qrdszo1x8xIBMaIdwAPjVLcs8QRQbly6x6KwgeUT9lXGA4liUVR3YjmSFnzOuprFKfqgqfgkWuyZkZ78D3ltouug0LsC0acgKsbXZ3DLrkZtI8TGBHQAgCY101pD9o7KkBmy/ny1pOO7RWkEoc8jQiI+MkUjlJ9jckWSYW2qhUUKo2CiB8hpSgCJ8/qrFYjtZdJlQqjmAd/PUaUSdpcTAhRz1InTfXQUHBrZ32mva11J6zpPxNE4J3JPr8qy57U3QPELU+u89On8jQxnahyvgULOxHiOpERptEmfXpUmvQPsvyaTF41La5ncek6n0G5qjxPaggRbtwf3iCfkCPt51l8RinYl3XMTuQ2qxJJLHSPQTrVRiuIrBAYz7pnYmN40576xTwxSk9C2W+P4uwlmuOTqfEY89jtPlpArVdmzatpba8wN11JIGuRW1ynXQkAfARXNVtNdckzA5np0Ec613DreVfOvQwfFitvspB8dm//AF9hwN2/yn76jYrjth1ZCjMrCOXMeZrLFzRhzWv60PzZmMcTYuSB4J2I0g89NOlDCcUu3G9sIJ0iMzGNhBnmNYjX41a8XwneKSADpWVtJdsFpzFCdDPmCRofzFZc3xou2lsnKN7Nxe4tda0Lf7NyJhnUMxHqdAeW3Ks1iGfMc+jE67fk78qr8NxOXMFoAkhZnz1zQo2671aWeLgkJlkT4pObQLM7fDpp8Kw/TOHiyE4WRhSo9al57VwkyRHURAHIzGm3z+T/AOrpUlbg0+kpA5c/jPwrvsrvQvBldHy9aJsKp9pQT5xPz3qVfs5T7QI5EEazzAJmKZc9Dy8qopXtAqhpMJlIa27oRtB01+0VY28W/vBW9UH3AVX94eu2/wBlNXMSdY+zfSqRyTXRSM5ImY5FueNVVWAHMgGCDrM+dVWMtWyruCZUAZdpJAJMiI1B09dqJsQ4JY3GHl+d6ZvS5EhSNZIiTM6Hyq8MkvJSM77odwNi8G8NwBnSWZohRGvtAjZj6ZjtOui4ecVbVCO6YKDCBebbsdZzHXU66nqazVi86sWKgxsM2nLkZ0AVdIqwsY9m55T59fLaneavFj8q9mi/Xt5f6ywvwYj7ajN2tAJ/Z+HlBM/KKrb16465ZVtZ0O/8I/8ANVTpcQjKggTus7kaE8/50jyRk9OgOf8AJqf+srI3tv8AAgj4HSaFY+8MzE92mvkfxoU1r2d9j9k1sP1/GjGF6cj8aFClrRJ9B27Hn+dqtMFeuWoZHZdeR+0fnaioUkkKh/FcTuvIdpB58x6U22IYjLLEnT2jG3rR0KnKKSGYYwBjaJmJPKJG1INtV9qWI1YDkNI33knlQoVm5tsFB/plpVzm2QnI77+RbqelRW41bKyM2UkgQW9NNiNx+NFQrRDBGSt2EiXMZbkzO+0SBpGpOuvxppsXmJKM4kEnYDwncBYXfqKFCrRxo4q7l5iTPM6kknkPU84pCePRR4iYBn7Z35mhQrSkiiNTwjCZREbdTOtXyNFChVV0EBuUtWoUKIQOdIrK8XsE6DzIHInoaFCll0FdmbzlCDpqpBj+fP8AGpCYhsu+kjbTUiOWvL7KFCptJoEkicmNyhiTrpAjQ+o1ggkCZ/GpNnjUE5pkjRk0O3mN9xNChUJYovtEgxxMM6szMSB7PONzJ0nnzmpOHxtqQIB1kwvoMgJ1A09N+tChUp440KTrfdXf7Pu4kEA6zAM6SCYjy1ND9W2ynga4WkkliDAAnbTlJ35D0oUKxybi9MLSDHBVILliRE6gSYXn5klTp51Fbs8xjxLJPUgAQSTou41HnR0KmvkTV7DxRW4vgdxBmYACQD4gd4I2/O9MDBvsfKNRsQD9hGlChWyGWUkrFJlq26AswDKDEmJ00P11PXCq6B1ciTlA13IH1eIc6FCkk9NjUVV7MrEFtRoaFChVE9CH/9k=",
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
                        "image_url": "https://gmrit.edu.in/images/blocks/Landing.png",
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
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return []
