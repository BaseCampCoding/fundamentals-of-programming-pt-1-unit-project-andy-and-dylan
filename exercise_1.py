name_of_file = input('What is the name of the file?')
newfile = name_of_file + '.bak'
backup = open(newfile, 'w')

for line in open(name_of_file):
    backup.write(line)

backup.close()