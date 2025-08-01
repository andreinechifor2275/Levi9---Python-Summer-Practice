import math
import random
from idlelib.pyparse import trans


def exercise_1(text):
    freq = {}
    for char in text:
        if char in freq and char.isalpha():
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def exercise_2():
    p = 1000
    coords_set = set()
    while len(coords_set) < p:
        x = random.randint(-90, 90)
        y = random.randint(-180, 180)
        coords_set.add((x, y))

    coords = list(coords_set)

    max_dist = 0
    min_dist = float("inf")
    closest_coord = []
    farthest_coord = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            if math.dist(coords[i], coords[j]) > max_dist:
                max_dist = math.dist(coords[i], coords[j])
                farthest_coord = coords[i], coords[j]
            elif math.dist(coords[i], coords[j]) < min_dist:
                min_dist = math.dist(coords[i], coords[j])
                closest_coord = coords[i], coords[j]

    print("Farthest distance: ", max_dist, "; Coords: ", farthest_coord)
    print("Closest distance: ", min_dist, "; Coords: ", closest_coord)

def read_plates(filename):
    with open(filename, 'r') as file:
        return set(line.strip() for line in file)

def exercise_3():
    cars_in = read_plates("cars_in.txt")
    cars_out = read_plates("cars_out.txt")
    existing_cars = read_plates("existing_cars.txt")


    print("Existing cars: ", existing_cars)
    print("cars_out: ", cars_out)
    print("cars_in: ", cars_in)
    cars_parked_today = cars_in & cars_out
    cars_already_parked_left_today = existing_cars & cars_out
    cars_in_parking = cars_in | existing_cars - cars_out
    print("Cars that have parked and also left today: ", cars_parked_today)
    print("Cars that were already parked (before today) and left today: " , cars_already_parked_left_today)
    print("Cars that are still in the parking lot: ", cars_in_parking)


def exercise_4():
    transactions = []
    transaction_count = dict()
    item_bought_count = dict()

    with open("input_tranzactii.txt", 'r') as file:
        transactions = [tuple(line.strip().split(',')) for line in file]

    for transaction in transactions:
        name, item, amount = transaction[0], transaction[1], transaction[2]
        if name in transaction_count.keys():
            transaction_count[name] += 1
        else:
            transaction_count[name] = 1

        if item in item_bought_count.keys():
            item_bought_count[item] += int(amount)
        else:
            item_bought_count[item] = int(amount)

    print("Transactions count: ", transaction_count)
    print("Item bought count: ", item_bought_count)
    print("Most transactions: ", max(transaction_count), "-> ", max(transaction_count.values()))
    print("Most bought item: ", max(item_bought_count), "-> ", max(item_bought_count.values()))

def exercise_5():
    dictionary = dict()
    averages = dict()
    with open("input_studenti.txt", 'r') as file:
        for line in file:
            line = line.strip()
            line_split = line.split(';')
            name = line_split[0]
            subjects = line_split[1:]
            dictionary[name] = {}
            average_grade = 0

            for subject in subjects:
                subject_name, subject_grades = subject.split(':')
                grades = subject_grades.split(',')
                grades_list = list(map(int,grades))
                average_grade += float(sum(grades_list)) / len(grades_list)
                dictionary[name].update({subject_name: grades_list})

            average_grade = average_grade / len(subjects)
            averages[name] = average_grade
            print(f"Average grade for {name} ", average_grade)

    highest_average = max(averages, key=averages.get)
    print(f"Highest average: {highest_average} with {averages[highest_average]}")
    print(dictionary)

def exercise_6():
    intervals = []
    while len(intervals) < 100:
        x = random.randint(0, 1000)
        y = random.randint(x, 1000)
        intervals.append((x, y))

    merged_intervals = []
    print(intervals)
    intervals.sort(key = lambda x: x[0])
    print(intervals)

    for interval in intervals:
        if not merged_intervals:
            merged_intervals.append(interval)
        else:
            last_interval = merged_intervals[-1]
            if interval[0] <= last_interval[1]:
                merged_intervals[-1] = (last_interval[0], max(interval[1], last_interval[1]))
            else:
                merged_intervals.append(interval)
    print("Merged: ")
    print(merged_intervals)


if __name__ == '__main__':
     print(exercise_1("Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos."))
     print(exercise_2())
     exercise_3()
     exercise_4()
     exercise_5()
     exercise_6()