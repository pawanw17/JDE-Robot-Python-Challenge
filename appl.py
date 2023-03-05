"""
JDE Robot GSoC 2023 Python Challenge 

author: Pawan Wadhwani
email: pawanw17@gmail.com

"""

import brownianbox
import matplotlib.pyplot as plt
from matplotlib import animation

box = brownianbox.BrownianBox()

def init():
    box.ax.add_patch(box.robot)
    return box.robot,

def animate(i):
    x, y = box.robot.center

    box.find_temps()
    box.does_it_collide(x,y)
    box.update_center(x,y)

    return box.robot,

anim = animation.FuncAnimation(box.fig, animate, 
                               init_func=init, 
                               frames=3000, 
                               interval=20,
                               blit=True,repeat=False)

writervideo = animation.FFMpegWriter(fps=60)
plt.axis('scaled')
anim.save('brownian_box.gif',writer=writervideo)

# plt.show()
plt.close()