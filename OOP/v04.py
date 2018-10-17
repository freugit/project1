import xml.etree.ElementTree as et

stu = et.Element("Student")
stu.text = "student"

name = et.SubElement(stu,"Name")

name.attrib = {"lang":"en"}

name.text = "maosb"

age = et.SubElement(stu,"Age")

age.text = '18'

et.dump(stu)