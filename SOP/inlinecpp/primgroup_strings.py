node = hou.pwd()
geo = node.geometry()

import inlinecpp

mymodule = inlinecpp.createLibrary(
    name="cpp_marc_library_prims_string",
    includes="""
    #include <UT/UT_String.h>
    #include <GU/GU_Detail.h>
    #include <GA/GA_AttributeRef.h>
    #include <GEO/GEO_Primitive.h>
    #include <iostream>
    #include <string>
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
            const char * attname = "string_groups";
            // Create group attribute
                
            GA_RWAttributeRef grpAtt = gdp->findStringTuple(GA_ATTRIB_PRIMITIVE, attname,1);
                if (!grpAtt.isValid())
                    {
                            grpAtt = gdp->addStringTuple(GA_ATTRIB_PRIMITIVE, attname,1);           
                    } 
            GA_RWHandleS grpatthandle( grpAtt.getAttribute() );
                
            GEO_Primitive *prim;
            UT_String newname = groupname;
            GA_FOR_ALL_PRIMITIVES(gdp, prim)
            {
                GA_Offset       primOff = prim->getMapOffset();
                if (grp->containsOffset(primOff))
                {
                    UT_String       oldname = grpatthandle.get(primOff);
                    if (oldname.length() > 0)
                                {
                                    newname = groupname;
                                    newname.append(", ");
                                    newname.append(oldname);
                                }
    
                    grpatthandle.set(primOff, newname );
                }// inf contains offset
            } // for all primitives


        } // For all primgroups

} // inGroup()
"""
    ],
)

mymodule.primInGroup(hou.pwd().geometry())
