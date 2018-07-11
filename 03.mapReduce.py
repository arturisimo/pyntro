from functools import reduce
'''
	Ejercicio Python Map and Reduce pag 26


			Field Data Example
			0 - Date Time: 2014-03-15:10:10:31
			1 - Model name and number: Titanic 4000
			2 - Unique device ID: 1882b564-c7e0-4315-aa24-228c0155ee1b
			3 - Device temperature (Celsius): 58
			4 - Ambient temperature (Celsius): 36
			5 - Battery available (percent): 39
			6 - Signal strength (percent): 31
			7 - CPU utilization (percent): 15
			8 - RAM memory usage (percent): 0
			9 - GPS status (enabled=TRUE, disabled=FALSE): TRUE
			10 - Bluetooth status (enabled, disabled, or connected): enabled
			11 - WiFi status (enabled, disabled, or connected): enabled
			12 - Latitude: 40.69206648
			13 - Longitude: -119.4216429

'''

def celsiusAFahreinheit(s): return int(s) * float(9) / 5 + 32

path_file = '../data/loudacre.log'

file = open(path_file, 'rt')
lines = file.readlines()
file.close()

#Extract all the device temperature data into a tuple.
devices_temp = tuple([ int(line.split(',')[3]) for line in lines])

#Convert the temperatures to Fahrenheit using the Python map() function with
#an anonymous function to perform the conversion
temp_F = list(map(lambda temp:temp*9/5+32, devices_temp))

#Use reduce() to find the average device temperature
temp_average = reduce(lambda x,y: x+y, temp_F)/len(temp_F)

hottest_device_temp = reduce(lambda x,y: x if x > y else y, temp_F)

print (temp_F)
print (temp_average,'ªF')
print (hottest_device_temp,'ªF')