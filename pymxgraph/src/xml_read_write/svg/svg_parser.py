# -*- coding: utf-8 -*-

import io
#import matplotlib.pyplot as plt
#import numpy             as np
import re
import sys
import svgelements      # https://pypi.org/project/svgelements/
# svgelements & shapely 共に Polygon クラスがある為
# importによる名前空間の汚染には、要注意
from shapely.geometry   import Polygon

#from matplotlib.path        import Path
#from matplotlib.patches     import PathPatch
#from matplotlib.collections import PatchCollection

def main():
    # with io.StringIO(svg_string) as f:
    #     svg = svgelements.SVG.parse(f)

    svg_file = sys.argv[1]
    print( svg_file )
    svg = svgelements.SVG.parse(svg_file,
                                ppi= 1/0.0393701 # 1 inch = 25.4 mm
                                )
    elms = svg.elements()
    polygons = []
    for elm in elms:
        if type(elm) == svgelements.svgelements.Group:
            print("group")
            continue
        
        if type(elm) in [svgelements.svgelements.Text,
                         svgelements.svgelements.Path ]:
            print("WARNING not applicable for ",type(elm),
                  file=sys.stderr)
            continue

        if type(elm) == svgelements.svgelements.Rect:
            print("rect")
            polygons.append( rect_to_shapely(elm) )
            continue
        
        if type(elm) == svgelements.svgelements.Polygon:
            print("polygon")
            # if not elm.values["class"] in ["outer","convex"]:
            #    continue
            polygons.append( polygon_to_shapely(elm) )
            continue
        
    #fig, ax = plt.subplots()
    
    for polygon in polygons:
        print(polygon)

    #for polygon in polygons:
    #    plot_polygon(ax, polygon,
    #                 facecolor='lightgray',
    #                 edgecolor='black',
    #                 alpha=0.2)
    #plt.show()

def rect_to_shapely( elm:svgelements.svgelements.Rect ):
    pathds =  re.split("[, ]", elm.d() )
    return pathds_to_shapely( pathds )

def polygon_to_shapely( elm:svgelements.svgelements.Polygon ):
    pathds =  re.split("[, ]", elm.d() )
    return pathds_to_shapely( pathds )

def pathds_to_shapely( pathds ):
    holes = []
    holes_tmp = []

    while len(pathds):
        if pathds[0] in ["M","L"]:
            pathds.pop(0)
            continue
        if pathds[0] == "Z":
            pathds.pop(0)
            holes.append( holes_tmp )
            holes_tmp = []
            continue
        
        co_x = float( pathds.pop(0) )
        co_y = float( pathds.pop(0) )
        holes_tmp.append( (co_x, co_y) )
        
    # 念の為 座標群:dが Zで終わらない場合にも備える
    if len( holes_tmp ):
        holes.append( holes_tmp )

    shell = holes.pop(0)
    polygon = Polygon( shell=shell, holes=holes)
    return polygon
    

# Plots a Polygon to pyplot `ax`
# cf. https://stackoverflow.com/questions/55522395
def plot_polygon(ax, poly, **kwargs):
    path = Path.make_compound_path(
        Path(np.asarray(poly.exterior.coords)[:, :2]),
        *[Path(np.asarray(ring.coords)[:, :2]) for ring in poly.interiors])

    patch = PathPatch(path, **kwargs)
    collection = PatchCollection([patch], **kwargs)
    
    ax.add_collection(collection, autolim=True)
    ax.autoscale_view()
    return collection

if __name__ == '__main__':
    main()

