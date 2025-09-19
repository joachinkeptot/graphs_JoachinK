"""
Test cases for the graphs_JoachinK package.
"""

import sys
sys.path.insert(0, 'src')

from graphs_JoachinK import sp
from graphs_JoachinK.heapq import MinHeap

def test_min_heap():
    """Test the MinHeap implementation."""
    print("Testing MinHeap...")
    
    heap = MinHeap()
    
    # Test empty heap
    assert heap.empty() == True
    assert heap.size() == 0
    assert heap.pop() == None
    
    # Test adding elements
    heap.push((5, 'five'))
    heap.push((1, 'one'))
    heap.push((3, 'three'))
    heap.push((2, 'two'))
    
    assert heap.size() == 4
    assert heap.empty() == False
    
    # Test popping in sorted order
    assert heap.pop() == (1, 'one')
    assert heap.pop() == (2, 'two')
    assert heap.pop() == (3, 'three')
    assert heap.pop() == (5, 'five')
    
    assert heap.empty() == True
    print("✓ MinHeap tests passed!")

def test_dijkstra_simple():
    """Test Dijkstra's algorithm with a simple graph."""
    print("Testing Dijkstra's algorithm (simple case)...")
    
    # Create a simple graph: 0 -> 1 (weight 4), 0 -> 2 (weight 2), 1 -> 2 (weight 1)
    graph = {
        0: {1: 4, 2: 2},
        1: {2: 1},
        2: {}
    }
    
    distances, paths = sp.dijkstra(graph, 0)
    
    # Check distances
    assert distances[0] == 0
    assert distances[1] == 4
    assert distances[2] == 2
    
    # Check paths
    assert paths[0] == [0]
    assert paths[1] == [0, 1]
    assert paths[2] == [0, 2]
    
    print("✓ Simple Dijkstra test passed!")

def test_dijkstra_assignment_example():
    """Test Dijkstra's algorithm with the example from the assignment."""
    print("Testing Dijkstra's algorithm (assignment example)...")
    
    # Create the graph from the assignment (9 vertices)
    graph = {
        0: {1: 4, 7: 8},
        1: {0: 4, 2: 8, 7: 11},
        2: {1: 8, 3: 7, 8: 2, 5: 4},
        3: {2: 7, 4: 9, 5: 14},
        4: {3: 9, 5: 10},
        5: {2: 4, 3: 14, 4: 10, 6: 2},
        6: {5: 2, 7: 1, 8: 6},
        7: {0: 8, 1: 11, 6: 1, 8: 7},
        8: {2: 2, 6: 6, 7: 7}
    }
    
    distances, paths = sp.dijkstra(graph, 0)
    
    # Test some key distances from the assignment
    assert distances[0] == 0
    assert distances[1] == 4
    assert distances[7] == 8
    assert distances[6] == 9  # 0 -> 7 -> 6 = 8 + 1 = 9
    assert distances[8] == 14  # Better path found by algorithm
    
    print("✓ Assignment example test passed!")

def test_file_format():
    """Test that the package can be used as shown in the assignment."""
    print("Testing assignment usage format...")
    
    # Simulate the graph loading format from assignment
    graph = {}
    test_data = [
        "0 1 4",
        "0 7 8", 
        "1 0 4",
        "1 2 8",
        "1 7 11"
    ]
    
    for line in test_data:
        s, d, w = line.split()
        s = int(s)
        d = int(d)
        w = int(w)
        if s not in graph:
            graph[s] = {}
        graph[s][d] = w
    
    # Test the function call format from assignment
    source = 0
    dist, path = sp.dijkstra(graph, source)
    
    # Verify it returns the expected format
    assert isinstance(dist, dict)
    assert isinstance(path, dict)
    assert dist[0] == 0
    
    print("✓ Assignment format test passed!")

def test_disconnected_graph():
    """Test Dijkstra with disconnected components."""
    print("Testing disconnected graph...")
    
    graph = {
        0: {1: 5},
        1: {},
        2: {3: 2},
        3: {}
    }
    
    distances, paths = sp.dijkstra(graph, 0)
    
    # Vertex 0 and 1 should be reachable
    assert distances[0] == 0
    assert distances[1] == 5
    
    # Vertices 2 and 3 should be unreachable (infinite distance)
    assert distances[2] == sys.maxsize
    assert distances[3] == sys.maxsize
    
    print("✓ Disconnected graph test passed!")

def test_bfs():
    """Test BFS shortest path algorithm."""
    print("Testing BFS shortest path...")
    
    # Create unweighted graph: 0-1-2-3, 0-4
    graph = {
        0: [1, 4],
        1: [0, 2],
        2: [1, 3],
        3: [2],
        4: [0]
    }
    
    distances, paths = sp.bfs_shortest_path(graph, 0)
    
    # Check distances (number of edges)
    assert distances[0] == 0
    assert distances[1] == 1  # 0 -> 1
    assert distances[2] == 2  # 0 -> 1 -> 2
    assert distances[3] == 3  # 0 -> 1 -> 2 -> 3
    assert distances[4] == 1  # 0 -> 4
    
    # Check paths
    assert paths[0] == [0]
    assert paths[1] == [0, 1]
    assert paths[2] == [0, 1, 2]
    assert paths[3] == [0, 1, 2, 3]
    assert paths[4] == [0, 4]
    
    print("✓ BFS tests passed!")

def test_graph_connectivity():
    """Test graph connectivity checker."""
    print("Testing graph connectivity...")
    
    # Connected graph
    connected_graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    assert sp.is_connected(connected_graph) == True
    
    # Disconnected graph
    disconnected_graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    assert sp.is_connected(disconnected_graph) == False
    
    # Single vertex
    single_vertex = {0: []}
    assert sp.is_connected(single_vertex) == True
    
    # Empty graph
    empty_graph = {}
    assert sp.is_connected(empty_graph) == True
    
    print("✓ Graph connectivity tests passed!")

if __name__ == '__main__':
    print("Running tests for graphs_JoachinK package...\n")
    
    try:
        test_min_heap()
        test_dijkstra_simple()
        test_dijkstra_assignment_example()
        test_file_format()
        test_disconnected_graph()
        test_bfs()
        test_graph_connectivity()
        
        print("\n🎉 All tests passed! Your implementation is working correctly.")
        print("📈 Bonus algorithms (BFS + connectivity) implemented successfully!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)