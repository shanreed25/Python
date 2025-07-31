





# open()*********************************************
file = open("my_file.txt")

# read()*********************************************
contents = file.read()

# write()********************************************
file = open("my_file.txt", mode='w' )
file.write("I like the color purple")# will overwrite

# append
file = open("my_file.txt", mode='a' )
file.write("I like the color purple")
