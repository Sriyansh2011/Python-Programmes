file = open('Codingal (1).txt','r')
print(file.read())
file.close()

file = open('Codingal (1).txt','r')
print("\n Read in Parts \n")
print(file.read(8))
file.close()

file = open('Codingal (1).txt','a')
file.write("Hi! I am Penguin and am 1 yr old")
file.close()