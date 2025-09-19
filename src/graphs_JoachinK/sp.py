"""
Shortest path algorithms implementation.
"""

import sys
from .heapq import MinHeap

def dijkstra(graph, source):
    """
    Find shortest paths from source vertex to all other vertices using Dijkstra's algorithm.
    
    Args:
        graph (dict): A dictionary representing the weighted graph
                     Format: graph[source][destination] = weight
        source: The starting vertex
    
    Returns:
        tuple: (distances, paths) where:
            - distances (dict): shortest distance from source to each vertex
            - paths (dict): shortest path from source to each vertex
    
    Time Complexity: O((V + E) log V) where V is vertices and E is edges
    Space Complexity: O(V)
    """
    
    # Initialize distances with infinity for all vertices
    distances = {}
    paths = {}
    visited = set()
    
    # Get all vertices in the graph
    all_vertices = set()
    for vertex in graph:
        all_vertices.add(vertex)
        for neighbor in graph[vertex]:
            all_vertices.add(neighbor)
    
    # Initialize distances and paths
    for vertex in all_vertices:
        distances[vertex] = sys.maxsize
        paths[vertex] = []
    
    # Distance to source is 0
    distances[source] = 0
    paths[source] = [source]
    
    # Create min-heap and add source vertex
    heap = MinHeap()
    heap.push((0, source))
    
    while not heap.empty():
        # Get vertex with minimum distance
        current_distance, current_vertex = heap.pop()
        
        # Skip if we've already visited this vertex with a better distance
        if current_vertex in visited:
            continue
        
        # Mark as visited
        visited.add(current_vertex)
        
        # Skip if this distance is outdated
        if current_distance > distances[current_vertex]:
            continue
        
        # Check all neighbors of current vertex
        if current_vertex in graph:
            for neighbor, weight in graph[current_vertex].items():
                # Calculate new distance through current vertex
                new_distance = distances[current_vertex] + weight
                
                # If we found a shorter path to neighbor
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    # Update path to neighbor
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    # Add neighbor to heap with new distance
                    heap.push((new_distance, neighbor))
    
    return distances, paths

def print_shortest_paths(distances, paths, source):
    """
    Helper function to print shortest paths in a readable format.
    
    Args:
        distances (dict): Distance from source to each vertex
        paths (dict): Path from source to each vertex  
        source: Source vertex
    """
    print(f"Shortest distances from vertex {source}:")
    for vertex in sorted(distances.keys()):
        if distances[vertex] == sys.maxsize:
            print(f"  To {vertex}: No path exists")
        else:
            print(f"  To {vertex}: distance = {distances[vertex]}, path = {' -> '.join(map(str, paths[vertex]))}")


def bfs_shortest_path(graph, source, target=None):
    """
    Find shortest paths in an unweighted graph using Breadth-First Search.
    
    Args:
        graph (dict): Dictionary representation of unweighted graph
        source: Starting vertex
        target: Optional target vertex. If None, finds paths to all vertices
    
    Returns:
        tuple: (distances, paths) where:
            - distances (dict): shortest distance (number of edges) from source
            - paths (dict): shortest path from source to each vertex
    """
    from collections import deque
    
    # Initialize
    distances = {source: 0}
    paths = {source: [source]}
    visited = {source}
    queue = deque([source])
    
    while queue:
        current = queue.popleft()
        
        # If we're looking for a specific target and found it, we can stop
        if target and current == target:
            break
            
        # Explore neighbors
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    distances[neighbor] = distances[current] + 1
                    paths[neighbor] = paths[current] + [neighbor]
                    queue.append(neighbor)
    
    return distances, paths

def is_connected(graph):
    """
    Check if an undirected graph is connected (all vertices reachable from any vertex).
    
    Args:
        graph (dict): Dictionary representation of undirected graph
    
    Returns:
        bool: True if graph is connected, False otherwise
    """
    if not graph:
        return True
    
    # Get all vertices
    all_vertices = set()
    for vertex in graph:
        all_vertices.add(vertex)
        for neighbor in graph[vertex]:
            all_vertices.add(neighbor)
    
    if not all_vertices:
        return True
    
    # Run BFS from first vertex
    start_vertex = next(iter(all_vertices))
    distances, _ = bfs_shortest_path(graph, start_vertex)
    
    # Check if all vertices were reached
    return len(distances) == len(all_vertices)