import csv
import sys
import os
import copy
import re

sys.setrecursionlimit(sys.getrecursionlimit()*4)
words = []

def index(i, o):
	f = open(i, 'r')
	out = open(o, 'w')
	for w in f.readlines():
		words.append(w.rstrip().lower())
		out.write(w.rstrip().lower()+",")
	
	out.write("ClassLabel")
	f.close()
	out.close()

def parse_reviews(i, o):
	out = open(o, 'w')

	for file in os.listdir(i+"/pos/"):
		f = open(os.path.join(i+"/pos/", file), 'r')
		rev_w = re.findall('\w+', f.read().lower())
		l = [0]*(len(words)-1)
		for w in rev_w:	
			try:
				ind = words.index(w)
				l[ind] = 1
			except(ValueError):
				pass
		f.close()
		l.append("pos")
		
#	for w in reader.readlines():
#		r = open(i, 'rb')
#		c = Counter()
#		out.write(w.rstrip()+",")
#	out.write("pos")
#	
#	for w in reader.readlines():
#		r = open(i, 'rb')
#		out.write(w.rstrip()+",")
#	out.write("neg")


#	reader.close()
	out.close()


if len(sys.argv) != 3:
	print "Useage: python classifier.py < training data file > < testing data file >"
	sys.exit("")

vocab_file = "vocabulary.txt"
training_file = sys.argv[1]
testing_file = sys.argv[2]

pre_proc = "training.txt"

index(vocab_file, pre_proc)
parse_reviews(training_file, pre_proc)


#f = open(pre_proc, 'w')

#f.write("Num expanded: "+str(n_e)+"\n")
#while node != None:
#	f.write(str(node)+"\n")
#	node = node.parent
#f.close()
