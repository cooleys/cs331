#!/usr/bin/env python

# Sarah Cooley
# CS331 Spring 2011

import sys
import csv
from math import log


training	= sys.argv[1]
testing		= sys.argv[2]

train = csv.reader(open(training))
test = csv.reader(open(testing))

words = train.next()
len(test.next())
l = len(words)-1

pos	= [0]*l
neg = [0]*l
recs = 0
pos_r = 0
neg_r = 0

for row in train:
	if row[l] == "pos":
		pos_r = pos_r + 1
		for i in range(l):
			pos[i] = pos[i] + int(row[i])
	elif row[l] == "neg":
		neg_r = neg_r + 1
		for i in range(l):
			neg[i] = neg[i] + int(row[i])
recs = pos_r + neg_r

prob = {}
for i in range(l):
	# Stores in the format [ p(!found | neg ), p(!found | pos ), p(found | neg), p(found | pos)]
	prob[words[i]] = [ \
			float(neg_r - neg[i] + 1) / float(neg_r + 2),\
			float(pos_r - pos[i] + 1)/ float(pos_r + 2),\
			float(neg[i] + 1) / float(neg_r + 2),\
			float(pos[i] + 1) / float(pos_r + 2) ]

prob["totals"] = [ \
		float(neg_r) / float(recs),\
		float(pos_r) / float(recs) ]

pos_pred = 0
neg_pred = 0

pos_corr = 0
neg_corr = 0

for row in test:
	prob_pos = log(prob["totals"][1])
	prob_neg = log(prob["totals"][0])

	for i in range(l):
		if row[i] == '1':
			prob_pos = log(prob[words[i]][3]) + prob_pos
			prob_neg = log(prob[words[i]][2]) + prob_neg
	
	if prob_pos > prob_neg:
		pos_pred = pos_pred + 1
		if row[l] == "pos":
			pos_corr = pos_corr + 1
	else:
		neg_pred = neg_pred + 1
		if row[l] == "neg":
			neg_corr = neg_corr + 1

print "Positive accuracy: " + str(float(pos_corr) / float(pos_pred))
print "Negative accuracy: " + str(float(neg_corr) / float(neg_pred))
