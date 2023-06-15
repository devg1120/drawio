import sys
sys.path.append("../")
import mxgraph.mxgraph 
import xml.etree.ElementTree as XET
import igraph as ig


def create_compress_write_drawio():
    g =  mxgraph.mxgraph.MxGraph(diagram_id='idunno')
    parent = g.create_group_cell(cell_id='1', parent=g.root)
    style = { 'ellipse': None, 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    source_vertex = g.insert_vertex(parent=parent, value="Hello!", x=100, y=200, width=400, height=300, style=style, relative=False)
    target_vertex = g.insert_vertex(parent=parent, value="Goodbye!", x=400, y=200, width=400, height=300, style=style, relative=False)
    # edge_style = { 'edgeStyle': 'none', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    # edge = g.insert_edge(parent=parent, source=source_vertex, target=target_vertex, style=edge_style)
    # g.add_edge_geometry(edge, [(10,20),(30,40)])
    # g.set_source_point(edge, (50,60))
    # g.set_target_point(edge, (70,80))
    # ET.dump(g.mxgraph_model.to_xml(g.cells))

    g.to_file_compress(sys.stdout)

def create_write_drawio():
    g =  mxgraph.mxgraph.MxGraph(diagram_id='idunno')
    parent = g.create_group_cell(cell_id='1', parent=g.root)
    style = { 'ellipse': None, 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    source_vertex = g.insert_vertex(parent=parent, value="Hello!", x=100, y=200, width=40, height=30, style=style, relative=False)
    target_vertex = g.insert_vertex(parent=parent, value="Goodbye!", x=400, y=200, width=40, height=30, style=style, relative=False)

    # https://blog.kakinota.net/how-to-zukai/programming/library/mxgraph/basic/style/
    #EDGESTYLE_SIDETOSIDE: 'sideToSideEdgeStyle',
    #EDGESTYLE_TOPTOBOTTOM: 'topToBottomEdgeStyle',
    #EDGESTYLE_ORTHOGONAL: 'orthogonalEdgeStyle',  #直交
    #EDGESTYLE_SEGMENT: 'segmentEdgeStyle',

    # endArrow=none;html=1;rounded=0;jumpStyle=arc

    ## straight
    edge_style1 = { 'edgeStyle': 'none', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ## curved
    edge_style2 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ## bending
    edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}

    edge = g.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST", style=edge_style3)

    g.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    #g.add_edge_geometry(edge, [(10,20),(30,40)])
    #g.set_source_point(edge, (50,60))
    #g.set_target_point(edge, (70,80))
    # ET.dump(g.mxgraph_model.to_xml(g.cells))
    f = open("/var/tmp/test.xml","w")
    #g.to_file(sys.stdout)
    g.to_file(f)
    f.close()
    tree = XET.parse("/var/tmp/test.xml")
    XET.indent(tree, space='  ')
    tree.write('test.drawio', encoding='UTF-8', xml_declaration=True)
    #print("")
    #print("")
    #g.to_file_compress(sys.stdout)

def create_write_drawio2():
    g =  mxgraph.mxgraph.MxGraph(diagram_id='idunno')
    parent = g.create_group_cell(cell_id='1', parent=g.root)
    #style = { 'ellipse': None, 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    style = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    vertex = g.insert_vertex(parent=parent, value="Hello!2", x=200, y=200, width=200, height=200, style=style, relative=False)

    # https://blog.kakinota.net/how-to-zukai/programming/library/mxgraph/basic/style/
    #EDGESTYLE_SIDETOSIDE: 'sideToSideEdgeStyle',
    #EDGESTYLE_TOPTOBOTTOM: 'topToBottomEdgeStyle',
    #EDGESTYLE_ORTHOGONAL: 'orthogonalEdgeStyle',  #直交
    #EDGESTYLE_SEGMENT: 'segmentEdgeStyle',

    # endArrow=none;html=1;rounded=0;jumpStyle=arc



    #g.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    #g.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    #g.add_right_port(vertex, "A1", style={'labelBackgroundColor' : "#ffffff"} )
    #style2 = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    style2 = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1'  }
   
    g.port_size = 30
    g.add_right_port(vertex, "A1", 10,style=style2 )
    g.add_right_port(vertex, "A2", 50,style=style2 )
    g.add_left_port(vertex, "B1", 10, style=style2 )
    g.add_left_port(vertex, "B2", 50, style=style2 )
    g.add_top_port(vertex, "C1", 10,style=style2 )
    g.add_top_port(vertex, "C2", 50,style=style2 )
    g.add_bottom_port(vertex, "D1", 10,style=style2 )
    g.add_bottom_port(vertex, "D2", 50,style=style2 )

    #g.add_edge_geometry(edge, [(10,20),(30,40)])
    #g.set_source_point(edge, (50,60))
    #g.set_target_point(edge, (70,80))
    # ET.dump(g.mxgraph_model.to_xml(g.cells))
    f = open("/var/tmp/test.xml","w")
    #g.to_file(sys.stdout)
    g.to_file(f)
    f.close()
    tree = XET.parse("/var/tmp/test.xml")
    XET.indent(tree, space='  ')
    tree.write('test.drawio', encoding='UTF-8', xml_declaration=True)
    #print("")
    #print("")
    #g.to_file_compress(sys.stdout)

def create_write_drawio3():
    g =  mxgraph.mxgraph.MxGraph(diagram_id='idunno')
    parent = g.create_group_cell(cell_id='1', parent=g.root)
    style = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    rt_a = g.insert_vertex(parent=parent, cell_id="ROUTER_A", value="ROUTER_A", x=200, y=200, width=200, height=200, style=style, relative=False)
    rt_b = g.insert_vertex(parent=parent, cell_id="ROUTER_B", value="ROUTER_B", x=700, y=400, width=200, height=200, style=style, relative=False)

    style2 = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1'  }
   
    g.port_size = 30
    g.add_right_port(rt_a, "A1", 10,style=style2 )
    g.add_right_port(rt_a, "A2", 50,style=style2 )
    g.add_left_port(rt_a, "B1", 10, style=style2 )
    g.add_left_port(rt_a, "B2", 50, style=style2 )
    g.add_top_port(rt_a, "C1", 10,style=style2 )
    g.add_top_port(rt_a, "C2", 50,style=style2 )
    g.add_bottom_port(rt_a, "D1", 10,style=style2 )
    g.add_bottom_port(rt_a, "D2", 50,style=style2 )

    g.add_right_port(rt_b, "A1", 10,style=style2 )
    g.add_right_port(rt_b, "A2", 50,style=style2 )
    g.add_left_port(rt_b, "B1", 10, style=style2 )
    g.add_left_port(rt_b, "B2", 50, style=style2 )
    g.add_top_port(rt_b, "C1", 10,style=style2 )
    g.add_top_port(rt_b, "C2", 50,style=style2 )
    g.add_bottom_port(rt_b, "D1", 10,style=style2 )
    g.add_bottom_port(rt_b, "D2", 50,style=style2 )

    #print("----cells----")
    #for cell in g.cells:
    #    print(cell)
    #print("----cells end----")
    #c = g.cells.get_cell("ROUTER_B-B1")
    #print(c.cell_id)

    edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}
    source_vertex = g.cells.get_cell("ROUTER_A-A1")
    target_vertex = g.cells.get_cell("ROUTER_B-C1")
    edge = g.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST1", style=edge_style3)
    source_vertex = g.cells.get_cell("ROUTER_A-A2")
    target_vertex = g.cells.get_cell("ROUTER_B-C2")
    edge = g.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST2", style=edge_style3)

    f = open("/var/tmp/test.xml","w")
    g.to_file(f)
    f.close()
    tree = XET.parse("/var/tmp/test.xml")
    XET.indent(tree, space='  ')
    tree.write('test.drawio', encoding='UTF-8', xml_declaration=True)

def create_write_drawio4():
    g1 =  mxgraph.mxgraph.MxGraph(diagram_id='idunno-1')
    parent = g1.create_group_cell(cell_id='1', parent=g1.root)
    style = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    rt_a = g1.insert_vertex(parent=parent, cell_id="ROUTER_A", value="ROUTER_A", x=200, y=200, width=200, height=200, style=style, relative=False)
    rt_b = g1.insert_vertex(parent=parent, cell_id="ROUTER_B", value="ROUTER_B", x=700, y=400, width=200, height=200, style=style, relative=False)

    style2 = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1'  }
   
    g1.port_size = 30
    g1.add_right_port(rt_a, "A1", 10,style=style2 )
    g1.add_right_port(rt_a, "A2", 50,style=style2 )
    g1.add_left_port(rt_a, "B1", 10, style=style2 )
    g1.add_left_port(rt_a, "B2", 50, style=style2 )
    g1.add_top_port(rt_a, "C1", 10,style=style2 )
    g1.add_top_port(rt_a, "C2", 50,style=style2 )
    g1.add_bottom_port(rt_a, "D1", 10,style=style2 )
    g1.add_bottom_port(rt_a, "D2", 50,style=style2 )

    g1.add_right_port(rt_b, "A1", 10,style=style2 )
    g1.add_right_port(rt_b, "A2", 50,style=style2 )
    g1.add_left_port(rt_b, "B1", 10, style=style2 )
    g1.add_left_port(rt_b, "B2", 50, style=style2 )
    g1.add_top_port(rt_b, "C1", 10,style=style2 )
    g1.add_top_port(rt_b, "C2", 50,style=style2 )
    g1.add_bottom_port(rt_b, "D1", 10,style=style2 )
    g1.add_bottom_port(rt_b, "D2", 50,style=style2 )


    edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}
    source_vertex = g1.cells.get_cell("ROUTER_A-A1")
    target_vertex = g1.cells.get_cell("ROUTER_B-C1")
    edge = g1.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST1", style=edge_style3)
    source_vertex = g1.cells.get_cell("ROUTER_A-A2")
    target_vertex = g1.cells.get_cell("ROUTER_B-C2")
    edge = g1.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST2", style=edge_style3)
    
    ###############################################
    g2 =  mxgraph.mxgraph.MxGraph(diagram_id='idunno-2')
    parent = g2.create_group_cell(cell_id='1', parent=g2.root)
    style = { 'ellipse': None, 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    source_vertex = g2.insert_vertex(parent=parent, value="Hello!", x=100, y=200, width=40, height=30, style=style, relative=False)
    target_vertex = g2.insert_vertex(parent=parent, value="Goodbye!", x=400, y=200, width=40, height=30, style=style, relative=False)

    ## straight
    edge_style1 = { 'edgeStyle': 'none', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ## curved
    edge_style2 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ## bending
    edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}

    edge = g2.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST", style=edge_style3)

    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    f = open("/var/tmp/test.xml","w")
    #mxgraph.mxgraph.multi_graph_to_file([g1, g2], f)

    gdict = { "router-net" : g1,  "ip-net" : g2}
    mxgraph.mxgraph.multi_graphdict_to_file(gdict, f)

    f.close()
    tree = XET.parse("/var/tmp/test.xml")
    XET.indent(tree, space='  ')
    tree.write('test.drawio', encoding='UTF-8', xml_declaration=True)

def ip_network_drawio():
    g2 =  mxgraph.mxgraph.MxGraph(diagram_id='ip-network')
    parent = g2.create_group_cell(cell_id='1', parent=g2.root)
    #style = { 'ellipse': None, 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    router_style = { 'shape': "ellipse", 'strokeWidth' :'3','whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    router1 = g2.insert_vertex(parent=parent, value="VRF\n10", x=400, y=50, width=60, height=60, style=router_style, relative=False)
    router2 = g2.insert_vertex(parent=parent, value="VRF\n20", x=500, y=400, width=60, height=60, style=router_style, relative=False)

    style1 = { 'shape': "ellipse", 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    subnet1 = g2.insert_vertex(parent=parent, value="10.100.2.0 /24", x=100, y=200, width=180, height=50, style=style1, relative=False)
    subnet2 = g2.insert_vertex(parent=parent, value="10.100.3.0 /24", x=600, y=200, width=180, height=50, style=style1, relative=False)
    subnet3 = g2.insert_vertex(parent=parent, value="10.100.3.0 /24", x=100, y=600, width=180, height=50, style=style1, relative=False)
    subnet4 = g2.insert_vertex(parent=parent, value="10.100.3.0 /24", x=400, y=600, width=180, height=50, style=style1, relative=False)
    subnet5 = g2.insert_vertex(parent=parent, value="10.100.3.0 /24", x=700, y=600, width=180, height=50, style=style1, relative=False)

    ## straight
    edge_style1 = { 'edgeStyle': 'none', 'endArrow': 'none','curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ## curved
    edge_style2 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    ## bending
    edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}

    edge = g2.insert_edge(parent=parent, source=router1, target=subnet1,  style=edge_style1)
    g2.set_edge_src_label(edge, "100.1", style={'labelBackgroundColor' : "#ffffff"} )
    edge = g2.insert_edge(parent=parent, source=router1, target=subnet2,  style=edge_style1)
    g2.set_edge_src_label(edge, "200.1", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=router2, target=subnet2,  style=edge_style1)
    g2.set_edge_src_label(edge, "200.254", style={'labelBackgroundColor' : "#ffffff"} )

    edge = g2.insert_edge(parent=parent, source=router2, target=subnet3,  style=edge_style1)
    g2.set_edge_src_label(edge, "300.1", style={'labelBackgroundColor' : "#ffffff"} )
    edge = g2.insert_edge(parent=parent, source=router2, target=subnet4,  style=edge_style1)
    g2.set_edge_src_label(edge, "400.1", style={'labelBackgroundColor' : "#ffffff"} )
    edge = g2.insert_edge(parent=parent, source=router2, target=subnet5,  style=edge_style1)
    g2.set_edge_src_label(edge, "500.1", style={'labelBackgroundColor' : "#ffffff"} )

    return g2

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

def autolayout(vlist, elist):
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

    layout.scale(200)

    #layoutprint(layout)
    print(layout.boundaries())
    top_left_point     = layout.boundaries()[0]
    bottom_right_point = layout.boundaries()[1]

    tx = 0
    if top_left_point[0] < 0:
        tx = -top_left_point[0] + 100
    elif top_left_point[0] <= 100:
        tx = 100 - top_left_point[0]
    else:
        tx = 0
    ty = 0
    if top_left_point[1] < 0:
        ty = -top_left_point[1] + 100
    elif top_left_point[1] <= 100:
        ty = 100 - top_left_point[1]
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

            ["hostname_A21", 350,  600, 160, 60],
            ["hostname_A22",  50,  600, 160, 60],

            ["hostname_B31", 950,  600, 160, 60]
            ]

    elist = [
            ["hostname_A",  "Gi0/0/1","hostname_B",  "Gi0/0/1", True, "TEST"],
            ["hostname_A",  "Gi0/0/2","hostname_A1", "Gi0/0/1", False,"TEST"],
            ["hostname_A",  "Gi0/0/3","hostname_A2", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/1","hostname_B1", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/2","hostname_B2", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/3","hostname_B3", "Gi0/0/1", False,"TEST"],
            ["hostname_B",  "Gi0/0/4","hostname_B4", "Gi0/0/1", False,"TEST"],
            ["hostname_A2", "Gi0/0/2","hostname_A21","Gi0/0/1", False,"TEST"],
            ["hostname_B3", "Gi0/0/2","hostname_B31","Gi0/0/1", False,"TEST"],
            ["hostname_A22","Gi0/0/1","hostname_B4", "Gi0/0/2", False,"TEST"],
            ["hostname_A22","Gi0/0/2","hostname_A1", "Gi0/0/2", True, "TEST"]
            ]

    autolayout(vlist, elist)

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
        vt = g2.insert_vertex(parent=parent, value=hostname, x=x , y=y, width=w , height=h , style=sw_style, relative=False)
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

    return g2

def stp_network_drawio():
    g2 =  mxgraph.mxgraph.MxGraph(diagram_id='stp-network')
    parent = g2.create_group_cell(cell_id='1', parent=g2.root)
    #sw_style = { 'shape': "rectangle", 'strokeWidth' :'3','whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    stp_style = { 'swimlane':None ,'whiteSpace': 'wrap', 'html': '1'  }

    hostname_A = g2.insert_vertex(parent=parent, cell_id="hostname_A", value="hostname_A", x=350, y=50, width=180, height=150, style=stp_style, relative=False)
    hostname_B = g2.insert_vertex(parent=parent, cell_id="hostname_B", value="hostname_B", x=100, y=400, width=180, height=150, style=stp_style, relative=False)
    hostname_C = g2.insert_vertex(parent=parent, cell_id="hostname_C", value="hostname_C", x=600, y=400, width=180, height=150, style=stp_style, relative=False)

    style2 = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1'  }
    g2.port_size = 20
    g2.add_bottom_port(hostname_A, "D1", "DP", 10,style=style2 )
    g2.add_bottom_port(hostname_A, "D2", "DP", 90,style=style2 )

    g2.add_top_port(hostname_B, "D1", "DP",10,style=style2 )
    g2.add_top_port(hostname_B, "D2", "DP",90,style=style2 )
    g2.add_right_port(hostname_B, "D3", "DP",10,style=style2 )
    g2.add_right_port(hostname_B, "D4", "DP",50,style=style2 )

    g2.add_top_port(hostname_C, "D1", "DP",10,style=style2 )
    g2.add_top_port(hostname_C, "D2", "DP",90,style=style2 )
    g2.add_left_port(hostname_C, "D3", "DP",10,style=style2 )
    g2.add_left_port(hostname_C, "D4", "DP",50,style=style2 )

    #print("----cells----")
    #for cell in g2.cells:
    #    print("["+cell+"]")
    #print("----cells end----")

    edge_style3 = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}
    edge_style4 = { 'edgeStyle': 'none', 'curved': '0', 'orthogonalLoop': '1', 'endArrow': 'none', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}

    source_vertex = g2.cells.get_cell("hostname_A-D1")
    target_vertex = g2.cells.get_cell("hostname_B-D1")
    edge = g2.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST1", style=edge_style4)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    source_vertex = g2.cells.get_cell("hostname_A-D2")
    target_vertex = g2.cells.get_cell("hostname_B-D2")
    edge = g2.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST1", style=edge_style4)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    source_vertex = g2.cells.get_cell("hostname_B-D3")
    target_vertex = g2.cells.get_cell("hostname_C-D3")
    edge = g2.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST1", style=edge_style4)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    source_vertex = g2.cells.get_cell("hostname_B-D4")
    target_vertex = g2.cells.get_cell("hostname_C-D4")
    edge = g2.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST1", style=edge_style4)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    source_vertex = g2.cells.get_cell("hostname_A-D1")
    target_vertex = g2.cells.get_cell("hostname_C-D1")
    edge = g2.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST1", style=edge_style4)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    source_vertex = g2.cells.get_cell("hostname_A-D2")
    target_vertex = g2.cells.get_cell("hostname_C-D2")
    edge = g2.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST1", style=edge_style4)
    g2.set_edge_src_label(edge, "G1/1/1", style={'labelBackgroundColor' : "#ffffff"} )
    g2.set_edge_dst_label(edge, "E1/1/1", style={'labelBackgroundColor' : "#ffffff"} )

    return g2

def xtest_read_file():
    #mx = mxgraph.mxgraph.MxGraphModel()
    mx = mxgraph.mxgraph.MxGraph()
    mx.from_file("test.drawio")
    mx.to_file(sys.stdout)

def dump_geometry(filename, diagramid):
    #mx = mxgraph.mxgraph.MxGraphModel()
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename,"r")
    #g = mx.from_file(f )
    #g = mx.from_file_getbyid(f, "phy-network-layout")
    g = mx.from_file_getbyid(f, diagramid)
    print(g.diagram_id)
    print(XET.dump(g.mxgraph_model.to_xml(g.cells)))

    print("----cells----")
    for cell in g.cells:
        if g.cells[cell].vertex:
            print("vertex", end=" ")
            print(cell)
            print(g.cells[cell].vertex_type)
        elif g.cells[cell].edge:
            print("edge  ", end=" ")
            print(cell)
        else:
            print("***   ", end=" ")
            print(cell)
    print("----end cells----")
            
    w = open("." + filename + "_" + diagramid + ".geometry" ,"w")
    for cell in g.cells:
        if g.cells[cell].vertex and g.cells[cell].vertex_type == 'Vertex.NODE':
           #print(g.cells[cell].value())
           print(g.cells[cell]._value, end=",", file=w)
           geo = g.cells[cell].geometry
           print(geo.x, end=",", file=w)
           print(geo.y, end=",", file=w)
           print(geo.width, end=",", file=w)
           print(geo.height, end=",", file=w)
           print("", file=w)

    #mx.to_file(sys.stdout)
    w.close()
    f.close()

