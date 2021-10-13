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

def PlacePieces(window):
    print("Placing some pieces...")
    img = Image(Point(40,40),"img/Chess_bdt45.svg")
    img.draw(window)

    img = Image(Point(120,120),"img/Chess_kdt45.svg")
    img.draw(window)

    img = Image(Point(200,200),"img/Chess_klt45.svg")
    img.draw(window)

    img = Image(Point(280,280),"img/Chess_qdt45.svg")
    img.draw(window)

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
    PlacePieces(win)
    selectedSquare = None 
    prev = None
    while(True):
        mousePoint = win.getMouse()
        prev = highlightSelectedSquare(squares, mousePoint, prev)
        print(mousePoint)
    win.close()
    

main()
