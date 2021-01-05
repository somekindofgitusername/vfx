import sys

sys.path.append("/opt/houdini/hfs18.5.408/houdini/python2.7libs/")
import hou

def color_nodes():
    ns = hou.selectedNodes()

    class Look:
        """A class for printing formatted text"""

        PURPLE = hou.Color((0.205, 0.101, 0.300))
        RED = hou.Color((1.0, 0.0, 0.0))
        BLACK = hou.Color((0.0, 0.0, 0.0))
        WHITE = hou.Color((1.0, 1.0, 1.0))

        GREY1 = hou.Color((0.1, 0.1, 0.1))
        GREY2 = hou.Color((0.2, 0.2, 0.2))
        GREY5 = hou.Color((0.5, 0.5, 0.5))
        GREY8 = hou.Color((0.8, 0.8, 0.8))

        YELLOW = hou.Color((0.5, 0.5, 0.0))
        ORANGE = hou.Color((0.7, 0.29, 0.0))
        GREEN = hou.Color((0.087, 0.383, 0.1515)

        LIGHTBLUE = hou.Color((0.0, 0.5, 0.5))    
        BLUE = hou.Color((0.0, 0.18, 0.5))

        BEIGE=hou.Color((0.3, 0.1875, 0.075))
        PINKL=hou.Color((0.956, 0.172, 1.0)
        
        TILTED='tilted'
        RECT='rect'
        BONE='bone'
        BULGE='bulge'
        BULGED='bulge_down'
        BURST='burst'
        CIRCLE='circle'
        SQUARE='squared'
        TRAPD='trapezoid_down'

        
    d={  "box": [Look.GREEN, LOOK.rect]
        ,"attribwrangle": [Look.PURPLE, Look.SQUARE]
        , "object_merge": [Look.BLACK, Look.TRAPD]
        ,"null": [Look.BLACK, Look.CIRCLE]
        }


    for n in ns:
        node = n.type().name()
        data = d.get(node)
        n.setColor(data[0])
        n.setUserData("nodeshape", data[1] )
