import pygame
import random
import matplotlib.pyplot as plt
from matplotlib.artist import Artist
import numpy as np

#------Config pygame-------------------------
width = 900
height = 900
radius = width
red =pygame.Color('Red')
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

#-----Setup pygame---------------------------
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(('Calculo de Pi'))
border_width = 2
screen.fill((white))
pygame.draw.circle(screen, black, (0,height), radius, border_width)

#------Constants ------------------------
N = 600000                 #Number of interactions
Count =0
x_Pi = (0,N,1)             #Pi value
y_Pi= (np.pi,np.pi,np.pi)  #Pi value
xValues = []
yValues = []
nPoints = 0
inCircle = 0
outCircle = 0

#------Config matplotlib-----------------
fig, ax = plt.subplots()
plt.rcParams["figure.figsize"] = [8.6, 8.6]
plt.rcParams["figure.autolayout"] = False
ax.set(title=r"MC Sampling for $\pi$",ylabel="$\pi$ value", xlabel="Interactions")
text = plt.text(200, 3.142, '$\pi$ value', fontsize=20,  color='red',family='monospace', fontweight='ultralight')
Pi_value = plt.plot(x_Pi,y_Pi, lw=.5,c='black')

#------start program-------------------
while Count <=N:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    x= random.uniform(0,width)
    y = random.uniform(0, height)
    nPoints += 1
    #'----------Monte Carlo simulation
    if x**2 + y**2 <= radius**2:
        pygame.draw.circle(screen, 'blue',(x,height-y), radius = 2)
        inCircle += 1
    else:
        pygame.draw.circle(screen, 'red', (x, height-y), radius=2)
        outCircle += 1

    if (nPoints) % 1000 == 0:
    #-------output values-------------------------------
        pi = 4 * inCircle / nPoints
        sMsg = f'{nPoints}\t{pi}\n'
        print(sMsg,end='')
        xValues.append(nPoints)
        yValues.append((pi))
        plt.xlim(0,nPoints+1000)
        plt.plot(xValues,yValues,lw=0.5,c='blue')
        pi_number = ax.text(0.37,0.405,'$\pi$ =       =',fontsize=20,transform=plt.gcf().transFigure, color='green', family='monospace', fontweight='ultralight')
        numerator = ax.text(0.47, 0.43, str(inCircle),fontsize=20, transform=plt.gcf().transFigure,  color='black', family='monospace', fontweight='ultralight' )
        bare = ax.text(0.46, 0.44, '______ ', fontsize=20, color='black', transform=plt.gcf().transFigure, family='monospace',fontweight='ultralight')
        denominator = ax.text(0.47, 0.36, str(nPoints), fontsize=20, transform=plt.gcf().transFigure, color='black', family='monospace',fontweight='ultralight')
        pi_result = ax.text(0.67, 0.40, str('%.3f'%pi),fontsize=20, transform=plt.gcf().transFigure,  color='black', family='monospace', fontweight='ultralight' )
        plt.pause(0.001)
        Artist.remove(numerator)
        Artist.remove(denominator)
        Artist.remove(pi_result)
    pygame.display.flip()
    Count+= 1
    plt.show
pygame.quit()
