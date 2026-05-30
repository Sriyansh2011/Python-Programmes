file1 = open('Codingal (1).txt','r')
file2 = open('codingal updated.txt','w')

for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)

file2.close()
file1.close()