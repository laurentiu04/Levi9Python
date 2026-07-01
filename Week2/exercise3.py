"""
 Problem 3: Temperature Logger (Read/Write File)
Write two functions:

 - log_temperature(temp) ➔ Appends the temperature to a file named "temperatures.txt".
 - read_temperatures() ➔ Reads all temperatures from the file and prints the average temperature

Example:
log_temperature(25) -> saves 25 in file
log_temperature(30) -> saves 30 in file
read_temperatures() ➔ Average temperature: 27.5°C
"""

def log_temperature(temp):
    try:
        with open("temperatures.txt", "a") as log_file:
            log_file.write(str(temp) + "\n")
    except IOError as error:
        print(f"Error while trying to log temperature:\n {error}")

def read_temperatures():
    try:
        with open("temperatures.txt", "r") as log_file:
            avg = 0
            line_count = 0
            for line_num, line in enumerate(log_file, 1):
                avg += int(line)
                line_count += 1

            print(f"Average temperature: {avg/line_count}°C")

    except IOError as error:
        print("Error while trying to read temperatures:\n" + error);

log_temperature(20)
log_temperature(25)
log_temperature(10)
read_temperatures()