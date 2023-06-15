import sys
sys.path.append("../")
import mxgraph.mxgraph 
import xml.etree.ElementTree as XET
import igraph as ig



def xtest_read_file():
    #mx = mxgraph.mxgraph.MxGraphModel()
    mx = mxgraph.mxgraph.MxGraph()
    mx.from_file("test.drawio")
    mx.to_file(sys.stdout)


import defusedxml.ElementTree as dxml
import xml.etree.ElementTree as ET
def diagram_id_2_name(filename,id):
     et = dxml.parse(f)
     root = et.getroot()
     lists = root.findall('.//diagram')
     for diagram in lists:
        if id == diagram.get('id'):
           return diagram.get('name')
             
     return None

def dump_file(filename):
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename,"r")
    gdict = mx.from_file(f )
    for id in gdict:
        print("diagram-id:\t",id)
        print("diagram-name:\t", gdict[id].diagram_name)
        g = gdict[id]
        print("----cells----")
        for id in g.cells:
            cell = g.cells[id]
            if cell.vertex:
                print(cell.cell_id, "vertex", end=" ")
                print(cell.style)
                #print(g.cells[cell].vertex_type)
            elif cell.edge:
                print(cell.cell_id, "edge  ", cell._source_id, cell._target_id, end=" ")
                print(cell.style)
            else:
                print("***   ", end=" ")
                print(cell.cell_id)
        print("----end cells----")
            

def modify_file(filename, filename2):
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename,"r")
    gdict = mx.from_file(f )
    g = gdict["idunno###"]

    cell = g.cells["idunno-3"]
    cell.style.attrs["shape"] = "cylinder"

    cell = g.cells["idunno-5"]
    cell.style.attrs["exitX"] = "1.0"

    #rectangle
    # ellipse
    # triangle
    # rhombus
    # hexagon
    # cylinder

    w = open("test.xml","w")
    mxgraph.mxgraph.multi_graphdict_to_file(gdict, w)
    f.close()
    w.close()
    tree = XET.parse("test.xml")
    XET.indent(tree, space='  ')
    tree.write(filename2, encoding='UTF-8', xml_declaration=True)

import zlib

from urllib.parse import quote, unquote
import base64

def js_encode_uri_component(data):
    return quote(data, safe='~()*!.\'')


def js_decode_uri_component(data):
    return unquote(data)


def js_string_to_byte(data):
    return bytes(data, 'utf-8')


def js_bytes_to_string(data):
    return data.decode('utf-8')


def js_btoa(data):
    return base64.b64encode(data)


def js_atob(data):
    return base64.b64decode(data)


def pako_deflate(data):
    compress  = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, 15,
        memLevel=8, strategy=zlib.Z_DEFAULT_STRATEGY)
    compressed_data = compress.compress(js_string_to_byte(js_encode_uri_component(data)))    
    compressed_data += compress.flush()
    return compressed_data

def pako_deflate_raw(data):
    compress = zlib.compressobj(
        #zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15, memLevel=8,
        9, zlib.DEFLATED, -15, memLevel=8,
        #5, zlib.DEFLATED, -15, memLevel=8,
        strategy=zlib.Z_DEFAULT_STRATEGY)
    compressed_data = compress.compress(js_string_to_byte(js_encode_uri_component(data)))    
    compressed_data += compress.flush()
    return compressed_data

