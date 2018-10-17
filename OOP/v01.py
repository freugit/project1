import xml.dom.minidom



DomTree = xml.dom.minidom.parse("x02.xml")

doc = DomTree.documentElement

for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("----Node{0}-----".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "Name":
                print("Name:{0}".format(child.childNodes[0].data))
            if child.nodeName == "Age":
                print("Age:{0}".format(child.childNodes[0].data))
                if child.hasAttribute("details"):
                    print("Age details:{0}".format(child.getAttribute("details")))
            if child.nodeName == "Mobile":
                print("Mobile:{0}".format(child.childNodes[0].data))

