#Vector 3D - An interactive python-based web app for mapping vectors
from vpython import *

#Create scene are regulatory conditions
scene = canvas(width=1200, height=500, background=color.white, title="Vector3 - A Vector Mapping Tool")

scene.ambient = color.white * 0.8

distance = 5
mode = "draw"

#Create horizonal surface for vectors to rest off
plane_normal = vec(0, 1, 0)  
plane_distance = 0           

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

#Define vector draw function
def vector_draw():
    global start_position, user_arrow
    start_position = mouse.pos
    user_arrow = arrow(pos=vec(start_position), axis=vec(0,0,0), color=color.purple, round=True, shaftwidth=0.05)

#Define vector simulating function
def vector_simulate():
    arrow_sim_position = scene.mouse.project(normal=plane_normal, d=plane_distance)
    if arrow_sim_position: #Update the arrow's final position to the cursor
        user_arrow.axis = arrow_sim_position - user_arrow.pos


#Intialize the scene loop and drawing controls
scene.bind("mousedown", vector_draw)
scene.bind("mousemove", vector_simulate)

while True:
    rate(5)