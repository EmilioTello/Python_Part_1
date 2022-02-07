num1 = 42 # variable declaration, initialize number or integer
num2 = 2.3 # variable declaration, initialize number or integer
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access list value 
pizza_toppings.append('Mushrooms') # add value to list
print(person['name']) # log statement, access dictionary value
person['name'] = 'George' # assign value
person['eye_color'] = 'blue' # add value to dictionary
print(fruit[2]) # log statement, access value of tuple

if num1 > 45: # if conditional
    print("It's greater") # log statement
else: # else conditional
    print("It's lower") # log statement

if len(string) < 5: # if conditional, length check
    print("It's a short word!") # log statement
else if len(string) > 15: # else if conditional, length check
    print("It's a long word!") # log statement
else: # else conditional
    print("Just right!") # log statement

for x in range(5): # for loop
    print(x) # log statement
for x in range(2,5): # for loop
    print(x) # log statement
for x in range(2,10,3):
    print(x) # log statement
x = 0 # for loop start
while(x < 5): # while loop
    print(x) # log statement
    x += 1 # while loop increment

pizza_toppings.pop() # delete value from list
pizza_toppings.pop(1) # delete value from list

print(person) # log statement
person.pop('eye_color') # delete value from dictionary
print(person) # log statement

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # if conditional
        continue # for loop continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if conditional
        break # for loop stop

def print_hello_ten_times(): # function start
    for num in range(10): # for loop
        print('Hello') # log string

print_hello_ten_times() # log statement of function argument

def print_hello_x_times(x): # function start
    for num in range(x): # for loop
        print('Hello') # log string

print_hello_x_times(4) # log statement of function argument

def print_hello_x_or_ten_times(x = 10):# function start
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # log statement
print_hello_x_or_ten_times(4) # log statement


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'
