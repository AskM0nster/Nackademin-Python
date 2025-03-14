
#Creates the button to turn on the plugin and runs the custom_menu function from interface script when pressed
def initializePlugin(obj):
    print('Menu is loaded')
    from interface import custom_menu
    custom_menu()

#Removes the custom menu when the plugin is disabled
def uninitializePlugin(obj):
    from maya import cmds
    menu_name = 'darkspear'
    if cmds.menu(menu_name, exists = True):
        cmds.deleteUI(menu_name)
    print('Menu removed')
