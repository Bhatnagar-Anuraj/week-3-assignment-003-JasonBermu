"""
DIGM 131 - Assignment 3: Function Library (scene_functions.py)
===============================================================

OBJECTIVE:
    Create a library of reusable functions that each generate a specific
    type of scene element. This module will be imported by main_scene.py.

REQUIREMENTS:
    1. Implement at least 5 reusable functions.
    2. Every function must have a complete docstring with Args and Returns.
    3. Every function must accept parameters for position and/or size so
       they can be reused at different locations and scales.
    4. Every function must return the name(s) of the Maya object(s) it creates.
    5. Follow PEP 8 naming conventions (snake_case for functions/variables).

GRADING CRITERIA:
    - [30%] At least 5 functions, each creating a distinct scene element.
    - [25%] Functions accept parameters and use them (not hard-coded values).
    - [20%] Every function has a complete docstring (summary, Args, Returns).
    - [15%] Functions return the created object name(s).
    - [10%] Clean, readable code following PEP 8.
"""

import maya.cmds as cmds
import math

#This line of code will give the buildings geometry and make sure they don't fall below the coordinate plane
def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    building = cmds.polyCube(w=width, h=height, d=depth)[0]
    pos_x = position[0]
    pos_y = position[1]
    pos_z = position[2]
    
    cmds.move(pos_x, pos_y + (height / 2.0), pos_z, building)
    return building

#This line of code will make the tall trees that will go in my scene
def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2, position=(0, 0, 0)):
    trunk = cmds.polyCylinder(r=trunk_radius, h=trunk_height, name="trunk")[0]
    cmds.move(0, trunk_height / 2.0, 0, trunk)
    canopy = cmds.polySphere(r= canopy_radius, name="canopy")[0]
    cmds.move(0, trunk_height, 0, canopy)
    #This Line of code makes sure maya reads these two objects as one 
    tall_tree = cmds.group(trunk, canopy, n="tall_tree")

    pos_x = position[0]
    pos_y = position[1]
    pos_z = position[2]

    cmds.move(pos_x, pos_y, pos_z, tall_tree)

    return tall_tree

#This line of code will create a fence that will go around the buildings and trees, kind of
def create_fence(num_posts=5, spacing=1.5, position=(0, 0, 0)):
    slats = []
    
    for i in range(num_posts):
        slat = cmds.polyCube(w=0.1, h=1.5, d=0.6, name=f"slat_{i}")[0]
        cmds.move(i * spacing, 0.75, 0, slat)
        slats.append(slat)
    
    total_length = spacing * (num_posts - 1)
    rail = cmds.polyCube(w=total_length, h=0.1, d=0.2, name="fence_rail")[0]
    cmds.move(total_length / 2.0, 1.0, 0, rail)
    slats.append(rail)
        
    fence = cmds.group(slats, n="fence_grp")
    
    pos_x = position[0]
    pos_y = position[1]
    pos_z = position[2]
    
    cmds.move(pos_x, pos_y, pos_z, fence)
    
    return fence


#This creates a lamp post from a sphere and a cylinder
def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    
    post = cmds.polyCylinder(r=0.1, h=pole_height, name="lamp_pole")[0]
    cmds.move(0, pole_height / 2.0, 0, post)
    bulb = cmds.polySphere(r=light_radius, name="lamp_bulb")[0]
    cmds.move(0, pole_height, 0, bulb)

    Lamp = cmds.group(post, bulb, n="lamp_post")
    pos_x, pos_y, pos_z = position
    cmds.move(pos_x, pos_y, pos_z, Lamp)

    return Lamp
#This will create some rough fencing for around all of my scene
def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0)):
    results = []
    for i in range(count):
        # Calculate angle and coordinates
        angle = (2 * math.pi / count) * i
        x = center[0] + math.cos(angle) * radius
        z = center[2] + math.sin(angle) * radius
        
        # Call the function using the position tuple
        result = create_func(position=(x, center[1], z))
        results.append(result)
    return results

def create_fountain(radius=1, position=(0, 0, 0)):
    #This will create the base of our fountain
    base = cmds.polyTorus(r=radius, sectionRadius=0.4, name="fountain_base")[0]
    cmds.move(0, 0.2, 0, base)
    #This will create to top or nozel of the fountain
    top = cmds.polyCone(r=radius * 0.4, h=1.5, name="fountain_top")[0]
    cmds.move(0, 0.75, 0, top)

    fountain = cmds.group(base, top, n="fountain")
    pos_x, pos_y, pos_z = position
    cmds.move(pos_x, pos_y, pos_z, fountain)
    return fountain

# Clear scene before running
cmds.file(new=True, force=True)

# This makes a ring of trees
place_in_circle(create_tree, count=10, radius=10, center=(0, 0, 5))

#This makes ring of lampposts
place_in_circle(create_lamp_post, count=6, radius=13, center=(0, 0, 5))

#Makes a ring of buildings
place_in_circle(create_building, count=3, radius=5, center=(0, 0, 5))

#This guy makes a fence round everything
place_in_circle(create_fence, count=8, radius=12, center=(0, 0, 5))

#This will create the fountain in the midde
place_in_circle(create_fountain, count=1, radius=1, center=(0, 0, 5))

cmds.viewFit(allObjects=True)
print("City layout complete.")