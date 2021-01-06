# hou tool to render non-contigous sequences
# Highly job specific so not recommended for general use

try:
    import hou
except:
    sys.path.append("/opt/houdini/hfs18.5.408/houdini/python2.7libs/")
    import hou


def renderseq():
    """Loop over a string containing frame numbers
    and render each frame while checking if it exists in the render folder.
    Various scene relevant pieces of information are stored as file attribute.
    """
    import os.path
    from os import path
    import time
    import os

    print("\n\n===== renderseq ==================")

    hou.hipFile.save()

    # get string of frames to render
    nums_node = hou.node("/stage/nums")
    frames = map(int, nums_node.parm("nums").eval().split())

    rs_node = hou.selectedNodes()[0]
    image_path = rs_node.parm("picture").eval()
    n = rs_node
    xs = str(rs_node.parmTuple(n.path() + "/resolution")[0].eval())
    ys = str(rs_node.parmTuple(n.path() + "/resolution")[0].eval())
    imagesize = xs + "_x_" + ys

    print("frames: ", str(frames))
    print("redshift render node (rsNode): ", rs_node)

    for f in frames:
        print("\n ... frame ", str(f))
        hou.setFrame(f)
        image_path = rs_node.parm("picture").eval()

        if path.exists(image_path):
            print(image_path, " exists")

        else:
            print(image_path, " does not exist")

            rs_node.parm("execute").pressButton()
            path_is = path.exists(image_path)
            path_is_not = not path_is

            while path_is_not:
                print(" ... waiting for file ... ", image_path)
                time.sleep(20)
                path_is = path.exists(image_path)
                path_is_not = not path_is
                if path_is:
                    break

            print("\n out of while for path", image_path)

            hipfilename = hou.hipFile.path()
            mycommand = "setfattr -n user.hipfile -v " + hipfilename + " " + image_path
            mycommand2 = (
                "setfattr -n user.frame -v " + str(hou.frame()) + " " + image_path
            )
            mycommand3 = (
                "setfattr -n user.houversion -v "
                + hou.applicationVersionString()
                + " "
                + image_path
            )
            mycommand4 = "setfattr -n user.imagesize -v " + imagesize + " " + image_path
            print("mycommand ", mycommand)
            print("mycommand2 ", mycommand2)
            os.system(mycommand)
            os.system(mycommand2)
            os.system(mycommand3)
            os.system(mycommand4)
            try:
                # some hard coded paths. Beware.
                lut = hou.parm("/obj/cam1/RS_campro_lutFile").eval()
                env = hou.parm("/stage/domelight1/xn__texturefile_0ta").eval()
                dist = (
                    hou.node(
                        hou.parm(
                            "/stage/camera1/xn__karmacameralensshadervop_4fbg"
                        ).eval()
                    )
                    .parm("curv_map")
                    .eval()
                )
                foc = (
                    hou.node(
                        hou.parm(
                            "/stage/camera1/xn__karmacameralensshadervop_4fbg"
                        ).eval()
                    )
                    .parm("focus_map")
                    .eval()
                )
                mycommand5 = "setfattr -n user.lut -v " + lut + " " + image_path
                mycommand6 = "setfattr -n user.env -v " + env + " " + image_path
                mycommand7 = "setfattr -n user.distort -v " + dist + " " + image_path
                mycommand8 = "setfattr -n user.focus -v " + foc + " " + image_path
                os.system(mycommand5)
                os.system(mycommand6)
                os.system(mycommand7)
                os.system(mycommand8)
            except:
                pass

    os.system("shutdown")
    # os.system('systemctl suspend')
