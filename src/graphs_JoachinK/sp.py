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