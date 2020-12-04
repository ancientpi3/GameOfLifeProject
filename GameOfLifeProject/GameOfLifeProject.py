

from tkinter import Tk, Canvas, PhotoImage, mainloop

import copy
import time
import random
import numpy
import unittest


class GameModel:
    
    SET=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    
    #Initialize a gamemodel with cell width and height.
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.gridState=numpy.array([[0]*(width+1)]*(height+1))
    
    #Loops through copy of gamestate array and updates gamestate according to rules.
    def updateState(self):
        oldState = self.gridState.copy()
        for x in range(1,self.width):
            for y in range(1,self.height):

                #Observe surrounding cells
                adj = [oldState[x+self.SET[0][0]][y+self.SET[0][1]]]
                for L in range(1,8):
                    adj = adj+[oldState[x+self.SET[L][0]][y+self.SET[L][1]]]
                    
                #Change state based on rules
                if oldState[x][y]==0:
                    if sum(adj) == 3:
                        self.gridState[x][y]=1
                else:
                    if sum(adj)<=1 or sum(adj)>=4:
                        self.gridState[x][y]=0
    
    #Returns true if the cell is live and false if the cell is dead
    def cellIsLive(self,x,y):
        return bool(self.gridState[x][y])
    
    #Activates cell if it is dead, Deactivates cell if it is alive.
    def activateCell(self,x,y):
        if bool(self.gridState[x][y]):
            self.gridState[x][y] = 0
        else:
            self.gridState[x][y] = 1


class GameView():
    
    hexx = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","10"]
    #Initialize a gameview, passing a GameModel as a parameter. Constructs a Canvas object
    def __init__(self,model):
        print("stub")
    #This code looks smelly but all it does is convert an RGB value to a Hex value
    def RGBtoHex(self,r,g,b):
        return "stub"
    #Reads from the current state of the gamemodel and 
    def updateScreen(self):
        print("stub")

class Controller:
    #This constructor will create a GameModel, GameView, and pass the model into the view
    def __init__(self):
        print("stub")
    #Event function called when any key is pressed
    def Update(self,char):
        print("stub")
    #Event function called when mouse is clicked
    def callback(self,event):
        print("stub")

class TestGameModel(unittest.TestCase):
    def test_basicTest(self):
        GM = GameModel(20,20)
        GM.activateCell(3,2)
        GM.activateCell(3,3)
        GM.activateCell(3,4)
        GM.updateState()

        self.assertFalse(GM.cellIsLive(3,2))
        self.assertFalse(GM.cellIsLive(3,4))

        self.assertTrue(GM.cellIsLive(2,3))
        self.assertTrue(GM.cellIsLive(3,3))
        self.assertTrue(GM.cellIsLive(4,3))
unittest.main()
