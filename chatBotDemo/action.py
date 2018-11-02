
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

import datetime
from astral import Astral

class ActionTime(Action):
	def name(self):
		return 'action_Time'
		
	def run(self, dispatcher, tracker, domain):
		
		
		loc = tracker.get_slot('location')
		
                a = Astral()
                a.solar_depression= 'civil'

                city = a[loc]

		cityRegion= city.region
                cityTimeZone=city.timezone
                sun = city.sun(date=datetime.date(2009, 4, 22),local=True)
                sunRize=str(sun['sunrise'])


		response = """It is {} in {} at the moment. The timezone is {} , sun rise at {} .""".cityRegion,city_name,cityTimeZone,sunRize)
						
		dispatcher.utter_message(response)
return [SlotSet('location',loc)]
