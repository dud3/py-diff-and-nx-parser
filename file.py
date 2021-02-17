def diff_files(nodes0, nodes1, fnf, nfnf): # fnf = file found, nfnf = no file found
	for n1 in nodes1:
		fnode = n1.find(n1.value, nodes0)

		if(fnode != None):
			diff_files(fnode['self'].children, n1.children, fnf, nfnf)
			for n1file in n1.files:
				if(n1file in fnode['self'].files):
					fnf(n1, fnode['self'], n1file)
					continue
				else:
					fnnf(n1, n1file)

def remove_file(node, filename):
	fpath = node.name + '/' + filename
	os.remove(fpath)
	print("Removed files: -> " + fpath)
