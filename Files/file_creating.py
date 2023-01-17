# w writing a appending r reading r+ reading/writing
file = open("./data.csv", "w") #create

file = open("./data.csv", "r+") #write

file.write("id,name,email\n")

file.write("1,Sur,Dog@kitty.com\n")
file.write("2,Muz,Cat@gmail.com\n")

file.close() #close

file = open("./data.csv", "a")  # add to file
file.write("3,Susi,cow@gmail.com\n")


file.close()  # close

file = open("./data.csv", "r")  # reading

#print(file.read())

#for line in file:
#    print(line)

print(file.readlines())
file.close()  # close
