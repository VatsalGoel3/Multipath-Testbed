"""A Multipath testbed with four d430 nodes with multiple connections.

Instructions:
Wait for the profile instance to start, and then log in to either node via the ssh ports specified below.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a portal context
pc = portal.Context()

# Create a Request object to start building the RSpec
request = pc.makeRequestRSpec()

# Create four raw "PC" nodes
node1 = request.RawPC("node1")
node2 = request.RawPC("node2")
node3 = request.RawPC("node3")
node4 = request.RawPC("node4")

# Set disk images and hardware types
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD"
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD"
node4.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"

node1.hardware_type = "d430"
node2.hardware_type = "d430"
node3.hardware_type = "d430"
node4.hardware_type = "d430"

# Add interfaces and set IP addresses for node1
eth1a = node1.addInterface("eth1a")
eth2a = node1.addInterface("eth2a")
eth1a.addAddress(rspec.IPv4Address("10.0.0.1", "255.255.255.0"))
eth2a.addAddress(rspec.IPv4Address("192.168.0.1", "255.255.255.0"))

# Add interfaces and set IP addresses for node2
eth1b = node2.addInterface("eth1b")
eth3a = node2.addInterface("eth3a")
eth1b.addAddress(rspec.IPv4Address("10.0.0.2", "255.255.255.0"))
eth3a.addAddress(rspec.IPv4Address("10.0.1.1", "255.255.255.0"))

# Add interfaces and set IP addresses for node3
eth2b = node3.addInterface("eth2b")
eth4a = node3.addInterface("eth4a")
eth2b.addAddress(rspec.IPv4Address("192.168.0.2", "255.255.255.0"))
eth4a.addAddress(rspec.IPv4Address("192.168.1.1", "255.255.255.0"))

# Add interfaces and set IP addresses for node4
eth3b = node4.addInterface("eth3b")
eth4b = node4.addInterface("eth4b")
eth3b.addAddress(rspec.IPv4Address("10.0.1.2", "255.255.255.0"))
eth4b.addAddress(rspec.IPv4Address("192.168.1.2", "255.255.255.0"))

# Create links
link1 = request.LAN("link1")
link2 = request.LAN("link2")
link3 = request.LAN("link3")
link4 = request.LAN("link4")

# Add interfaces to links
link1.addInterface(eth1a)
link1.addInterface(eth1b)

link2.addInterface(eth3a)
link2.addInterface(eth3b)

link3.addInterface(eth2a)
link3.addInterface(eth2b)

link4.addInterface(eth4a)
link4.addInterface(eth4b)

# Add the service to run the setup script on each node
node1.addService(rspec.Execute(shell="bash", command="sudo chmod +x /local/repository/setup.sh && sudo /local/repository/setup.sh"))
node2.addService(rspec.Execute(shell="bash", command="sudo chmod +x /local/repository/setup.sh && sudo /local/repository/setup.sh"))
node3.addService(rspec.Execute(shell="bash", command="sudo chmod +x /local/repository/setup.sh && sudo /local/repository/setup.sh"))
node4.addService(rspec.Execute(shell="bash", command="sudo chmod +x /local/repository/setup.sh && sudo /local/repository/setup.sh"))

# Print the RSpec
pc.printRequestRSpec(request)
