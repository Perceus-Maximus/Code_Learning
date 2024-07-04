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



######### APPEND LIST WITH THE LENGTH OF THE ORIGINAL LIST ################
#Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list
#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))


############# APPEND LIST AFTER ADDING THE LAST TWO COMPONENTS OF THE LIST TOGETHER 3 TIMES ##############
#Write your function here
def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


######### The function should return the last element of the list that contains more elements ###########
######### If both lists are the same size, then return the last element of my_list1 ##############
# Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]
#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


################Does item appear more than n ##########
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False
#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


############# Combine lists and sort ##########
#Write your function here
def combine_sort(my_list1, my_list2):
  unsorted = my_list1 + my_list2
  sortedList = sorted(unsorted)
  return sortedList
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


#Write your function here - Print every three numbers from the start including 100
def every_three_nums(start):
  return list(range(start, 101, 3))
#Uncomment the line below when your function is done
print(every_three_nums(91))


#Write your function here
def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]
#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))



def double_index(my_list, index):
  # Checks to see if index is too big
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list 
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list
  print(double_index([3, 8, -10, 12], 2))


def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2
  else:
    return my_list[int(len(my_list)/2)]

#Write your function here

def divisible_by_tens(numbers):
  count = 0
  for number in numbers:
    if (number % 10 == 0):
      count += 1
  return count

def divisible_by_ten(nums):
  for num in nums:
    if num % 10 == 0:
      print(num)


print(divisible_by_tens([20, 25, 30, 35, 40]))

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


#Write your function here
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


#Write your function here
def delete_starting_evens(my_list):
  while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


#Write your function here
def odd_indices(my_list):
  my_new_list = []
  for index in range(1, len(my_list), 2):
    my_new_list.append(my_list[index])
  return my_new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))




#Write your function here
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list
  
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))



#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
    return lst1
  else:
    return lst2 
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))



#Write your function here
def over_nine_thousand(lst):
  sum = 0 
  for number in lst:
    sum += number
    if sum > 9000:
        break
  return sum
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))



#Write your function here
def max_num(nums):
  return max(nums)

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#######ALTERNATIVE OPTION
def max_nums(numbers):
  maximum = numbers[0]
  for number in numbers:
    if number > maximum:
      maximum = number
  return maximum


  #Write your function here
def same_values(lst1, lst2):
  lst1 = []
  lst2 = []
  new_list = []
  for index in range(len(lst1)):
    if lst1[0] == lst2[0]:
      return new_list.append()

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
  print(max_nums([50, -10, 0, 75, 20]))
