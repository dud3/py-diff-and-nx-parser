from file import *
from lxml import etree
import os

def traverse(nodes, f = lambda x, i: None, i = 0):
	i += 1
	for node in nodes:
		f(node, i)
		traverse(list(node), f, i)

def findbytag(nodes, fnode):
	for node in nodes:
		if node.tag == fnode.tag:
			return node

	return None

def findbyattrib(nodes, fnode):
	for node in nodes:
		if str(node.attrib) == str(fnode.attrib):
			return node

	return None

def findbykeys(nodes, fnode):
	for node in nodes:
		if node.tag == fnode.tag and node.attrib.keys() == fnode.attrib.keys():
			return node

	return None

def hasdiffkeys(nodes, fnode):
	for node in nodes:
		if node.tag == fnode.tag and node.attrib.keys() != fnode.attrib.keys():
			return node

	return None

def findbyattribfull(nodes, attrib, fnodes = []):
	for node in nodes:
		for k, v in node.attrib.items():
			if k.find(attrib) > -1:
				fnodes.append(node)

		findbyattribfull(list(node), attrib, fnodes)

	return fnodes

"""
# Alternative solution

def traversecompare(nodes0, nodes1, f = lambda x: None):
	# Compare nodes... compare then traverse
	# 0. fnode exists, update -> traverse
	# 1. fnode exists not, remove -> traverse not
	for node0 in nodes0:
		fnode = findbyattrib(nodes1, node0)

		# print(node0, "==", fnode)

		if fnode != None:
			traversecompare(list(node0), list(fnode))
		else:
			print(node0.attrib)
			nfnode = findbytag(nodes1, node0)

			if nfnode != None:
				if (len(list(nfnode)) > 0):
					print("update")
					traversecompare(list(node0), list(nfnode))
				else:
					print("delete")
			else:
				print("delete")
"""

def comaprenodes(nodes0, nodes1):
	if (len(nodes0) == 0 or len(nodes1) == 0):
		return

	len0 = len(nodes0)
	len1 = len(nodes1)

	if len0 != len1:
		j = 0
		knodes = [] # keep nodes

		while j < len0:
			n0 = nodes0[j]
			if findbyattrib(nodes1, n0) != None:
				knodes.append(n0)
			else:
				print("diff - remove", n0.tag, n0.attrib)
				n0.getparent().remove(n0)

			j += 1

		nodes0 = knodes # replace nodes
	else:
		for n0 in nodes0:
			if hasdiffkeys(nodes1, n0) != None:
				print("diff - possible update?")
				print(n0.tag, n0.attrib, list(map(lambda x: { 'tag': x.tag, 'atrib': x.attrib }, nodes1)))

	i = 0
	while i < len(nodes0):
		comaprenodes(list(nodes0[i]), list(nodes1[i]))
		i += 1

# notes:
# Convert node(s) to string
# etree.tostring(pf0)

def mutate_xml(node0, node1, filename):
	leftfile = node0.name + '/' + filename
	rightfile = node1.name + '/' + filename

	parseleft = etree.parse(r'' + leftfile)
	parseright = etree.parse(r'' + rightfile)

	rootleft = parseleft.getroot()
	rootright = parseright.getroot()

	print()
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("Parsing: " + leftfile + " -> " + rightfile)
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

	# Flatten nodes...
	# traverse(list(rootleft), lambda node, i: rightnodes.append(node))
	# traverse(list(rootright), lambda node, i: print(node.tag, i))

	comaprenodes(list(rootleft), list(rootright))

	file = open(leftfile, "wb")
	file.write(etree.tostring(rootleft))
	file.close()

def diff_xml(nodes0, nodes1):
	diff_files(nodes0, nodes1, mutate_xml, lambda n1, file: None)
