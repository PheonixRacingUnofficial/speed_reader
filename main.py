import reader
import matplotlib.pyplot as plt

def main():
	file = "nov_1_log.txt"
	list_time = reader.get_time(file)
	dict = reader.get_dict_time(list_time)

	reader.get_rpm(dict)

	time = reader.get_float_time(file)

	list_speed_48 = reader.get_list_speed(dict, 48)

	list_speed_16 = reader.get_list_speed(dict, 16)

	plt.scatter(time, list_speed_48, color='b')

	plt.scatter(time, list_speed_16, color='r')

	plt.xlabel("Time (s)")
	plt.ylabel("Speed (Mph)")

	plt.title("Calculated Speed with 16 vs 48 pulses")

	plt.legend(["48 Pulses", "16 Pulses"])

	plt.show()


if __name__ == "__main__":
	main()
