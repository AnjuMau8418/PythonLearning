'''f=open("student.txt", mode='w+')
f.write("Good Bye\n")
f.write("Welcome to the chapter file handling\n")
f.write("Enjoy the session,\n")
n=f.write("Hello")
print(n)
f.close()

f=open("student.txt",mode='r')
data=f.read()
#print(data)
f.close()'''

f=open("student.txt",mode='w')
#f.write("hello,how are you,\n")
#f.write("welcome to python,\n")
#f.write("good bye\n")
f.close()


f=open("student.txt",mode='r')
data=f.readlines()
#print(data)
f.close

f=open("student.txt",mode='a+')
f.write("name\n")
f.write("Hello")
f.close




