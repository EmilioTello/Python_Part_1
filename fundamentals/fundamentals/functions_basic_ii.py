#1
def countdown(a):
    output = []
    for x in range(a,-1,-1):
        output.append(x)
    return output
print(countdown(5))

#2
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([3,2]))

#3
def first_plus_length(some_list):
    sum = (some_list[0]) + (len(some_list))
    return sum
print (first_plus_length([1,2,3,4,5]))

#4
def greater(next_list):
    if len(next_list) < 2:
        return False
    output = []
    for i in range(0,len(next_list)):
        if next_list[i] > next_list[1]:
            output.append(next_list[i])
    print(len(output))
    return output

print(greater([5,2,3,2,1,4]))
print(greater([3]))

#5
def length_and_value(c,d):
    output = [d] * c
    return output
print(length_and_value(4,7))
print(length_and_value(6,2))