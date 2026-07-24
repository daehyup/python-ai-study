my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[-1])
print(len(my_list))

print(my_list[4])  

sliced = my_list[1:4]
print(sliced)

fruits = ["apple", "banana", "cherry"]

# 바나나가 포함되어 있나요
is_banana_in_fruits = "banana" in fruits
print(is_banana_in_fruits)

index_cheery = fruits.index("cherry")  
print(index_cheery)

# 리스트의 정렬 
numbers = [5, 2, 9, 1, 7]
print("정렬 전:", numbers)
numbers.sort()
print("정렬 후:", numbers)
numbers.reverse()
print("역순 정렬 후:", numbers)

# 리스트의 요소 추가 및 제거
my_list = []
my_list.extend([1, 2, 3])
print(my_list)

# 리스트의 연산
my_list = [1, 2, 3]
my_list2 = [4, 5, 6]
result = my_list + my_list2
print(result)

del my_list[1]
print(my_list)

max_value = max(my_list2)
print(max_value)   
min_value = min(my_list2)
print(min_value)
print(f"최대값은 {max_value}이고, 최소값은 {min_value}입니다.")