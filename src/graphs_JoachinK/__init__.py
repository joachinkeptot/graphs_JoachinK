"""
graphs_JoachinK - A Python library for graph algorithms

This package provides implementations of fundamental graph algorithms,
starting with Dijkstra's shortest path algorithm.
"""

__version__ = "0.1.0"
__author__ = "Joachin K"

# Import main modules for easy access
from . import sp
from . import heapq

# Make key functions available at package level
from .sp import dijkstra, print_shortest_paths

__all__ = ['sp', 'heapq', 'dijkstra', 'print_shortest_paths']