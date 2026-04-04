src=open("source.txt","r")
data=opensrc.read()
src.close()

dst=open("destination.txt","w")
dst.write(data)
dst.close()
print("file copied successfully.")
