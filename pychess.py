#!/usr/bin/env python3
import argparse
from graphics import *
import math

light_fill = color_rgb(200,200,200)
dark_fill = color_rgb(50,50,50)

def DrawBoard(window):
    board = Rectangle(Point(0,0),Point(639,639))
    board.draw(window)

    boardSquares = []
    for i in range(8):
        squareRow = []
        for j in range(8):
            x1 = i*80
            x2 = i*80 + 79
            y1 = j*80
            y2 = j*80 + 79

            p1 = Point(x1,y1)
            p2 = Point(x2,y2)

            r = Rectangle(p1,p2)
            r.setFill(light_fill)

            if((i%2 != 0) and (j%2 == 0)):
                r.setFill(dark_fill)

            if((i%2 == 0) and (j%2 != 0)):
                r.setFill(dark_fill)

            r.draw(window)
            squareRow.append(r)
        boardSquares.append(squareRow)
    return boardSquares

class Piece:
    def __init__(self, pieceId, coord, window):
        self.Id = pieceId
        self.Location = coord
        self.window = window
        self.image = Image(Point(40,40), "img/Chess_bdt45.svg")
    
    def move(self):
        xIdx = ord(self.Location[0]) - 97
        yIdx = int(self.Location[1])

        x = xIdx * 80 + 40
        y = yIdx * 80 + 40

        point = self.image.getAnchor()
        dx = x - point.getX()
        dy = y - point.getY()

        self.image.move(dx, dy) 

    def Place(self, coord = None):
        if(coord):
            self.Location = coord

        self.move()
        self.image.draw(self.window)
        a = self.image.getAnchor()
        print("Placed at", a.getX(), a.getY())

    def Move(self, coord):
        self.Location = coord
        #check for move validity 
        self.move()

        return coord


def PlacePieces(window, pieceArray=None):
    print("Placing some pieces...")

    if(not pieceArray or (type(pieceArray) is not list)):
        img = Image(Point(40,40),"img/Chess_bdt45.svg")
        img.draw(window)

        img = Image(Point(120,120),"img/Chess_kdt45.svg")
        img.draw(window)

        img = Image(Point(200,200),"img/Chess_klt45.svg")
        img.draw(window)

        img = Image(Point(280,280),"img/Chess_qdt45.svg")
        img.draw(window)
        return

    print("Placing using classes...")
    for p in pieceArray:
        p.Place()

    

def highlightSelectedSquare(squares, point, previous):
    prevSquare = previous

    xIdx = math.floor(point.getX()/80)
    yIdx = math.floor(point.getY()/80)
    selectedSquare = squares[xIdx][yIdx]
    if(prevSquare):
        fill = light_fill
        x = math.floor(prevSquare.getCenter().getX()/80)
        y = math.floor(prevSquare.getCenter().getY()/80)
        if (x%2 !=0) and (y%2 == 0):
            fill = dark_fill
        if (x%2 ==0) and (y%2 != 0):
            fill = dark_fill
        prevSquare.setFill(fill)
    
    prevSquare = selectedSquare
    selectedSquare.setFill("red")
    return prevSquare

def main():
    #Do some things
    print("Hello, pychess!")
    print("I'm gonna draw a board...")
    win = GraphWin("Board", 640,640)
    squares = DrawBoard(win)
    pieceArray = [Piece('k','h8',win )]
    PlacePieces(win, pieceArray)
    selectedSquare = None 
    prev = None
    while(True):
        mousePoint = win.getMouse()
        prev = highlightSelectedSquare(squares, mousePoint, prev)
    win.close()
    

main()
