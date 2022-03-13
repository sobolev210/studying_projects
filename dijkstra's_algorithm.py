infinity = float("inf")
graph = dict()
graph['book'] = {"rare lp": 5, "poster": 0}
graph["rare lp"] = {"bass guitar": 15, "drums": 20}
graph["poster"] = {"bass guitar": 30, "drums": 35}
graph["bass guitar"] = {"piano": 20}
graph["drums"] = {"piano": 10}
graph["piano"] = {}

table = {'rare lp': {'parent': 'book', 'cost': 5},
         'poster': {'parent': 'book', 'cost': 0},
         'bass guitar': {'parent': None, 'cost': infinity},
         'drums': {'parent': None, 'cost': infinity},
         'piano': {'parent': None, 'cost': infinity}}


def find_node_with_lowest_cost(table, checked):
    lowest_cost = float('inf')
    result_node = None
    for key in table:
        cost = table[key]['cost']
        if key not in checked and cost < lowest_cost:
            lowest_cost = cost
            result_node = key
    return result_node

checked = []
node = find_node_with_lowest_cost(table, checked)
while node:
    neighbors = graph.get(node)
    for name, cost in neighbors.items():

        new_cost = cost + table[node]['cost']
        if new_cost < table[name]['cost']:
            table[name]['cost'] = new_cost
            table[name]['parent'] = node
    checked.append(node)
    node = find_node_with_lowest_cost(table, checked)

print("Final table: ", table)
start_node = 'book'
end_node = 'piano'
parent = table[end_node]['parent']
path = end_node

while parent != start_node:
    path += "<-" + parent
    parent = table[parent]['parent']
path += "<-" + start_node
path = "->".join(reversed(path.split("<-")))

print("Final path: ", path)


