import random
import time
import pygame, sys
from pygame.locals import *
import pygame as pg
import pygame.mixer 
import pygame.time

pygame.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mixer = pygame.mixer
mixer.init()
perd = mixer.Sound("pukan.wav")
otskok = mixer.Sound("otskok.wav")
stena = mixer.Sound("stena.wav")
sc = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Sber Pong')
ochki_1 = 0
ochki_2 = 0

y1=300
y2=500
y3=300
y4=500
bx=300
by=200
v=60
r=10
ball_speedx = 5
ball_speedy = 5
st=0
ball = pygame.draw.circle(sc, WHITE, [bx, by], 10)

line1=pygame.draw.line(sc, WHITE,[50, y1], [50, y2], 10)
line2=pygame.draw.line(sc, WHITE,[950, y3], [950, y4], 10)
ball=pygame.draw.circle(sc, WHITE, [bx, by], 10)
game = False
flag = True
start=False
minet=0
def get_blobjob(head):
	global minet
	if ball.left<=55 or ball.right>=945:
		minet+=head
	else:
		minet=0
while flag:
	sc.fill(BLACK)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()	
			sys.exit()

	if ball.top<=0 or ball.bottom>=800:
		stena.play()
		ball_speedy = -1*ball_speedy
		by += ball_speedy
	if ball.right >= 950 and ball.right<=960 and ball.top>y3 and ball.bottom<y4:
		ball_speedx = -1*ball_speedx
		bx += ball_speedx-10-abs(minet)/10
		ball_speedy+=minet/10
		
		v+=5
		otskok.play()
	elif ball.left <= 50 and ball.left>=40 and ball.top>y1 and ball.bottom<y2:
		ball_speedx = -1*ball_speedx
		bx += ball_speedx+10+abs(minet)/10
		ball_speedy+=minet/10
		
		v+=5
		otskok.play()
	elif ball.left <= 0 or ball.right >= 1000:
		bx=500
		by=400
		y1=300
		y2=500
		y3=300
		y4=500
		r=10
		v=60
		time.sleep(1)
		start=True
			
	bx += ball_speedx
	by += ball_speedy
	#print(bx,by,ball_speedx,ball_speedy)
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		if y3>0:
			y3 -=12
			y4 -=12
			get_blobjob(-12)
		else:
			y3=1
			y4=201
	keys = pygame.key.get_pressed()
	if keys[pygame.K_DOWN]:
		if y4<800:
			y3 +=12
			y4 +=12
			get_blobjob(12)
		else:
			y3=599
			y4=799
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		if y1>0:
			y1 -=12
			y2 -=12
			get_blobjob(-12)
		else:
			y1=1
			y2=201
	keys = pygame.key.get_pressed()
	if keys[pygame.K_s]:
		if y2<800:
			y1 +=12
			y2 +=12
			get_blobjob(12)
		else:
			y1=599
			y2=799
	if keys[pygame.K_r]:
		y1-=10
		y2+=10
	if keys[pygame.K_t] and y4-y3>5:
		y3+=10
		y4-=10
	if keys[pygame.K_y] and r>1:
		r-=1
	
	if bx < 0:
		ochki_1 += 1
	elif bx > 1000:
		ochki_2 += 1
	if ball.left <= 0:
		ochki_1 += 1
		perd.play()
	if ball.right >= 1000:
		ochki_2 += 1
		perd.play()

	font = pygame.font.Font(None, 74)
	text = font.render(str(ochki_2), 1, WHITE)
	sc.blit(text, (400,10))
	text = font.render(str(ochki_1), 1, WHITE)
	sc.blit(text, (570,10))

	#linecenter = pygame.draw.line(sc, WHITE, [])
	i=0
	j=21
	k=800/j
	ly=0
	while i<=j/2:
		pygame.draw.line(sc, WHITE,[505, ly], [505, ly+k], 5)
		ly=ly+k*2
		i+=1
	line1=pygame.draw.line(sc, WHITE,[50, y1], [50, y2], 10)
	line2=pygame.draw.line(sc, WHITE,[950, y3], [950, y4], 10)
	ball=pygame.draw.circle(sc, WHITE, [bx, by], r)
	pygame.display.flip()
	if start:
		time.sleep(2)
		start=False
		if ball_speedx>0:
			ball_speedx=random.randrange(5, 10, 1)
		else:
			ball_speedx=random.randrange(-5, -10, -1)
		if ball_speedy>0:
			ball_speedy=random.randrange(2, 5, 1)
		else:
			ball_speedy=random.randrange(-2, -5, -1)
	clock.tick(v)



    
