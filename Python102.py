#Using multiple lists and seeing where they intersect
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

#Dicts
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#You can add more key:values to an existing dictionary // delete values with del dict[]
alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)
#You can modify values in an existing dictionary
alien_0['x_position'] = 10
print(alien_0['x_position'])
#Looping through dicts -- if looping using Key AND value, you need dict.items(), otherwise defaults to Key or you can call the values with dict.value()
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
# for key in user_0:
#     print("\nKey: " + key)
print(list(user_0.items())[1])

my_dict = {"x" : "y", "a" : "b"}
my_dict.update({"test" : 3})
print(my_dict["test"])

# #input() functions and While loops
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print("\nHello, " + name + "!")
# #input() always returns a string so if you want it to be a number use height = input("How tall are you in inches") / height = int(height)

#While loop
current_number = 1
while current_number <= 5:
 print(current_number)
 current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


#Writing functions
def describe_pet(animal_type, pet_name):
 """Display information about a pet.""" #basically a comment but when defining a function, this is the "proper" way to document what the function does
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='cat', pet_name='steven') #position matters when you have to pass multiple arguments/parameters but you can also set them to = which parameter it is)
#in the "def" line, you can also default one of the paramters so when passing the argument, you only need to describe one arguement:
#def describe_pet(animal_type='dog', pet_name):
#describe_pet('steven') ----- this defaults animal type to dog

#when you're passing multiple parameters through a function, you can make them optional by using if statement
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def make_pizza(*toppings): #asterisk* lets you pass as many arguemnts as u want
 """Print the list of toppings that have been requested."""
 print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Another example of asterisk
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
print(user_profile)

#importing functions from different modules (which are basically just another .py file) -- import [file name (without .py)] then you use the function like this:  filename.function()
#if you import a specific function from a module -- from filename import functionname -- then you only need to use function()
#you can give the imported function an alias -- from filename import functionname as [x](alias) -- then the function becomes x()
#you can also import the module as an alias -- import filename as x