"""
JDE Robot GSoC 2023 Python Challenge 

author: Pawan Wadhwani
email: pawanw17@gmail.com

"""

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

class BrownianBox:

    LENGTH = 100
    WIDTH = 50
    EDGE_COLOR = 'black'
    EDGE_WIDTH = 2
    ORIGIN = (0, 0)

    RADIUS_OF_BOT = 2
    START_ANGLE = 90 #degrees

    def __init__(self):
        self.box = plt.Rectangle(self.ORIGIN, self.LENGTH, self.WIDTH, edgecolor=self.EDGE_COLOR, facecolor='none', linewidth=self.EDGE_WIDTH)
        self.fig, self._ = plt.subplots()
        self.ax = plt.gca()
        self.ax.add_patch(self.box)

        self.robot_start_position = (self.LENGTH/2, self.WIDTH/2)
        self.robot = plt.Circle(self.robot_start_position,radius=self.RADIUS_OF_BOT,ec="black",fc="blue")
        self.robot.center = self.robot_start_position
        self.sa = self.START_ANGLE
        self.x = self.robot_start_position[0]
        self.y = self.robot_start_position[1]
        self.dx = 0
        self.dy = 0

    def find_temps(self):
        self.dx, self.dy = np.cos(np.radians(self.sa)), np.sin(np.radians(self.sa))

    def does_it_collide(self, x, y):
        if x + self.dx <= self.RADIUS_OF_BOT or x + self.dx >=self.LENGTH - self.RADIUS_OF_BOT \
            or y + self.dy <= self.RADIUS_OF_BOT or y + self.dy >= self.WIDTH - self.RADIUS_OF_BOT:
            
            print("collision",x + self.dx, y + self.dy)
            self.sa = np.random.randint(0,360)
            self.find_temps()
            self.does_it_collide(x, y)

    def update_center(self, x, y):
        self.x = x + self.dx
        self.y = y + self.dy
        self.robot.center = (self.x, self.y)

    def init_sim(self):
        self.ax.add_patch(self.robot)
        return self.robot,

    def animate(self,i):
        x, y = self.robot.center

        self.find_temps()
        self.does_it_collide(x,y)
        self.update_center(x,y)

        return self.robot,

    def run_sim(self):
        anim = animation.FuncAnimation(self.fig, self.animate, 
                               init_func=self.init_sim, 
                               frames=3000, 
                               interval=20,
                               blit=True,repeat=False)
        plt.axis('scaled')
        # writervideo = animation.FFMpegWriter(fps=60)
        # anim.save('brownian_box_2.mp4',writer=writervideo)
        plt.show()