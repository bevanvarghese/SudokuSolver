import pygame
import sys

pygame.init()

#GUI instantiations
HEIGHT = 510
WIDTH = 510
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (106, 108, 110)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELLSIZE = (WIDTH-60)//9
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku Solver')
font = pygame.font.SysFont('Arial', CELLSIZE//2)

board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
cell_colors = [[GREY for i in range(9)] for j in range(9)]
solving = True

def validMove(row, col, n):
    #check row
    for i in range(0,9):
        if board[row][i]==n:
            return False
    #check column
    for i in range(0,9):
        if board[i][col]==n:
            return False
    #check 3x3 box
    r_top = 3*(row//3)
    c_left = 3*(col//3)
    for i in [r_top, r_top+1, r_top+2]:
        for j in [c_left, c_left+1, c_left+2]:
            if board[i][j]==n:
                return False
    return True

def findEmpty():
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                #print(i,j)
                return [i,j]
    return False

def solve(board):
    found = findEmpty()
    if not found:
        return True
    row, col = found
    for n in range(1, 10):
        if validMove(row, col, n):
            board[row][col] = n
            cell_colors[row][col] = GREEN
            if solve(board):
                return True
            #backtracking
            board[row][col] = 0
            cell_colors[row][col] = RED
    return False

#game loop
while True:
    surface.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                solving = True
        #drawing each cell
        if not solving:
            for i in range(9):
                for j in range(9):
                    pygame.draw.rect(surface, cell_colors[i][j], (30+j*CELLSIZE, 30+i*CELLSIZE, CELLSIZE, CELLSIZE), 1)
                    if board[i][j]!=0:
                        surface.blit(font.render(str(board[i][j]), True, BLACK), (30+(j+0.4)*CELLSIZE, 30+(i+0.2)*CELLSIZE))
        else:
            solve(board)
            for i in range(9):
                for j in range(9):
                    if cell_colors[i][j]==GREY:
                        pygame.draw.rect(surface, cell_colors[i][j], (30+j*CELLSIZE, 30+i*CELLSIZE, CELLSIZE, CELLSIZE), 1)
                        surface.blit(font.render(str(board[i][j]), True, BLACK), (30+(j+0.4)*CELLSIZE, 30+(i+0.2)*CELLSIZE))
                        continue
                    pygame.draw.rect(surface, cell_colors[i][j], (30+j*CELLSIZE, 30+i*CELLSIZE, CELLSIZE, CELLSIZE), 2)
                    surface.blit(font.render(str(board[i][j]), True, BLUE), (30+(j+0.4)*CELLSIZE, 30+(i+0.2)*CELLSIZE))
        #outermost boundaries
        pygame.draw.rect(surface, BLACK,(30, 30, WIDTH-60, HEIGHT-60), 3)
        #rectangle for middle three columns
        pygame.draw.rect(surface, BLACK,(30+(WIDTH-60)//3, 30, (WIDTH-60)//3, HEIGHT-60), 3)
        #rectangle for middle three rows
        pygame.draw.rect(surface, BLACK,(30, 30+(WIDTH-60)//3, WIDTH-60, (HEIGHT-60)//3), 3)
        pygame.display.update()

for i in range(9):
    print(board[i])
