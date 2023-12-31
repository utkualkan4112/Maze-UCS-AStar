# -*- coding: utf-8 -*-
"""A*Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16o9y7UMBnARMkE47Ct-GiJlDsaXebJYi
"""

import heapq
import copy
import random
import math
import time
import psutil

class GameState:
    def init(self, grid): #Inital Value
        self.grid = copy.deepcopy(grid) #snapshot of first grid
        self.cost = 0 #initial cost
        self.parent = None #initial parent null
        for r in grid:
          for c in r:
            if(c == 'S'):
              self.agentpos = [self.grid.index(r), r.index(c)] #start of agent pos
    def __cost__(self, other): #cost fucntion
        return self.cost + other.cost
    
    def __lt__(self, other): #Override of heap "<" operator it is comoparing the heuristic + real cost
        return (self.cost + unpainted_cells_count_heuristic(self)) < (other.cost + unpainted_cells_count_heuristic(other))

    def __state__(self): #state function
      States = []
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: #coordinates that indicates Left, Right, Up, Down
        nx, ny = self.agentpos[0], self.agentpos[1]
        New_state = GameState()
        New_grid = copy.deepcopy(self.grid)
        New_grid[self.agentpos[0]][self.agentpos[1]] = '1'
        New_state.grid = New_grid
        cost = 0
        while is_valid_move(self.grid, nx + dx, ny + dy): #while there is no wall on that way keep going
            nx, ny = nx + dx, ny + dy
            cost += 1 #inrement cost at each visited cell
            if grid[nx][ny] == '0':      #if not painted paint the cell   
                New_state.grid[nx][ny] = '1'
        New_state.agentpos = [nx, ny]
        New_state.cost = cost
        New_state.grid[nx][ny] = 'S' #put 'S' in the state last location (agent pos)
        if(self.grid != New_state.grid): #if current state and new state's grid not same add on states array
          States.append(New_state)
      return States

    def __goal__(self): #checks if there is '0' left 
      for r in self.grid:
        for c in r:
          for i in c:
            if(i == '0'):
              return False
      return True

def is_valid_move(grid, x, y): #cheks if agent is out of bound or is on X
      return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X'

def __is_in_list__(List, n): #checks if not in List
  if(List):
    for i in List:
      if(i.grid == n.grid):
        return True
    return False
  return False

def print_path(state): #prints the result path by visiting every parent of its
  current_path = ((state.agentpos[0], state.agentpos[1]))
  Path = [current_path]
  while(state.parent):
    Path.append((state.parent.agentpos[0], state.parent.agentpos[1]))
    state = state.parent
  for a in reversed(Path):
    print(a)

def unpainted_cells_count_heuristic(state): #Heuristic function that checks the unpainted cells and return them
    unpainted_cells_count = 0
    for i in range(len(state.grid)):
        for j in range(len(state.grid[i])):
            if state.grid[i][j] == '0':
                unpainted_cells_count += 1
    return unpainted_cells_count



def A_Star(grid): #Main A* function
  total_distance = 0 #Chekcs the total distance that agent went
  total_expanded_nodes = 1 #Checks number of expanded nodes
  CLOSED = []
  FRONTIER = []
  heapq.heapify(FRONTIER) #create heap frontier
  Start = GameState() #inital value
  Start.init(grid)
  heapq.heappush(FRONTIER,Start) #Push the initial value to frontier
  while FRONTIER:
    Node = heapq.heappop(FRONTIER)
    if(Node.__goal__()): #check goal
      return Node, total_distance, total_expanded_nodes
    for s in Node.__state__(): #visit every state 
      total_expanded_nodes += 1
      New_Node = copy.deepcopy(s) #New_Node equal to current state
      New_Node.parent = Node #parent is Node
      New_Node.cost += Node.cost #Add the parent cost to new node cost for real cost
      if(not (__is_in_list__(FRONTIER, New_Node)) and not (__is_in_list__(CLOSED, New_Node))):   #if not in Closed or Frontier add in frontier 
        heapq.heappush(FRONTIER, New_Node)
      elif(__is_in_list__(FRONTIER, New_Node)): #if there is same grid as new node in frontier than update the node in frontier
        for i in FRONTIER:
          if(i.grid == New_Node.grid):
            if(i.cost > New_Node.cost):
              i.cost = New_Node.cost
              i.parent = New_Node.parent
    total_distance += Node.cost
    CLOSED.append(Node)

start_time = time.time()

grid = str(input())
grid = grid.split()
for i in range(len(grid)):
  grid[i] = grid[i].split("#")
cell_count = 0
for r in grid:
  for c in r:
    if(c == 'X'):
      cell_count += 1

Result, total_distance, total_expanded_nodes = A_Star(grid)
print("Resulting Board:")
for r in Result.grid:
  print(r)

print("Resulting Path that gives the min cost:")
print_path(Result)

print("Resulting min cost: ",Result.cost)

print("Total cell count: ", cell_count)
print("Total number of expanded nodes: ", total_expanded_nodes)
print("Total Distance Agent Traveled: ", total_distance)
print("--- %s seconds ---" % (time.time() - start_time))
print('memory % used:', psutil.virtual_memory()[2])