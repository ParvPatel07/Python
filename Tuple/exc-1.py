# Create an empty tuple
tuple = ()

# Create a tuple containing names of your sisters and your brothers 
sister = ("Monica" , "Phoebe" , "Rachel" , "Jenice")
brother = ("Chandler" , "Joey" , "Ross", "Gunther")

# Join brothers and sisters tuples and assign it to 
siblings=sister+brother
print(siblings)

# How many siblings do you have
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ("John", "Maria")+siblings 
print(family_members)

# Unpack siblings and parents from family_members
Father, Mother, *Siblings = family_members
print(Father)
print(Mother)
print(Siblings)
