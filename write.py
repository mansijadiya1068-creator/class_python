from curses import LINES


f=open("info.txt","w")
f.write("hello students\n")
f.write("welcome to python file\n")
f.write("learning is fun\n")
f.close()

f=open("info.txt","w")
f.write("new content only\n")
f.close()

f=open("info.txt","a")
f.write("this line is added\n")
f.close()

f=open("topics.txt","w")
lines[
    "python programming\n"
    "file handling\n"
    "error handling\n"
]
f.writelines(LINES)
f.close()
