import pygame
import sys
import random
pygame.init()

color_disp=[55,155,200]
size_blok=20
cout_blok=20
otstup=1
otstup_verh=70
color_snake = [255, 0, 0]


size = [size_blok*cout_blok+2*size_blok+otstup*cout_blok,
        size_blok*cout_blok+2*size_blok+otstup*cout_blok + otstup_verh]

screan = pygame.display.set_mode(size)

pygame.display.set_caption("Вуж))")
timer = pygame.time.Clock()
Shrift = pygame.font.SysFont("Shrift",40)
Shrift_2 = pygame.font.SysFont("Shrift",25)


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_inside(self):
        return 0<=self.x<size_blok and 0<=self.y<size_blok
    
    def __eq__(self,other):
        return isinstance(other,SnakeBlock) and self.x==other.x and self.y==other.y

def get_random_emty_block():
    x=random.randint(0, cout_blok-1)
    y=random.randint(0, cout_blok - 1)
    empty_block=SnakeBlock(x,y)
    while empty_block in snake_block:
        empty_block.x=random.randint(0, cout_blok-1)
        empty_block.x=random.randint(0, cout_blok-1)
    return empty_block

def draw_block(color,row,column):
    pygame.draw.rect(screan,color,[size_blok+column*size_blok+otstup*(column+1),
                                        otstup_verh + size_blok + row*size_blok+otstup*(row+1),
                                        size_blok,size_blok])

snake_block=[SnakeBlock(9,8),SnakeBlock(9,9),SnakeBlock(9,10)]

apple=get_random_emty_block()

d_row = 0
d_col = 1
score = 0
speed = 1

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col!=0:
                d_row = -1
                d_col = 0
            elif event.key==pygame.K_DOWN and d_col!=0:
                d_row = 1 
                d_col = 0
            elif event.key==pygame.K_LEFT and d_row!=0:
                d_row=0
                d_col=-1
            elif event.key==pygame.K_RIGHT and d_row!=0:
                d_row=0
                d_col=1

    screan.fill(color_disp)
    pygame.draw.rect(screan,[100,155,200],[0,0,size[0],otstup_verh])
    text_score = Shrift.render(f"Score: {score}", 0, [255,255,255]) 
    text_speed = Shrift.render(f"Level: {speed}", 0, [255,255,255])
    text_avtor = Shrift_2.render(f"by Vitaliy Duma", 0, [255,0,0])
    screan.blit(text_score,(size_blok,size_blok))
    screan.blit(text_speed,(size_blok + 200,size_blok))
    screan.blit( text_avtor,(size_blok+150,size_blok+490))

    for row in range(cout_blok):
        for column in range(cout_blok):
            if (column+row)%2==0:
                color=[170,240,240]
            else:
                color=[255,255,255]    
            
            draw_block(color,row,column)
    
    HEAD=snake_block[-1]

    if not HEAD.is_inside():
        print("cash")
        pygame.quit()
        sys.exit()
    
    draw_block([0,0,0],apple.x , apple.y)

    for block in snake_block:
       
        draw_block(color_snake, block.x, block.y)
    
    if apple == HEAD:
        score+=1
        speed = score//5+1
        snake_block.append(apple)
        apple=get_random_emty_block()
        
    NEW_HEAD=SnakeBlock(HEAD.x+d_row,HEAD.y+d_col)
    snake_block.append(NEW_HEAD)
    snake_block.pop(0)
   
    pygame.display.flip()        
    timer.tick(3+speed)