#!/usr/bin/env python3
import pygame
import random

def showmult(screen,running):
    intro = pygame.image.load("images/ticmult.png")
    screen.blit(intro, (0,0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>234 and x<360 and y>140 and y<184:
                    show3x3(screen,running)
                    intro = pygame.image.load("images/ticmult.png")
                    screen.blit(intro, (0,0))
                    pygame.display.flip()                                
                if x>234 and x<360 and y>210 and y<245:
                    show5x5(screen,running)
                    intro = pygame.image.load("images/ticmult.png")
                    screen.blit(intro, (0,0))
                    pygame.display.flip()                
                if x>0 and x<96 and y>0 and y<78:
                    return

 
 
def showcomp(screen,running):
    intro = pygame.image.load("images/ticcomp.png")
    screen.blit(intro, (0,0))
    pygame.display.flip() 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>234 and x<360 and y>115 and y<184:
                    show3x3c(screen,running)
                    intro = pygame.image.load("images/ticcomp.png")
                    screen.blit(intro, (0,0))
                    pygame.display.flip()                           
                if x>234 and x<360 and y>190 and y<222:
                    show5x5c(screen,running)                    
                    intro = pygame.image.load("images/ticcomp.png")
                    screen.blit(intro, (0,0))
                    pygame.display.flip()                  
                if x>0 and x<96 and y>0 and y<78:
                    return


def show3x3(screen,running):
    intro = pygame.image.load("images/3*3.png")
    screen.blit(intro, (0,0))
    pygame.display.flip()
    t=[]
    move="x"
    x0 = 170
    x1 = 396
    dx = int((x1 - x0) / 3)
    y0 = 87
    y1 = 320
    dy = int((y1 - y0) / 3)
    while running:
        showcurrentturn(screen,move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>x0 and x<x1 and y>y0 and y<y1:
                    v=int((y-y0)/dy)
                    h=int((x-x0)/dx)
                    if addturn(t,v,h,move):
                        showx(screen,move,v,h,y0,dy,x0,dx)  
                        if move=="x":
                            move="o"
                        else:
                            move="x"
                        if win("x",t):
                            winscr("x",screen,running)
                            return
                        if win("o",t):
                            winscr("o",screen,running)
                            return
                        if len(t)==9:
                            draw3(screen,running)
                            return                       
                if x>0 and x<96 and y>0 and y<78:
                    return


def addturn(t,v,h,move):
    t0=[v,h,"x"]
    t1=[v,h,"o"]
    if t0 in t or t1 in t:
        return False
    t.append([v,h,move])
    return True
def win(move,t):
    wc=wnc(move)
    for v in wc:
        if v[0] in t and v[1] in t and v[2] in t:
            return True
    return False


def wnc(move):
    a=[]
    for v in [0,1,2]:
        a.append([[v,0,move],[v,1,move],[v,2,move]])
        a.append([[0,v,move],[1,v,move],[2,v,move]])
    a.append([[0,0,move],[1,1,move],[2,2,move]])
    a.append([[2,0,move],[1,1,move],[0,2,move]])
    return a

def win5(move,t):
    wc=wnc5(move)
    for v in wc:
        if v[0] in t and v[1] in t and v[2] in t and v[3] in t and v[4] in t:
            return True
    return False


def wnc5(move):
    a=[]
    for v in [0,1,2,3,4]:
        a.append([[v,0,move],[v,1,move],[v,2,move],[v,3,move],[v,4,move]])
        a.append([[0,v,move],[1,v,move],[2,v,move],[3,v,move],[4,v,move]])
    a.append([[0,0,move],[1,1,move],[2,2,move],[3,3,move],[4,4,move]])
    a.append([[0,4,move],[1,3,move],[2,2,move],[3,1,move],[4,0,move]])
    return a

def winscr(move,screen,running):
    if move=="o":
        image = pygame.image.load("images/3*3blue.png")
    else:
        image = pygame.image.load("images/3*3red.png")
    screen.blit(image, (0,0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

def movec5(t):
    m=remturn5(t)
    v,h=intcho5(t,m)
    t.append([v,h,"o"])
    return v,h

def draw3(screen,running):
    image = pygame.image.load("images/3*3draw.png")
    screen.blit(image, (0,0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
 
def winscr5(move,screen,running):
    if move=="o":
        image = pygame.image.load("images/5*5blue.png")
    else:
        image = pygame.image.load("images/5*5red.png")
    screen.blit(image, (0,0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

def show5x5c(screen,running):
    intro = pygame.image.load("images/5*5.png")
    screen.blit(intro, (0,0))
    pygame.display.flip()
    t=[]
    move="x"
    x0 = 159
    x1 = 479
    dx = int((x1 - x0) / 5)
    y0 = 63
    y1 = 355
    dy = int((y1 - y0) / 5)
    while running:
        showcurrentturn5(screen,move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>x0 and x<x1 and y>y0 and y<y1:
                    v=int((y-y0)/dy)
                    h=int((x-x0)/dx)
                    if addturn(t,v,h,move):
                        showx5(screen,move,v,h,y0,dy,x0,dx)  
                        if move=="x":
                            move="o"
                        else:
                            move="x" 
                        if win5("x",t):
                            winscr5("x",screen,running)
                            return
                        if len(t)==25:
                            draw5(screen,running)
                            return           
                        v,h=movec5(t)
                        move="o"
                        showx5(screen,move,v,h,y0,dy,x0,dx) 
                        move="x"
                        if win5("o",t):
                            winscr5("o",screen,running)
                            return
                        if len(t)==25:
                            draw5(screen,running)
                            return                                    
                if x>0 and x<96 and y>0 and y<78:
                    return


def show3x3c(screen,running):
    intro = pygame.image.load("images/3*3.png")
    screen.blit(intro, (0,0))
    pygame.display.flip()
    t=[]
    move="x"
    x0 = 170
    x1 = 396
    dx = int((x1 - x0) / 3)
    y0 = 87
    y1 = 320
    dy = int((y1 - y0) / 3)
    while running:
        showcurrentturn(screen,move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>x0 and x<x1 and y>y0 and y<y1:
                    v=int((y-y0)/dy)
                    h=int((x-x0)/dx)
                    if addturn(t,v,h,move):
                        showx(screen,move,v,h,y0,dy,x0,dx)  
                        if move=="x":
                            move="o"
                        else:
                            move="x"
                        if win("x",t):
                            winscr("x",screen,running)
                            return
                        if len(t)==9:
                            draw3(screen,running)
                            return           
                        v,h=movec3(t)
                        move="o"
                        showx(screen,move,v,h,y0,dy,x0,dx) 
                        move="x"
                        if win("o",t):
                            winscr("o",screen,running)
                            return
                        if len(t)==9:
                            draw3(screen,running)
                            return                               
                if x>0 and x<96 and y>0 and y<78:
                    return


def remturn3(t):
    m=[]
    for v in [0,1,2]:
        for h in [0,1,2]:
            t0=[v,h,"x"]
            t1=[v,h,"o"]
            if not (t0 in t or t1 in t):
                m.append([v,h])
    return m

def movec3(t):
    m=remturn3(t)
    v,h=intcho(t,m)
    t.append([v,h,"o"])
    return v,h

def intcho(t,m):
    for v,h in m:
        t.append([v,h,"o"])
        if win("o",t):
            t.pop()
            return v,h
        t.pop()
    return random.choice(m)
   
def intcho5(t,m):
    for v,h in m:
        t.append([v,h,"o"])
        if win5("o",t):
            t.pop()
            return v,h
        t.pop()
    return random.choice(m) 

def showx(screen,move,v,h,y0,dy,x0,dx):
    intro = pygame.image.load(f"images/{move}3*3.png")
    screen.blit(intro, (x0+h*dx,y0+v*dy))
    pygame.display.flip()

def showcurrentturn(screen,move):
    intro = pygame.image.load(f"images/{move}3*3scm.png")
    screen.blit(intro, (330,330))
    pygame.display.flip()

def show5x5(screen,running):
    intro = pygame.image.load("images/5*5.png")
    screen.blit(intro, (0,0))
    pygame.display.flip()
    t=[]
    move="x"
    x0 = 159
    x1 = 479
    dx = int((x1 - x0) / 5)
    y0 = 63
    y1 = 355
    dy = int((y1 - y0) / 5)
    while running:
        showcurrentturn5(screen,move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>x0 and x<x1 and y>y0 and y<y1:
                    v=int((y-y0)/dy)
                    h=int((x-x0)/dx)
                    if addturn(t,v,h,move):
                        showx5(screen,move,v,h,y0,dy,x0,dx)  
                        if move=="x":
                            move="o"
                        else:
                            move="x"  
                        if win5("x",t):
                            winscr5("x",screen,running)
                            return
                        if win5("o",t):
                            winscr5("o",screen,running)
                            return
                        if len(t)==25:
                            draw5(screen,running)
                            return                          
                if x>0 and x<96 and y>0 and y<78:
                    return

def draw5(screen,running):
    image = pygame.image.load("images/5*5draw.png")
    screen.blit(image, (0,0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

def remturn5(t):
    m=[]
    for v in [0,1,2,3,4]:
        for h in [0,1,2,3,4]:
            t0=[v,h,"x"]
            t1=[v,h,"o"]
            if not (t0 in t or t1 in t):
                m.append([v,h])
    return m

def showcurrentturn5(screen,move):
    intro = pygame.image.load(f"images/{move}5*5scm.png")
    screen.blit(intro, (10,310))
    pygame.display.flip()

def showx5(screen,move,v,h,y0,dy,x0,dx):
    intro = pygame.image.load(f"images/{move}5*5.png")
    screen.blit(intro, (x0+h*dx,y0+v*dy))
    pygame.display.flip()


def main():
    pygame.init()
    logo = pygame.image.load("images/logo32x32.png")
    intro = pygame.image.load("images/tic intro.png")

    pygame.display.set_icon(logo)
    pygame.display.set_caption("tic-tac-toe")
     
    screen = pygame.display.set_mode((640,400))
    screen.blit(intro, (0,0))
    pygame.display.flip() 
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>250 and x<352 and y>118 and y<178:
                    showcomp(screen,running)
                    screen.blit(intro, (0,0))
                    pygame.display.flip()                 
                if x>250 and x<352 and y>190 and y<240:
                    showmult(screen,running)
                    screen.blit(intro, (0,0))
                    pygame.display.flip() 


if __name__=="__main__":
    # call the main function
    main()
