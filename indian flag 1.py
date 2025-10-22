

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D


width, height = 600, 400


saffron = [255/255, 153/255, 52/255]
white = [1, 1, 1]
green = [19/255, 136/255, 8/255]
navy_blue = [0, 0, 128/255]


flag = np.zeros((height, width, 3), dtype=np.float32)
stripe_height = height // 3

flag[:stripe_height] = saffron 
flag[stripe_height:2*stripe_height] = white  
flag[2*stripe_height:] = green  


chakra_radius = stripe_height // 2
chakra_center = (width // 2, stripe_height // 2 + stripe_height)
num_spokes = 24
angle_inc = 360 / num_spokes
line_width = 3


fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(flag)
ax.axis('off')


ax.add_patch(Circle(chakra_center, chakra_radius, edgecolor=navy_blue, facecolor='none', linewidth=line_width))


for i in range(num_spokes):
    angle_rad = np.deg2rad(i * angle_inc)
    x = chakra_center[0] + chakra_radius * np.sin(angle_rad)
    y = chakra_center[1] + chakra_radius * np.cos(angle_rad)
    ax.add_line(Line2D([chakra_center[0], x], [chakra_center[1], y], color=navy_blue, linewidth=line_width))

plt.show()