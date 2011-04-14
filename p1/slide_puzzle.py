import csv
import sys
import copy
from heapq import heappush, heappop

sys.setrecursionlimit(sys.getrecursionlimit()*4)
checked = []
n = 3
m = 3
n_e = 0

class Node:
	def __init__(self, parent, action, state, path_cost, depth):
		global n_e
		self.parent = parent
		self.action = action
		self.state = state
		self.cost = path_cost
		self.depth = depth
		n_e += 1
	
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
	moves = ((-1,0),(0,1),(1,0),(0,-1))
	if not mode == "bfs": 
		moves = ((0,-1),(1,0),(0,1),(-1,0))
	
	results = []
	loc = (0,0)

	for x in range(n):
		for y in range(m):
			if node.state[x][y] == '0':
				loc = (x,y)
	x,y = loc
	possible = map(lambda (i, j): (x + i, y + j), moves)
	possible = filter(lambda (i, j): 0 <= i < n and 0 <= j < m, possible)

	for (i,j) in possible:
		new_state = copy.deepcopy(node.state)
		new_state[x][y] = new_state[i][j]
		new_state[i][j] = '0'
		results.append((new_state, str(i) + ", " + str(j) + " to " + str(x) + ", " + str(y)))

	return results

def bfs(s, e):
	n = Node(None, "bfs_init", s, 0, 1)
	if s == e:
		return n

	fringe = []
	fringe.append(n)
	while fringe != []:
		node = fringe.pop(0)
		checked.append(node.state)
		for ex in expand(node):
			if ex.state == e:
				f.write("Goal!\n")
				return ex
			fringe.append(ex)

	f.write("No Goal :(")
	return None

def dfs(s, e):
	n = Node(None, "def_init", s, 0, 1)
	if s == e:
		return n
	
	fringe = []
	fringe.append(n)
	while fringe != []:
		node = fringe.pop(0)
		checked.append(node.state)
		for ex in expand(node):
			if ex.state == e:
				f.write("Goal!\n")
				return ex
			fringe.insert(0,ex)

	f.write("No Goal :(")
	return None

def iddfs(s, e):	
	n = Node(None, "iidfs_init", s, 0, 1)
	if s == e:
		return n
	global checked	
	d = 1
	fringe = []
	fringe.append(n)
	
	while fringe != []:
		node = fringe.pop(0)
		checked.append(node.state)
		for ex in expand(node):
			if ex.state == e:
				f.write("Goal!\n")
				return ex
			if ex.depth <= d:
				fringe.insert(0,ex)
		
		if fringe == [] and node.depth >= d:
			d += 1
			del checked[:]
			fringe.append(n)

	f.write("No Goal :(")
	return None

def a(s, e):
	n = Node(None, "iidfs_init", s, 0, 1)
	if s == e:
		return n
	
	fringe = []

	g_score = 0
	h_score = a_heur(n.state, e)
	f_score = h_score

	heappush(fringe, (f_score, n))
	
	while fringe != []:
		score, node = heappop(fringe)
		if node.state == e:
			return node
		checked.append(node.state)
		for exp in expand(node):
			exp.score = exp.depth + a_heur(exp.state, e)
			heappush(fringe, (exp.score, exp))
	return None


def a_heur(state, e):
    total_score = 0
    for i in range(3):
        for j in range(3):
            temp_score = 0
            value = state[i][j]
            for h in range(3):
                for k in range(3):
                    if e[h][k] == value:
                        temp_score = abs( h - i ) + abs ( k - j )
            total_score += temp_score
    return total_score


start = parseFile(sys.argv[1])
end = parseFile(sys.argv[2])
mode = sys.argv[3]
f = open('log', 'w')

if mode == "bfs":
	node = bfs(start, end)
elif mode == "dfs":
	node = dfs(start, end)
elif mode == "iddfs":
	node = iddfs(start, end)
elif mode == "a":
	node = a(start, end)

f.write("Num expanded: "+str(n_e)+"\n")
while node != None:
	f.write(str(node)+"\n")
	node = node.parent