def modify_file2(filename, filename2):
    mx = mxgraph.mxgraph.MxGraph()
    f = open(filename,"r")
    gdict = mx.from_file(f )
    g = gdict["GQk0Czdau2B2E7RYG4eq"]
    """
        <mxCell id="G0avHX12ZUL-R_R_pCqJ-7" value="TASK_C" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;" vertex="1" parent="G0avHX12ZUL-R_R_pCqJ-4">
          <mxGeometry x="520" y="30" width="120" height="60" as="geometry" />
        </mxCell>
    """
    print("----cells----")
    for id in g.cells:
            cell = g.cells[id]
            if cell.vertex:
                print("vertex", cell.cell_id, cell._value, end=" ")
                print(cell.style)
    print("----end cells----")

    style = {
      'shape': "rhombus",
      }
    style1 = { 'shape': "rhombus", 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    style2 = { 'shape': "ellipse", 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed', 
               'fillColor' : 'red',
               'fontSize' : 40,
             }


    g.insert_vertex(parent="G0avHX12ZUL-R_R_pCqJ-4", value = "task_X" , x=40 , y=40, width=180, height=50, style=style1, relative=False )
    g.insert_vertex(parent="G0avHX12ZUL-R_R_pCqJ-3", value = "task_Y" , x=40 , y=40, width=180, height=50, style=style2, relative=False )


    import base64
    import urllib.parse

    with open(r"test.svg","rb") as imagefile:
        b64_string = base64.b64encode(imagefile.read())
    
    data = b64_string.decode('utf-8')
    print(data)
    xml_data = "bVRtk6I4EP4rU963m6sbRNzSc9gqXhzEBdQBBfkWIRuiQSwTJfLrt4GZ2dqqo6orD91Pd56kOv1aSueKLoVf5Zh9f71Wlfj+WkoLM/ZEc32gDJ5e/nAMB08XdMVn8T8x9XcMaHd8FVj2ELEb1geDJy4eDAAv0AXrtEQEz1oazRDz0AGzdcWpoNVZP1RCVOWMtU4TZSdyrW7n3KpYddX/+tl9X5kGo+Ssi+oyQ/yCM6H/pBLns6680XuU/k/PkUD/dfCF38mzLNk/60Wgpg9TO8TyljUKRYt3JbOruzfKR/ljPPIf43tWZnf/aNS+NW3yMqPuImXZObgcVG3qHuc3P3QJijdT9yQLHO8eSTMHDoGYWWPLJThSqL8wNZeaKop3o0051dahW7u2QaBua9R1drd9vORpOKT7OLimo+U9j8endbi8pUlGfMsAvtsbbfXW37KRWezV7dQ9m480CUBTytyj9mPtZL2e8u2Uvk1k8nCfLXKapI32w9qcJpnzpiDLLFEsuZcshwcHapQ7NY3H99TZgJaAo8QQ2XnHU9CeJik7lNNTCmdJbYVG0bz2bNMOLE1ZWTVgg//G83rfwH+oDX1aK95xo7W+T8saWKPNLbAJ9yNDgBHXMsimcSH+6d/egsjlvlVLsBpTMwAe+Itjn9vGFM2LfOARsQKcNZ+4Bn/RwNp4xy3sTfjqzZetPtAjV31NuVpUBM4x9GxWedF7HMQ+6DKgxlb4wA1CRXrRXPhhq8+MVmF3FuCfeJDsldDeHT/4rRYJdwC6IDesZXt+qDEMQriPLmfOWz+y39XA8euO2+W1+9Syiye+7OrZ4Ie9c6oowD9+1bHn4osfzT/ubK6Cnj6nu7MtB50SOGNMXbJXZZGN/LY/itwh0DfGfU2q5dqanmGdeGr2bB1lky8Y9J2p4MRk0G9KmhSKpwZNBn3jfeRiNb0cnPqb28A7sFsT03X7HtrcSJt4I3hHjabPcE4FOjBscf5+Y5jr//49aMeEg6sSi+vjqaa5KPSBBvOjwJQUoseI6wPywekmy0s/WgD0Y+nlj1n1Cw=="

    style4 = {
      "shape": "image",
      "verticalLabelPosition": "bottom",
      "labelBackgroundColor": "#ffffff",
      "verticalAlign": "top",
      "aspect": "fixed",
      "imageAspect": 0,
      "image": "data:image/svg+xml," + data
      #"image":  "data:image/svg+xml," + xml_data
    }

    style3 = {
      "shape": "image",
      "verticalLabelPosition": "bottom",
      "labelBackgroundColor": "#ffffff",
      "verticalAlign": "top",
      "aspect": "fixed",
      "imageAspect": 0,
      "image": "data:image/svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMjAgMjAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDIwIDIwIiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPGcgaWQ9ImFkZF8xXyI+Cgk8Zz4KCQk8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEwLDBDNC40OCwwLDAsNC40OCwwLDEwYzAsNS41Miw0LjQ4LDEwLDEwLDEwczEwLTQuNDgsMTAtMTAgICAgQzIwLDQuNDgsMTUuNTIsMCwxMCwweiBNMTAsMThjLTQuNDIsMC04LTMuNTgtOC04czMuNTgtOCw4LThzOCwzLjU4LDgsOFMxNC40MiwxOCwxMCwxOHogTTE1LDloLTRWNWMwLTAuNTUtMC40NS0xLTEtMSAgICBTOSw0LjQ1LDksNXY0SDVjLTAuNTUsMC0xLDAuNDUtMSwxYzAsMC41NSwwLjQ1LDEsMSwxaDR2NGMwLDAuNTUsMC40NSwxLDEsMXMxLTAuNDUsMS0xdi00aDRjMC41NSwwLDEtMC40NSwxLTEgICAgQzE2LDkuNDUsMTUuNTUsOSwxNSw5eiIgY2xhc3M9InBhdGgwIiAvPgoJPC9nPgo8L2c+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+LnBhdGgwe2ZpbGw6IzAwMDAwMDt9PC9zdHlsZT48L3N2Zz4=",
       "editableCssRules": ".*"
    }

    g.insert_vertex(parent="G0avHX12ZUL-R_R_pCqJ-4", value = "task_svg" , x=340 , y=40, width=20, height=20, style=style4, relative=False )
    g.insert_vertex(parent="G0avHX12ZUL-R_R_pCqJ-4", value = "task_q" , x=440 , y=40, width=20, height=20, style={"shape" : "gslib_png/notes"}, relative=False )

    style6 = {
    "verticalLabelPositionr": "bottom",
    "html" :1,
    "verticalAlign":"top",
    "align" : "centerx",
    "shape" : "mxgraph.floorplan.table"
    #"shape" : "file://c/Users/h005655/_py/drawio/pymxgraph/src/xml_read_write/gusa_table.xml"
    }
    g.insert_vertex(parent="G0avHX12ZUL-R_R_pCqJ-4", value = "task_q" , x=740 , y=40, width=100, height=100, style=style6, relative=False )

    style7 = {
    "verticalLabelPositionr": "bottom",
    "html" :1,
    "verticalAlign":"top",
    "align" : "centerx",
    "shape" : "stencil(xZPRDoIgFIafhnuCXHXZrJ7AF0DFZBo4oKy3Dzm6hloXbtXGzfn+s/P/sAOisSlZwxHBzDQ8s4geECE3pgVLa4eJU0qAEYZSsgsHkrx6jNWq4q3Ibd8tZMm1sKC2wHZ+Aj0ivHewOzTOlJTOVyhpPDuN9JRl1Vmrq8wDYZB1l3kSMfAj+A5lXz2CauroyBtTGhdK8w9pClHX8BIzk+cjb4LEqwWJh7nfM17T3zlv/3bnkXO01Npv0GRRPIW/5sET)"
    #"shape" : "file://c/Users/h005655/_py/drawio/pymxgraph/src/xml_read_write/gusa_table.xml"
    }
    g.insert_vertex(parent="G0avHX12ZUL-R_R_pCqJ-4", value = "task_z" , x=840 , y=40, width=100, height=100, style=style7, relative=False )


    shape_data = "xZPRDoIgFIafhnuCXHXZrJ7AF0DFZBo4oKy3Dzm6hloXbtXGzfn+s/P/sAOisSlZwxHBzDQ8s4geECE3pgVLa4eJU0qAEYZSsgsHkrx6jNWq4q3Ibd8tZMm1sKC2wHZ+Aj0ivHewOzTOlJTOVyhpPDuN9JRl1Vmrq8wDYZB1l3kSMfAj+A5lXz2CauroyBtTGhdK8w9pClHX8BIzk+cjb4LEqwWJh7nfM17T3zlv/3bnkXO01Npv0GRRPIW/5sET"





    #decoded = base64.decodebytes(shape_data.encode('utf-8'))
    decoded = base64.b64decode(shape_data.encode('utf-8'))
    print("********")
    print(decoded)
    print("********")

    data = zlib.decompress(decoded, -zlib.MAX_WBITS)
    print(data)
    data2 = urllib.parse.unquote(data)
    print("decode----------------------")
    print(data2)
    print("----------------------")

    #shape_encode(data2)
    #sys.exit()
    #shape_decode(shape_data)

    ###############################
    f = open("gusa_table.xml", "rb") 

    data = f.read()
    data2_ = urllib.parse.quote(data)
    data3 = pako_deflate_raw(data.decode('utf-8'))

    encoded = base64.b64encode(data3)
    shape_data2 = encoded.decode('utf-8')

    style8 = {
    "verticalLabelPositionr": "bottom",
    "html" :1,
    "verticalAlign":"top",
    "align" : "centerx",
    "shape" : "stencil(" + shape_data2 + ")"
    }
    g.insert_vertex(parent="G0avHX12ZUL-R_R_pCqJ-4", value = "task_yyy" , x=840 , y=240, width=100, height=100, style=style8, relative=False )


    ###############################
    f = open("opamp.xml", "rb") 

    data = f.read()
    data2_ = urllib.parse.quote(data)
    data3 = pako_deflate_raw(data.decode('utf-8'))

    encoded = base64.b64encode(data3)
    shape_data3 = encoded.decode('utf-8')

    style8 = {
    "verticalLabelPositionr": "bottom",
    "html" :1,
    "verticalAlign":"top",
    "align" : "centerx",
    "shape" : "stencil(" + shape_data3 + ")"
    }
    g.insert_vertex(parent="G0avHX12ZUL-R_R_pCqJ-4", value = "amp" , x=840 , y=440, width=100, height=100, style=style8, relative=False )



    #rectangle
    # ellipse
    # triangle
    # rhombus
    # hexagon
    # cylinder

    w = open("test.xml","w")
    mxgraph.mxgraph.multi_graphdict_to_file(gdict, w)
    f.close()
    w.close()
    tree = XET.parse("test.xml")
    XET.indent(tree, space='  ')
    tree.write(filename2, encoding='UTF-8', xml_declaration=True)

def shape_encode( data ):
    import base64
    import urllib.parse
    print("shape_encode")
    data2_ = urllib.parse.quote(data).encode('utf-8')
    print(data2_)
    #data3 = zlib.compress(data2_,  -zlib.MAX_WBITS)
    #data3 = zlib.compress(data2_)
    data3 = zlib.compress(data2_, level = 9 )
    print(data3)

    encoded = base64.b64encode(data3)
    print("******** encode")
    #print(encoded)
    print(encoded.decode('utf-8'))
    print("********")
    shape_decode2( encoded.decode('utf-8') )

def shape_decode2( shape_data ):
    print("shape_code2")
    import base64
    import urllib.parse
    decoded = base64.b64decode(shape_data.encode('utf-8'))
    print("********")
    print(decoded)
    print("********")

    #data = zlib.decompress(decoded, -zlib.MAX_WBITS)
    data = zlib.decompress(decoded )
    print(data)
    data2 = urllib.parse.unquote(data)
    print("----------------------")
    print(data2)
    print("----------------------")

def shape_decode( shape_data ):
    import base64
    import urllib.parse
    decoded = base64.b64decode(shape_data.encode('utf-8'))
    print("********")
    print(decoded)
    print("********")

    data = zlib.decompress(decoded, -zlib.MAX_WBITS)
    print(data)
    data2 = urllib.parse.unquote(data)
    print("----------------------")
    print(data2)
    print("----------------------")

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

    dump_file("test.drawio")
    modify_file("test.drawio",  "test2.drawio")

    dump_file("lane1.drawio")
    modify_file2("lane1.drawio",  "lane2.drawio")

    #dump_geometry("test.drawio", "phy-network-layout")

    #file_diagram_read_write("test.drawio", "ip-network", "ip-network.drawio")
    #xml_format("ip-network.drawio",  "ip-network2.drawio")

    #file_diagram_read_write("test.drawio", "phy-network-layout", "test2.drawio")

    #file_read_write("test.drawio",  "test3.drawio")



if __name__=="__main__":
    main()

