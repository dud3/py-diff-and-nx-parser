from tree import *
from folder import *
from file import *
from _xml import *

node = Tree("example/Character.wz")
nodeh = Tree("example/(higher)Character.wz")

path_to_node(node, "example/Character.wz")
path_to_node(nodeh, "example/(higher)Character.wz")

node.print()
nodeh.print()

diff_folder([node], [nodeh], remove_folder)
diff_files([node], [nodeh], lambda n0, n1, file : None, remove_file)
diff_xml([node], [nodeh])
