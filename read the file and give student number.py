num = input("Type Student Number Or Name: ")
search = open(r"C:\Mypythonstuff\studentList (4).txt","r")
for line in search:
    line = line.rstrip()
    if num in line:
        print (line )
