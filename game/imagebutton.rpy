init python:

    # Create a variable to keep track of whether we're in a conversation
    global jump_lock
    jump_lock = 0

    # Only jump to the label if the lock is 0 (false), indicating we're
    # not already in a conversattion.
    def locked_jump(jump_label):
        global jump_lock
        if jump_lock == 0:
            jump_lock = 1
            renpy.jump(jump_label)
            # After the conversation at jump_label is finished, we'll come
            # back to this point and set jump_lock to 0, allowing jumps again.
            jump_lock = 0

    # Helper function for clearing the lock, if u need it
    def clear_lock():
        global jump_lock
        jump_lock = 0

    # No need for this junk no more
    # def jump(jump_label):
    #     renpy.jump(jump_label)




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


screen bedroom():

    imagebutton:
        xpos 0
        ypos 360
        auto 'gui/left_%s.png'
        