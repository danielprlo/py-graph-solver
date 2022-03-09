import queue as Q

def search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return

    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))

def run():
    print('run')
    graph = {
        '0': {'3': 12, '5': 4},
        '1': {'2':13, '3': 21, '4': 1},
        '2': {'0':2},
        '3': {'5':1},
        '4': {'0':7},
        '5': {'9':3, '8':8},
        '6': {'4':2, '0':1, '7':12, '8':3},
        '7': {'0':3, '8':21, '9':2},
        '8': {},
        '9': {'6': 1, '8': 4, '5': 4},
    }
    search(graph, '0', '7')

if __name__ == '__main__':
  run()

# V1 -> V3 -> V4 -> V5 -> V6
# Length of the path: 6
