print("Hello World!") # the way this command works is simple you use print and inside () you put something you want to print 
input("promt or what text will be printed") # this is used to take user input
# the inner stuff will execute 1st then the rest will execute
print("hello" + input("What's your")) # this input will be replaced by the user inputed value
len() # this method is used to get the length of the string
print(len(input("What is your name"))) # the input function will replaced by the string and the length will be printed
name = input("Enter your name ") # here name acts as a variable which will store the data entred by the user
# the variable can be used to refer later on to the user input 
#we can varay the value of the variable like
name = 'Kunal Chauhan'

user_name  #✅ you can use underscore as space 
#user name ❌ you cant use spacebar in your variable
number1 #✅ you can have a number between or at end
# 2number # ❌ you can't start a variable with a number
# try to make your variable more meaningful


# project 1 🎊🎊✨

# Band name genrator

print("Welcome to the band name genrator")

city = input("In which city you grew up\n")

pet_name = input("What is your pet's name\n")

band_name = city + " " + pet_name

print("Your band name could be "+band_name)
