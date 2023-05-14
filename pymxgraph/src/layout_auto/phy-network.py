import sys
import os
sys.path.append("../")
import mxgraph.mxgraph 
import xml.etree.ElementTree as XET
import igraph as ig


def phy_network_drawio():
    g2 =  mxgraph.mxgraph.MxGraph(diagram_id='phy-network')
    parent = g2.create_group_cell(cell_id='1', parent=g2.root)
    #sw_style = { 'shape': "rectangle", 'strokeWidth' :'3','whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    sw_style = { 'shape': "rectangle", 'strokeWidth' :'3','whiteSpace': 'wrap', 'html': '1'  }

    hostname_A = g2.insert_vertex(parent=parent, value="hostname_A", x=200, y=50, width=160, height=60, style=sw_style, relative=False)
    hostname_B = g2.insert_vertex(parent=parent, value="hostname_B", x=800, y=50, width=160, height=60, style=sw_style, relative=False)

    hostname_A1 = g2.insert_vertex(parent=parent, value="hostname_A1", x= 50, y=400, width=160, height=60, style=sw_style, relative=False)
    hostname_A2 = g2.insert_vertex(parent=parent, value="hostname_A2", x=350, y=400, width=160, height=60, style=sw_style, relative=False)

    hostname_B1 = g2.insert_vertex(parent=parent, value="hostname_B1", x=550, y=400, width=160, height=60, style=sw_style, relative=False)
    hostname_B2 = g2.insert_vertex(parent=parent, value="hostname_B2", x=750, y=400, width=160, height=60, style=sw_style, relative=False)
    hostname_B3 = g2.insert_vertex(parent=parent, value="hostname_B3", x=950, y=400, width=160, height=60, style=sw_style, relative=False)
    hostname_B4 = g2.insert_vertex(parent=parent, value="hostname_B4", x=1150, y=400, width=160, height=60, style=sw_style, relative=False)

    hostname_A21 = g2.insert_vertex(parent=parent, value="hostname_A21", x=350, y=600, width=160, height=60, style=sw_style, relative=False)
    hostname_A22 = g2.insert_vertex(parent=parent, value="hostname_A22", x= 50, y=600, width=160, height=60, style=sw_style, relative=False)

    hostname_B31 = g2.insert_vertex(parent=parent, value="hostname_B31", x=950, y=600, width=160, height=60, style=sw_style, relative=False)

    ## straight
    edge_style1 = { 'edgeStyle': 'none', 'endArrow': 'none','curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    edge_style4 = { 'edgeStyle': 'none', 'strokeWidth' :'3', 'startArrow': 'box','endArrow': 'box','curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ## curved
    edge_style2 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ## bending
    #edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle', 'rounded': '0', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}
    edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle',  'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}

    edge = g2.insert_edge(parent=parent, source=hostname_A, target=hostname_B, value="TEST", style=edge_style4)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_A, target=hostname_A1, value="TEST", style=edge_style1)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_A, target=hostname_A2, value="TEST", style=edge_style1)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_B, target=hostname_B1, value="TEST", style=edge_style1)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_B, target=hostname_B2, value="TEST", style=edge_style1)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_B, target=hostname_B3, value="TEST", style=edge_style1)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_B, target=hostname_B4, value="TEST", style=edge_style1)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_A2, target=hostname_A21, value="TEST", style=edge_style1)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_B3, target=hostname_B31, value="TEST", style=edge_style1)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=hostname_A22, target=hostname_B4, value="TEST", style=edge_style3)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )


    #style1 = { 'shape': "ellipse", 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    #subnet1 = g2.insert_vertex(parent=parent, value="10.100.2.0 /24", x=100, y=200, width=180, height=50, style=style1, relative=False)
    #subnet2 = g2.insert_vertex(parent=parent, value="10.100.3.0 /24", x=600, y=200, width=180, height=50, style=style1, relative=False)
    #subnet3 = g2.insert_vertex(parent=parent, value="10.100.3.0 /24", x=100, y=600, width=180, height=50, style=style1, relative=False)
    #subnet4 = g2.insert_vertex(parent=parent, value="10.100.3.0 /24", x=400, y=600, width=180, height=50, style=style1, relative=False)
    #subnet5 = g2.insert_vertex(parent=parent, value="10.100.3.0 /24", x=700, y=600, width=180, height=50, style=style1, relative=False)

    ### straight
    #edge_style1 = { 'edgeStyle': 'none', 'endArrow': 'none','curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ### curved
    #edge_style2 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ### bending
    #edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}

    #edge = g2.insert_edge(parent=parent, source=router1, target=subnet1,  style=edge_style1)
    #g2.set_edge_src_label(edge, "100.1", style={'labelBackgroundColor' : "#ffffff"} )
    #edge = g2.insert_edge(parent=parent, source=router1, target=subnet2,  style=edge_style1)
    #g2.set_edge_src_label(edge, "200.1", style={'labelBackgroundColor' : "#ffffff"} )

    #edge = g2.insert_edge(parent=parent, source=router2, target=subnet2,  style=edge_style1)
    #g2.set_edge_src_label(edge, "200.254", style={'labelBackgroundColor' : "#ffffff"} )

    #edge = g2.insert_edge(parent=parent, source=router2, target=subnet3,  style=edge_style1)
    #g2.set_edge_src_label(edge, "300.1", style={'labelBackgroundColor' : "#ffffff"} )
    #edge = g2.insert_edge(parent=parent, source=router2, target=subnet4,  style=edge_style1)
    #g2.set_edge_src_label(edge, "400.1", style={'labelBackgroundColor' : "#ffffff"} )
    #edge = g2.insert_edge(parent=parent, source=router2, target=subnet5,  style=edge_style1)
    #g2.set_edge_src_label(edge, "500.1", style={'labelBackgroundColor' : "#ffffff"} )

    return g2

