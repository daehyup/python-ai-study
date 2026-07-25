empty_set = set()
my_set = {1, 2, 3, 4, 5}

print(my_set)

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")

fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"banana", "kiwi", "mango"}

# 합집합    
union_set = fruits1.union(fruits2)
print(union_set)

# 교집합
intersection_set = fruits1.intersection(fruits2)
print(intersection_set)

# 차집합
difference_set = fruits1.difference(fruits2)
print(difference_set)