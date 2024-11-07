"""
Returns List of all time stamps
"""
import os
import math

def get_float_time(file):
	numbers = []
	with (open(file, "r")) as file:
		for line in file:
			num = ""
			if line[0] == 'M':
				continue
			for char in line:
				if char >= '0' and char <= '9':
					num += char
			numbers.append(int(num) / 1000)
	return numbers

def get_time(file):
	numbers = []
	with (open(file, "r")) as file:
		for line in file:
			num = ""
			if line[0] == 'M':
				continue
			for char in line:
				if char >= '0' and char <= '9':
					num += char
			numbers.append(math.floor(int(num) / 1000))
	return numbers

def get_dict_time(list):
	dict = {}
	for num in list:
		# add instance in dictionary or add new entry in dictionary
		try:
			dict[num] += 1
		except Exception as e:
			dict[num] = 1
	return dict

def get_rpm(dict):
	# Currently have number of pulses per second
	for num in dict:
		print ("Second:", num)
		rps = (dict[num] / 48)
		rpm = rps * 60
		mph = rpm * 3.14159265389 * 1.8 * 60 / 5280
		print ("RPM:", "\x1b[10;42m", round(rpm, 2), "\x1b[0m")
		print ("MPH:", round(mph, 2))

def get_rpm_dict(dict, pulse):
	new_dict = {}
	for num in dict:
		rps = (dict[num] / pulse)
		rpm = rps * 60
		new_dict[num] = rpm

	return new_dict

def get_mph_dict(rpm_dict):
	new_dict = {}
	for num in rpm_dict:
		mph = (rpm_dict[num] * 60 * 3.14159265389 * 1.8 / 5280)
		new_dict[num] = mph

	return new_dict

def get_list_speed(dict, pulse):
	speed_dict = get_mph_dict(get_rpm_dict(dict, pulse))
	speed_list = []
	for num in dict:
		for i in range(dict[num]): # looping through the number of instances of pulses
			speed_list.append(speed_dict[num])

	return speed_list

