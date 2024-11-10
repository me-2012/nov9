# from datetime import datetime

# class Person:
#     def __init__(self, email, first, last, dob, city):
#         self.email = email
#         self.first  = first
#         self.last = last
#         self.dob = datetime.strptime(dob, "MM/DD/YYYY")
#         self.city = city

# def age(dob):
#     today = datetime.now()
#     if dob.month > today.month:
#         age = today.year - dob.year - 1
#     elif dob.month < today.month:
#         age = today.year - dob.year
#     else:
#         if dob.day > today.day:
#             age = dob.year - today.year - 1
#         else:
#             age = dob.year - today.year
#     return int(age)

# def searchAge():
#     dob = input("Enter your date of birth: ")
#     age = age(dob)
#     for person in people.values():
#         if person.age == age:
#             print(person.first, person.last)

# def searchCity():
#     city = input("Enter your city: ")
#     for person in people.values():
#         if person.city == city:
#             print(person.first, person.last)

# def searchFirst():
#     first = input("Enter your first name: ")
#     for person in people.values():
#         if person.first == first:
#             print(person.first, person.last)

# def searchLast():
#     last = input("Enter your last name: ")
#     for person in people.values():
#         if person.last == last:
#             print(person.first, person.last)

# def addPerson(email):
#     first = input("Enter your first name: ")
#     last = input("Enter your last name: ")
#     dob = input("Enter your date of birth (MM/DD/YYYY): ")
#     city = input("Enter your city: ")
#     people[email] = Person(email, first, last, dob, city)
#     print("Person added")

# people = {}

# while True:
#     email = input("Enter your email: ")
#     if email == "last":
#         searchLast()
#     if email == "first":
#         searchFirst()
#     elif email == "city":
#         searchCity()
#     elif email in people:
#         print("Found: ", people[email].first, people[email].last)
#     else:
#         addPerson(email)

class State:
    def __init__(self, name, capitol, population):
        self.name = name
        self.capitol = capitol
        self.population = population
    def printState(self):
        print(self.name, self.capitol, self.population)

def createState(): # This is a function
    name = input("Enter a name for your state: ")
    capitol = input("Enter a capitol for your state: ")
    population = int(input("Enter a population for your state: "))
    state = State(name, capitol, population)
    state.printState()

createState()

'''
hw:

1. verify date is in format MM/DD/YYYY
2. add  function to search by first name
3. add  function to search by last name
4. create a state class with name capital and populatioin
5. create a list of states and write a function that finds the state with the biggest population

'''
