import os
import shutil
from tree import *

def path_to_node(node, path):
	for(dirpath, dirnames, filenames) in os.walk(path):
		node.files = []

		for filename in filenames:
			fpath = dirpath + '/' + filename
			node.files.append(filename)

		if(len(dirnames) > 0):
			for (dirname) in dirnames:
				full_path = dirpath + '/' + dirname
				path_to_node(node.add_child(Tree(full_path, dirname)), dirpath + '/' + dirname)

		break

def diff_folder(nodes0, nodes1, fnf): # fnf = folder found
	for n1 in nodes1:
		fnode = n1.find(n1.value, nodes0)
		if(fnode != None):
			diff_folder(fnode['self'].children, n1.children, fnf)
		else:
			fnf(n1, nodes1)

def remove_folder(node, siblings):
	# siblings.remove(node) # abstract sturct
	shutil.rmtree(node.name)
	print("Removed folders -> " + node.name)
