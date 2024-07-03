# Define a welcome trip function 
def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
# No output since we are just defining the function

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")
# No output since we are just defining the function
# Call your function here:
directions_to_timesSq()

def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
print("Woah, look at the weather outside! Don't walk, take the train!")
trip_welcome()
# The print statement would print line 18 first and then line 19 since you called the function after printing line 18 that was not indented into the function

print("Checking the weather for you!")
def weather_check():
  print("Looks great outside! Enjoy your trip.")
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")
weather_check()
# False Alarm would print 2nd and function would print 3rd

def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")
trip_welcome("Times Square")
# prints a function that has a single parameter = Times Square as the destination

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)
generate_trip_instructions("Grand Central Station")
# Another Example

def trip_welcome(origin, destination):
  print("Welcome to Tripcademy")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)
print(trip_welcome("origin" + "destination"))  
# function with two paramaters "origin and destination

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  return trip_total
print(calculate_expenses(200, 100, 100, 5))


# Examples: 
# Positional arguments: arguments that can be called by their position in the function definition.
# Keyword arguments: arguments that can be called by their name.
# Default arguments: arguments that are given default values.
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France" , "Germany" , "Denmark")
trip_planner("Denmark" , "France" , "Germany")
trip_planner(first_destination = "Iceland" , final_destination = "Germany" , second_destination = "India")
trip_planner("Brooklyn" , "Queens")


# Built in Function versus User Defined Functions
destination_name = "Venkatanarasimharajuvaripeta"
# Built-in function: len()
length_of_destination = len(destination_name)
# Built-in function: print()
print(length_of_destination)
# 28