def layoutprint(layout):
    print("+++++++++++++++++++++++++++")
    print(layout.coords)
    print("-")
    print(layout.boundaries())
    print("-")
    print(layout.centroid())
    print("-")

    for e in layout:
        print(e)
    print("-")

#def autolayout(vlist, elist):
def autolayout(vlist, elist, scale, margin):
    #
    # https://qiita.com/scapegoat_11_/items/d99cbcfea053d9fcd8d2
    #
    vertices = []
    edges = []

    for v in vlist:
        vertices.append( v[0])

    for e in elist:
        source_hostname = e[0]
        target_hostname = e[2]
        s_index = vertices.index(source_hostname)
        t_index = vertices.index(target_hostname)
        edges.append((s_index,t_index))

    #print(vertices)
    #print(edges)
    g = ig.Graph(vertex_attrs={"name": vertices}, edges=edges, directed=False)
    #print(g.vs["name"])
    #for v in g.vs:
    #    print(v.index, end=" ")
    #    print(v.attributes() )

    #layout = g.layout_kamada_kawai()
    #layout = g.layout(layout='auto')
    #layout = g.layout(layout='kk')
    #layout = g.layout(layout='fr')
    #layout = g.layout(layout='rt')
    layout = g.layout(layout='tree')

    # https://python.igraph.org/en/stable/api/igraph.layout.Layout.html
    # https://igraph.org/python/tutorial/0.9.6/visualisation.html
    #

    #layout.scale(200)
    layout.scale(scale)

    #layoutprint(layout)
    print(layout.boundaries())
    top_left_point     = layout.boundaries()[0]
    bottom_right_point = layout.boundaries()[1]

    tx = 0
    if top_left_point[0] < 0:
        tx = -top_left_point[0] + margin
    elif top_left_point[0] <= margin:
        tx = margin - top_left_point[0]
    else:
        tx = 0
    ty = 0
    if top_left_point[1] < 0:
        ty = -top_left_point[1] + margin
    elif top_left_point[1] <= margin:
        ty = margin - top_left_point[1]
    else:
        ty = 0

    layout.translate([tx, ty])
    #layout.translate([600, 100])
    #layoutprint(layout)
    print(layout.boundaries())

    for i,l in enumerate(layout):
        #print(i,l)
        vlist[i][1] = l[0]  # set x
        vlist[i][2] = l[1]  # set x

def lag_link_check(g):
    def complink(cells, cell):
        edges = []
        for cell_ in cells:
            if g.cells[cell].edge:
               if cell_ != cell:
                  if cells[cell_].source == cells[cell].source and cells[cell_].target == cells[cell].target and cells[cell_].style == cells[cell].style:
                        edges.append(cell_)
        return edges

    for cell in g.cells:
        if g.cells[cell].edge:
            print(cell)
            edges = complink(g.cells, cell)
            if len(edges) > 0:
                print(edges)

        #geo = g.cells[cell].geometry
        #if geo != None:
        #    print(geo.x)
    pass

