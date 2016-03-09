from matplotlib import pyplot as plt

INPUT_DIR = "C:\\Users\\Tushar-PC\\Downloads\\BX-CSV-Dump\\"
FileRatings = "BX-Book-Ratings.csv"
FileUsers = "BX-Users.csv"

#users = open(INPUT_DIR + FileUsers, 'r')
ratings = open(INPUT_DIR + FileRatings, 'r')

# ageset = [0] * 245
# for line in users:
# 	if line.startswith('"Us'):
# 		continue
# 	words = line.split(";")
# 	age = words[-1]
# 	#print(line)
# 	if not age.startswith('N'):
# 		agen = int(age[1:-2])
# 		#if agen not in ageset:
# 		#	ageset[agen] = 0	
# 		ageset[agen] += 1

# print(min(ageset))
# print(max(ageset))
# #print(ageset)
# print(len(ageset))

# for x in range(16):
# 	ageset[x] = 0
# for x in range(91,245):
# 	ageset[x] = 0
# plt.plot(ageset[:91])
# plt.show()

#userctr = [0] * 13603

users = dict()
listrat = [0] * 11
for line in ratings:
	if line.startswith('"User'):
		continue
	words = line.split(';')
	rat = int(words[2][1:-2])
	listrat[rat] += 1
	if words[0] not in users and rat > 0:
		users[words[0]] = list()
	if rat > 0:
		users[words[0]].append(rat)

#print(max([users[key] for key in users]))
#print(min([users[key] for key in users]))
typeuser = [0] * 3
print(len(users))
for key in users:
	avg = sum(users[key])/len(users[key])
	if avg < 5:
		typeuser[0] += 1
	elif avg > 8:
		typeuser[2] += 1
	else:
		typeuser[1] += 1
	#userctr[users[key]] += 1

plt.pie(typeuser, labels=['Critical', 'Moderate', 'Generous'], shadow=True, autopct='%1.1f%%')
plt.title('User Attitude')
plt.show()

print(typeuser)
#print(sum(userctr[:11])/sum(userctr))
#print(sum(userctr[51:1001]))
#print(sum(userctr))
#plt.plot(userctr[:51])
#plt.show()
#plt.pie([listrat[0], sum(listrat[1:])], labels=['Implicit: '+str(listrat[0]), 'Explicit: '+ str(sum(listrat[1:]))], shadow=True)
#plt.title('Implicit vs. Explicit Ratings')

listrat[0] = 0
suml  = 0
#plt.plot(listrat)
for i in range(11):
	suml += listrat[i]
	listrat[i] *= i
#print(sum(listrat[1:])/suml)
#print(listrat)
#plt.show()