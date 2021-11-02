screen saveload:
    imagebutton:
        hovered
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 650
        auto "gui/mm_load1_%s.png"
        action ShowMenu("load")
    imagebutton:
        hovered
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 650
        auto "gui/mm_save1_%s.png"
        action ShowMenu("save")

