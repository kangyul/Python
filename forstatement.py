# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호: {0}".format(waiting_no))

# randrange()
# for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
#     print("대기번호: {0}".format(waiting_no))

# starbucks =["Iron Man", "Thor", "Groot"]
# for customer in starbucks:
#     print("{0}, Coffee is ready.".format(customer))

# One line for statement
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# name to length of a name
students = ["Iron Man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# name to Capital
students = ["Iron Man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)