import sys
#import mxgraph.mxgraph 

sys.path.append("../")
import mxgraph.mxgraph 
import xml.etree.ElementTree as XET


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

    print("----cells----")
    for cell in g.cells:
        print(cell)
    print("----cells end----")
    c = g.cells.get_cell("ROUTER_B-B1")
    print(c.cell_id)

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
    g1.add_right_port(rt_a, "A1", "A1",10,style=style2 )
    g1.add_right_port(rt_a, "A2", "A2",50,style=style2 )
    g1.add_left_port(rt_a, "B1", "B1",10, style=style2 )
    g1.add_left_port(rt_a, "B2", "B2",50, style=style2 )
    g1.add_top_port(rt_a, "C1", "C1",10,style=style2 )
    g1.add_top_port(rt_a, "C2", "C2",50,style=style2 )
    g1.add_bottom_port(rt_a, "D1", "D1",10,style=style2 )
    g1.add_bottom_port(rt_a, "D2", "D2",50,style=style2 )

    g1.add_right_port(rt_b, "A1", "A1",10,style=style2 )
    g1.add_right_port(rt_b, "A2", "A2",50,style=style2 )
    g1.add_left_port(rt_b, "B1", "B1",10, style=style2 )
    g1.add_left_port(rt_b, "B2", "B2",50, style=style2 )
    g1.add_top_port(rt_b, "C1", "C1",10,style=style2 )
    g1.add_top_port(rt_b, "C2", "C2",50,style=style2 )
    g1.add_bottom_port(rt_b, "D1", "D1",10,style=style2 )
    g1.add_bottom_port(rt_b, "D2", "D2",50,style=style2 )


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

    #f = open("/var/tmp/test.xml","w")
    f = open("test.xml","w")
    #mxgraph.mxgraph.multi_graph_to_file([g1, g2], f)

    gdict = { "router-net" : g1,  "ip-net" : g2}
    mxgraph.mxgraph.multi_graphdict_to_file(gdict, f)

    f.close()
    #tree = XET.parse("/var/tmp/test.xml")
    tree = XET.parse("test.xml")
    XET.indent(tree, space='  ')
    tree.write('test.drawio', encoding='UTF-8', xml_declaration=True)

def xtest_read_file():
    #mx = mxgraph.mxgraph.MxGraphModel()
    mx = mxgraph.mxgraph.MxGraph()
    mx.from_file("test.drawio")
    mx.to_file(sys.stdout)


def main():
    # read_write_drawio()
    #print("#create_write_drawio()")

    #create_write_drawio()
    #create_write_drawio2()
    #create_write_drawio3()
    create_write_drawio4()

    #print("#create_compress_write_drawio()")
    #create_compress_write_drawio()
    #print("")

    # mxgraph = MxGraph.from_file(sys.stdin)
    # mxgraph.to_file(sys.stdout)
    # ET.dump(mxfile.diagram.mxgraph_model.to_xml(mxfile.diagram.cell_store))
    # mxfile.to_file(sys.stdout)

    #print("#xtest_read_file()");

    #xtest_read_file()

if __name__=="__main__":
    main()

