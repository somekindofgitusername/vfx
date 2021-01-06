# Python sop tool
#
# wedge renumbering such that a non-contigous sequence will be made contigous

node = hou.pwd()
geo = node.geometry()

clusterName = "cluster"

# list of existing clusters
clusters = list(set([int(p.attribValue(clusterName)) for p in geo.points()]))

# remap clusters into contigous order starting at 0
dic = {t[1]: t[0] for t in enumerate(clusters)}
print("cluster remap {old_cluster:new_cluster} = ", dic)

[
    p.setAttribValue("cluster", float(dic[p.attribValue("cluster")]))
    for p in geo.points()
]
