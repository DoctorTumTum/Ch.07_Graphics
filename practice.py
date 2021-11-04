import arcade
SW=600
SH=400

arcade.open_window(SW, SH, "star wars art", True)
arcade.set_background_color(arcade.color.CARIBBEAN_GREEN)
arcade.start_render()
#drawing commands
arcade.draw_lrtb_rectangle_filled(200,400,300,200, arcade.color.AFRICAN_VIOLET)
arcade.draw_rectangle_filled( 300, 200, 50, 50,(255, 207, 241, 175), 45)
arcade.draw_point(300,200,(0,0,0),10)
arcade.draw_line(300,30,300,330,arcade.color.PEAR,7)
arcade.draw_circle_filled(300,290,25,arcade.color.BULGARIAN_ROSE)
arcade.finish_render()
arcade.run()
