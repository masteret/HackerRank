numOfTC = int(input())
for tc in range(numOfTC):
    graph = {}
    result = {}
    numNode, numEdge = (int(x) for x in input().split())

    for edge in range(numEdge):
        sta, end = (int(x) for x in input().split())
        if sta in graph.keys():
            graph[sta].append(end)
        else:
            graph[sta] = [end]
        if end in graph.keys():
            graph[end].append(sta)
        else:
            graph[end] = [sta]

    startP = int(input())
    def bfs(startP, distance):
        if startP in graph.keys():
            for node in graph[startP]:
                if node not in result.keys():
                    result[node] = distance*6
                    bfs(node, distance+1)
                elif result[node] > distance*6:
                    result[node] = distance*6

    bfs(startP, 1)
    for index in range(2, numNode+1):
        if index in result.keys():
            print(result[index], end=' ')
        else:
            print("-1", end=' ')
    print()