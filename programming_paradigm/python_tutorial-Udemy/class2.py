from class1 import Class_of_things
import datetime

class User:
    """ This class collects input from user and later display all the collected 
    informations provided by the user."""
    def __init__(self, first_name, last_name, dob, resident, describtion):
        self.f_name = first_name
        self.l_name = last_name
        self.place = resident
        self.birthday = dob
        self.about_user = describtion

# A traditional function containing User class object 

def my_classes():

    personal_data = User(

        input("First name: "), 
        input("Surname: "),
        int(input("DOB: ")),
        input("Address: "), 
        input("""About me: """)
        
        ) 
    
    print("\n")
    print("Loading....... \n")
    
    # current_year = datetime.date.year()

    print(f'Name: {personal_data.f_name} {personal_data.l_name} \nAge: {2023 - personal_data.birthday} \nResident: {personal_data.place} \nAbout Me: {personal_data.about_user}  ')

my_classes()
# help(User)

print('\n')

# object of the class declared in class1.py file

obj = Class_of_things("Light pole", "Gray", "7ft")

print( "The object name is " + obj.name + " it has a " + obj.color + " color" + " with a height of " + obj.height)
print(f"The item name is {obj.name} it has a {obj.color} color with a height of {obj.height}")

print(obj.name)




