import numpy as np

class Maze:
    class Node:
        def __init__(self, position):
            self.position = position
            self.neighbours = [None, None, None, None]
            #0 Up
            #1 rigth
            #2 down
            #3 left
    def __init__(self, matrix):
        self.start = None
        self.end = None
        self.shape = matrix.shape
        M = np.zeros((self.shape[0]+2,self.shape[1]),dtype=Maze.Node)

        #print(M.shape,', ',self.shape)

        scaffoldMatrix = np.concatenate((np.zeros((1,self.shape[1])) , matrix))
        matrix = np.concatenate((scaffoldMatrix,np.zeros((1,self.shape[1]))))
        for j in range(self.shape[1]):
            M[0][j] = Maze.Node((0,j))
            M[self.shape[0]+1][j] = Maze.Node((self.shape[0]+1,j))
        for i in range(1,self.shape[0]+1):
            for j in range(0,self.shape[1]):
                #print(i,',',j)
                if(matrix[i][j] == 0):
                    M[i][j] = Maze.Node((i,j))

        for i in range(0,self.shape[0]+1):
            for j in range(0,self.shape[1]-1):
                #print(i,' ',j)
                if(matrix[i][j] == 0):
                    if(matrix[i+1][j]==0): #if lower node is soft
                        #print(M[i+1][j],'L at:(',i,',',j,')')
                        #print(matrix[i+1][j])
                        M[i][j].neighbours[2]=M[i+1][j]
                        M[i+1][j].neighbours[0]=M[i][j]
                    if(matrix[i][j+1]==0): #if rigth node is soft
                        #print(M[i][j+1],'R at:(',i,',',j,')')
                        #print(matrix[i][j+1])
                        M[i][j].neighbours[1]=M[i][j+1]
                        M[i][j+1].neighbours[3]=M[i][j]

        for i in range(0,self.shape[0]+1):
            if(matrix[i][self.shape[1]-1] == 0):
                if(matrix[i+1][self.shape[1]-1]==0): #if lower node is soft
                    M[i][self.shape[1]-1].neighbours[2]=M[i+1][self.shape[1]-1]
                    M[i+1][self.shape[1]-1].neighbours[0]=M[i][self.shape[1]-1]
        
        for j in range(0,self.shape[1]-1):
            if(matrix[self.shape[0]+1][j] == 0):
                if(matrix[self.shape[0]+1][j+1]==0): #if rigth node is soft
                    M[self.shape[0]+1][j].neighbours[1]=M[self.shape[0]+1][j+1]
                    M[self.shape[0]+1][j+1].neighbours[3]=M[self.shape[0]+1][j]


        self.start = M[0][0]
        self.end = M[self.shape[0]+1][0]
        self.height = M.shape[0] 
        self.width = M.shape[1]
        #print(self.start.neighbours,self.start.position)
        #print(self.end.neighbours,self.end.position)
                    
