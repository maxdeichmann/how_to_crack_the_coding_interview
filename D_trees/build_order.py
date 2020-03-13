from functools import reduce

class Graph(object):

    def __init__(self):
        self.nodes = []

    def __str__(self):

        return reduce(lambda x, y: str(x) + "\n" + str(y), self.nodes)


    class Node(object):
        def __init__(self, value):
            self.value = value
            self.dependencies = []
        
        def add_dependency(self, node):
            self.dependencies.append(node)
        
        def get_dependencies(self):
            return self.dependencies
        
        def remove_dependency(self, node):
            self.dependencies.remove(node)
        
        def __str__(self):
            return str(self.value) + ", dep: " + ",".join([node.value for node in self.dependencies])

    def create_node(self, project):
        self.nodes.append(self.Node(project))

    def get_nodes(self):
        return self.nodes


    def find_sequence(self):
        seq = []


        while len(seq) < len(graph.get_nodes()):

            for node in self.nodes:
                if len(node.get_dependencies()) == 0 and node not in seq:
                    seq.append(node)
            for initialised_node in seq:
                for node in self.nodes:
                    if initialised_node in node.get_dependencies():
                        node.remove_dependency(initialised_node)
        return [str(node.value) for node in seq]


def build_graph(projects, dependencies):

    graph = Graph()

    for project in projects:
        graph.create_node(project)

    for key in dependencies:
        evaluated_node = [node for node in graph.get_nodes() if node.value == key][0]

        for node_value in dependencies[key]:
            for node in graph.get_nodes():
                if node.value == node_value:
                    evaluated_node.add_dependency(node)
    return graph



projects = ["a", "b", "c", "d", "e", "f", "g"]
dependencies = {
    "a": ["c", "f", "b"],
    "b": ["f"],
    "c": ["f"],
    "d": [],
    "e": ["a", "b"],
    "f": [],
    "g": ["d"],
}
    
# run
graph = build_graph(projects, dependencies)
print(graph)
seq = graph.find_sequence()
print(seq)
