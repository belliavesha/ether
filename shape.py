from matplotlib.pyplot import *
from numpy import *
from random import random as rnd
from matplotlib.widgets import Slider, TextBox, Button
import matplotlib.text as txt


fig, ax = subplots()
ax.set_title( 'scale: {:<.2e}'.format(1.0) )
subplots_adjust(left=0.25, bottom=0.25) 
l, = plot([1], [0], 'r-',markersize=1.)
ax.axis('scaled')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

axiC = axes([0.25, 0.15, 0.65, 0.03], facecolor='gray')
axrC = axes([0.25, 0.11, 0.65, 0.03], facecolor='grey')
axN = axes([0.25, 0.03, 0.65, 0.03], facecolor='green')
# SrMtxt = txt.Text(text = '1.0')

sliC =  Slider(axiC, 'b', -1, 2, valinit=0)
slrC =  Slider(axrC, 'a', -1, 2, valinit=1)
slN =  Slider(axN, 'N', 1., 4, valinit=2.)

def draw(N,C):
    rN =range(N)
    P = 51
    rss = zeros((2*P,)) 
    rss[:P] = linspace(-2,2,P)
    rss[P:] = linspace(-2,2,P)
    iss = zeros((2*P,))

    for k in range(P):
        rS = rss[k]
        iS = 2
        diS = iS/2
        for i in range(12):
            an = 1
            S = rS + iS*1j
            for n in rN:
                an = an *(S + C*sin(n))
                if abs(an)< 1e-4:
                    iS = iS + diS
                    diS/=2
                    break
                if abs(an)> 1e4:
                    iS = iS - diS
                    diS/=2
                    break
        iss[k]=iS if iS > 1e-3 else None
        iS = -2
        diS = iS/2
        for i in range(12):
            an = 1
            S = rS + iS*1j
            for n in rN:
                an = an *(S + C*sin(n))
                if abs(an)< 1e-4:
                    iS = iS + diS
                    diS/=2
                    break
                if abs(an)> 1e4:
                    iS = iS - diS
                    diS/=2
                    break
        iss[k+P]=iS if iS < -1e-3 else None


    b = iss[P//2]
    a = 2-iss[P//2]
    print(C,a,b)
    l.set_data(rss, iss)
    # ax.set_title('scale: {:<.2e}'.format(mabs) )
    ax.axis('scaled')
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    fig.canvas.draw_idle()



    
def update(val):
    iC = sliC.val
    rC = slrC.val
    C = rC + 1j*iC
    N = int(exp(slN.val*log(1e1)))
    draw(N,C)

slrC.on_changed(update)
sliC.on_changed(update)
slN.on_changed(update)
show()

