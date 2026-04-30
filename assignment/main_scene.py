"""
DIGM 131 - Assignment 3: Function Library (main_scene.py)
==========================================================

OBJECTIVE:
    Use the functions you wrote in scene_functions.py to build a complete
    scene. This file demonstrates how importing and reusing functions makes
    scene creation clean and readable.

REQUIREMENTS:
    1. Import scene_functions (the module you completed).
    2. Call each of your 5+ functions at least once.
    3. Use place_in_circle with at least one of your create functions.
    4. The final scene should contain at least 15 objects total.
    5. Comment your code explaining what you are building.

GRADING CRITERIA:
    - [30%] All 5+ functions from scene_functions.py are called.
    - [25%] place_in_circle is used at least once.
    - [20%] Scene contains 15+ objects and looks intentional.
    - [15%] Code is well-commented.
    - [10%] Script runs without errors from top to bottom.
"""

import maya.cmds as cmds
import scene_functions as sf

# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# Create a ground plane.
ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]

# ---------------------------------------------------------------------------
# Placing the fountain exactly in the middle.
sf.create_fountain(radius=2, position=(0, 0, 0))

# This will create buildings in a circle around the fountain.
sf.place_in_circle(sf.create_building, count=3, radius=10, center=(0, 0, 0))

# Makes lamps for outside fo the building
sf.place_in_circle(sf.create_lamp_post, count=6, radius=16, center=(0, 0, 0))

# Creating a forest border on the outside.
sf.place_in_circle(sf.create_tree, count=12, radius=20, center=(0, 0, 0))

# This places 4 fence sections around the edges of the complex
sf.place_in_circle(sf.create_fence, count=9, radius=25, center=(0, 0, 0))
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
