# for use as a houdini shelf tool
# upsaves the file
try:
    import hou
except:
    sys.path.append("/opt/houdini/hfs18.5.408/houdini/python2.7libs/")
    import hou


def upsave():
    print("\n====================\n")
    print("current filename ", hou.hipFile.basename())
    print(" ... upversion save ...")
    hou.hipFile.saveAndIncrementFileName()
    print("current filename ", hou.hipFile.basename())
    print("\n---------------------\n")
