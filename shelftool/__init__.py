# init file

import sys

try:
    import hou
except:
    sys.path.append("/opt/houdini/hfs18.5.408/houdini/python2.7libs/")
    import hou

from .omerge import omerge
from .renderseq import renderseq
from .colorsnodes import color_nodes