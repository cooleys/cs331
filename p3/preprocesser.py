#!/usr/bin/env python

# Sarah Cooley
# CS331 Spring 2011

import csv
import sys
import os
import copy
import re

sys.setrecursionlimit(sys.getrecursionlimit()*4)
words = []

def index(i):
	f = open(i, 'r')
	for w in f.readlines():
		words.append(w.rstrip().lower())
	out.writerow(words+["ClassLabel"])	
	f.close()

def parse_reviews(i, val):
	for file in os.listdir(i+"/"+val+"/"):
		f = open(os.path.join(i+"/"+val+"/", file), 'r')
		rev_w = re.findall('\w+', f.read().lower())
		l = [0]*(len(words)-1)
		for w in rev_w:	
			try:
				ind = words.index(w)
				l[ind] = 1
			except(ValueError):
				pass
		f.close()
		l.append(val)
		out.writerow(l)
	
if len(sys.argv) != 3:
	print "Useage: python classifier.py < training data file > < testing data file >"
	sys.exit("")

vocab_file = "vocabulary.txt"
training_file = sys.argv[1]
testing_file = sys.argv[2]

train = "training.txt"
test = "testing.txt"

out = csv.writer(open(train, 'w'))
index(vocab_file)
parse_reviews(training_file, "pos")
parse_reviews(training_file, "neg")

out = csv.writer(open(test, 'w'))
index(vocab_file)
parse_reviews(testing_file, "pos")
parse_reviews(testing_file, "neg")
