import sys
sys.path.append("../")
import mxgraph.mxgraph 
import xml.etree.ElementTree as XET
import igraph as ig
import defusedxml.ElementTree as dxml
import xml.etree.ElementTree as ET
import zlib
from urllib.parse import quote, unquote
import urllib.parse
import base64
import svg2stencil

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
        zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15, memLevel=8,
        #9, zlib.DEFLATED, -15, memLevel=8,
        strategy=zlib.Z_DEFAULT_STRATEGY)
    compressed_data = compress.compress(js_string_to_byte(js_encode_uri_component(data)))    
    compressed_data += compress.flush()
    return compressed_data

def append_shape(g, parent):

    style  = {
               'shape': "rhombus",
             }
    style1 = { 'shape': "rhombus", 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    style2 = { 'shape': "ellipse", 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed', 
               'fillColor' : 'red',
               'fontSize' : 40,
             }

    g.insert_vertex(parent=parent, value = "task_X" , x=40 , y=40, width=180, height=50, style=style1, relative=False )
    g.insert_vertex(parent=parent, value = "task_Y" , x=40 , y=40, width=180, height=50, style=style2, relative=False )

    with open(r"test.svg","rb") as imagefile:
        b64_string = base64.b64encode(imagefile.read())
    
    data = b64_string.decode('utf-8')
    #print(data)
    xml_data = "bVRtk6I4EP4rU963m6sbRNzSc9gqXhzEBdQBBfkWIRuiQSwTJfLrt4GZ2dqqo6orD91Pd56kOv1aSueKLoVf5Zh9f71Wlfj+WkoLM/ZEc32gDJ5e/nAMB08XdMVn8T8x9XcMaHd8FVj2ELEb1geDJy4eDAAv0AXrtEQEz1oazRDz0AGzdcWpoNVZP1RCVOWMtU4TZSdyrW7n3KpYddX/+tl9X5kGo+Ssi+oyQ/yCM6H/pBLns6680XuU/k/PkUD/dfCF38mzLNk/60Wgpg9TO8TyljUKRYt3JbOruzfKR/ljPPIf43tWZnf/aNS+NW3yMqPuImXZObgcVG3qHuc3P3QJijdT9yQLHO8eSTMHDoGYWWPLJThSqL8wNZeaKop3o0051dahW7u2QaBua9R1drd9vORpOKT7OLimo+U9j8endbi8pUlGfMsAvtsbbfXW37KRWezV7dQ9m480CUBTytyj9mPtZL2e8u2Uvk1k8nCfLXKapI32w9qcJpnzpiDLLFEsuZcshwcHapQ7NY3H99TZgJaAo8QQ2XnHU9CeJik7lNNTCmdJbYVG0bz2bNMOLE1ZWTVgg//G83rfwH+oDX1aK95xo7W+T8saWKPNLbAJ9yNDgBHXMsimcSH+6d/egsjlvlVLsBpTMwAe+Itjn9vGFM2LfOARsQKcNZ+4Bn/RwNp4xy3sTfjqzZetPtAjV31NuVpUBM4x9GxWedF7HMQ+6DKgxlb4wA1CRXrRXPhhq8+MVmF3FuCfeJDsldDeHT/4rRYJdwC6IDesZXt+qDEMQriPLmfOWz+y39XA8euO2+W1+9Syiye+7OrZ4Ie9c6oowD9+1bHn4osfzT/ubK6Cnj6nu7MtB50SOGNMXbJXZZGN/LY/itwh0DfGfU2q5dqanmGdeGr2bB1lky8Y9J2p4MRk0G9KmhSKpwZNBn3jfeRiNb0cnPqb28A7sFsT03X7HtrcSJt4I3hHjabPcE4FOjBscf5+Y5jr//49aMeEg6sSi+vjqaa5KPSBBvOjwJQUoseI6wPywekmy0s/WgD0Y+nlj1n1Cw=="

    style4 = {
      "shape": "image",
      "verticalLabelPosition": "bottom",
      "labelBackgroundColor": "#ffffff",
      "verticalAlign": "top",
      "aspect": "fixed",
      "imageAspect": 0,
      "image": "data:image/svg+xml," + data
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

    g.insert_vertex(parent=parent, value = "task_q" , x=340 , y=40, width=20, height=20, style=style4, relative=False )
    g.insert_vertex(parent=parent, value = "task_q" , x=440 , y=40, width=20, height=20, style={"shape" : "gslib_png/notes"}, relative=False )

    style6 = {
    "verticalLabelPositionr": "bottom",
    "html" :1,
    "verticalAlign":"top",
    "align" : "centerx",
    "shape" : "mxgraph.floorplan.table"
    }
    g.insert_vertex(parent=parent, value = "task_q" , x=40 , y=200, width=100, height=100, style=style6, relative=False )

    style7 = {
    "verticalLabelPositionr": "bottom",
    "html" :1,
    "verticalAlign":"top",
    "align" : "centerx",
    "shape" : "stencil(xZPRDoIgFIafhnuCXHXZrJ7AF0DFZBo4oKy3Dzm6hloXbtXGzfn+s/P/sAOisSlZwxHBzDQ8s4geECE3pgVLa4eJU0qAEYZSsgsHkrx6jNWq4q3Ibd8tZMm1sKC2wHZ+Aj0ivHewOzTOlJTOVyhpPDuN9JRl1Vmrq8wDYZB1l3kSMfAj+A5lXz2CauroyBtTGhdK8w9pClHX8BIzk+cjb4LEqwWJh7nfM17T3zlv/3bnkXO01Npv0GRRPIW/5sET)"
    #"shape" : "file://c/Users/h005655/_py/drawio/pymxgraph/src/xml_read_write/gusa_table.xml"
    }
    g.insert_vertex(parent=parent, value = "task_z" , x=40 , y=340, width=100, height=100, style=style7, relative=False )


    #shape_data = "xZPRDoIgFIafhnuCXHXZrJ7AF0DFZBo4oKy3Dzm6hloXbtXGzfn+s/P/sAOisSlZwxHBzDQ8s4geECE3pgVLa4eJU0qAEYZSsgsHkrx6jNWq4q3Ibd8tZMm1sKC2wHZ+Aj0ivHewOzTOlJTOVyhpPDuN9JRl1Vmrq8wDYZB1l3kSMfAj+A5lXz2CauroyBtTGhdK8w9pClHX8BIzk+cjb4LEqwWJh7nfM17T3zlv/3bnkXO01Npv0GRRPIW/5sET"

    #decoded = base64.b64decode(shape_data.encode('utf-8'))
    #data = zlib.decompress(decoded, -zlib.MAX_WBITS)
    #data2 = urllib.parse.unquote(data)

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
    g.insert_vertex(parent=parent, value = "task_yyy" , x=400 , y=200, width=100, height=100, style=style8, relative=False )


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
    g.insert_vertex(parent=parent, value = "amp" , x=400 , y=340, width=100, height=100, style=style8, relative=False )



    #rectangle
    # ellipse
    # triangle
    # rhombus
    # hexagon
    # cylinder


def insert_vertex(g, parent):
    y = 100   
    v_style = { 'shape':'rectangle', 'whiteSpace': 'wrap', 'html': '1', 'aspect': 'fixed' }
    e_style = { 'edgeStyle': 'orthogonalEdgeStyle', 'curved': '0', 'orthogonalLoop': '1', 'jettySize': 'auto', 'html': '1' , 'jumpStyle' : 'arc'}

    source_vertex = g.insert_vertex(parent=parent, value="Hello#!", x=100, y=y, width=90, height=30, style=v_style, relative=False)
    target_vertex = g.insert_vertex(parent=parent, value="Goodbye!", x=600, y=y, width=90, height=30, style=v_style, relative=False)
    edge = g.insert_edge(parent=parent, source=source_vertex, target=target_vertex, value="TEST", style=e_style)


def read_shapes(filename):
    f = open(filename, "rb") 
    xml_string = f.read()
    root = ET.fromstring(xml_string)
    #print(root.tag)
    #print(root.attrib)
    if root.tag != 'shapes':
         print("error")
         return None
    shapes_name = root.attrib['name']
    shapes_dict = {}
    for shape in root.iter('shape'):
            _name = shape.attrib['name'].replace(' ', '_')
            _text = ET.tostring(shape)
            shapes_dict[_name] = _text
    #print(shapes_dict)
    return (shapes_name, shapes_dict)


def instart_shape( g, parent, value, x,  y , xml):
    #data2_ = urllib.parse.quote(xml)
    data3 = pako_deflate_raw(xml)

    encoded = base64.b64encode(data3)
    shape_data = encoded.decode('utf-8')

    style = {
    "verticalLabelPositionr": "bottom",
    "html" :1,
    "verticalAlign":"top",
    "align" : "centerx",
    "shape" : "stencil(" + shape_data + ")"
    }
    g.insert_vertex(parent=parent, value=value , x=x , y=y, width=100, height=100, style=style, relative=False )



def create_write_drawio_shape_dict(filename, shape_dict):
    g =  mxgraph.mxgraph.MxGraph(diagram_id='shapes')
    parent = g.create_group_cell(cell_id='1', parent=g.root)
    #for shape in shape_dict:
    #    print(shape)

    # Script_Task

    xml = shape_dict['Script_Task'].decode('utf-8')
    instart_shape( g, parent, "Script Task", 10,  10 , xml)

    # OK
    #parser = svg2stencil.SvgParser("svg/rect.svg")


    # ERROR
    #parser = svg2stencil.SvgParser("svg/line.svg")
    #parser = svg2stencil.SvgParser("svg/star.svg")
    #parser = svg2stencil.SvgParser("svg/path.svg")
    #parser = svg2stencil.SvgParser("svg/circle.svg")

    #xml2 = parser.read()
    #print(xml2)

    #instart_shape( g, parent, "test", 100,  100 , xml2)

    with open(r"svg/line.svg","rb") as imagefile:
            b64_string = base64.b64encode(imagefile.read())
    data1 = b64_string.decode('utf-8')
    with open(r"svg/path.svg","rb") as imagefile:
            b64_string = base64.b64encode(imagefile.read())
    data2 = b64_string.decode('utf-8')
    with open(r"svg/rect.svg","rb") as imagefile:
            b64_string = base64.b64encode(imagefile.read())
    data3 = b64_string.decode('utf-8')

    style1 = {
      "shape": "image",
      "verticalLabelPosition": "bottom",
      "labelBackgroundColor": "#ffffff",
      "verticalAlign": "top",
      "aspect": "fixed",
      "imageAspect": 0,
      "image": "data:image/svg+xml," + data1
    }
    g.insert_vertex(parent=parent, value = "task_svg" , x=50 , y=200, width=120, height=120, style=style1, relative=False )

    style2 = {
      "shape": "image",
      "verticalLabelPosition": "bottom",
      "labelBackgroundColor": "#ffffff",
      "verticalAlign": "top",
      "aspect": "fixed",
      "imageAspect": 0,
      "image": "data:image/svg+xml," + data2
    }
    g.insert_vertex(parent=parent, value = "task_svg" , x=200 , y=200, width=120, height=120, style=style2, relative=False )

    style3 = {
      "shape": "image",
      "verticalLabelPosition": "bottom",
      "labelBackgroundColor": "#ffffff",
      "verticalAlign": "top",
      "aspect": "fixed",
      "imageAspect": 0,
      "image": "data:image/svg+xml," + data3
    }
    g.insert_vertex(parent=parent, value = "task_svg" , x=350 , y=200, width=120, height=120, style=style3, relative=False )
    ###############################
    f = open("test.xml","w")
    g.to_file(f)
    f.close()
    tree = XET.parse("test.xml")
    XET.indent(tree, space='  ')
    tree.write(filename, encoding='UTF-8', xml_declaration=True)

def create_write_drawio_new(filename):
    g =  mxgraph.mxgraph.MxGraph(diagram_id='shapes')
    parent = g.create_group_cell(cell_id='1', parent=g.root)

    insert_vertex(g, parent)
    append_shape(g, parent)

    f = open("test.xml","w")
    g.to_file(f)
    f.close()
    tree = XET.parse("test.xml")
    XET.indent(tree, space='  ')
    tree.write(filename, encoding='UTF-8', xml_declaration=True)




def main():

    #create_write_drawio_new("shapes.drawio")


    (name, dict) = read_shapes("bpmn.xml")
    print(name)
    for shape in dict:
        print(shape)

    create_write_drawio_shape_dict("shapes_dict.drawio", dict)




if __name__=="__main__":
    main()

