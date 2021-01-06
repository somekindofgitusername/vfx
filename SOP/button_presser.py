# Presses buttons

node = hou.pwd()
geo = node.geometry()

print "\n= Button presser starts ===========================\n"
print
nodes = node.parm("folder0").eval()
name = "node"
button = node.parm("button").eval()
multiParms = [p.name() for p in node.spareParms() if "node" in p.name()]

print " Wedge :", node.parm("wedge").eval(), "\n"
print " parms in folder0: ", multiParms
print

for e, parm in enumerate(multiParms):
    try:
        n = node.parm(parm).eval()
        print "\tNode:\t", n,
        print "\tButton:\t", button
        print "\tPress: \t", hou.node(n).parm(button).pressButton(), "\n\t--"
    except Exception as e:
        print "error ", e

print "\n= Button presser done ============================="
