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


# Min, Max, and Round Built in Functions
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(9.75, 15.50, 5.99, 2.00)
print(max_price)
# Prints 15.50
min_price = min(9.75, 15.50, 5.99, 2.00)
print(min_price)
# Prints 2.00
rounded_price = round(tshirt_price, 1)
print(rounded_price)
# Prints 9.8 - seond input is how many decimal places. - O would round to 10 - 2 would round to 9.75


favorite_locations = "Paris, Norway, Iceland" # Without adding this line defining our variables outside of the function we would not be able to access favorite locations
def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)
print_count_locations()
show_favorite_locations()


def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate # Return lets us use a value calculated or "created" in a function outside of the function
new_zealand_exchange = calculate_exchange_usd(100, 1.4)
print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")
# Output: 100 dollars in US currency would give you 140 New Zealand dollars


##########
########### - Hard example
current_budget = 3500.75
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget)) 
print_remaining_budget(current_budget)


shirt_expense = 9 # Can use this inside and outside of the function
def deduct_expense(current_budget, shirt_expense):
  return current_budget - shirt_expense # Lets us declare new_budget after shirt outside the function by assigning it to the called deduct expense function 
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense) # minus the $9 that is assigned to shirt expense
print_remaining_budget(new_budget_after_shirt)

