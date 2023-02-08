"""
my_input = input("type in number 1: ")
my_input2 = input("type in number 2: ")
my_num1 = int(my_input)
my_num2 = float(my_input2)
print(my_num1 + my_num2)
"""
""""
my_list = [1, 2, 3, 4]
print(my_list)
print(my_list[2])
my_list[2] = -4
print(my_list[2])
my_second_list = [1, 'Martina', [2, 4, 5]]
print(type(my_second_list))
my_list.append(9)
print(my_list)

my_tuple = (1, 2, 3)
print(type(my_tuple))
print(my_tuple[2])
# my_tuple.append(9) ?
print(len(my_tuple))

my_set = {1, 2, 3}

i = 1
while i <= 8:
    print(i * '*')
    i = i + 1



# another list
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 9)
numbers.remove(3)
# numbers.clear() clears the list
# print(numbers)
# print(1 in numbers) # checking if 1 is in the numbers list -> True
print(len(numbers)) # checking the amount of items in a list -> 5

numbers = [1, 2, 3, 4, 5]
#for item in numbers:    - the for loop is easier here
#   print(item)
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

numbers = range(4, 10, 3) # 4+3, +3 aż do 10, bez 10
#print(numbers)
for number in numbers:
    print(number)
"""
