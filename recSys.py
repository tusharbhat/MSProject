import numpy as np
from heapq import heappop, heappush
from collections import Counter
import random

INPUT_DIR = "C:\\Users\\Tushar-PC\\Downloads\\BX-CSV-Dump\\"
FileRatings = "BX-Book-Ratings.csv"
FileUsers = "BX-Users.csv"

users = open(INPUT_DIR + FileUsers, 'r')
ratings = open(INPUT_DIR + FileRatings, 'r')

ageusr = dict()
for line in users:
	if line.startswith('"Us'):
		continue
	words = line.split(";")
	age = words[-1]
	#print(line)
	if not age.startswith('N'):
		agen = int(age[1:-2])
		if agen >= 16 and agen <= 90:
			ageusr[words[0]] = agen


userdict = dict()
allratingset = set()
for line in ratings:
	if line.startswith('"User'):
		continue
	words = line.split(';')
	if words[0] not in userdict:
		userdict[words[0]] = set()
	userdict[words[0]].add(words[1])
	allratingset.add(words[1])

print(len(allratingset))

final_sol = list()

train_set = list()

for key in userdict:
	if len(userdict[key]) >= 10 and len(userdict[key]) <= 50:
		train_set.append(key)
	#if len(train_set) >= 4000:
	#	break

random.shuffle(train_set)
train_set = train_set[:4000]

#test = None
usrctr = 0
correct = 0
for u in train_set:
	usrctr += 1
	if usrctr % 500 == 0:
		print(usrctr)
	scoreh = []
	cands = userdict[u].copy()
	test = cands.pop()
	#if usrctr == 500:
	#	print(len(cands))
	#	print(len(userdict[u]))
	for u2 in train_set:
		if u == u2:
			continue
		score = len(cands.intersection(userdict[u2]))
		heappush(scoreh, (score, u2))
		if len(scoreh) > 100:
			heappop(scoreh)

	solns = dict()
	for nn in scoreh:
		new_cands = userdict[nn[1]].difference(cands)
		for nc in new_cands:
			if nc not in solns:
				solns[nc] = 0
			solns[nc] += nn[0]
			#solns[nc] += 1

	for k, v in Counter(solns).most_common(10):
			if k == test:
				correct += 1

print(correct)
print(len(train_set))
print(correct/len(train_set))