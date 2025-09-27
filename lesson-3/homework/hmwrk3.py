1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.
royhat=('apple','nok','shaftoli','olcha','behi')
print(royhat[2])
2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.
nums1=(1,2,3,4,5)
nums2=(6,7,8,9,10)
print(nums1+nums2)

3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers=[1,2,3,4,5,6,7,8,9,10]
first=numbers[0]
middle=numbers[len(numbers)//2]
last=numbers[-1]
result=[first,middle,last]
print(result)
4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.
favorite_movies = ["Inception", "The Dark Knight", "Interstellar", "Avatar", "The Matrix"]# bu list
favorite=tuple(favorite_movies)
print(favorite)

5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.
cities=["London","Berlin","madrid","Paris","Lisbon"]
if "Paris" in cities:
    print( "ha bor")
else:
    print("yoq")
6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3, 4, 5]

# Method 1: Using slicing
duplicate_list = numbers[:]

# Method 2: Using list() constructor
duplicate_list2 = list(numbers)

# Method 3: Using copy() method
duplicate_list3 = numbers.copy()

print(duplicate_list)
print(duplicate_list2)
print(duplicate_list3)

7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.
numbers = [1, 2, 3, 4, 5]
numbers[0],numbers[-1]=numbers[-1],numbers[0]
print(numbers)
8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers=(1,2,3,4,5,6,7,8,9,10,11)
print(type(numbers))
nums1=numbers[3:7]
print(nums1)
9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.
colors = ["red", "blue", "green", "blue", "yellow", "blue"]

blue_count = colors.count("blue")

print("Blue appears", blue_count, "times.")

10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".
animals = ("lion", "tiger", "elephant", "giraffe", "zebra")
finding=animals.index("lion")
print(finding)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2

print(merged_tuple)

my_list = [10, 20, 30, 40, 50]
my_tuple = ("apple", "banana", "cherry")

print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

my_tuple = ("apple", "banana", "cherry")
listim=list[my_tuple]
print(listim)
numbers=(1,2,3,4,5,6,7,8,9,10,11)
print(type(numbers))
print(max(numbers))
print(min(numbers))
words = ("hello", "world", "python", "coding")

reversed_tuple = words[::-1]

print(reversed_tuple)

