import urllib3
import json
import requests
import urllib.parse
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
	

for i in range(0, 40):
	myListOfSwell.append(data[i]['swell']['absMinBreakingHeight'])
	myListOfWind.append(data[i]['wind']['compassDirection'])

	unixDayLoop = data[i]['localTimestamp']
	dayLoop = datetime.utcfromtimestamp(unixDayLoop).strftime('%A %H:00')
	myListOfDays.append(dayLoop)

	windDirection = myListOfWind[i]

	if windDirection == 'SSW':
		print(myListOfSwell[i])
		print(myListOfDays[i])
		print(myListOfWind[i])

		print('Good')



		print()



plt.bar(returnDate(), returnSwell())
plt.xlabel('Date')
plt.ylabel('Swell Height')


plt.title('Garretstown Swell Report')

plt.show()



#for i in data:
#	print(i)

























