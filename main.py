#!/usr/bin/env python
import sys
import pathlib 
import argparse
import pprint
pp=pprint.pprint
from ruamel.yaml import YAML #instead of pyyaml because ruamel.yaml preserves anchors and comments!
import glob

def merge_templates(all_under_path, outputfile):
    P = pathlib.Path(all_under_path)
    yaml=YAML()
    merged = {'_comment':"This file generated from main.py",'templates':[]}
    for each in P.rglob("*.yaml"):
        with open(each, "r") as s:
            try:
                single = yaml.load(s)
                for t in single['templates']:
                    t.yaml_set_anchor(str(each).replace('/','_').replace(each.suffix,''),always_dump=True) 
                    #always_dump=True is the key here!
                    merged['templates'].append(t)
            except Exception as e:
                print(each, e)
    with open(outputfile, 'w') as fd:
        yaml.dump(merged,fd)
   
def render_all_connectors(connectorsfile):
    yaml=YAML()
    p = pathlib.Path("./connectors_temp")
    p.mkdir(exist_ok=True)
    with open(connectorsfile,'r') as fd:
        allconnectors = yaml.load(fd)
        for t in allconnectors['templates']:
            print(t.anchor.value)
            tp = p / pathlib.Path(t.anchor.value + ".yaml")
            with tp.open("w") as fd:
                fd.write("""
connectors:
    %s:
        <<: *%s
                """%(t.anchor.value,t.anchor.value))

def main():
    #load up all the yaml in devices/
    #merge all templates together into one big yaml file
    allconnectors = "devices.yaml"
    merge_templates("devices/",allconnectors)
    render_all_connectors(allconnectors)

if __name__ == "__main__":
    main()
