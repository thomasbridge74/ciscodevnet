# Virl Base Line management only

I was using Cisco Devnets VIRL server with VMMasetro and although
VIRL has the means to do quite clever "standardish" configurations what
it doesn't seem to do well is to deploy a bunch of devices with a minimal
config for access from the management hosts only.

The scripts in here are designed to create a basic VIRL configuration
that will put interface GigabitEthernet 0/0 on the vIOS and vIOSL2 types
into a mgmt VRF and allow remote configuration.   It does this by processing
a CSV file (I may move this to YAML for greater flexibility)

What is in here is very alpha as of Feb 2nd 2020 (I've just spent a couple 
of hours looking at the XML in the VIRL file and seeing if I can use
Jinja to create the configs).   It's partly being done as a learning excercise
(I've not done a lot of work with Jinja or XML) but 
there are a few issues I can already see.

1. I'm not currently specifying different coordinates for the devices
in the XML - this means right now all devices of the same type will be 
in the same position on the topology.
2. At this point, I haven't had a chance to test the output VIRL against 
VMMaestro or even do a diff against a known VIRL file (the one I'm effectively
reverse engineering)

It would seem a good approach would be to provide a second script that
can take a VIRL topology and write it out to a CSV or YAML file, so that the file can
be edited and reloaded.   