# Object merge version2 ------------------------------------------------------------------------------

import sys

sys.path.append("/opt/houdini/hfs18.5.408/houdini/python2.7libs/")
import hou


def omerge():
    # n = hou.selectedNodes()[0]
    for n in hou.selectedNodes():
        print "n: ", (n)
        node_path = n.path()
        n_pos = n.position()
        m = n.parent().createNode("object_merge")
        print "n.parent()", n.parent()
        offset_y = n.size()[1]
        v2 = hou.Vector2((0, offset_y))

        m_pos = n_pos - 3 * v2

        m.move(m_pos)

        parm_dict = {}
        parm_dict["numobj"] = 2
        parm_dict["objpath1"] = node_path
        parm_dict["objpath2"] = m.relativePathTo(n)
        parm_dict["enable2"] = False
        m.setParms(parm_dict)
        name = "_merge"
        m.setName(name, True)
        m.setColor(hou.Color((0, 0, 0)))
        m.setDisplayFlag(True)
        n.setRenderFlag(False)
        m.setCurrent(True, True)