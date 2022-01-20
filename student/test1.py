from student_base import student_base
import time
import numpy
from typing import Dict

class my_flight_controller(student_base):
	"""
	Student flight controller class.

	Students develop their code in this class.

	Parameters
	----------
	student_base : student_base
		Class defining functionality enabling base functionality
	
	Methods
	-------
	student_run(self, telemetry: Dict, commands: Dict (optional))
		Method that takes in telemetry and issues drone commands.
	"""
	
    def student_run(self, telemetry: Dict, commands: Dict) -> None:
		"""
		Defines drone behavior with respect to time given the telemetry.

		Students develop their based code in this method (you may develop)
		your own methods and classes in addition to this).

		Parameters
		----------
		telemetry : Dict
			Telemetry coming from the simulated drone.
		commands : Dict
			Issue basic commands via this dictionary (you use the method in 
   			the example missions).
		"""
        print("Printing telemetry")
		for i in range(4):
			print(telemetry)
			time.sleep(0.5)
        print("Arming")
		self.arm()
		
		print("Taking off")
		homeLat = telemetry['latitude']
		homeLon = telemetry['longitude']
		self.takeoff()
		
		# Get Water
		print("Get to water")
		goalLat = 42.3587 # water
		goalLon = -70.9925
		goalAlt = 100 
		self.goto(goalLat, goalLon, goalAlt)
		err = numpy.linalg.norm([goalLat - telemetry['latitude'], goalLon - telemetry['longitude']])
		tol = 0.0001 # Approximately 50 feet tolerance
		while err > tol:
			print('Aircraft is enroute to water')
			time.sleep(10)
			err = numpy.linalg.norm([goalLat - telemetry['latitude'], goalLon - telemetry['longitude']])


        goalLat = 42.3587 # traveling over water to pick it up
		goalLon = -70.989
		goalAlt = 100 
		self.goto(goalLat, goalLon, goalAlt)
		err = numpy.linalg.norm([goalLat - telemetry['latitude'], goalLon - telemetry['longitude']])
		tol = 0.0001 # Approximately 50 feet tolerance
		while err > tol:
			print('Aircraft is enroute to water')
			time.sleep(10)
			err = numpy.linalg.norm([goalLat - telemetry['latitude'], goalLon - telemetry['longitude']])


		print("Picking up water")
		water_start_time = time.time()
		while(time.time() - water_start_time < 10.0):
			print("Water level: " + str(round(telemetry['water_pct_remaining'], 2)) + '%')
			time.sleep(5)
		print("Water level: " + str(round(telemetry['water_pct_remaining'], 2)) + '%')

        print("Go to first fire")
		goalLat = 42.3595 # fire
		goalLon = -70.9924
		goalAlt = 100 
		self.goto(goalLat, goalLon, goalAlt)
		err = numpy.linalg.norm([goalLat - telemetry['latitude'], goalLon - telemetry['longitude']])
		tol = 0.0001 # Approximately 50 feet tolerance
		while err > tol:
			print('Aircraft is enroute to fire')
			time.sleep(10)
			err = numpy.linalg.norm([goalLat - telemetry['latitude'], goalLon - telemetry['longitude']])
			
		# Home

		print("Putting out fire")
		water_start_time = time.time()
		while(time.time() - water_start_time < 10.0):
			time.sleep(5)
			print("Fire remaining: " + str(round(telemetry['fires_pct_remaining'], 2)) + '%')
   
			# print("Fire polygons")
			# for poly in self.telemetry['fire_polygons']:
			# 	print(poly.wkt)
		print("Fire remaining: " + str(round(telemetry['fires_pct_remaining'], 2)) + '%')

        print("Go to second fire")
		goalLat = 42.3602 # fire
		goalLon = -70.9936
		goalAlt = 100 
		self.goto(goalLat, goalLon, goalAlt)
		err = numpy.linalg.norm([goalLat - telemetry['latitude'], goalLon - telemetry['longitude']])
		tol = 0.0001 # Approximately 50 feet tolerance
		while err > tol:
			print('Aircraft is enroute to fire')
			time.sleep(10)
			err = numpy.linalg.norm([goalLat - telemetry['latitude'], goalLon - telemetry['longitude']])
			
		# Home

		print("Putting out fire")
		water_start_time = time.time()
		while(time.time() - water_start_time < 10.0):
			time.sleep(5)
			print("Fire remaining: " + str(round(telemetry['fires_pct_remaining'], 2)) + '%')
   
			# print("Fire polygons")
			# for poly in self.telemetry['fire_polygons']:
			# 	print(poly.wkt)
		print("Fire remaining: " + str(round(telemetry['fires_pct_remaining'], 2)) + '%')





		
		
		
		
# This bit of code just makes it so that this class actually runs when executed from the command line,
# rather than just being silently defined.

if __name__ == "__main__":
	fcs = my_flight_controller()
	fcs.run()