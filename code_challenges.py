################REFRESHER##################

def some_function(some_input1, some_input2):
  # … do something with the inputs …
  return output

#Example that retirns the sum of the first and last elements of a given list
def first_plus_last(lst):
  return lst[0] + lst[-1]
  
#### OUTPUT
#### >>> first_plus_last([1, 2, 3, 4])
#### 5
#### >>> first_plus_last([8, 2, 5, -8])
#### 0
#### >>> first_plus_last([-10, 2, 3, -4])
#### -14


##### Else if Statement
num1 = 6
num2 = 3
# Write your if statement here
if num1 + num2 != 10:
  not_ten = True
else:
  not_ten = False
# Uncomment the below lines to show the result
print("Does the sum of the numbers equal 10? " + str(not_ten))




####### else_if_statement round 2 #####
# Monthly budget
budget = 2000
# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500
# Calculate the total amount of expenses
total = rent + internet_bill + electricity_bill + food_bill
# Check if the total is greater than the budget and store the result in over_budget
if total > budget:
  over_budget = True
else:
  over_budget = False
# Uncomment the below lines to see the results
print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))



### Function with else_if_statement
# Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else: 
    return False
#Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False





