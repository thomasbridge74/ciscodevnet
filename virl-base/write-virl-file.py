#!/usr/bin/env python

from jinja2 import Template
import csv

# Script to write virl file based on inputs.   Written in python 3.7.


def write_from_file_to_handle(filename, filehandle):
    f = open(filename, "r")
    for line in f.readlines():
        filehandle.write(line)


def write_template_to_handle(**kwargs):
    filename = "templates/" + kwargs["type"] + "-base.jinja"
    try:
        template = Template(open(filename).read())
    except:
        print("Cannot open template file for " + kwargs["type"])
        return
    outputfile = kwargs["handle"]
    outputfile.write(template.render(hostname = kwargs["devicename"], mgmtip = kwargs["mgmtip"]))


def main():
    devicelist = "input.csv"
    outputfile = "topology.virl"
    topology_file = open(outputfile, "w")

    write_from_file_to_handle("templates/topology-header.xml", topology_file)
    with open(devicelist) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(row)
            write_template_to_handle(
                handle=topology_file,
                devicename=row["name"],
                type=row["type"],
                mgmtip=row["mgmt_ip"]
            )

    # This leaves open the option for adding connection management

    write_from_file_to_handle("templates/topology-end.xml", topology_file)







if __name__ == "__main__":
    main()
