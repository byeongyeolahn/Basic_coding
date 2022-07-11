import pygame
import random

def checkBoard(board):...
blocks =[...]
blockColor = [...]

screenSize = {
    'width' : 480, #높이 설정
    'height' : 800
}

def getInitializeBoard():
    board = []
    for i in range(0,20): # 줄 개수 
        board.append([0, 0 , 0 , 0 , 0, 0, 0, 0, 0, 0]) # 블록 개수
        
pygame.init()
screen=pygame.display.set_mode((screenSize['width'], screenSize['height'])) # 디스플레이 설정
pygame.display.set_caption("HEXA") # 게임 창 이름

board = getInitializeBoard() # 게임판 로드 