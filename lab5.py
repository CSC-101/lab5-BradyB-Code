import data
import math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
#Input are two instances of the Time class. We want to make new variables to store
#the combined values of each attribute of the class objects. Also, to change
#any number of seconds over 59 to minutes, we need an if statement for the
#seconds to minutes and minutes to hours. The output is of the Time class with
#the new total values we found.
def time_add(time1: data.Time, time2: data.Time)->data.Time:
    sec = 0
    min = 0
    if (time1.second + time2.second) < 60:
        total_seconds = time1.second + time2.second
    else:
        total_seconds = (time1.second + time2.second) - 60
        sec = 1

    if (time1.minute + time2.minute + sec) < 60:
        total_minutes = time1.minute + time2.minute + sec
    else:
        total_minutes = (time1.minute + time2.minute + sec) - 60
        min = 1
    total_hours = time1.hour + time2.hour + min
    return data.Time(total_hours, total_minutes, total_seconds)

# Part 4
#Input is one list containing floats. We want to iterate through the list with a
#for loop and use an if statement to compare each element to the one ahead of it
#in the index. We will return False when we see that it is not in order, else return True
def is_descending(list1: list[float])->bool:
    for i in range(len(list1)-2):
         if list1[i] >= list1[i + 1]:
             return False
    return True

# Part 5
#Input is an int list and two other integers. We can return the largest value
#with the max function and give the bounds of the "lower" integer, and the
#upper is not inclusive so 1 + the "upper" integer to get the desired answer/
def largest_between(list2: list[int], lower: int, upper: int)->int:
    return max(list2[lower:(upper+1)])

# Part 6
#Input is a list with elements from the Point class. We want to keep track of the max distance
#so we can save the max index, so we create two variables to hold the value of the distance
#and index. Then, use a for loop to iterate through the list using enumerate to take the index
#and the distance, which we test with the max distance. If the new distance is larger, it's
#value will be stored in the max index variable and the loop continues until it goes through
#the whole list. Then the max index which was also stored alongside the max distance, is returned.
def furthest_from_origin(list_a: list[data.Point]):
    max_dist = -1
    max_index = 0
    for index, point in enumerate(list_a):
        distance = math.sqrt(point.x ** 2 + point.y ** 2)
        if distance > max_dist:
            max_dist = distance
            max_index = index
    return max_index

