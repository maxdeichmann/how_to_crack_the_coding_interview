class Graph(object):
    def __init__(self):
        self.nodes = []

    def __str__(self):
        output = ""
        for node in self.nodes:
            output += str(node) + "\n"
        return output

    class Node(object):
        def __init__(self, value):
            self.value = value
            self.visited = False
            self.children = []
        
        def __str__(self):
            output = str(self.value)
            output += ":  "
            for child in self.children:
                output += str(child.value) + ", "
            return output
        
    def add_node(self, value):
        new_node = self.Node(value)
        self.nodes.append(new_node)
    
    def add_link(self, node_value, children):
        node = [element for element in self.nodes if element.value == node_value]
        node[0].children = node[0].children + [element for element in self.nodes if element.value in children]


    def route_between_nodes(self, a, b):
        a_node = [node for node in self.nodes if node.value == a ][0]
        b_node = [node for node in self.nodes if node.value == b ][0]
        stack = [[a_node]]
        a_node.visited = True

        while len(stack) > 0:
            node = stack.pop()
            if node[-1].value == b_node.value:
                return [element.value for element in node]
            new_routes = self.new_routes(node)
            stack = new_routes + stack


    
    def new_routes(self, path):
        last_node = path[-1]
        new_paths = []
        for node in last_node.children:
            if node.visited == False:
                node.visited = True
                new_path = path + [node]
                new_paths.append(new_path)
        return new_paths


graph = Graph()
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
# graph.add_node(4)
# graph.add_node(5)
# graph.add_node(6)

graph.add_link(0, [1])
graph.add_link(1, [2])
graph.add_link(2, [0,3])
graph.add_link(3, [2])
# graph.add_link(4, [6])
# graph.add_link(5, [4])
# graph.add_link(6, [5])
        
print(graph)
print(graph.route_between_nodes(0, 3))



