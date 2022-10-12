import pygame
import math

print("\nWhat is the color of the first square?")
r1 = int(input("\nRED: "))
g1 = int(input("\nGREEN: "))
b1 = int(input("\nBLUE: "))

print("\nWhat is the color of the second square?")
r2 = int(input("\nRED: "))
g2 = int(input("\nGREEN: "))
b2 = int(input("\nBLUE: "))

size = int(input("\nEnter how many checkers will be in each row/column:\n"))
dim = 500
color1 = (r1,g1,b1) # color1
color2 = (r2,g2,b2) # color2

display = pygame.display.set_mode((dim, dim))     # Sets dimensions of checkerboard
display.fill((255,255,255))     # Fill checkerboard with color2
square_dim = math.ceil(int(dim / size))   # Sets the base of each checker, divide by 8 since there are 8 squares in each row and column
fill = dim - (square_dim * size)
current_color = color1

for x in range(0,size + fill,1):
    for y in range(0,size + fill,1):
        pygame.draw.rect(display,current_color,(x * square_dim, y * square_dim, square_dim, square_dim))
        pygame.display.update()
        if current_color == color2:
            current_color = color1
        else:
            current_color = color2
    if current_color == color2:
        current_color = color1
    else:
        current_color = color2 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()