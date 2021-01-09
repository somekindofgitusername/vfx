# hou shelftool
# Left-select node(s) and run script.
# Colors and shapes will be assigned to nodes
# depending on what type they are and certain node settings

import re
import sys

try:
    import hou
except:
    houPyPath = "/opt/houdini/hfs18.5.408/houdini/python2.7libs/"
    sys.path.append(houPyPath)
    import hou


def _find_matches(d, item):
    for k in d:
        if re.match(k, item):
            return d[k]


def color_nodes():
    """Applies standardized look to Houdini nodes.
    Select nodes and run script.
    """
    ns = hou.selectedNodes()

    class Look:
        """A class for houdini nodes look"""

        # colors
        PURPLE = hou.Color((0.205, 0.101, 0.300))
        LIGHTPURPLE = hou.Color((0.451, 0.369, 0.796))
        BORDEAUX = hou.Color((0.384, 0.184, 0.329))
        RED = hou.Color((1.0, 0.0, 0.0))
        BLACK = hou.Color((0.0, 0.0, 0.0))
        WHITE = hou.Color((1.0, 1.0, 1.0))
        GREY1 = hou.Color((0.1, 0.1, 0.1))
        GREY2 = hou.Color((0.2, 0.2, 0.2))
        GREY5 = hou.Color((0.5, 0.5, 0.5))
        GREY8 = hou.Color((0.8, 0.8, 0.8))
        GREYGREEN = hou.Color((0.7, 0.8, 0.7))
        YELLOW = hou.Color((0.5, 0.5, 0.0))
        ORANGE = hou.Color((0.7, 0.29, 0.0))
        GREEN = hou.Color((0.087, 0.383, 0.1515))
        LIGHTBLUE = hou.Color((0.0, 0.5, 0.5))
        BLUE = hou.Color((0.0, 0.18, 0.5))
        WATERBLUE = hou.Color((0.094, 0.369, 0.690))
        BEIGE = hou.Color((0.3, 0.1875, 0.075))
        PINKL = hou.Color((0.956, 0.172, 1.0))
        PEACH = hou.Color((0.8, 0.3, 0.3))

        # userData("nodeshape")
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
        LIGHT = "light"
        SLASH = "slash"
        STAR = "star"
        OVAL = "oval"
        CLOUD = "cloud"
        SLASH = "slash"
        NONE = ""

    d = {
        "box": [Look.GREEN, Look.RECT],
        "blast": [Look.RED, Look.RECT],
        "delete": [Look.RED, Look.RECT],
        "attribwrangle": [Look.WATERBLUE, Look.SQUARE],
        "deformationwrangle": [Look.WATERBLUE, Look.SQUARE],
        "volumewrangle": [Look.WHITE, Look.SQUARE],
        "object_merge": [Look.BLACK, Look.TRAPD, Look.GREY2, Look.TRAPU],
        "null": [Look.BLACK, Look.CIRCLE, Look.GREY5, Look.NULLS, Look.BORDEAUX],
        "dopnet": [Look.LIGHTPURPLE, Look.STAR],
        "file*": [Look.PEACH, Look.SLASH],
        "vdb*": [Look.WHITE, Look.CLOUD],
        "group*": [Look.GREYGREEN, Look.NONE],
    }

    for n in ns:
        node = n.type().name()
        data = _find_matches(d, node)

        try:
            n.setColor(data[0])
            n.setUserData("nodeshape", data[1])
        except:
            pass  # node may not be listed

        # Change according to absolute or relative paths
        if node == "object_merge":
            paths = [p.name() for p in n.parms() if "objpath" in p.name()]
            pathsEnabled = [p.eval() for p in n.parms() if "enable" in p.name()]
            parmPairs = zip(paths, pathsEnabled)
            activeParm = [p[0] for p in parmPairs if p[1] == 1]
            activePaths = n.parm(activeParm[0]).eval()
            if "../" in activePaths:
                n.setColor(data[2])
                n.setUserData("nodeshape", data[3])

        # Change if outputwire is present in null sop
        if node == "null":
            outputCount = len(n.outputs())
            if outputCount > 0:
                n.setColor(data[2])
                n.setUserData("nodeshape", data[3])
            if "OUT" in n.name():
                n.setColor(data[4])
