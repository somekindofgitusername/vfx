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
// This function creates a point attribute called "string_groups" that stores the names of all of the point groups
// that a given point belongs to, as a comma-separated string.
void pointStringGroup(GU_Detail *gdp)
{
    // Use the GA_PointGroup iterator to loop over all of the point groups in the detail object.
    GA_PointGroup* grp;
    GA_FOR_ALL_POINTGROUPS(gdp, grp)
    {
        // Get the name of the current point group.
        const UT_String groupname = grp->getName();

        // Set the name of the point attribute to be created or modified.
        const char* attname = "string_groups";

        // Check if the "string_groups" attribute already exists. If not, create it.
        GA_RWAttributeRef grpAtt = gdp->findStringTuple(GA_ATTRIB_POINT, attname, 1);
        if (!grpAtt.isValid())
        {
            grpAtt = gdp->addStringTuple(GA_ATTRIB_POINT, attname, 1);
        }

        // Create a handle to the "string_groups" attribute, to read and write its values.
        GA_RWHandleS grpatthandle(grpAtt.getAttribute());

        // Use the GA_Offset iterator to loop over all of the points in the detail object.
        GA_Offset ptOff;
        GA_FOR_ALL_PTOFF(gdp, ptOff)
        {
            // Check if the current point belongs to the current point group.
            if (grp->containsOffset(ptOff))
            {
                // Get the current value of the "string_groups" attribute for the current point.
                UT_String oldname = grpatthandle.get(ptOff);

                // Initialize the new value of the attribute to be the name of the current point group.
                UT_String newname = groupname;

                // If the old value of the attribute is not an empty string, append it to the new value, separated by a comma and a space.
                if (oldname.length() > 0)
                {
                    newname.append(", ");
                    newname.append(oldname);
                }

                // Set the new value of the "string_groups" attribute for the current point.
                grpatthandle.set(ptOff, newname);
            }
        }
    }
}



"""
    ],
)

mymodule.pointStringGroup(hou.pwd().geometry())
