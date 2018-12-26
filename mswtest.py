import json
import requests
from datetime import datetime

import matplotlib.pyplot as plt

response = requests.get("http://magicseaweed.com/api/28c500e859576a4f8bbcbe09c83e2492/forecast/?spot_id=52")

data = json.loads(response.text)

myListOfDays = []
myListOfSwell = []
myListOfWind = []


def returnSwell():

	for i in range(0, 40):
		myListOfSwell.append(data[i]['swell']['absMinBreakingHeight'])

	return myListOfSwell

def returnWind():

	for i in range(0, 40):
		myListOfWind.append(data[i]['wind']['compassDirection'])

	return myListOfWind
		

def returnDate():

	for i in range(0, 40):
		unixDayLoop = data[i]['localTimestamp']
		dayLoop = datetime.utcfromtimestamp(unixDayLoop).strftime('%A %H:00')
		myListOfDays.append(dayLoop)
	
	return myListOfDays


fig, ax = plt.subplots(figsize=(12, 6))

swellBars = ax.bar(returnDate(), returnSwell())	


def windChanger(firstWind, secondWind, thirdWind):

	for i in range(0, 40):

		myListOfWind.append(data[i]['wind']['compassDirection'])

		windDirection = myListOfWind[i]

		if windDirection == firstWind or windDirection == secondWind or windDirection == thirdWind :
			print(myListOfSwell[i])
			print(myListOfDays[i])
			print(myListOfWind[i])

			print('Good')

			swellBars[i].set_color('g')

		else:

			swellBars[i].set_color('r')

			print()


windChanger('S', 'SSW', 'SW')


plt.xlabel('Date')
plt.ylabel('Swell Height')

plt.title('Garretstown Swell Report')

plt.show()