def file_read_write(filename1, filename2):
    #mx = mxgraph.mxgraph.MxGraphModel()
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename1,"r")
    gdict = mx.from_file(f )

    w = open("test.xml","w")
    mxgraph.mxgraph.multi_graphdict_to_file(gdict, w)
    f.close()
    w.close()
    tree = XET.parse("test.xml")
    XET.indent(tree, space='  ')
    tree.write(filename2, encoding='UTF-8', xml_declaration=True)

def xml_format(filename1,  filename2):
    tree = XET.parse(filename1)
    XET.indent(tree, space='  ')
    tree.write(filename2, encoding='UTF-8', xml_declaration=True)

def file_diagram_read_write(filename1, diagram_id, filename2):
    #mx = mxgraph.mxgraph.MxGraphModel()
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename1,"r")
    w = open(filename2,"w")
    #mx = mx.from_file(f )
    mx = mx.from_file_getbyid(f, diagram_id)
    mx.to_file(w, name=diagram_id)

def main():

    dump_geometry("test.drawio", "phy-network-layout")

    #file_diagram_read_write("test.drawio", "ip-network", "ip-network.drawio")
    #xml_format("ip-network.drawio",  "ip-network2.drawio")

    #file_diagram_read_write("test.drawio", "phy-network-layout", "test2.drawio")

    #file_read_write("test.drawio",  "test3.drawio")



if __name__=="__main__":
    main()

