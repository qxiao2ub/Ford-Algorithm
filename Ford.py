#1st chunk: node

import sys; #following use max function

#define nodes
class Node(object):
  
  def __init__(self, name):#build constructor with node name
    self.name = name;    
    self.visited = False #define visited nodes
    #self.adjacentciesList = []; #adjacencies list is empty list
    self.predecessor = None; #define predecessor
    self.minDistance = sys.maxsize; #above import sys, to use max function, this first initialize shortest distance to infinity

#2nd chunk: edge

#define edge
class Edge(object):
  
  def __init__(self, weight, startVertex, targetVertex): #build constructor with wegiht, starting vertex and end vertex
    self.weight = weight;
    self.startVertex = startVertex;
    self.targetVertex = targetVertex;

#3rd chunk: algorithm
    
#build algorithm
class Algorithm(object):
  
  HAS_CYCLE = False; #default 
  
  def caculateShortestPath(self, vertexList, edgeList, startVertex):
    
    startVertex.minDistance = 0;#starting point mindistance is 0
    
    for i in range(0,9999): #loop for iterations < vertex no.
      for edge in edgeList:#for each iteration, relaxation for each edge
        
        u = edge.startVertex;
        v = edge.targetVertex;
        newDistance = u.minDistance + edge.weight;
        
        if newDistance < v.minDistance: #check new distance
          v.minDistance = newDistance; #update minDistance
          v.predecessor = u; #update predecessor

    for edge in edgeList: #if negative cycle
      if self.hasCycle(edge): #hasCycle in following def
        print("Ford Algorithm: Loop detected");
        Algorithm.HAS_CYCLE = True;
        return;
          
  def hasCycle(self, edge):#check loop cycle
    if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
      return True; #return true if it has negative cycle
    else:
      return False;
    
    
  def getShortestPathTo(self, targetVertex):
    
    if not Algorithm.HAS_CYCLE:#if no cycle, then print
      print("Shortest path to targetVertex: ", targetVertex.minDistance);
         
      node = targetVertex;
      
      while node is not None:
        print("%s ->" % node.name)
        node = node.predecessor;
      
#4th chunk: application
      
node1 = Node("r");
node2 = Node("a");
node3 = Node("p");
node4 = Node("q");
node5 = Node("b");          
        
edge1 = Edge(2, node1, node2);          
edge2 = Edge(1, node2, node3);          
#edge3 = Edge(4, node3, node4);
edge3 = Edge(-6, node3, node4);          
edge4 = Edge(2, node5, node4);          
edge5 = Edge(4, node1, node5);          
edge6 = Edge(3, node2, node5);          
edge7 = Edge(3, node4, node2);          
edge8 = Edge(2, node3, node5);          
        
#node1.adjacentciesList.append(edge1);
#node1.adjacentciesList.append(edge2);
#node2.adjacentciesList.append(edge3);
#node3.adjacentciesList.append(edge4);
#node3.adjacentciesList.append(edge2);

vertexList = [node1, node2, node3, node4, node5];
edgeList = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8];

algorithm = Algorithm();
algorithm.caculateShortestPath(vertexList, edgeList, node1); #node-r is starting vertex
algorithm.getShortestPathTo(node4); #here we give example to end node-q
