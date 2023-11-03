#Doc on how to create a mulitple input with python 
#first i print the brand name and use a sprator 

print("Welcome to your name band generator!")
print("------------------------------------------------\n") #---> \n --> stands for new line in python 
name  =  input("What is your name? \n")
city  =  input("What city are you form? \n")
pet  =  input("What is the name of your pet? \n")
print("------------------------------------------------\n")

print(f"Your Band Name is :{name}{city}{pet} ")# and i also use f-string  instead of using strings concatenation that known as pluse sign ("+")