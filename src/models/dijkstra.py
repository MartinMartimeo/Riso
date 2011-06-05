# Dijkstra Heap Implementation
# Coded by Robert Heumueller
# <robert@heum.de>
#!/usr/bin/python
from heapq import *
import logging
import sys

__author__  = "Robert Heumueller <robert@heum.de>"
__date__    = "$25.05.2011 12:00:00$"

class Node(object):
	nodes = [] #holds all nodes
	def __init__(self, name):
		self.name = name
		self.cost = 0
		self.infinite = True
		self.active = True
		self.edges = []
		self.prev = None
		Node.nodes.append(self)
		logging.debug(str(self) + " created")
		
	def __repr__(self):
		return self.name
		
	#needed for minheap	
	def __cmp__(self, object):
		if self.infinite:
			if object.infinite:
				return 0 #equal if both infinite
			return 1 #larger if self infinite
		if object.infinite:
			return -1 #smaller if object infinite
		#if neither infinite decide by cost
		return cmp(self.cost, object.cost) 
	
	#add list of edges; edge is tuple => (distance, node)	
	def addEdges(self, edgelist):
		self.edges.extend(edgelist)
		
	#check if route via prev is shorter than old route
	#returns True if cost is updated	
	def reconsider(self, prev, dist):
		if ((prev.cost + dist < self.cost) or self.infinite):
				self.cost = prev.cost + dist
				self.prev = prev # needed for path reconstruction
				self.infinite = False
				logging.debug("Shorter path to "+str(self)+" found")
				return True
		return False
		
#set all node costs to 0 and infinite to True
def init():
	for temp in Node.nodes:
		temp.cost = 0
		temp.infinite = True
		temp.previous = None

def dijkstra(startnode, endnode = None):
	init() #initialize
	startnode.cost = 0 #set startnode cost to 0
	startnode.infinite = False #set startnode infinite to False
	queue = [] #create queue
	queue.extend(Node.nodes) #add all nodes in
	heapify(queue) #transfigure list into minheap
	while len(queue) > 0:
		u = heappop(queue) #node cost is final and minimal
		logging.debug("Extracting " +str(u))
		if u is endnode: #no shorter path possible
			logging.info("Shortest path found")
			break
		for temp in u.edges: #check edges
			if not temp[1] in queue or not temp[1].active : #already minimal
				continue
			logging.debug("Considering "+str(temp[1]))
			if temp[1].reconsider(u, temp[0]): #if changed rebuild heap
				heapify(queue)
	if endnode is None:
		return
	#logging.info("Path: " + getPathString(endnode)+ " length: "+str(endnode.cost))
	return getPath(endnode)

# reconstructs path to dest path
def getPathString(dest):
	path = str(dest)
	while True:
		temp = dest.prev
		if temp is None:
			return path
		path = str(temp) +"-" + path
		dest = temp
		
def getPath(dest):
	path = [dest]
	while True:
		temp = dest.prev
		if temp is None:
			return path
		path.insert(0, temp)
		dest = temp
		
	

if __name__ == "__main__":
	logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(message)s')
	n0 = Node("0")
	n1 = Node("1")
	n2 = Node("2")
	n3 = Node("3")
	n4 = Node("4")
	n5 = Node("5")
	
	n0.addEdges([(2,n1), (3,n3), (5, n2)])
	n1.addEdges([(4, n5)])
	n2.addEdges([(1, n3), (8,n5), (7, n4)])
	n3.addEdges([(6, n5)])
	n4.addEdges([(9, n5)])
	
	dijkstra(n0)
	
		
