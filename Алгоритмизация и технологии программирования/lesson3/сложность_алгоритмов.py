n = 10

for i in range(n):  # O(n)
    print(i)


count = 0
while count < n:  # O(n)
    print(count)
    count += 1

print(56)  # O(1)
data = {
    'key': 'value',
}

print(data['key'])  # O(1)


for i in range(n):  # O(n)
    if i == n - 1:
        print(i)

print()

# O(n^2)
for i in range(n):  # O(n)
    for j in range(n):  # O(n)
        if i == j:
            if i == n - 1:
                print(i)
                print(j)