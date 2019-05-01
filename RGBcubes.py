import sys
import xml.etree.ElementTree as ET

def tree(treeXML, cost_dict , cost=2):
    for child in treeXML:
        cost_dict[child.attrib["color"]] += cost
        tree(child, cost_dict, cost + 1)

def main():
    cost = dict(red=0, blue=0, green=0)
    reader = (line.rstrip() for line in sys.stdin)
    dataXML = next(reader)
    root = ET.fromstring(dataXML)

    cost[root.attrib["color"]] += 1
    tree(root, cost)

    print("{0[red]} {0[green]} {0[blue]}".format(cost))

if __name__ == "__main__":
    main()