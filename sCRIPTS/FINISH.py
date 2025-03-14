#Creates a function to unfold and layout
def unwrap():
    from maya import mel, cmds

    # 1) Chooses select tool
    mel.eval('setToolTo selectSuperContext;')

    # Gets the selected object(s)
    goose = cmds.ls(sl=True)

    # Ensures there is at least one object selected
    if goose:
        # 2) Changes edge mode to UV shell mode
        mel.eval(f'doMenuComponentSelection("{goose[0]}", "meshUVShell");')

        # 3) Selects everything (ctrl+shift+A)
        mel.eval("SelectAll;")

        possum = cmds.ls(sl=True)

        # 4) Unfold
        mel.eval(f'u3dUnfold -ite 1 -p 0 -bi 1 -tf 1 -ms 1024 -rs 0 "{possum[0]}";')

        # 5) Layout
        mel.eval(f'u3dLayout -res 2048 -scl 1 -box 0 1 0 1 "{possum[0]}";')
    else:
        print("No object selected.")

