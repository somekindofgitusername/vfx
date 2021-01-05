# hou shelftool
# select node and run script

import sys

sys.path.append("/opt/houdini/hfs18.5.408/houdini/python2.7libs/")
import hou


def color_nodes():
    """Applies standardized look to Houdini nodes.
    Select nodes and run script.
    """    
    ns = hou.selectedNodes()

    class Look:
        """A class for houdini nodes look
        """        

        PURPLE = hou.Color((0.205, 0.101, 0.300))
        LIGHTPURPLE = hou.Color((0.451, 0.369, 0.796))
        RED = hou.Color((1.0, 0.0, 0.0))
        BLACK = hou.Color((0.0, 0.0, 0.0))
        WHITE = hou.Color((1.0, 1.0, 1.0))
        GREY1 = hou.Color((0.1, 0.1, 0.1))
        GREY2 = hou.Color((0.2, 0.2, 0.2))
        GREY5 = hou.Color((0.5, 0.5, 0.5))
        GREY8 = hou.Color((0.8, 0.8, 0.8))
        YELLOW = hou.Color((0.5, 0.5, 0.0))
        ORANGE = hou.Color((0.7, 0.29, 0.0))
        GREEN = hou.Color((0.087, 0.383, 0.1515))
        LIGHTBLUE = hou.Color((0.0, 0.5, 0.5))
        BLUE = hou.Color((0.0, 0.18, 0.5))
        WATERBLUE = hou.Color((0.094, 0.369, 0.690))
        BEIGE = hou.Color((0.3, 0.1875, 0.075))
        PINKL = hou.Color((0.956, 0.172, 1.0))

        TILTED = "tilted"
        RECT = "rect"
        BONE = "bone"
        BULGE = "bulge"
        BULGED = "bulge_down"
        BURST = "burst"
        CIRCLE = "circle"
        NULLS = "null"
        SQUARE = "squared"
        TRAPD = "trapezoid_down"
        TRAPU = "trapezoid_up"

    d = {
        "box": [Look.GREEN, Look.RECT],
        "blast": [Look.RED, Look.RECT],
        "delete": [Look.RED, Look.RECT],
        "attribwrangle": [Look.WATERBLUE, Look.SQUARE],
        "object_merge": [Look.BLACK, Look.TRAPD, Look.GREY2, Look.TRAPU],
        "null": [Look.BLACK, Look.CIRCLE, Look.GREY5, Look.NULLS],
        "dopnet": [Look.LIGHTPURPLE, Look.BURST],
    }

    for n in ns:
        node = n.type().name()
        data = d.get(node)
        n.setColor(data[0])
        n.setUserData("nodeshape", data[1])

        if node == "object_merge":
            print "merge detected"
            paths = [p.name() for p in n.parms() if "objpath" in p.name()]
            pathsEnabled = [p.eval() for p in n.parms() if "enable" in p.name()]
            parmPairs = zip(paths, pathsEnabled)
            activeParm = [p[0] for p in parmPairs if p[1] == 1]
            activePaths = n.parm(activeParm[0]).eval()
            print activePaths
            if "../" in activePaths:
                n.setColor(data[2])
                n.setUserData("nodeshape", data[3])
        if node == "null":
            outputCount = len(n.outputs())
            if outputCount > 0:
                n.setColor(data[2])
                n.setUserData("nodeshape", data[3])