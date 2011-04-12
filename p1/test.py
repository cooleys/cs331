import sys

file = sys.argv[1]

csvfile = open(file, "r")

for ln in csvfile:
	ln = ln.strip()
	print ln.split(',')

csvfile.close()
