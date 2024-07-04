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



# Function and greater than practice
# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True



#Divisible by function#######
# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False
# Uncomment these print() function calls to test your divisible_by_ten() function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False


#####GREATER THAN OR EQUAL TO AND LESS THAN AND EQUAL TOO
# Write your in_range function here:
def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False


######Comparing String Names#################
# Write your same_name function here:
def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False


##########ALWAYS FALSE############
# Write your always_false function here:
def always_false(num):
  if (num > 0 and num < 0):
    return True
  return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False


############ LONG VERSION ############
# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  if (rating > 5 and rating < 9):
    return "This one was fun."
  if rating >= 9:
    return "Outstanding!" 
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

############## SHORTER VERSION ############
def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"
  # Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."


############# MAX Number ELS IF STATEMENT #################
# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
