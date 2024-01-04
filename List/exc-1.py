
# Declare an empty list
list1=[]

# add items to list
list1.append('hello')

# Display list
print(list1)

# Declare a list with more than 5 items
list2=['item1','item2','item3','item4',5,6]

#  Find the length of your list
print(len(list2))

# Get the first item, the middle item and the last item of the list
print(list2[0])
print(list2[int(len(list2)/2)])
print(list2[len(list2)-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['rohan',19,5.2,'single','23 yogidarsha township']
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# Print the list using _print()_
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[int(len(it_companies)/2)])
print(it_companies[len(it_companies)-1])

# Print the list after modifying one of the companies
it_companies[0]="Whatsapp"
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Instagram')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4,'Lenovo')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]=it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;&nbsp; '
s='#;&nbsp;'
s.join(it_companies)
print(it_companies)
print(s.join(it_companies))

#Check if a certain company exists in the it_companies list.
print('GOOGLE' in it_companies )

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:3])

#  Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[int(len(it_companies)/2)])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(int(len(it_companies)/2))
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack=front_end[:]
print(full_stack)
full_stack.insert(full_stack.index('Redux')+1,'Python')
full_stack.insert(full_stack.index('Redux')+2,'SQL')
print(full_stack)


