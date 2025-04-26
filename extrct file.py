with open('file.txt','w') as file:
    file.write("HI I AM PRAGATHI AND I AM 13 YEARS OLD")
file.close()

with open('file.txt','r') as file:
    data = file.readlines()
    print("Words in this file are.....")
    for line in data:
       word = line.split()
       print (word)
    file.close()