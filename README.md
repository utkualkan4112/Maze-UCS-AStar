# Maze-UCS-AStar
Solving Color-Maze Puzzle using Search

Q1: Each state consist of:
There is 4 posible state for one node
Left, Right, Up, Down
Cost : Individual cost of each directional state. It calculates the painted cells along the way.
Grid: It take a snapshot of board in that moment.
Parent: It poin to parent node of that state
Agentpos: It’s the position (x, y) coordinates of the agent of current state’s grid
Inıtıal state is the first position of the agent in the table. Parent is Null. Cost is 0. Agent pos is the start 
agent pos.
Goal test: Checks if there is any ‘0’ marked cells on the board. If not returns true
Step coast function: Parent.cost + current.cost
Q3: Heuristic function that I take: I counted remaining ‘0’ cells for heuristic function. This heuristic is 
admissible because the agent has to visit each unpainted cell at least once, so the actual cost can never 
be less than the number of unpainted cells.
Q5. My Difficulty levels are depends on the wall count if Wall count is 
Esay: 80 < = x < 100 or straight line
1.Maze
X#X#X#X#X#X#X#X#X#X
X#X#X#0#0#0#0#0#0#X
X#X#X#0#X#X#X#X#0#X
X#X#X#0#0#X#X#X#0#X
X#X#X#X#X#X#X#X#0#X
X#X#X#0#X#X#X#X#0#X
X#X#X#S#0#0#0#0#0#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 80
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', '1', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', '1', 'S', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', '1', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(6, 3)
(5, 3)
(6, 3)
(6, 8)
(1, 8)
(1, 3)
(3, 3)
(3, 4)
Resulting min cost: 20
Total number of expanded nodes: 36
Total Distance Agent Traveled: 226
--- 1.900240182876587 seconds ---
memory % used: 8.0
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', '1', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', '1', 'S', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', '1', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(6, 3)
(5, 3)
(6, 3)
(6, 8)
(1, 8)
(1, 3)
(3, 3)
(3, 4)
Resulting min cost: 20
Total number of expanded nodes: 25
Total Distance Agent Traveled: 142
--- 2.2467854022979736 seconds ---
memory % used: 7.8
2.Maze
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#S#X#X#X#X
X#X#X#X#X#0#X#X#X#X
X#X#0#0#0#0#0#0#0#X
X#X#0#X#X#0#X#X#0#X
X#X#0#X#X#0#X#X#0#X
X#X#0#0#0#0#X#X#0#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 80
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', '1', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', '1', 'X', 'X', 'X', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', '1', 'X', 'X', '1', 'X', 'X', '1', 'X']
['X', 'X', '1', 'X', 'X', '1', 'X', 'X', '1', 'X']
['X', 'X', '1', '1', '1', '1', 'X', 'X', 'S', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(2, 5)
(7, 5)
(7, 2)
(4, 2)
(4, 8)
(7, 8)
Resulting min cost: 20
Total number of expanded nodes: 18
Total Distance Agent Traveled: 109
--- 1.5516688823699951 seconds ---
memory % used: 7.9
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', '1', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', '1', 'X', 'X', 'X', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', '1', 'X', 'X', '1', 'X', 'X', '1', 'X']
['X', 'X', '1', 'X', 'X', '1', 'X', 'X', '1', 'X']
['X', 'X', '1', '1', '1', '1', 'X', 'X', 'S', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(2, 5)
(7, 5)
(7, 2)
(4, 2)
(4, 8)
(7, 8)
Resulting min cost: 20
Total cell count: 80
Total number of expanded nodes: 10
Total Distance Agent Traveled: 41
--- 2.0987701416015625 seconds ---
memory % used: 7.7
3.Maze
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#0#0#0#X
X#X#0#X#X#X#0#X#0#X
X#X#0#0#0#0#0#0#0#X
X#X#0#X#X#X#0#X#X#X
X#X#0#X#X#X#0#0#0#X
X#X#X#X#X#X#X#X#S#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 80
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', '1', '1', '1', 'X']
['X', 'X', '1', 'X', 'X', 'X', '1', 'X', '1', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', '1', 'X', 'X', 'X', '1', 'X', 'X', 'X']
['X', 'X', 'S', 'X', 'X', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(7, 8)
(6, 8)
(6, 6)
(2, 6)
(2, 8)
(4, 8)
(4, 2)
(3, 2)
(6, 2)
Resulting min cost: 21
Total number of expanded nodes: 39
Total Distance Agent Traveled: 244
--- 1.706798791885376 seconds ---
memory % used: 7.9
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', '1', '1', '1', 'X']
['X', 'X', '1', 'X', 'X', 'X', '1', 'X', '1', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', '1', 'X', 'X', 'X', '1', 'X', 'X', 'X']
['X', 'X', 'S', 'X', 'X', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(7, 8)
(6, 8)
(6, 6)
(2, 6)
(2, 8)
(4, 8)
(4, 2)
(3, 2)
(6, 2)
Resulting min cost: 21
Total number of expanded nodes: 20
Total Distance Agent Traveled: 100
--- 1.956031084060669 seconds ---
memory % used: 7.7
4.Maze
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#0#X
X#0#0#0#S#0#0#0#0#X
X#X#X#X#X#X#X#X#0#X
X#X#X#X#X#X#X#X#0#X
X#X#X#X#X#X#X#X#0#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 88
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'S', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(5, 4)
(5, 1)
(5, 8)
(4, 8)
(8, 8)
Resulting min cost: 15
Total number of expanded nodes: 17
Total Distance Agent Traveled: 84
--- 2.101517677307129 seconds ---
memory % used: 7.9
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'S', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(5, 4)
(5, 1)
(5, 8)
(4, 8)
(8, 8)
Resulting min cost: 15
Total number of expanded nodes: 17
Total Distance Agent Traveled: 84
--- 2.081721067428589 seconds ---
memory % used: 7.7
5.Maze
0#0#0#0#0#0#0#0#0#0
0#X#X#X#X#X#X#X#X#0
0#X#X#X#X#X#X#X#X#0
X#X#X#X#X#X#X#X#X#0
X#X#X#X#X#X#X#X#X#0
S#0#0#X#X#X#X#X#X#0
X#X#0#X#X#X#X#X#X#0
X#X#0#0#0#0#0#0#0#0
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 70
UCS:
Resulting Board:
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
['1', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['S', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['1', '1', '1', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['X', 'X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['X', 'X', '1', '1', '1', '1', '1', '1', '1', '1']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(5, 0)
(5, 2)
(7, 2)
(7, 9)
(0, 9)
(0, 0)
(2, 0)
Resulting min cost: 29
Total number of expanded nodes: 23
Total Distance Agent Traveled: 165
--- 1.976165771484375 seconds ---
memory % used: 8.0
A*:
Resulting Board:
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
['1', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['S', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['1', '1', '1', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['X', 'X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '1']
['X', 'X', '1', '1', '1', '1', '1', '1', '1', '1']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(5, 0)
(5, 2)
(7, 2)
(7, 9)
(0, 9)
(0, 0)
(2, 0)
Resulting min cost: 29
Total number of expanded nodes: 12
Total Distance Agent Traveled: 62
--- 1.9074020385742188 seconds ---
memory % used: 7.7
Medium: 60 <= x < 80
1.Maze
X#X#X#X#X#X#X#X#X#X
X#X#0#0#0#0#0#0#0#X
X#0#0#0#0#0#0#0#0#X
X#0#X#X#X#X#X#X#0#X
X#0#0#0#X#X#X#X#0#X
X#0#X#0#X#X#X#X#0#X
X#0#X#0#0#0#0#0#0#X
X#X#0#0#0#0#0#S#X#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 63
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'S', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', 'X', '1', 'X']
['X', '1', 'X', '1', 'X', 'X', 'X', 'X', '1', 'X']
['X', '1', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(7, 7)
(7, 2)
(7, 7)
(6, 7)
(6, 3)
(4, 3)
(4, 1)
(6, 1)
(2, 1)
(2, 8)
(6, 8)
(1, 8)
(1, 2)
Resulting min cost: 47
Total number of expanded nodes: 2172
Total Distance Agent Traveled: 32480
--- 2.4397494792938232 seconds ---
memory % used: 7.9
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'S', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', 'X', '1', 'X']
['X', '1', 'X', '1', 'X', 'X', 'X', 'X', '1', 'X']
['X', '1', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(7, 7)
(7, 2)
(7, 7)
(6, 7)
(6, 3)
(4, 3)
(4, 1)
(6, 1)
(2, 1)
(2, 8)
(6, 8)
(1, 8)
(1, 2)
Resulting min cost: 47
Total number of expanded nodes: 1286
Total Distance Agent Traveled: 16703
--- 5.021480560302734 seconds ---
memory % used: 7.8
2.Maze
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
X#X#X#X#X#X#X#X#X#X
X#0#0#0#0#0#0#0#X#X
X#0#0#0#X#X#X#0#X#X
X#0#0#0#X#X#X#0#X#X
X#0#0#0#X#X#X#0#X#X
X#X#0#0#X#X#X#0#X#X
X#X#S#0#0#0#0#0#X#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 72
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', 'X', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', 'X', 'S', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 2)
(3, 2)
(3, 1)
(6, 1)
(6, 3)
(8, 3)
(3, 3)
(3, 7)
(8, 7)
(8, 2)
Resulting min cost: 32
Total number of expanded nodes: 357
Total Distance Agent Traveled: 3704
--- 1.6690781116485596 seconds ---
memory % used: 7.9
A*: 
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', 'X', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', 'X', 'S', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 2)
(3, 2)
(3, 1)
(6, 1)
(6, 3)
(8, 3)
(3, 3)
(3, 7)
(8, 7)
(8, 2)
Resulting min cost: 32
Total number of expanded nodes: 127
Total Distance Agent Traveled: 1056
--- 1.7355754375457764 seconds ---
memory % used: 7.7
3.Maze
X#X#X#X#X#X#X#X#X#X
X#X#X#0#X#X#0#0#0#X
X#X#X#0#0#0#0#0#X#X
X#X#X#X#X#0#0#0#0#X
X#X#X#0#0#X#0#0#0#X
X#X#X#0#0#0#0#0#0#X
X#X#X#X#X#X#X#0#0#X
X#X#X#0#0#0#0#0#0#X
X#X#X#S#0#X#0#0#0#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 63
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', '1', 'X', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', 'X', 'X', 'X', '1', '1', '1', '1', 'X']
['X', 'X', 'X', '1', 'S', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', '1', '1', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 3)
(8, 4)
(8, 3)
(7, 3)
(7, 8)
(8, 8)
(8, 6)
(8, 8)
(3, 8)
(3, 5)
(2, 5)
(2, 3)
(1, 3)
(2, 3)
(2, 7)
(8, 7)
(1, 7)
(1, 8)
(1, 6)
(5, 6)
(5, 3)
(4, 3)
(4, 4)
Resulting min cost: 55
Total number of expanded nodes: 15828
Total Distance Agent Traveled: 285723
--- 49.863869428634644 seconds ---
memory % used: 7.9
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', '1', 'X', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', 'X', 'X', 'X', '1', '1', '1', '1', 'X']
['X', 'X', 'X', '1', 'S', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', '1', '1', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 3)
(8, 4)
(7, 4)
(7, 3)
(7, 8)
(8, 8)
(8, 6)
(8, 8)
(3, 8)
(3, 5)
(2, 5)
(2, 3)
(1, 3)
(2, 3)
(2, 7)
(8, 7)
(1, 7)
(1, 8)
(1, 6)
(5, 6)
(5, 3)
(4, 3)
(4, 4)
Resulting min cost: 55
Total number of expanded nodes: 11370
Total Distance Agent Traveled: 193714
--- 21.19397759437561 seconds ---
memory % used: 7.8
4.Maze
X#X#X#X#X#X#X#X#X#X
X#X#0#0#0#0#0#X#X#X
X#X#0#0#0#0#0#0#X#X
X#X#0#X#0#X#X#0#X#X
X#X#0#X#0#X#X#0#X#X
X#0#0#X#0#0#0#0#0#X
X#0#0#X#0#X#X#0#0#X
X#0#0#X#0#X#X#0#0#X
X#S#0#0#0#X#X#0#0#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 60
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', '1', '1', '1', '1', '1', 'X', 'X', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', '1', 'X', '1', 'X', 'X', '1', 'X', 'X']
['X', 'X', '1', 'X', '1', 'X', 'X', '1', 'X', 'X']
['X', '1', '1', 'X', 'S', '1', '1', '1', '1', 'X']
['X', '1', '1', 'X', '1', 'X', 'X', '1', '1', 'X']
['X', '1', '1', 'X', '1', 'X', 'X', '1', '1', 'X']
['X', '1', '1', '1', '1', 'X', 'X', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 1)
(5, 1)
(5, 2)
(1, 2)
(1, 6)
(2, 6)
(2, 2)
(8, 2)
(8, 4)
(1, 4)
(1, 6)
(2, 6)
(2, 7)
(8, 7)
(8, 8)
(5, 8)
(5, 4)
Resulting min cost: 50
Total number of expanded nodes: 2888
Total Distance Agent Traveled: 45705
--- 3.5724050998687744 seconds ---
memory % used: 7.9
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', '1', '1', '1', '1', '1', 'X', 'X', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', '1', 'X', '1', 'X', 'X', '1', 'X', 'X']
['X', 'X', '1', 'X', '1', 'X', 'X', '1', 'X', 'X']
['X', '1', '1', 'X', 'S', '1', '1', '1', '1', 'X']
['X', '1', '1', 'X', '1', 'X', 'X', '1', '1', 'X']
['X', '1', '1', 'X', '1', 'X', 'X', '1', '1', 'X']
['X', '1', '1', '1', '1', 'X', 'X', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 1)
(5, 1)
(5, 2)
(1, 2)
(1, 6)
(2, 6)
(2, 2)
(8, 2)
(8, 4)
(1, 4)
(1, 6)
(2, 6)
(2, 7)
(8, 7)
(8, 8)
(5, 8)
(5, 4)
Resulting min cost: 50
Total number of expanded nodes: 1558
Total Distance Agent Traveled: 21050
--- 4.240910053253174 seconds ---
memory % used: 7.8
5.Maze
X#X#X#X#X#X#X#0#0#X
X#0#0#0#X#X#X#0#X#X
X#0#0#0#0#0#0#0#X#X
X#0#X#X#X#X#X#0#0#X
X#0#X#X#X#X#X#0#0#X
X#0#X#X#X#X#X#X#0#X
X#0#0#0#0#0#X#X#0#X
X#0#X#X#0#X#X#X#0#X
X#S#X#X#0#0#0#0#0#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 64
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', '1', '1', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', '1', 'X', 'X', 'X', 'X', 'X', '1', '1', 'X']
['X', '1', 'X', 'X', 'X', 'X', 'X', '1', '1', 'X']
['X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'S', '1', '1', '1', '1', 'X', 'X', '1', 'X']
['X', '1', 'X', 'X', '1', 'X', 'X', 'X', '1', 'X']
['X', '1', 'X', 'X', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 1)
(1, 1)
(1, 3)
(2, 3)
(2, 1)
(2, 7)
(0, 7)
(0, 8)
(0, 7)
(4, 7)
(4, 8)
(3, 8)
(8, 8)
(8, 4)
(6, 4)
(6, 5)
(6, 1)
Resulting min cost: 44
Total number of expanded nodes: 682
Total Distance Agent Traveled: 10461
--- 2.2492575645446777 seconds ---
memory % used: 8.0
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', '1', '1', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', 'X', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', '1', 'X', 'X', 'X', 'X', 'X', '1', '1', 'X']
['X', '1', 'X', 'X', 'X', 'X', 'X', '1', '1', 'X']
['X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '1', 'X']
['X', 'S', '1', '1', '1', '1', 'X', 'X', '1', 'X']
['X', '1', 'X', 'X', '1', 'X', 'X', 'X', '1', 'X']
['X', '1', 'X', 'X', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 1)
(1, 1)
(1, 3)
(2, 3)
(2, 1)
(2, 7)
(0, 7)
(0, 8)
(0, 7)
(4, 7)
(4, 8)
(3, 8)
(8, 8)
(8, 4)
(6, 4)
(6, 5)
(6, 1)
Resulting min cost: 44
Total cell count: 64
Total number of expanded nodes: 499
Total Distance Agent Traveled: 7253
--- 2.3559529781341553 seconds ---
memory % used: 7.8
Hard: 40 <= x < 60
1.Maze:
X#X#X#X#X#X#X#X#X#X
X#0#X#X#X#0#0#0#0#X
X#0#0#0#0#0#0#X#0#X
X#0#0#0#0#0#0#X#0#X
X#X#0#0#0#0#0#0#0#X
X#0#0#0#0#0#0#0#0#X
X#X#X#0#0#0#0#0#0#X
X#0#0#0#0#X#X#0#0#X
X#0#0#0#0#S#X#0#0#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 47
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', '1', 'X', 'X', 'X', '1', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', 'X', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', 'X', '1', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'S', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', 'X', 'X', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', 'X', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 5)
(8, 1)
(7, 1)
(7, 4)
(2, 4)
(2, 6)
(1, 6)
(1, 5)
(6, 5)
(6, 3)
(2, 3)
(2, 1)
(1, 1)
(3, 1)
(3, 6)
(6, 6)
(1, 6)
(1, 8)
(8, 8)
(8, 7)
(4, 7)
(4, 2)
(5, 2)
(5, 1)
Resulting min cost: 67
Total number of expanded nodes: 56872
Total Distance Agent Traveled: 1325167
--- 901.4274642467499 seconds ---
memory % used: 8.0
A*:Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', '1', 'X', 'X', 'X', 'S', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', 'X', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', 'X', '1', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', 'X', 'X', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', 'X', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 5)
(8, 1)
(7, 1)
(7, 4)
(2, 4)
(2, 1)
(1, 1)
(3, 1)
(3, 6)
(1, 6)
(1, 5)
(6, 5)
(6, 3)
(6, 8)
(8, 8)
(8, 7)
(4, 7)
(4, 2)
(5, 2)
(5, 1)
(5, 8)
(1, 8)
(1, 5)
Resulting min cost: 67
Total number of expanded nodes: 21617
Total Distance Agent Traveled: 453206
--- 142.7306785583496 seconds ---
memory % used: 7.7
2.Maze
X#X#X#X#X#X#X#X#X#X
X#0#0#0#X#X#X#0#0#X
X#X#0#0#0#X#0#0#0#X
X#0#0#0#0#X#0#0#X#X
X#0#0#0#0#X#0#0#0#X
X#0#X#0#0#X#0#0#0#X
X#0#X#X#0#X#0#0#0#X
X#0#X#X#0#X#0#X#0#X
X#S#0#0#0#0#0#X#0#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 54
UCS:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', '1', 'X']
['X', 'X', '1', '1', '1', 'X', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', 'X', '1', '1', 'X', 'X']
['X', '1', '1', '1', '1', 'X', '1', '1', '1', 'X']
['X', '1', 'X', '1', '1', 'X', '1', '1', '1', 'X']
['X', '1', 'X', 'X', '1', 'X', '1', '1', '1', 'X']
['X', '1', 'X', 'X', '1', 'X', '1', 'X', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', 'X', 'S', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 1)
(3, 1)
(3, 4)
(2, 4)
(2, 2)
(4, 2)
(4, 4)
(2, 4)
(2, 2)
(1, 2)
(1, 1)
(1, 3)
(5, 3)
(5, 4)
(8, 4)
(8, 1)
(8, 6)
(2, 6)
(2, 8)
(1, 8)
(1, 7)
(6, 7)
(6, 8)
(4, 8)
(8, 8)
Resulting min cost: 61
Total number of expanded nodes: 9517
Total Distance Agent Traveled: 192514
--- 16.89471435546875 seconds ---
memory % used: 8.0
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', '1', '1', '1', 'X', 'X', 'X', '1', '1', 'X']
['X', 'X', '1', '1', '1', 'X', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', 'X', '1', '1', 'X', 'X']
['X', '1', '1', '1', '1', 'X', '1', '1', '1', 'X']
['X', '1', 'X', '1', '1', 'X', '1', '1', '1', 'X']
['X', '1', 'X', 'X', '1', 'X', '1', '1', '1', 'X']
['X', '1', 'X', 'X', '1', 'X', '1', 'X', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', 'X', 'S', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 1)
(3, 1)
(3, 4)
(2, 4)
(2, 2)
(4, 2)
(4, 4)
(2, 4)
(2, 2)
(1, 2)
(1, 1)
(1, 3)
(5, 3)
(5, 4)
(8, 4)
(8, 1)
(8, 6)
(2, 6)
(2, 8)
(1, 8)
(1, 7)
(6, 7)
(6, 8)
(4, 8)
(8, 8)
Resulting min cost: 61
Total number of expanded nodes: 5100
Total Distance Agent Traveled: 93665
--- 5.823872089385986 seconds ---
memory % used: 7.7
3.Maze
X#X#X#X#X#X#X#0#0#0
X#X#X#0#0#0#0#0#X#X
X#0#0#0#0#0#0#0#X#0
X#0#X#0#X#X#0#0#0#0
X#0#X#0#X#0#0#0#0#0
X#0#X#0#X#0#0#0#0#X
X#0#X#0#0#0#0#0#0#X
X#0#X#X#0#0#0#0#0#0
X#0#0#0#0#0#0#0#0#S
X#X#X#X#X#X#X#X#X#X
Total cell count: 42
UCS: Takes Lots of time
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', '1', '1', '1']
['X', 'X', 'X', '1', '1', '1', '1', '1', 'X', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', 'X', '1']
['X', '1', 'X', '1', 'X', 'X', '1', '1', '1', '1']
['X', '1', 'X', '1', 'X', '1', '1', '1', '1', '1']
['X', '1', 'X', '1', 'X', '1', '1', '1', '1', 'X']
['X', '1', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', 'X', 'X', '1', '1', '1', '1', '1', '1']
['X', '1', '1', '1', '1', '1', '1', '1', '1', 'S']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 9)
(7, 9)
(7, 4)
(6, 4)
(6, 8)
(3, 8)
(3, 6)
(8, 6)
(1, 6)
(1, 3)
(6, 3)
(6, 8)
(3, 8)
(3, 9)
(2, 9)
(4, 9)
(4, 5)
(8, 5)
(8, 1)
(2, 1)
(2, 7)
(0, 7)
(0, 9)
(0, 7)
(8, 7)
(8, 9)
Resulting min cost: 88
Total cell count: 42
Total number of expanded nodes: 48961
Total Distance Agent Traveled: 1203439
--- 492.6881377696991 seconds ---
memory % used: 8.6
4.Maze
X#X#X#X#X#X#X#X#X#X
X#X#0#0#0#0#X#0#0#X
X#0#0#0#0#0#0#0#0#X
X#0#0#X#0#0#X#0#X#X
X#0#0#0#0#0#0#0#0#X
X#0#0#0#0#0#X#0#0#X
X#X#X#0#0#0#0#0#0#X
X#X#0#0#0#X#0#0#0#X
X#X#0#0#0#0#0#S#X#X
X#X#X#X#X#X#X#X#X#X
UCS: Take too long to execute
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', '1', '1', '1', 'S', 'X', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', '1', 'X', '1', '1', 'X', '1', 'X', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', 'X', '1', '1', 'X']
['X', 'X', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', 'X', '1', '1', '1', 'X', '1', '1', '1', 'X']
['X', 'X', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 7)
(1, 7)
(1, 8)
(2, 8)
(2, 1)
(5, 1)
(5, 5)
(6, 5)
(6, 3)
(4, 3)
(4, 8)
(7, 8)
(7, 6)
(6, 6)
(8, 6)
(8, 2)
(7, 2)
(7, 4)
(1, 4)
(1, 2)
(5, 2)
(5, 5)
(1, 5)
Resulting min cost: 67
Total cell count: 48
Total number of expanded nodes: 22851
Total Distance Agent Traveled: 464342
--- 196.74383735656738 seconds ---
memory % used: 8.6
5.Maze
X#X#X#X#X#X#X#X#X#X
X#X#0#0#X#0#X#0#0#X
X#0#0#0#0#0#0#0#0#X
X#0#0#0#0#0#0#0#X#X
X#0#X#0#0#0#0#0#0#X
X#0#X#0#X#0#0#0#0#X
X#0#0#0#0#0#0#X#0#X
X#0#0#0#0#0#0#0#X#X
X#0#0#0#0#X#0#0#S#X
X#X#X#X#X#X#X#X#X#X
Total cell count: 46
UCS: Take Too long to execute
A*:
Resulting Board:
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', '1', '1', 'X', '1', 'X', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', 'S', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', '1', 'X', '1', '1', '1', '1', '1', '1', 'X']
['X', '1', 'X', '1', 'X', '1', '1', '1', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', 'X', '1', 'X']
['X', '1', '1', '1', '1', '1', '1', '1', 'X', 'X']
['X', '1', '1', '1', '1', 'X', '1', '1', '1', 'X']
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
Resulting Path that gives the min cost:
(8, 8)
(8, 6)
(2, 6)
(2, 8)
(1, 8)
(1, 7)
(5, 7)
(5, 8)
(6, 8)
(4, 8)
(4, 3)
(8, 3)
(1, 3)
(1, 2)
(3, 2)
(3, 7)
(5, 7)
(5, 5)
(1, 5)
(7, 5)
(7, 7)
(7, 1)
(8, 1)
(8, 4)
(6, 4)
(6, 1)
(2, 1)
(2, 8)
Resulting min cost: 86
Total number of expanded nodes: 55094
Total Distance Agent Traveled: 1551500
--- 832.0909488201141 seconds ---
memory % used: 8.6
As Conclusion A* Search is more efficient than UCS at every phase. A* start predicts the right path easily
and finish its execution way sooner than UCS. Also, it consumes less memory. These results excepted but 
it doesn’t mean it surprised me. Each algorithm explores its space node by node but in A* search since 
heuristic function estimates the final cost of each node its more accurate than real cost.


