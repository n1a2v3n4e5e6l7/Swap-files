def swapFileData():
    file1 = input("What is Your File name?: ")
    file2 = input("What is Your File name?: ")
   
    a = open (file1,'r')
    dataA = a.read()

    b = open (file2,'r')
    dataB = b.read()

    a = open (file1,'w')                                                 
    a.write(dataB)

    b = open (file2,'w')
    b.write(dataA)

swapFileData()