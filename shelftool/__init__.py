# init file

import sys

try:
    import hou
except:
    houPyPath = "/opt/houdini/hfs18.5.408/houdini/python2.7libs/"
    sys.path.append(houPyPath)
    import hou

from .omerge import omerge
from .renderseq import renderseq
from .colorsnodes import color_nodes