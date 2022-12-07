import tubemap
# TODO THIS DOESN'T WORK, NEEDS FIXIMG WHEN UNDERSTANDING GRAPHS


def find_path(graph, start, end, path):
    path = [path + [start]]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path):
    path = [path + [start]]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, shortestLength, path):
    shortestLength = -1
    path = [path + [start]]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            if shortestLength == -1 or len(path) < (shortestLength - 1):
                newpath = find_shortest_path(graph, node, end, shortestLength, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
                        shortestLength = len(newpath)
    return shortest


stationFrom = "Tower Hill"
stationTo = "Wimbledon"
print("From: " + stationFrom)
print("To: " + stationTo)
print("Searching shortest route... This may take a while...")
path = find_shortest_path(tubemap, stationFrom, stationTo, find_path(tubemap, stationFrom, stationTo, 0), 0)
print("Suggested Route: ")
print(path)
