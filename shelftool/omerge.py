
    """hou shelftool to Object merge selected nodes.

 Usage: Left-select node(s) and run script.
 Creates filemergenode(s) with selected node(s) as input.
 
 Absolute and relative paths are automatically filled out.

 Node is named after merged node.

 Suggested shortcut F1
    """

try:
    import hou
except:
    houPyPath = "/opt/houdini/hfs18.5.408/houdini/python2.7libs/"
    sys.path.append(houPyPath)
    import hou


def omerge():
    for n in hou.selectedNodes():
        print("node: ", str(n))

        # Get node data
        node_path = n.path()
        n_pos = n.position()

        # Create object_merge node
        m = n.parent().createNode("object_merge")
        print("node parent: ", n.parent())

        # Calculate object_merge node's position
        offset_y = n.size()[1]
        v2 = hou.Vector2((0, offset_y))
        m_pos = n_pos - 3 * v2
        m.move(m_pos)

        # Set Parms of object_merge node
        parm_dict = {}
        parm_dict["numobj"] = 2
        parm_dict["objpath1"] = node_path
        parm_dict["objpath2"] = m.relativePathTo(n)
        parm_dict["enable2"] = False
        m.setParms(parm_dict)

        name = "_merge_" + n.name()

        # Set Flags on object_merge_node
        m.setName(name, True)
        m.setColor(hou.Color((0, 0, 0)))
        m.setDisplayFlag(True)
        n.setRenderFlag(False)
        m.setCurrent(True, True)