def phy_network_layout():
    print("phy_network_layout():")
    
    vlist = [                 # x    y   w   h
            ["hostname_A",   200,   50, 160, 60],
            ["hostname_B",   800,   50, 160, 60],

            ["hostname_A1",   50,  400, 160, 60],
            ["hostname_A2",  350,  400, 160, 60],

            ["hostname_B1",  550,  400, 160, 60],
            ["hostname_B2",  750,  400, 160, 60],
            ["hostname_B3",  950,  400, 160, 60],
            ["hostname_B4", 1150,  400, 160, 60],
            ["hostname_B5", 1150,  400, 160, 60],

            ["hostname_A21", 350,  600, 160, 60],
            ["hostname_A22",  50,  600, 160, 60],

            ["hostname_B31", 950,  600, 160, 60]
            ]

    elist = [
            ["hostname_A",  "Gi0/0/1","hostname_B",  "Gi0/0/1", True, "TEST"],
            ["hostname_A",  "Gi0/0/2","hostname_A1", "Gi0/0/1", False,"TEST"],
            ["hostname_A",  "Gi0/0/X","hostname_A1", "Gi0/0/X", False,"TEST"], # duble link
            ["hostname_A",  "Gi0/0/3","hostname_A2", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/1","hostname_B1", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/2","hostname_B2", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/3","hostname_B3", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/4","hostname_B4", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/4","hostname_B5", "Gi0/0/1", False,"TEST"],
            ["hostname_A2", "Gi0/0/2","hostname_A21","Gi0/0/1", False,"TEST"],
            ["hostname_B3", "Gi0/0/2","hostname_B31","Gi0/0/1", False,"TEST"],
            ["hostname_A22","Gi0/0/1","hostname_B4", "Gi0/0/2", False,"TEST"],
            ["hostname_A22","Gi0/0/2","hostname_A1", "Gi0/0/2", True, "TEST"]
            ]

    geopath =  "." + "test.drawio" + "_" + "phy-network-layout" + ".geometry"

    #autolayout(vlist, elist)
    autolayout(vlist, elist, 200, 100)   # scale = 200  margin = 100

    if os.path.isfile(geopath):
        print("geometry exist!!!")
        #import_geometry(vlist, geopath)
        f = open(geopath, "r")
        lines = f.readlines()
        f.close()
        geometry_dict = {}

        for l in lines:
            para = l.split(",")
            hostname = para[0]
            x        = para[1]
            y        = para[2]
            geometry_dict[hostname] = (x, y)

        #print(geometry_dict)
        for v in vlist:
            hostname =v[0]
            if hostname in geometry_dict.keys():
              v[1] =  geometry_dict[hostname][0]
              v[2] =  geometry_dict[hostname][1]

        for v in vlist:
            print(v)
        #sys.exit()

    vdict = {}

    g2 =  mxgraph.mxgraph.MxGraph(diagram_id='phy-network-layout')
    parent = g2.create_group_cell(cell_id='1', parent=g2.root)
    #sw_style = { 'shape': "rectangle", 'strokeWidth' :'3','whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    sw_style = { 'shape': "rectangle", 'strokeWidth' :'3','whiteSpace': 'wrap', 'html': '1'  }
    ## straight
    edge_style1 = { 'edgeStyle': 'none', 'endArrow': 'none','curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    edge_style4 = { 'edgeStyle': 'none', 'strokeWidth' :'3', 'startArrow': 'box','endArrow': 'box','curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }

    for v in vlist:
        hostname = v[0]
        x        = v[1]
        y        = v[2]
        w        = v[3]
        h        = v[4]
        #print(hostname)
        vt = g2.insert_vertex(parent=parent, value=hostname, x=x , y=y, width=w , height=h , vertex_type=mxgraph.mxgraph.Vertex.NODE ,style=sw_style, relative=False)
        vdict[hostname] = vt
    #print(vdict)
    for e in elist:
        source_hostname = e[0]
        source_port     = e[1]
        target_hostname = e[2]
        target_port     = e[3]
        photo           = e[4]
        label           = e[5]
        if photo:
           edge = g2.insert_edge(parent=parent, source=vdict[source_hostname], target=vdict[target_hostname], value=label, style=edge_style4)
           g2.set_edge_src_label(edge, source_port, style={'labelBackgroundColor' : "#ffffff"} )
           g2.set_edge_dst_label(edge, target_port, style={'labelBackgroundColor' : "#ffffff"} )
        else:
           edge = g2.insert_edge(parent=parent, source=vdict[source_hostname], target=vdict[target_hostname], value=label, style=edge_style1)
           g2.set_edge_src_label(edge, source_port, style={'labelBackgroundColor' : "#ffffff"} )
           g2.set_edge_dst_label(edge, target_port, style={'labelBackgroundColor' : "#ffffff"} )

    lag_link_check(g2)

    return g2


def xtest_read_file():
    #mx = mxgraph.mxgraph.MxGraphModel()
    mx = mxgraph.mxgraph.MxGraph()
    mx.from_file("test.drawio")
    mx.to_file(sys.stdout)


def main():

    #g1 = ip_network_drawio()
    #g2 = phy_network_drawio()
    #g3 = phy_network_layout()
    #g4 = stp_network_drawio()
    #gdict = { "ip-network" : g1, "phy-network" : g2, "phy-layout" : g3, "stp-network" : g4}
    g3 = phy_network_layout()
    gdict = { "phy-layout" : g3 }

    #f = open("/var/tmp/test.xml","w")
    f = open("test.xml","w")
    mxgraph.mxgraph.multi_graphdict_to_file(gdict, f)
    f.close()

    #tree = XET.parse("/var/tmp/test.xml")
    tree = XET.parse("test.xml")
    XET.indent(tree, space='  ')
    tree.write('test.drawio', encoding='UTF-8', xml_declaration=True)


if __name__=="__main__":
    main()

