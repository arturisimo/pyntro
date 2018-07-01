#Use readlines() in loadfile to read a log file and return a list containing the contents of the file
def loadfile(path_file):
	file = open(path_file, 'rt')
	lines = file.readlines()
	file.close()
	return lines