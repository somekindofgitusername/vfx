# hou shelftool
# Object merge selected nodes.
# Usage: Left-select node(s) and run script.
# A filemergenode with selected node(s) as input appears.
# Absolute and relative paths are automatically filled out.
# Node is named after merged node.
# Suggested shortcut F1

try:
    import hou
except:
    houPyPath = "/opt/houdini/hfs18.5.408/houdini/python2.7libs/"
    sys.path.append(houPyPath)
    import hou


def omerge():
    for n in hou.selectedNodes():
        print("node: ", str(n))

        node_path = n.path()
        n_pos = n.position()
        m = n.parent().createNode("object_merge")
        print("node parent: ", n.parent())

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

        name = "_merge_" + n.name()

        m.setName(name, True)
        m.setColor(hou.Color((0, 0, 0)))
        m.setDisplayFlag(True)
        n.setRenderFlag(False)
        m.setCurrent(True, True)