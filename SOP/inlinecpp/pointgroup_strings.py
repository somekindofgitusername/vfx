node = hou.pwd()
geo = node.geometry()

import inlinecpp

mymodule = inlinecpp.createLibrary(
    name="cpp_marc_library_points_str",
    includes="""
    #include <UT/UT_String.h>
    #include <GU/GU_Detail.h>
    #include <GA/GA_AttributeRef.h>
    #include <iostream>
    #include <string>
    #include <typeinfo> 
    """,
    function_sources=[
        """
void pointStringGroup(GU_Detail *gdp)
{
    using namespace std;
        GA_PointGroup*              grp;

        // Loop over Groups and create group attribute
        GA_FOR_ALL_POINTGROUPS(gdp, grp)
        {
                const UT_String groupname = grp->getName();
                const char * attname = "string_groups";
       
                // Create group attribute
                GA_RWAttributeRef           grpAtt  = gdp->findStringTuple(GA_ATTRIB_POINT, attname,1);
                if (!grpAtt.isValid())
                    {
                            grpAtt = gdp->addStringTuple(GA_ATTRIB_POINT, attname,1);           
                    } 

                GA_RWHandleS grpatthandle( grpAtt.getAttribute() );
                //cout << typeid(grpatthandle(grpatthandle).name();

                // Loop over points and set attribute value
                GA_Offset  ptOff;
                UT_String newname = groupname;
                GA_FOR_ALL_PTOFF(gdp, ptOff)
                {

                    if (grp->containsOffset(ptOff))
                    {    
                        //cout << ptOff << ": groupname " << groupname << endl;

                        UT_String oldname = grpatthandle.get(ptOff);
                        if (oldname.length() > 0)
                            {
                                //cout << "\toldname " << oldname << endl;
                                //cout << "\tnewname " << newname << endl;
                                newname = groupname;
                                newname.append(", ");
                                newname.append(oldname);
                                //cout << "\tnewname " << newname << endl;

                            }

                        grpatthandle.set(ptOff, newname );  
                    }

                } // For all point offsets     

        } // For all pointgroups

} // inGroup()
"""
    ],
)

mymodule.pointStringGroup(hou.pwd().geometry())
