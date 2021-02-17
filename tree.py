class Tree(object):
    "Generic tree"

    def __init__(self, name='root', value='', children=None):
        self.name = name
        self.value = value
        self.children = []
        self.indent = 0

        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
        return node

    def remove(self, value):
        node = self.find(value, self.children)
        if node != None:
            node['siblings'].remove(node['self'])

    def find(self, value, children = []):
        for child in children:
            if child.value == value:
                d = dict()
                d['self'] = child
                d['siblings'] = children
                return d
            else:
                self.find(value, child.children)
        else:
            return None

    def print(self, indent = 0):
        istr = ''

        for i in range(indent): istr += ' - '
        value = istr + self.value

        print(value)

        for node in self.children:
            node.print(indent = indent + 1)
