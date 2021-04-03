# List - use "[]""
subway = ["Terry", "Sebastian", "Dylan"] 
print(subway) # ['John', 'Tim', 'Dylan']

# .index finds an index of an element
print(subway.index("Dylan")) # 0 

# .append inserts a new element at the end of the list
subway.append("Justin")
print(subway) # ['John', 'Tim', 'Dylan', 'Justin']

# inserting a new element "Ian" in subway[1]
subway.insert(1, "Ian")
print(subway) # ['Terry', 'Ian', 'Sebastian', 'Dylan', 'Justin']

# deleting an element from the back
subway.pop()
print(subway) # ['Terry', 'Ian', 'Sebastian', 'Dylan']

# check same element
subway.append("Dylan")
print(subway) # ['Terry', 'Ian', 'Sebastian', 'Dylan', 'Dylan']
print(subway.count("Dylan")) # 2

# sorting a list
num_list = [5, 3, 2, 4, 1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# reversing an order of a list
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# clearing every element in a list
num_list.clear()
print(num_list) # []

# list can be used with different data types
num_list = [5, 2, 4, 3, 1]
mix_list = ["Shri", 20, False]
print(mix_list) # ['Shri', 20, False]

# extending a list
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, 'Shri', 20, False]