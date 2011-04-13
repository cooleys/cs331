import csv
import sys
import copy

checked = []

class Node:
	def __init__(self, parent, action, state, path_cost, depth):
		self.parent = parent
		self.action = action
		self.state = state
		self.cost = path_cost
		self.depth = depth
	
	def __str__(self):
		return str(self.state)
	def __repr__( self):
		return str(self.state)

def parseFile(file):
	out = []
	reader = csv.reader(open(file, 'rb'))

	for row in reader:
		out.append(row)

	return out	

def expand(node):
	successors = []

	for result, action in suc_fun(node):
		if result not in checked:
			new_node = Node(node, action, result, node.cost+1, node.depth+1)
			successors.append(new_node)
	return successors

def suc_fun(node):
	state = node.state
	results = []
	loc = []
	for i in range(3):
		for j in range(3):
			if state[i][j] == '0':
				loc = [i, j]
				#print loc
	new_state = copy.deepcopy(state)
	i = loc[0]
	j = loc[1]
	#print state
	if j-1 >= 0:
		new_state[i][j] = new_state[i][j-1]
		new_state[i][j-1] = '0'
		results.append((new_state, str(i) + ", " + str(j-1) + " to " + str(i) + ", " + str(j)))
		#print "Appending1: " + str(new_state)
		new_state = copy.deepcopy(state)
		#print state
		#print new_state
	if j+1 <= 2:
		new_state[i][j] = new_state[i][j+1]
		new_state[i][j+1] = '0'
		results.append((new_state, str(i) + ", " + str(j+1) + " to " + str(i) + ", " + str(j)))
		#print "Appending2: " + str(new_state)
		new_state = copy.deepcopy(state)
	if i-1 >= 0:
		new_state[i][j] = new_state[i-1][j]
		new_state[i-1][j] = '0'
		results.append((new_state, str(i+1) + ", " + str(j) + " to " + str(i) + ", " + str(j)))
		#print "Appending3: " + str(new_state)
		new_state = copy.deepcopy(state)
	if i+1 <= 2:
		new_state[i][j] = new_state[i+1][j]
		new_state[i+1][j] = '0'
		results.append((new_state, str(i+1) + ", " + str(j) + " to " + str(i) + ", " + str(j)))
		#print "Appending4: " + str(new_state)
		new_state = copy.deepcopy(state)

	print results
	return results

def bfs(s, e):
	n = Node(None, "bfs_init", s, 0, 1)
	print n
	expand(n)
	'''
	fringe = []
	fringe.append(n)
	while fringe != []:
		node = fringe.pop(0)
		print node
		if node.state not in checked:
			if node.state == e:
				print "Goal"
				return node
			else:
				checked.append(node.state)
				ex = []
				for exp in expand(node):
					print exp
					ex = [exp] + ex
				fringe = ex + fringe
				print "Fringe: "
				print fringe
	'''
	return None

def dfs(s, e):
	n = Node(None, "Initial", s, 0, 1)
	return 0



start = parseFile(sys.argv[1])
end = parseFile(sys.argv[2])
mode = sys.argv[3]

if mode == "bfs":
	node = bfs(start, end)
elif mode == "dfs":
	node = dfs(start, end)

print node.state
while node != None:
	print node.state
	node = node.parent
