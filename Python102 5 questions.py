#Question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    return user_name
name = hello_name('kenny')
print("hello_" + name +'!\n')

#Question 2 Print first 100 odd numbers in Python.
odd100 = [value for value in range(1,100,2)]
print(odd100, end="\n\n")

#Question 3 Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    return max(a_list)
list = [1, 2, 3, 4545]
print(max_num_in_list(list))

#Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False
years = [2004, 2100, 2400, 1999]
for year in years:
    print(year, is_leap_year(year))

#Question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    for x in range(len(a_list)-1):
        print(a_list[x], a_list[x+1])
        if a_list[x] == a_list[x+1]-1:
            continue
        else:
            return False
    return True

mylist = [1, 2, 4, 5]
print(is_consecutive(mylist))

# if 2 == 3-1
