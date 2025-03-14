#Creates a function which makes a pop up window
def popUP():
    from maya import cmds, mel

    #Creates a layout for the window and opens it when pressed
    show_window = cmds.window(title = 'UV unwrap', width = 200, height = 34)
    cmds.columnLayout(show_window, adjustableColumn=True)
    cmds.showWindow(show_window)

    #Creates buttons and runs the PREPARE and FINISH scripts when pressed
    cmds.button(parent=show_window, label='PREPARE', c='from imp import reload; import PREPARE; reload(PREPARE); PREPARE.preparation()')
    cmds.button(parent=show_window, label='FINISH', c='from imp import reload; import FINISH; reload(FINISH); FINISH.unwrap()')

