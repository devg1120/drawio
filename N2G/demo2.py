from N2G import drawio_diagram


diagram = drawio_diagram()
diagram.add_diagram("Page-1")
diagram.add_node(id="R1", style="./shape_style.txt")
diagram.add_node(id="R2")
diagram.add_link("R1", "R2", label="DF", src_label="Gi1/1", trgt_label="GE23")
#diagram.add_link("R1", "R2", label="DF2", src_label="Gi1/2", trgt_label="GE24")
diagram.layout(algo="kk")
diagram.dump_file(filename="Sample_graph2.drawio", folder="./Output/")


