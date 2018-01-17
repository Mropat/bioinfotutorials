def printHello():
    print ("Hello, World")sd


def readAndSaveFile(filename):
	filehandle = open(filename, 'r')
	lines = filehandle.readlines()
	head = lines[0]
	tail = lines[-1]
	filending =""
	if "." in filename:
		filename, filending = filename.split(".")
		filending = "."+filending
	writefile = open(filename +"_headtail"+filending, 'w')
	writefile.write(head + tail)
	

def printTwoStrings(stringA, stringB):
    print (stringA, stringB)
	
if __name__=="__main__":
	printHello()
	readAndSaveFile("science.txt")
	printTwoStrings("please enter", "your strings")
		




