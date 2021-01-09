# for use as a houdini shelf tool
# increments and saves a file

try:
    import hou
except:
    houPyPath = "/opt/houdini/hfs18.5.408/houdini/python2.7libs/"
    sys.path.append(houPyPath)
    import hou


def upsave():
    print("\n====================\n")
    print("current filename ", hou.hipFile.basename())
    print(" ... upversion save ...")
    hou.hipFile.saveAndIncrementFileName()
    print("current filename ", hou.hipFile.basename())
    print("\n---------------------\n")
