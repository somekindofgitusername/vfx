# for use as a houdini shelf tool
# upsaves the file


def upsave():
    print("\n====================\n")
    print("current filename ", hou.hipFile.basename())
    print(" ... upversion save ...")
    hou.hipFile.saveAndIncrementFileName()
    print("current filename ", hou.hipFile.basename())
    print("\n---------------------\n")
