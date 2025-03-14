#Creates a function to make camera based UV and initialise 3D cut and sew tool
def preparation():
    from maya import mel, cmds

    # 1)turns on UV editing mode
    mel.eval('workspaceLayoutManager -setCurrent "UV Editing";')

    # Gets the selected object(s) as faces
    cmds.selectMode(component=True)
    mel.eval('SelectAll;')
    goose = cmds.ls(sl=True)

    # 2)Create -> Camera based
    mel.eval(f'polyProjection -type Planar -md p  -constructionHistory 1  "{goose[0]}";')

    # 3)3D cut and sew tool
    mel.eval('setToolTo superCutUVContext;')