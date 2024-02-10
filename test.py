from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll("Works")
    elif button_b.is_pressed():
        display.scroll("Still Works")
