# Percolation-problem
This is a python-library for demonstrating a simple percolation problem.
## Task setting
There is a square lattice NxN nodes given. Each node can be opened or closed. Nodes are independently set to be open with probability **p** (and closed with probability **1 − p**).
Connected nodes form a cluster. If there is a cluster that connects the upper row and the down row, then the system percolates.

![percolation_problem_demonstrating](https://github.com/marydrobotun/percolation/blob/master/docs/percolates.png)

The question is to find the minimal **p** which gives us a percolating system.
When N is sufficiently large, there is a threshold value **p*** such that when **p** < **p*** a random NxN grid almost never percolates, and when **p** > **p***, a random **NxN** grid almost always percolates. This program estimates **p***.

## Algorithmic base
The program uses the Union-Find algorithm to model the lattice. This algorithm uses a disjoint-set data sctructure.
Given a set of nodes that can be connected to each other, and two operations to be done: union and find.

## Demonstrating
To model a lattice and demonstrate a problem, you can run [*demonstrating.py*](https://github.com/marydrobotun/percolation/blob/master/demonstating.py).
```python
python demonstrating.py
```
Then you should input the size of a lattice and the number of nodes you want to open.

![demonstrating.py](https://github.com/marydrobotun/percolation/blob/master/docs/demonstrating.png)

The program models a lattice, randomly opens some nodes and then print if the lattice percolates.
Also it can print you a nice picture with your lattice.

![lattice](https://github.com/marydrobotun/percolation/blob/master/docs/lattice.png)

***Note that in fact less nodes will be opened than you specify. That's because of the random generator that gives coordinate of a node to open. Sometimes it gives the same nodes that are already opened.***
