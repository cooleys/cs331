import csv
import sys
import copy

checked = []
n = 3
m = 3

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

	for result, action in s_gen(node):
		if result not in checked:
			new_node = Node(node, action, result, node.cost+1, node.depth+1)
			successors.append(new_node)
	return successors

def s_gen(node):
	moves = ((1,0),(0,1),(-1,0),(0,-1))
	state = node.state
	results = []
	loc = (0,0)

	for x in range(n):
		for y in range(m):
			if state[x][y] == '0':
				loc = (x,y)
	
	new_state = copy.deepcopy(state)
	
	possible = map(lambda (i, j): (x + i, y + j), moves)
	possible = filter(lambda (i, j): 0 <= i < n and 0 <= j < m, possible)
	print possible

	for (x,y) in possible:
		i, j = loc
		new_state[i][j] = state[x][y]
		new_state[x][y] = '0'
		results.append((new_state, str(x) + ", " + str(y) + " to " + str(i) + ", " + str(j)))
		#print "Appending: " + str(new_state)
		new_state = copy.deepcopy(state)

	#print results
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
	return None
'''
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
