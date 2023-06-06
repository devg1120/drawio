import sys
sys.path.append("../")
import mxgraph.mxgraph 
import xml.etree.ElementTree as XET
import igraph as ig

def update_style(sx,sy,tx,ty,sw,sh,tw,th,style_dics):
     n = len(style_dics)
     print(n)
     print(sw)
     print(sh)
     print(tw)
     print(th)

     if sx == tx   :
         if sy <= ty:
            print("vertical-down")
         else:
            print("vertical-up")
     elif sy == ty :
         if sx <= tx:
            print("horizontal-left")
         else:
            print("horizontal-right")
     elif abs(sx - tx) < 200  :
         if sy <= ty:
            print("vertical-down-near")
         else:
            print("vertical-up-near")
     elif abs(sy - ty) < 200  :
         if sx <= tx:
            print("horizontal-left-near")
         else:
            print("horizontal-right-near")
     elif sx <= tx    and sy <= ty:
         print("right_down")
     elif sx <= tx and sy > ty:
         print("right_up")
     elif sx > tx  and sy <= ty:
         print("left_down")
     elif sx > tx  and sy > ty:
         print("left_up")



def modify_overlay_edge(filename, filename2,diagram_id):
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename,"r")
    g = mx.from_file_getbyid(f, diagram_id )

    vertex_geometry_dict = {}

    print("#----cells----")
    for cell in g.cells:
        if g.cells[cell].vertex:
            _id  = g.cells[cell].cell_id
            geo = g.cells[cell].geometry
            print(id)
            print(geo.x)
            print(geo.y)
            vertex_geometry_dict[_id] = ( geo.x, geo.y, geo.width, geo.height)

        elif g.cells[cell].edge:
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

    print("#----cellsdic----")

    edge_dict = {}
    edge_style_dict = {}
    overlay_edge_style_dict = {}

    for cell in g.cells:
        if g.cells[cell].edge:
            print("")
            edge_id = g.cells[cell]["id"]
            print("edge_id:" + edge_id)
            source_id = g.cells[cell].source["id"]
            print("source_id:" + source_id)

            target_id = g.cells[cell].target["id"]
            print("target_id:" + target_id)

            path1 = source_id + "@" + target_id
            #path2 = target_id + "@" + source_id

            style_dic = g.cells[cell].style
            edge_style_dict[edge_id] = style_dic
            for k in style_dic:
                print("  " + k + ":", end=" ")
                print("  " + style[k])

            if path1 in edge_dict:
                edge_dict[path1].append(edge_id)
            else:
                edge_dict[path1] = [edge_id]

            #if path2 in edge_dict:
            #    edge_dict[path2].append(edge_id)
            #else:
            #    edge_dict[path2] = [edge_id]

    for k in edge_dict.keys():
        if len(edge_dict[k]) > 1:
           print(k)
           for edge_id in edge_dict[k]:
               print("  " + edge_id)

    for k in edge_dict.keys():
        if len(edge_dict[k]) > 1:
           print(k)
           for edge_id in edge_dict[k]:
               print("  " + edge_id)
               if k in overlay_edge_style_dict:
                   #overlay_edge_style_dict[k].append(edge_style_dict[edge_id])
                   overlay_edge_style_dict[k].append((edge_id,edge_style_dict[edge_id]))
               else:
                   #overlay_edge_style_dict[k] = [edge_style_dict[edge_id]]
                   overlay_edge_style_dict[k] = [(edge_id,edge_style_dict[edge_id])]

    #for k in overlay_edge_style_dict:
    #    print(k)
    #    print(len(overlay_edge_style_dict[k]))
    #    for style_dic in overlay_edge_style_dict[k]:
    #        for k2 in style_dic:
    #            print("  " + k2 + ":", end=" ")
    #            print("  " + style[k2])
    for k in overlay_edge_style_dict:
        print(k)
        vertexs = k.split("@")
        source_vertex_id = vertexs[0]
        target_vertex_id = vertexs[1]
        (sx, sy, sw, sh)  = vertex_geometry_dict[source_vertex_id]
        (tx, ty, tw, th)  = vertex_geometry_dict[target_vertex_id]
        print("source:",source_vertex_id, sx, sy)
        print("target:",target_vertex_id, tx, ty)

        print(len(overlay_edge_style_dict[k]))
        for (edge_id,style_dic) in overlay_edge_style_dict[k]:
            print(edge_id)
            for k2 in style_dic:
                print("  " + k2 + ":", end=" ")
                print("  " + style[k2])
        update_style(sx,sy,tx,ty,sw,sh,tw,th,overlay_edge_style_dict[k])
        print("----")
        #update_style(0,0,0,5,overlay_edge_style_dict[k])
        #update_style(0,5,5,5,overlay_edge_style_dict[k])
        #update_style(0,0,5,5,overlay_edge_style_dict[k])
        #update_style(0,0,5,-5,overlay_edge_style_dict[k])
        #update_style(0,0,-5,-5,overlay_edge_style_dict[k])
        #update_style(0,0,-5,5,overlay_edge_style_dict[k])

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

    modify_edge_value("test.drawio", "test_dump.drawio", "phy-network-layout")
    #modify_edge_style("test.drawio", "test_dump.drawio", "phy-network-layout")
    #modify_overlay_edge("test.drawio", "test_dump.drawio", "phy-network-layout")



if __name__=="__main__":
    main()

