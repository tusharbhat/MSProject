import pickle
import json
import os
from difflib import SequenceMatcher

counter = 0
INPUT_DIR = "C:\\Users\\Tushar-PC\\Downloads\\ProjectGutenberg\\allnovels\\"
novels = dict()
failctr = 0
failarr = list()

for filename in os.listdir("C:\\Users\\Tushar-PC\\Downloads\\ProjectGutenberg\\allnovels\\"):
	counter += 1
	if counter % 100 == 0:
		print(counter)
	#if counter < 100000:
	if True:
		linecounter = 0
		name = ""
		titlefound = True
		try:
			thisfile = open(INPUT_DIR + filename, 'r')
			for line in thisfile:
				#titlefound = True
				if linecounter < 500:
					if titlefound and line.startswith("Title: "):
						#print("H1")
						temp = line[7:].strip().lower()
						#if temp.endswith("."):
						#	temp = temp[:-1]
						name += temp
						if temp.endswith("."):
							temp = temp[:-1]
						novels[temp] = list()
						novels[temp].append(filename)

						titlefound = False
						#print(name)
					elif titlefound is False:
						#print("H2")
						if line is not "\n":
							temp = line.strip().lower()
							if temp.endswith("."):
								temp = temp[:-1]
							name += " "
							name += temp
						novels[name] = list()
						novels[name].append(filename)
						break
				else:
					break
		except(Exception):
			failctr += 1
			failarr.append(filename)
			continue

	else:
		break
pickle.dump( novels, open( "E:\\MSProject\\nametofile2.p", "wb" ) )
print("Success")
print(counter)
print(failctr)