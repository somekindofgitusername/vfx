# init file

import sys

sys.path.append("/opt/houdini/hfs18.5.408/houdini/python2.7libs/")
import hou

from .omerge2 import omerge
from .renderseq import renderseq
from .colorsnodes import color_nodes