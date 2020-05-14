from graphics.graphics_canvas import *
from graphics.graphics_robot import *


def test_grid():
    canvas_grid = init_canvas()
    while True:
        sleep(1)
        canvas_grid.update_grid()


def test_reference_frames():
    le = 0.8
    canvas_grid = init_canvas()

    # Test 1 | Position (0, 0, 0), Axis (1, 0, 0), No Rotation
    # Drawn
    draw_reference_frame_axes(vector(0, 0, 0), vector(1, 0, 0), radians(0))
    # Actual
    arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=le, color=color.purple)

    # Test 2 | Position (1, 1, 1), Axis (0, 0, 1), No Rotation
    # Drawn
    draw_reference_frame_axes(vector(1, 1, 1), vector(0, 0, 1), radians(0))
    # Actual
    arrow(pos=vector(1, 1, 1), axis=vector(0, 0, 1), length=le, color=color.purple)

    # Test 3 | Position (2, 2, 2), Axis (1, 0, 0), 30 deg rot
    # Drawn
    draw_reference_frame_axes(vector(2, 2, 2), vector(1, 0, 0), radians(30))
    # Actual
    arrow(pos=vector(2, 2, 2), axis=vector(1, 0, 0), length=le, color=color.purple).rotate(radians(30))

    # Test 4 | Position (3, 3, 3), Axis (1, 1, 1), No Rotation
    # Drawn
    draw_reference_frame_axes(vector(3, 3, 3), vector(1, 1, 1), radians(0))
    # Actual
    arrow(pos=vector(3, 3, 3), axis=vector(1, 1, 1), length=le, color=color.purple)

    # Test 5 | Position (4, 4, 4), Axis (1, 1, 1), 30 deg rot
    # Drawn
    draw_reference_frame_axes(vector(4, 4, 4), vector(1, 1, 1), radians(30))
    # Actual
    arrow(pos=vector(4, 4, 4), axis=vector(1, 1, 1), length=le, color=color.purple).rotate(radians(30))

    # Test 6 | Position (5, 5, 5), Axis (2, -1, 4), No Rotation
    # Drawn
    draw_reference_frame_axes(vector(5, 5, 5), vector(2, -1, 4), radians(0))
    # Actual
    arrow(pos=vector(5, 5, 5), axis=vector(2, -1, 4), length=le, color=color.purple)

    # Test 7 | Position (6, 6, 6), Axis (2, -1, 4), 30 deg rot
    # Drawn
    draw_reference_frame_axes(vector(6, 6, 6), vector(2, -1, 4), radians(30))
    # Actual
    arrow(pos=vector(6, 6, 6), axis=vector(2, -1, 4), length=le, color=color.purple).rotate(radians(30))


def test_import_stl():
    canvas_grid = init_canvas()
    robot0 = import_object_from_stl('link0').color = color.white
    robot1 = import_object_from_stl('link1').color = color.red
    robot2 = import_object_from_stl('link2').color = color.green
    robot3 = import_object_from_stl('link3').color = color.blue
    robot4 = import_object_from_stl('link4').color = color.magenta
    robot5 = import_object_from_stl('link5').color = color.cyan
    robot6 = import_object_from_stl('link6').color = color.black
    # robot_height = robot.height
    # wanted_height = 2.0
    # scale = wanted_height / robot_height
    # robot.size *= scale
    # robot.pos = vector(1, 0, 1)
    # print("Robot height ", robot_height, " | Scale ", scale, " | New Size ", robot.size)


def test_place_joint():
    pass


def test_animate_joints():
    pass


def test_import_textures():
    pass
