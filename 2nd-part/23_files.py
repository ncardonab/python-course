file = open('2nd-part/text.txt')
# print(file.read()) # Heavier 'cause reads the whole file
print(file.readline())
print(file.readline())
print(file.readline())

print('For loop')
for line in file:
    print(line)

file.close()

with open('2nd-part/text.txt') as file:
    print('Inside with clause')
    for line in file:
        print(line)