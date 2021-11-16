#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
SW = 0
SH = 0

arcade.open_window(500, 400, "star wars art")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

for i in range(0,501,20):
    arcade.draw_line(SW, SH, SW+500, SH, (arcade.color.BLACK),1)
    SH+=20
SH = 0
for i in range(0,501,20):
    arcade.draw_line(SW, SH, SW, SH+500, (arcade.color.BLACK),1)
    SW+=20
arcade.draw_lrtb_rectangle_filled(20,80,380,360,(arcade.color.PHLOX))
arcade.draw_circle_filled(250,200,40,(arcade.color.WISTERIA))
arcade.draw_arc_filled(400,320,100,100,(arcade.color.YELLOW), 30, 330 )
arcade.draw_line(80,20,120,60,(arcade.color.BLUE))
arcade.draw_rectangle_filled(200,260,17,37,(arcade.color.BLUSH),45,)
arcade.draw_ellipse_filled(120,100,120,40,(arcade.color.AMBER))
arcade.draw_point(460,10,(arcade.color.RED),5)
arcade.draw_text("I love you. I know", 20, 160, arcade.color.BRICK_RED, 21)
arcade.finish_render()
arcade.run()