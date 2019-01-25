from sys import argv

#If we have an argument, do we have 
#an argument equal to -start and if so
#do we have an argument after that?

if ( len(argv) > 1):
	if (argv[1] == "-start"):
		if (argv[2]):
			print(argv[2])
else:
	print("No arguments")

