#!/usr/bin/env python

# Sarah Cooley
# CS331 Spring 2011

import sys
import csv
from math import log


training	= sys.argv[1]
testing		= sys.argv[2]
pos_dict	= {}
neg_dict	= {}

reader = csv.reader(open(training))
tester = csv.reader(open(testing))

fields = reader.next()
tester.next()
length = len(fields)

pos_count = []
neg_count = []
for i in range(length):
	neg_count.append(0)
	pos_count.append(0)

for row in reader:
	if row[length-1] == "pos":
		row[length-1] = 1
		for i in range(length):
			pos_count[i] = pos_count[i] + int(row[i])
	elif row[length-1] == "neg":
		row[length-1] = 1
		for i in range(length):
			neg_count[i] = neg_count[i] + int(row[i])

probs = {}
total_recs = neg_count[length-1] + pos_count[length-1]
for i in range(length-1):
	# Stores in the format [ p(!found | neg ), p(!found | pos ), p(found | neg), p(found | pos)]
	probs[fields[i]] = [ \
			float(neg_count[length-1] - neg_count[i] + 1) / float(neg_count[length-1] + 2),\
			float(pos_count[length-1] - pos_count[i] + 1)/ float(pos_count[length-1] + 2),\
			float(neg_count[i] + 1) / float(neg_count[length-1] + 2),\
			float(pos_count[i] + 1) / float(pos_count[length-1] + 2)\
			]

# Stores in the format [ prob neg, prob pos ]
probs[fields[length-1]] = [ \
		float(neg_count[length-1]) / float(total_recs),\
		float(pos_count[length-1]) / float(total_recs)\
		]

#file = open(testing, 'r')
#text = file.read()
#text = text.rsplit()

pos_pred = 0
neg_pred = 0

pos_corr = 0
neg_corr = 0

for row in tester:
	prob_pos = log(probs[fields[length-1]][1])
	prob_neg = log(probs[fields[length-1]][0])
	for i in range(length-1):
		if row[i] == '1':
			prob_pos = log(probs[fields[i]][3]) + prob_pos
			prob_neg = log(probs[fields[i]][2]) + prob_neg

	if prob_pos > prob_neg:
		pos_pred = pos_pred + 1
		if row[length-1] == "pos":
			pos_corr = pos_corr + 1
	else:
		neg_pred = neg_pred + 1
		if row[length-1] == "neg":
			neg_corr = neg_corr + 1

print "Positive correctly guessed: " + str(float(pos_corr) / float(pos_pred))
print "Negative correctly guessed: " + str(float(neg_corr) / float(neg_pred))
