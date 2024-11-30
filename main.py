#Vector 3D - An interactive python-based web app for mapping vectors
from vpython import *

#Create scene are regulatory conditions
scene = canvas(width=1200, height=500, background=color.white, title="Vector3 - A Vector Mapping Tool")

scene.ambient = color.white * 0.8
scene.userpan = False

distance = 2.5
mode = "draw"

global mouse
mouse = scene.mouse


#Create the 3D Scene

s = sphere(radius=0.05, color=color.white)

#Generate the cartesian axises
x_axis = arrow(pos=vec(0,0,0), axis=vec(distance, 0, 0), color=color.red, round=True, shaftwidth=0.05)
y_axis = arrow(pos=vec(0,0,0), axis=vec(0, distance, 0), color=color.green, round=True, shaftwidth=0.05)
z_axis = arrow(pos=vec(0,0,0), axis=vec(0, 0, distance), color=color.blue, round=True, shaftwidth=0.05)

#Generate the inverted cartesian axises
x_inv_axis = arrow(pos=vec(0,0,0), axis=vec(-distance, 0, 0), color=color.red, round=True, shaftwidth=0.05)
y_inv_axis = arrow(pos=vec(0,0,0), axis=vec(0, -distance, 0), color=color.green, round=True, shaftwidth=0.05)
z_inv_axis = arrow(pos=vec(0,0,0), axis=vec(0, 0, -distance), color=color.blue, round=True, shaftwidth=0.05)


def vector_draw():
    global start_position
    start_position = mouse.pos
    print(start_position)


def vector_draw_result():
    final_position = mouse.pos
    t = arrow(pos=vec(start_position), axis=vec(vec(final_position) - vec(start_position)), color=color.purple, shaftwidth=0.05)

#Intialize the scene loop
scene.bind("mousedown", vector_draw)
scene.bind("mouseup", vector_draw_result)

while True:
    rate(50)
