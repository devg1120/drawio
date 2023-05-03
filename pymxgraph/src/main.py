import sys
import mxgraph.mxgraph 


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
    source_vertex = g.insert_vertex(parent=parent, value="Hello!", x=100, y=200, width=400, height=300, style=style, relative=False)
    target_vertex = g.insert_vertex(parent=parent, value="Goodbye!", x=400, y=200, width=400, height=300, style=style, relative=False)
    # edge_style = { 'edgeStyle': 'none', 'curved': '1', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' }
    # edge = g.insert_edge(parent=parent, source=source_vertex, target=target_vertex, style=edge_style)
    # g.add_edge_geometry(edge, [(10,20),(30,40)])
    # g.set_source_point(edge, (50,60))
    # g.set_target_point(edge, (70,80))
    # ET.dump(g.mxgraph_model.to_xml(g.cells))

    g.to_file(sys.stdout)
    print("")
    #print("")
    #g.to_file_compress(sys.stdout)

def xtest_read_file():
    #mx = mxgraph.mxgraph.MxGraphModel()
    mx = mxgraph.mxgraph.MxGraph()
    mx.from_file("test.drawio")
    mx.to_file(sys.stdout)


def main():
    # read_write_drawio()
    print("#create_write_drawio()")
    create_write_drawio()
    print("")

    print("#create_compress_write_drawio()")
    create_compress_write_drawio()
    print("")

    # mxgraph = MxGraph.from_file(sys.stdin)
    # mxgraph.to_file(sys.stdout)
    # ET.dump(mxfile.diagram.mxgraph_model.to_xml(mxfile.diagram.cell_store))
    # mxfile.to_file(sys.stdout)

    print("#xtest_read_file()");

    xtest_read_file()

if __name__=="__main__":
    main()

