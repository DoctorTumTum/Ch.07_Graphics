'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
import arcade
SL = 494
SH = 250

BH = 140.01
BL = 197.6
STHOR = 14.04
STHBT = 14.04
STVT =16.38
STVBT = 16.38
STDI = 16.016
STH = 19.994
ZE = 19.994
ZERO = 0
HI = 20
BI = 12
arcade.open_window(SL, SH, "star wars art",True)
arcade.set_background_color(arcade.color.RED)
arcade.start_render()
for i in range(7):
    arcade.draw_line(0,ZE,SL,ZE,(255,255,255),STH)
    ZE+=2*(STH)
arcade.draw_lrtb_rectangle_filled(0,BL,SH,SH-BH+1,arcade.color.BLUE)
for x in range(5):
    for i in range(6):
        arcade.draw_text("*", ZERO+16.38, SH-STVT-HI, arcade.color.WHITE, 25)
        ZERO+=30
    HI+=2*STVBT-5
    ZERO = 0
for i in range(4):
    for i in range(5):
        arcade.draw_text("*", ZERO+2*STVT, SH-2*STVBT-BI-5, arcade.color.WHITE, 25)
        ZERO+=30
    BI += 2 * STVBT - 5
    ZERO = 0
arcade.finish_render()
arcade.run()