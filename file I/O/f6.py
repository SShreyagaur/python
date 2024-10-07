name= input("what's your name")

file = open("name.txt","a")
file.write(name)
file.close()
