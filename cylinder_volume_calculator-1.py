# Created by Jenny Trac
# Created on Nov 7 2017
# Program calculates volume of a cylinder

import ui

def calculate_volume(radius, height):
    # calculates volume
    
    pi = 3.14
    
    if radius < 0 or height < 0:
        return "-1"
    else:
        volume = 2 * pi * radius**2 * height
        return "Volume: " + str(volume) + " cm^3"

def calculate_touch_up_inside(sender):
    # button to calculate
    
    # input
    radius_input = float(view['radius_textfield'].text)
    height_input = float(view['height_textfield'].text)

    # process
    volume_answer = calculate_volume(radius_input, height_input)

    # output
    view['answer_label'].text = volume_answer

view = ui.load_view()
view.present('sheet')
