import csv
import sys

class Node:
	def __init__(self, parent, action, state, path_cost, depth):
		self.parent = parent
		self.action = action
		self.state = state
		self.cost = path_cost
		self.depth = depth

def parseFile(file):
	out = []
	reader = csv.reader(open(file, 'rb'))

	for row in reader:
		out.append(row)

	return out	
	

start = parseFile(sys.argv[1])
end = parseFile(sys.argv[2])
mode = sys.argv[3]

print start
print end
print mode

init_node = Node(None, "Initial", initial_state, 0, 1)

if mode == "bfs":
	node = bfs(init_node, goal_state)
elif mode == "dfs":
	node = dfs(init_node, goal_state)
print node.state

while node != None:
	print node.state
	node = node.parent
