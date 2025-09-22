print(0)
print(1)
print(2)
print(3)
print(4)

print()

count = 0
while count < 5:
    print(count)
    count += 1

print()

#для элементов               в  последовательности    :
#for <название_переменной>   in <последовательность>  :
for count in range(5):
    print(count)

str1 = "hello world"
print()

for letter in str1:
    print(letter)

print()

for _ in range(5):
    print('hello world')

print()

data_list = [1, 2, 3, 4, 5]

for i in data_list:
    print(i)

print()

print(list(range(5)))
