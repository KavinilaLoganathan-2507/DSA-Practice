#-----------------------------------------------------------#
#Class and Object
#class is a blueprint of an object. It is a collection of objects.
#Object is an instance of a class. It is a real-world entity.Ever objects have its own unique identity, state and behavior.
#object is a collection of data and methods/function .
# Creating an object is called instantiation. [Objectname = Classname()]
#The process of creating a class is called class definition.
#Access class data . Dot operator is used (Objectname.Variablename)
#Simple Class creation , variable and value .
#Variables is Attributes & using dot operator
#Class methods/function - to perform some actions - uses dot operator 
#__init__ method is a constructor method which is automatically called when an object of the class is created.
# It is used to initialize the variables/attributes of the class.
#Called only once when object is created . __x__(special method)
class Person:
    name ="John"
    age = 30
    #object creation
P1 = Person()

#Accessing class data using object name and dot operator
print(P1.name)
print(P1.age)
#-----------------------------------------------------------#
class Student:
    name = input("Enter the name of the student: ")
    roll_no = int(input("Enter the roll number of the student: "))
def greet(self): #self points to the current object of the class
    print(f"Hello, {self.name}!")
S=Student()
S.greet() #called greet method using object S

#-----------------------------------------------------------#
#__init__ method
class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
S1=Student(1,"John")
S2=Student(2,"Alice")
print(S1.id,S1.name)
print(S2.id,S2.name)

#__init__ with function
class Student:
    def __init__(self,name,fee):
        self.name=name
        self.fee=fee
    def display(self):
        print(f"Name: {self.name}, Fee: {self.fee}")
user_name = input("Enter student's name: ")
user_fee = int(input("Enter student's fee: "))
S1=Student(user_name,user_fee)
S1.display()
#-----------------------------------------------------------#
#delete object
del S1
print(S1.name) #name error tells that the object is deleted
 #-----------------------------------------------------------#
 #pass statement
 #used as a placeholder for future code. 
 # When the pass statement is executed, nothing happens, 
 # but you avoid getting an error when empty code is not allowed.
 
 
class MyClass:
     pass  # Placeholder for future code
 
 #class function never be empty  .
 # When the compiler sees the pass statement, it does nothing and moves on to the next line of code.

#---------------------------------------------------------------#

class Student:
    def __init__(self, name, mark_10th, mark_12th): 
        self.name = name
        self.mark_10th = mark_10th
        self.mark_12th = mark_12th

    def get_details(self):
        print(f"\n--- Student Details ---")
        print(self.name)
        print(self.mark_10th)
        print(self.mark_12th)


S1_name = input("Enter the name of the student: ")
S1_mark_10th = int(input("Enter 10th mark: "))
S1_mark_12th = int(input("Enter 12th mark: "))


int(input("Enter 12th mark: "))

S2_name = input("Enter the name of the student: ")
S2_mark_10th = int(input("Enter 10th mark: "))
S2_mark_12th = int(input("Enter 12th mark: "))

s1 = Student(S1_name, S1_mark_10th, S1_mark_12th)
s2 = Student(S2_name, S2_mark_10th, S2_mark_12th) 


s1.get_details()
s2.get_details()
