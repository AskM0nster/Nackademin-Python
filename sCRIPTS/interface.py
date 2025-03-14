from maya import cmds

#Creates the custom_menu function
def custom_menu():
    menu_name = 'darkspear'

    #Deletes duplicate menu if it exists
    if cmds.menu(menu_name, exists=True):
        cmds.deleteUI(menu_name)

    #Creates the custom menu
    custom_menu = cmds.menu(menu_name, parent='MayaWindow', label="Taz'dingo", tearOff=False)

    #Creates the button in the menu and runs the window when pressed
    cmds.menuItem(parent=custom_menu, label='UV unfold', c="import importlib; import window; importlib.reload(window); window.popUP()")
custom_menu()