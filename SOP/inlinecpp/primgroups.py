node = hou.pwd()
geo = node.geometry()

import inlinecpp

mymodule = inlinecpp.createLibrary(
    name="cpp_marc_library_primsC",
    includes="""
    #include <UT/UT_String.h>
    #include <GU/GU_Detail.h>
    #include <GA/GA_AttributeRef.h>
    #include <GEO/GEO_Primitive.h>
    #include <iostream>
    """,
    function_sources=[
        """
void primInGroup(GU_Detail *gdp)
{
        using namespace std;
        GA_PrimitiveGroup*              grp;

 // Loop over Groups and create group attribute
        GA_FOR_ALL_PRIMGROUPS(gdp, grp)
        {
            UT_String groupname = grp->getName();

            // Create group attribute
            GA_RWAttributeRef           grpAtt  = gdp->findIntTuple(GA_ATTRIB_PRIMITIVE, groupname,1);
            if (!grpAtt.isValid())
                {
                        grpAtt = gdp->addIntTuple(GA_ATTRIB_PRIMITIVE, groupname,1);            
                } 

                GA_RWHandleI grpatthandle(grpAtt.getAttribute());

                // Loop over prims and set attribute value
                GEO_Primitive *prim;
                cout << "blah"<<endl;
                GA_FOR_ALL_PRIMITIVES(gdp, prim)
                    {
                        GA_Offset     primOff = prim->getMapOffset();
                        //cout << "blih "<< primOff << ": " << grp->containsOffset(primOff) << endl;
                        if (grp->containsOffset(primOff)){    grpatthandle.set(primOff, 1);    }
                    } // For all prim offsets  

        } // For all primgroups


} // inGroup()
"""
    ],
)

mymodule.primInGroup(hou.pwd().geometry())
