# Create  an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Alex"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student["first_name"] = "Parv"
student["last_name"] = "Patel"
student["gender"] = "Male"
student["age"] = 20
student["marital_status"] = "Single"
student["skills"] = ["Programming", "Problem Solving", "Communication"]
student["country"] = "India"
student["city"] = " Anand"
student["address"] = "123 Main Street"
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))
print(student['skills'])

# Modify the skills values by adding one or two skills
student['skills'].append('e-Sports')
print(student['skills'])

#  Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using _items()_ method
stu_Tuple = student.items()
print(stu_Tuple)

# Delete one of the items in the dictionary
del student["marital_status"]
print(student)


# Delete one of the dictionaries
del dog



