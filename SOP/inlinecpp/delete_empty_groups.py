# deprecated. Houdini now does that automatically.

node = hou.pwd()
geo = node.geometry()

import inlinecpp

mymodule = inlinecpp.createLibrary(
    name="cpp_marc_library_kill",
    includes="""
    #include <GU/GU_Detail.h>
    """,
    function_sources=[
        """
void killEmptyGroup(GU_Detail *gdp)
{

        gdp->destroyAllEmptyGroups();

}
"""
    ],
)

mymodule.killEmptyGroup(hou.pwd().geometry())
