# # print("Hello world")
# message = "hello world"
# print(message)

# first_name = "ada "
# last_name = "lovelace"
# full_name = first_name + last_name
# print(full_name)

# favorite_language = ' python ' 
# favorite_language.rstrip()
# print(favorite_language)

#2-9 favorite number
# fav_num = 5
# print(str(fav_num))

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title())

# TestList = ['1', '2', 3, '4'] 
# print(TestList[2]) - you can have both ints and strings in a list and still returns np]

names = ['justin', 'duy', 'albert', 'nate']
names[1] = 'rasen'
print(names[1])
names.append('duy')
print(names)
names.insert(1, 'cam') #inserts into index pos 1
print(names)
del names[1]  # .remove() methods lets you remove based on (x)string instead of [x]position
print(names)
first_friend = names.pop(4) #you can put the index pos into parenthesis for specific position
print(first_friend)
names.sort() #sorts alphabetically
print(names)
names.sort(reverse=True) #to permanently reverse list alphabetically
print(names) 
#to temporarily sort a list use "sorted() function NOT method. Functions don't use .'s like methods

# .reverse() method reverses order of list but doesn't sort it

print(len(names)) #len() function to find out length of list

names1 = ['kenny', 'justin', 'albert', 'nate']
for ballers in names1:
    print(ballers) #First time going through the loop: reads first name in the list and assigns it to
                   #"baller" variable then prints it. Loop goes back to beginning and prints the second
                   #thing in the list, and so on.
print(ballers.title() + " test123\n")
print(ballers) #the last thing it looped through was nate so ballers currently = 'nate'

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers) #In this example, the range() function starts with the value 2 and then
#adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end
#value, 11, and produces this result:

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

#4-3 use a for loop to print the numbers from 1 to 20
list20 = [value for value in range(1,21)]
print(list20)

#4-5
list_mil = [value for value in range(1,1000001)]
print(min(list_mil))
print(max(list_mil))
print(sum(list_mil))

#4-6
odd_nums = [value for value in range(1,20,2)]
print(odd_nums)

#4-7
threes = [value for value in range(3,31,3)]
print(threes)

#4-8
cubes = [value**3 for value in range(1,11)]
print(cubes)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())
#you can loop through a slice by using [x:y]

#you can copy a list by using [:] - purpose being if you want to append.() something to one list, it won't add it to the other
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]