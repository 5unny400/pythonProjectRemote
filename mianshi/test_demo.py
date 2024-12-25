from typing import List


class Node:
    def __init__(self, children: int = None, father: int = None):
        self.children = children
        self.father = father


def get_children_ids(id: int, node_list: List[Node]):
    # key为父节点id， value为子节点id
    tmp_dict = {}
    for node in node_list:
        tmp_dict[node.father] = node.children
    res_children_ids = []
    while True:
        if id in tmp_dict:
            res_children_ids.append(tmp_dict[id])
            id = tmp_dict[id]
        else:
            break
    return res_children_ids


node1 = Node(1, 2)
node2 = Node(2, 3)
node3 = Node(3, 4)
node4 = Node(5, 6)
node_list = [node1, node2, node3, node4]
print(get_children_ids(4, node_list))
