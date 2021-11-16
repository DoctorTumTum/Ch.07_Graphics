'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade

arcade.open_window(500, 700, "Gavin Clarkson",True, True)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_ellipse_filled(120,400,153,1003, arcade.color.BLACK, 355)
arcade.draw_ellipse_filled(380,400,153,1003, arcade.color.BLACK, 5)
arcade.draw_ellipse_filled(380,400,150,1000, arcade.color.YELLOW, 5)
arcade.draw_ellipse_filled(120,400,150,1000, arcade.color.YELLOW, 355)
arcade.draw_circle_filled(250,-600,1002, arcade.color.BLACK)
arcade.draw_ellipse_filled(380,400,100,666, arcade.color.YELLOW, 5)
arcade.draw_ellipse_filled(120,400,100,666, arcade.color.YELLOW, 355)
arcade.draw_circle_filled(250,-600,1000, arcade.color.YELLOW)
arcade.draw_circle_filled(0,50,77, arcade.color.BLACK)
arcade.draw_circle_filled(500,50,77, arcade.color.BLACK)
arcade.draw_circle_filled(0,50,75, arcade.color.RED)
arcade.draw_circle_filled(500,50,75, arcade.color.RED)
arcade.draw_circle_filled(100,200,60,arcade.color.BLACK)
arcade.draw_circle_filled(400,200,60,arcade.color.BLACK)
arcade.draw_circle_filled(115,215,30,arcade.color.WHITE)
arcade.draw_circle_filled(385,215,30,arcade.color.WHITE)
arcade.draw_ellipse_filled(250,175,30,10,arcade.color.BLACK)
arcade.draw_arc_filled(200,100,100,50,arcade.color.BLACK,190, 350)
arcade.draw_arc_filled(300,100,100,50,arcade.color.BLACK,190, 350)
arcade.draw_arc_filled(200,102,100,50,arcade.color.YELLOW,190, 350)
arcade.draw_arc_filled(300,102,100,50,arcade.color.YELLOW,190, 350)
arcade.draw_circle_filled(250,450, 150, arcade.color.BLACK)
arcade.draw_arc_filled(250,450,280,285,arcade.color.RED,0,180)
arcade.draw_arc_filled(250,450,280,285,arcade.color.WHITE,180,360)
arcade.draw_rectangle_filled(250,450,280,15,arcade.color.BLACK)
arcade.draw_circle_filled(250,450,45,arcade.color.BLACK)
arcade.draw_circle_filled(250,450,32,arcade.color.WHITE)
arcade.finish_render()
arcade.run()

