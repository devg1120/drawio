import sys
sys.path.append("../")
import mxgraph.mxgraph 
import xml.etree.ElementTree as XET
import igraph as ig

def modify_overlay_edge(filename, filename2,diagram_id):
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename,"r")
    g = mx.from_file_getbyid(f, diagram_id )

def modify_edge_style(filename, filename2,diagram_id):
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename,"r")
    g = mx.from_file_getbyid(f, diagram_id )

    print("#----cells----")
    for cell in g.cells:
        if g.cells[cell].edge:

            print("style :",g.cells[cell].style)
            style = g.cells[cell].style
            for k in style:
                print("  " + k + ":", end=" ")
                print("  " + style[k])
            #print(cell)
            style["strokeWidth"] = 10

    print("#----end cells----")

    f.close()
            

    f2 = open("tmp.xml","w")
    g.to_file(f2, name=diagram_id + "2")


    tree = XET.parse("tmp.xml")
    XET.indent(tree, space='  ')
    tree.write(filename2, encoding='UTF-8', xml_declaration=True)


def modify_edge_value(filename, filename2,diagram_id):
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename,"r")
    g = mx.from_file_getbyid(f, diagram_id )

    print("----cells----")
    for cell in g.cells:
        if g.cells[cell].edge:
            print("edge  " )
            edge = g.cells[cell]
            for k in edge:
                print("  " + k + ":", end=" ")
                print("  " + edge[k])
            #edge["value"] = "UPDATE"
            edge.value = "UPDATE"

            print("source :",g.cells[cell].source)
            source = g.cells[cell].source
            for k in source:
                print("  " + k + ":", end=" ")
                print("  " + source[k])

            print("target :",g.cells[cell].target)
            target = g.cells[cell].target
            for k in target:
                print("  " + k + ":", end=" ")
                print("  " + target[k])

            print("style :",g.cells[cell].style)
            style = g.cells[cell].style
            for k in style:
                print("  " + k + ":", end=" ")
                print("  " + style[k])
            #print(cell)

    print("----end cells----")
    print("----cells----")
    for cell in g.cells:
        if g.cells[cell].edge:
            print("edge  " )
            edge = g.cells[cell]
            for k in edge:
                print("  " + k + ":", end=" ")
                print("  " + edge[k])

            print("source :",g.cells[cell].source)
            source = g.cells[cell].source
            for k in source:
                print("  " + k + ":", end=" ")
                print("  " + source[k])

            print("target :",g.cells[cell].target)
            target = g.cells[cell].target
            for k in target:
                print("  " + k + ":", end=" ")
                print("  " + target[k])

            print("style :",g.cells[cell].style)
            style = g.cells[cell].style
            for k in style:
                print("  " + k + ":", end=" ")
                print("  " + style[k])
            #print(cell)

    print("----end cells----")

    f.close()
            

    f2 = open("tmp.xml","w")
    g.to_file(f2, name=diagram_id + "2")


    tree = XET.parse("tmp.xml")
    XET.indent(tree, space='  ')
    tree.write(filename2, encoding='UTF-8', xml_declaration=True)



def main():

    #modify_edge_value("test.drawio", "test_dump.drawio", "phy-network-layout")
    #modify_edge_style("test.drawio", "test_dump.drawio", "phy-network-layout")
    modify_overlay_style("test.drawio", "test_dump.drawio", "phy-network-layout")



if __name__=="__main__":
    main()

