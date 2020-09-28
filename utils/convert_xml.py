import glob
import re
import json
import xml.etree.ElementTree as ET

def convert_to_json(file: str, output_dir: str):
    tree = ET.parse(file)
    root = tree.getroot()
    out_file = re.match(r".*/Advanced Combat Tracker.exe.([^/]*)\.xml", file).group(1) + ".json"

    string = False
    if out_file.startswith("InternalString"):
        string = True

    dd = dict()
    for elem in root:
        if string:
            dd[elem.attrib["key"]] = elem.attrib["value"]
        else:
            dd[elem.attrib["ControlPath"] + "##" + elem.attrib["UniqueName"]] = elem.attrib["Text"]

    json.dump(dd, open(output_dir + out_file, "w"), sort_keys=False, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    files = glob.glob("AdvancedCombatTracker/Localization/en-US/*.xml")
    for f in files:
        convert_to_json(f, "locales/en-US/")
