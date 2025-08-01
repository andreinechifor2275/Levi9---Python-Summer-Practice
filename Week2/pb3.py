import random
def log_temperature(temp):
    with open("temperatures.txt", "a") as file:
        file.write(f"{temp}\n")

def read_temperatures():
    sum = 0
    count = 0
    with open("temperatures.txt", "r") as file:
        for line in file:
            sum = sum + float(line)
            count = count + 1

    avg = sum / count
    print(f"Average temperature: {avg}")

for i in range(10):
    temp = random.uniform(40.0, 65.0)
    log_temperature(temp)

read_temperatures()