my_list = [10, 20, 30]
print(my_list)

my_list2 = []
my_list2.append(11)
my_list2.append(22)
my_list2.append(33)
print(my_list2)

print(len(my_list))

fruits = ["banana", "apple", "blueberry", "cherry"]

is_banana_included = "banana" in fruits
print("Is banana included? ", is_banana_included)

index_cherry = fruits.index("cherry") # 인덱스는 0부터 시작
print(index_cherry)

numbers = [3, 2, 1, 3, 8, 6, 7, 5]
print("Unsorted ", numbers)
numbers.sort()
print("Sorted ", numbers)

numbers.sort(reverse=True)
print("Sorted (Reverse) ", numbers)