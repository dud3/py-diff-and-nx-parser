# Not currently in use

"""
root0 = pf0.getroot()
nodes0 = list(root0)

root1 = pf1.getroot()
nodes1 = list(root1)

def findbytag(nodes, tag):
	fnode = None
	for node in nodes:
		if node.tag == tag:
			fnode = node
			break

	return fnode

def findbyattrib(nodes, attrib):
	fnode = None
	for node in nodes:
		if str(node.attrib) == str(attrib):
			fnode = node
			break

	return fnode

def getsiblings(nodes, tag):
	tags = list(map(lambda n: n.tag, nodes))
	return list(filter(lambda x: x == tag, tags))

def traverse(nodes1, nodes0):
	for node in nodes1:

		fnode = findbytag(nodes0, node.tag)

		# print(getsiblings(nodes0, node.tag))

		if fnode == None:
			fnode = []
			# print(">>> Not found: ", node.tag, node.attrib)
		else:
			# print("found: ", node.tag, node.attrib, "<<<")
			list(fnode)

		# print(node.tag)
		# print()
		traverse(list(node), fnode) # Recurse

traverse(nodes1, nodes0)
"""

"""
# formatter = formatting.XmlDiffFormatter(normalize=formatting.WS_NONE)

diff = main.diff_files(leftfile, rightfile, formatter=formatting.XMLFormatter(normalize=formatting.WS_NONE), diff_options={'F': 0.5, 'ratio_mode': 'accurate'})

# print(diff)

parser = etree.XMLParser(remove_blank_text=True)
rootdiff = etree.XML(diff, parser)

diffpatch = "{http://namespaces.shoobx.com/diff}"

fnodes = findbyattrib(list(rootdiff), diffpatch)

for node in fnodes:
	action = ''
	for k, v in node.attrib.items():
		if k.find(diffpatch) > -1:
			print(k.split('}')[1], "\n", node.tag, node.attrib)
			print()

# print(fnodes[0], fattrib)
"""