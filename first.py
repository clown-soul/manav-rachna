#String functions
str = "MANDEEP"
str.casefold()
str.capitalize()
str.count("e")
str.isalpha()
str.index("e")
str.istitle()
str.lstrip()
str.upper()

#sets functions
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)   #returns a set that are present in both sets
print(z)


x="hello world"
print(x[:2],x[:-2],x[-2:])
print(x[-1:-5:-1])
print(x[-4:-2],x[2:4])

i=str(input("enter first character : "))
a=str(input("enter second character: "))
s=str(input("enter third character: "))
o=str(input("enter fourth character: "))
print(i+s+a+o)

t="all"
t[0]                    #in this case since u have not written print()it had changed the output by output of t
t

x="hello"+\
"to print"+\
"world"
for char in x:
    y=char
    print(y+":",end=".")

my_list = [1, 2, 3]
my_list.append(4)
# Result: [1, 2, 3, 4]


list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
# Result: [1, 2, 3, 4, 5]


my_list = [1, 2, 3]
my_list.insert(1, 5)
# Result: [1, 5, 2, 3]

my_list = [1, 2, 3, 2]
my_list.remove(2)
# Result: [1, 3, 2]


my_list = [1, 2, 3]
popped_element = my_list.pop(1)
# Result: my_list is now [1, 3], and popped_element is 2

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
for i in range (0,2,1):
  print (my_dic(i))


