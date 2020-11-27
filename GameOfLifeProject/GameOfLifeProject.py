
##Births: Each dead cell adjacent to exactly three live neighbors will become live in the next generation.
##Death by isolation: Each live cell with one or fewer live neighbors will die in the next generation.
##Death by overcrowding: Each live cell with four or more live neighbors will die in the next generation.
##Survival: Each live cell with either two or three live neighbors will remain alive for the next generation.
from tkinter import Tk, Canvas, PhotoImage, mainloop
#from math import sin
import copy
import time
import random
import numpy
import unittest
#hexx = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","10"]
#def NumToHex(num):
#    return hexx[int(((num-(num%16))/16))]+hexx[int(num%16)]
#Boarder = 5

#PXW = 25
#WINW = 500
#WINH = 500 
#Yellow = "#ffff00"
#PXL_W = int(WINW/PXW)
#PXL_H = int(WINH/PXW)
#Key = True

#b = [0]*(PXL_W+1)
#d = [b]*(PXL_H+1)

#gridState=numpy.array(d)

#def callback(event):
#    global gridState
#    clickX = int(event.x/PXW)
#    clickY = int(event.y/PXW)
#    #print(clickX," ",clickY)
#    drawCanv.create_rectangle(clickX*PXW,clickY*PXW,clickX*PXW+PXW,clickY*PXW+PXW,fill = "#"+NumToHex(int((clickX/PXL_H)*255))+NumToHex(int((clickY/PXL_W)*255))+NumToHex(255))
#    gridState[clickX][clickY] = 1
#
#def Update(char):
#    global Key
#    Key = False

#drawTk = Tk()
#drawCanv = Canvas(drawTk, width=WINW, height=WINH, bg="#000000")
#drawCanv.bind("<ButtonPress>", callback)
#drawCanv.focus_set()
#drawCanv.bind('<Key>', Update)
#drawCanv.pack()



#SET=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
            
#while True:
#    if Key:
#        drawTk.update()
#    else:
#        drawCanv.delete("all")
#        oldState = gridState.copy()
#
#        for x in range(1,PXL_W):
#            for y in range(1,PXL_H):
#                adj = [oldState[x+SET[0][0]][y+SET[0][1]]]
#                for L in range(1,8):
#                    adj = adj+[oldState[x+SET[L][0]][y+SET[L][1]]]
#
#                if oldState[x][y]==0:
#
#                    if sum(adj) == 3:
#                        gridState[x][y]=1
#                        
#
#
#                else:
#                    if sum(adj)<=1 or sum(adj)>=4:
#                        gridState[x][y]=0
#
#
#        for x in range(PXL_W-1):
#            for y in range(PXL_H-1):
#                if gridState[x][y] == 1:
#                    drawCanv.create_rectangle(x*PXW,y*PXW,x*PXW+PXW,y*PXW+PXW,fill = "#"+NumToHex(int((x/PXL_H)*255))+NumToHex(int((y/PXL_W)*255))+NumToHex(255))
#        Key = True
#        
#drawTk.destroy()

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
        self.TK = Tk()
        self.model = model
        self.PIXEL_SIZE = 25
        self.gameCanvas = Canvas(self.TK, width = self.model.width * self.PIXEL_SIZE, height = self.model.height * self.PIXEL_SIZE, bg="#000000")
        self.gameCanvas.pack()
        
        
        
    #This code looks smelly but all it does is convert an RGB value to a Hex value
    def RGBtoHex(self,r,g,b):
        return "#" + self.hexx[int(((r-(r%16))/16))]+self.hexx[int(r%16)] + self.hexx[int(((g-(g%16))/16))]+self.hexx[int(g%16)] + self.hexx[int(((b-(b%16))/16))]+self.hexx[int(b%16)]
    #Reads from the current state of the gamemodel and 
    def updateScreen(self):
        self.gameCanvas.delete("all")
        for x in range(self.model.width-1):
            for y in range(self.model.height-1):
                if self.model.gridState[x][y] == 1:
                    self.gameCanvas.create_rectangle(x*self.PIXEL_SIZE,y*self.PIXEL_SIZE,x*self.PIXEL_SIZE+self.PIXEL_SIZE,y*self.PIXEL_SIZE+self.PIXEL_SIZE,fill = self.RGBtoHex((x/self.model.width)*255,(y/self.model.height)*255,255))


class Controller:
    
    #This constructor will create a GameModel, GameView, and pass the model into the view
    def __init__(self):
        self.GM = GameModel(20,20)
        self.GV = GameView(self.GM)
        
        self.GV.gameCanvas.bind("<ButtonPress>", self.callback)
        self.GV.gameCanvas.focus_set()
        self.GV.gameCanvas.bind('<Key>', self.Update)
        self.GV.gameCanvas.pack()

        while (True):
            self.GV.TK.update()
    #Event function called when any key is pressed
    def Update(self,char):
        self.GM.updateState()
        self.GV.updateScreen()
    #Event function called when mouse is clicked
    def callback(self,event):
        clickX = int(event.x/self.GV.PIXEL_SIZE)
        clickY = int(event.y/self.GV.PIXEL_SIZE)
        self.GM.activateCell(clickX,clickY)
        self.GV.updateScreen()

GC = Controller()
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

class TestGameView(unittest.TestCase):
    def test_TK(self):
        GM = GameModel(40,40)
        GV = GameView(GM)
        GM.activateCell(3,3)
        GV.updateScreen()
        GV.gameCanvas.update()
    def test_viewFunction(self):
        GV2 = GameView(GameModel(10,10))
        self.assertEqual(GV2.RGBtoHex(255,255,255),"#ffffff")

       

unittest.main()

        

