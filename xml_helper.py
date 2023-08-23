import xml.etree.ElementTree as ET


def save_data(data,file_name="zoo.xml"):
    root = ET.Element("data")

    for item in data:
        entry = ET.SubElement(root, "entry")
        ET.SubElement(entry, "kind").text = item["kind"]
        ET.SubElement(entry, "name").text = item["name"]
        ET.SubElement(entry, "age").text = item["age"]

    tree = ET.ElementTree(root)
    tree.write("zoo.xml")


def load_data(file_name="zoo.xml"):
    tree = ET.parse("zoo.xml")
    root = tree.getroot()

    data_list = []

    for entry in root.findall("entry"):
        kind = entry.find("kind").text
        name = entry.find("name").text
        age = entry.find("age").text
        data_list.append({"kind": kind, "name": name, "age": age})
    return data_list