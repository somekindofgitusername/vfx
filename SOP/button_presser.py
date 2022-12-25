# Presses buttons in a folder parameter
# Setup specific, not a general tool.

# Get the current node and its geometry
node = hou.pwd()
geo = node.geometry()

# Print a separator to indicate the start of the script
print("\n= Button presser starts ===========================\n")

# Get the name of the folder parameter and the button parameter
folder_name = "folder0"
button_name = "button"

# Evaluate the folder parameter to get a list of nodes
nodes = node.parm(folder_name).eval()

# Get a list of spare parameters whose names contain "node"
multi_parms = [p.name() for p in node.spareParms() if "node" in p.name()]

# Print the value of the "wedge" parameter and the list of spare parameters
print(" Wedge :", node.parm("wedge").eval(), "\n")
print(" parms in folder0: ", multi_parms)

# Iterate over the spare parameters
for e, parm in enumerate(multi_parms):
    try:
        # Get the name of the node specified by the current spare parameter
        n = node.parm(parm).eval()
        # Print the name of the node and the button parameter
        print("\tNode:\t", n)
        print("\tButton:\t", button_name)
        # Press the button on the node
        print("\tPress: \t", hou.node(n).parm(button_name).pressButton(), "\n\t--")
    except Exception as e:
        # Print any errors that occur
        print("error ", e)

# Print a separator to indicate the end of the script
print("\n= Button presser done =============================")
