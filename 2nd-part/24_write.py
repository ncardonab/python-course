with open('2nd-part/text.txt', 'w+') as file:
    for line in file:
        print(line)

    file.write('Hello there\n')
    file.write('Konichiwa\n')
    file.write('Bonjour\n')
    file.write('Guten tag\n')

# w: Just writes but doesn't allow to read
# r: Default one, reads but can't write
# w+: Reads everything and then overwrites
# r+: Reads everything and the concatenates to the end of the file