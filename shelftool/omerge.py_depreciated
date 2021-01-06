# hou shelftool
# select node and run script
# a filemergenode with selected node as input appears
# suggested shortcut F1

ns = hou.selectedNodes()
for n in ns:

    parent_path = n.parent().path()
    on = hou.node(parent_path)
    nn = "omerge_" + n.name()

    nt = "object_merge"
    omerge = on.createNode(nt, nn)
    omerge.setPosition(n.position())

    pdic = {"objpath1": omerge.relativePathTo(n)}

    omerge.setParms(pdic)
    black = hou.Color((0.1, 0.1, 0.1))
    omerge.setCurrent(True, True)

    omerge.setColor(black)
    omerge.setDisplayFlag(True)
