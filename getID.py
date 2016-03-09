import pickle

pos = pickle.load( open( "E:\\MSProject\\isbntoposdict.p", "rb" ) )

ctr = 0

bookno = list()

for key in pos:
	bookno.append(key)
	ctr += 1

pickle.dump( bookno, open( "E:\\MSProject\\bookarr.p", "wb" ) )
print(ctr)
print(len(bookno))