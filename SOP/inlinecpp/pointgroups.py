## To Be Reviewed


node = hou.pwd()
geo = node.geometry()

import inlinecpp

mymodule = inlinecpp.createLibrary(
    name="cpp_marc_library_points",
    includes="""
    #include <UT/UT_String.h>
    #include <GU/GU_Detail.h>
    #include <GA/GA_AttributeRef.h>
    """,
    function_sources=[
        """
void pointsInGroup(GU_Detail *gdp)
{
        GA_PointGroup*              grp;

        // Loop over Groups and create group attribute
        GA_FOR_ALL_POINTGROUPS(gdp, grp)
        {
                UT_String groupname = grp->getName();
       
                // Create group attribute
                GA_RWAttributeRef           grpAtt  = gdp->findIntTuple(GA_ATTRIB_POINT, groupname,1);
                if (!grpAtt.isValid())
                    {
                            grpAtt = gdp->addIntTuple(GA_ATTRIB_POINT, groupname,1);            
                    } 

                GA_RWHandleI grpatthandle(grpAtt.getAttribute());

                // Loop over points and set attribute value
                GA_Offset  ptOff;
                GA_FOR_ALL_PTOFF(gdp, ptOff)
                {
                    if (grp->containsOffset(ptOff)){    grpatthandle.set(ptOff, 1);    }
                } // For all point offsets     

        } // For all pointgroups

} // inGroup()
"""
    ],
)

mymodule.pointsInGroup(hou.pwd().geometry())
