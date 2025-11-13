from typing import Optional, Self

LIMIT = 10000


class Node:
    def __init__(self, label: str | int, value: int = LIMIT):
        self.label = label
        self.node_to: list[tuple[Self, int]] = []
        self.value = value
        self.previous_node: Optional[Self] = None

    def __repr__(self) -> str:
        neighbors = [(node.label, weight) for node, weight in self.node_to]
        return f"Node({self.label}, val={self.value}) -> {neighbors} -> prev -> {self.previous_node.label if self.previous_node else None}\n"

    def __str__(self) -> str:
        neighbors = [(node.label, weight) for node, weight in self.node_to]
        return f"{self.label} -> {neighbors}\n"


class Graph:
    def __init__(self):
        self.nodes: list[Node] = []
        self.nodes_map: dict[str | int, Node] = {}

    def _reset(self):
        for node in self.nodes:
            node.value = LIMIT
            node.previous_node = None

    def add_nodes(self, *labels):
        for label in labels:
            self.add_node(label)

    def add_node(self, label: Optional[str | int]):
        if not label:
            label = len(self.nodes) + 1
        node = Node(label)
        self.nodes.append(node)
        self.nodes_map[label] = node

    def add_arc(self, node_from_label: str | int, node_to_label: str | int, value: int):
        node_to = self.nodes_map[node_to_label]
        node_from = self.nodes_map[node_from_label]
        node_from.node_to.append((node_to, value))

    def _return_value(self, node: Node):
        return node.value

    def shortest_path(self, label_start: str | int = 0):
        self._reset()
        self.nodes_map[label_start].value = 0
        unvisited_nodes = self.nodes.copy()
        while len(unvisited_nodes) != 0:
            current_node = min(unvisited_nodes, key=self._return_value)

            for arc in current_node.node_to:
                node, value = arc
                new_value = value + current_node.value
                if node.value >= new_value:
                    node.value = new_value
                    node.previous_node = current_node

            unvisited_nodes.remove(current_node)


if __name__ == "__main__":
    G = Graph()
    G.add_nodes("A", "B", "C", "D", "E", "F")

    G.add_arc("A", "B", 2)
    G.add_arc("A", "D", 8)
    G.add_arc("B", "D", 5)
    G.add_arc("B", "E", 6)
    G.add_arc("D", "E", 3)
    G.add_arc("D", "F", 2)
    G.add_arc("E", "F", 1)
    G.add_arc("E", "C", 9)
    G.add_arc("F", "C", 3)

    G.shortest_path("D")
    print(G.nodes)
    G.shortest_path("A")
    print(G.nodes)
    G.shortest_path("C")
    print(G.nodes)
