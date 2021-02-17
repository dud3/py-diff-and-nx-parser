import sys
import os.path
from tree import *
from folder import *
from file import *
from _xml import *

if len(sys.argv) < 3:
	exit("usage: path/to/from.xml path/to/to.xml")

print(sys.argv, os.path.exists(sys.argv[1]))

frompath = sys.argv[1]
topath = sys.argv[2]

if (not (os.path.exists(frompath) and os.path.exists(topath))):
	exit("error: one of the files does not exists!")

fromnode = Tree(frompath)
tonode = Tree(topath)

path_to_node(fromnode, frompath)
path_to_node(tonode, topath)

fromnode.print()
tonode.print()

diff_folder([fromnode], [tonode], remove_folder)
diff_files([fromnode], [tonode], lambda n0, n1, file : None, remove_file)
diff_xml([fromnode], [tonode])

print("system: execution finished.")