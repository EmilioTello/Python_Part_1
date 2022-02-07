# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False


# def values_greater_than_second(lst):
#     if len(lst)< 2:
#         return False
# second = lst[1]
# count = 0
# for num in lst:
#     if num < second:
#         new_list.append(num)
#         count += 1
# print(len(new_list))
# return new_list



# values_greater_than_second([5,2,3,2,1,4])



# def len_val(size,value):
#     num_list = []
#     for i in range(size):
#         num_list.append(value)
#     return num_list
# print(len_val(4,7))


# 200

# 200


# def countdown(num):
#     output =[]
#     for i in range(num,-1,-1):
#         output.append(i)
#     return output

# print(countdown(5))

# def print_and_return(list):
#     print(list[0])
#     return list[1]

# print (print_and_return([1,2]))
    


# def first_plus_length(a_list):
#     sum = (a_list[0]) + (len(a_list))
#     return sum

# print(first_plus_length([1,2,3,4,5]))


# def values_greater_than_second(some_list):
#     newList = []
#     if len(some_list) < 2:
#         return False
#     for i in range(len(some_list)):
#         if some_list[i] > some_list[1]:
#             newList.append(some_list[i])
#     print (len(some_list))
#     return newList

# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]))

# def this_that(a,b):
#     new_list = [b] * a
#     return new_list

# print (this_that(4,7))
# print (this_that(6,2))

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(some_list):
#     for i in range (len(some_list)):
#         output = ""
#         for a,b in some_list[i].items():
#             output += f"{a} - {b},"
#         print (output)

# iterateDictionary(students)



# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# class Car:

#     def __init__ (self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#     def car_description (self):
#         print(f"The {self.color} car has {self.mileage} miles.")
#         return self

# Blue_Car = Car("blue", 20000)
# Red_Car = Car("red", 30000)

# Blue_Car.car_description()
# Red_Car.car_description()



movie_info= [ 
    {
        'title':"ET",
        'year':1982,
        'genre':"Family"
    },
    {
        'title':"Princess Bride",
        'year':1986,
        'genre':"Adventure"
    },
    {
        'title':"Smoke Signals",
        'year':1998,
        'genre':"Comedy"
    },
    {
        'title':"Legends of the Fall",
        'year':1994,
        'genre':"Drama"
    },
    {
        'title':"A River Runs Through It",
        'year':1992,
        'genre':"Drama"
    },
    {
        'title':"Seven Years in Tibet",
        'year':1997,
        'genre':"Drama"
    }
]


# print(movie_info[1]['year'])

def nineties (movie_list):
    output = []
    for i in movie_list:
        if (i['year'] >= 1990) and (i['year'] <= 2000):
            output.append(i)
    return output

# print(nineties(movie_info))

print(nineties(movie_info))











# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# My Answer:
# 3
# 5
# 8
# Correct Answer:
# 3
# 5
# Error



# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)

# My Answer:
# 500
# 500
# 300
# 300
# 500
# Correct Answer:
# 500
# 500
# 300
# 500




# Do you need return self on __.init__ method?
# NO

# How to do a bank account transfer once classes are associated?

