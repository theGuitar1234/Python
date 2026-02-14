#!/usr/bin/env python3
"""
Docstring for fibo
"""

class Fibonacci:

    """
    Docstring for Fibonacci
    """

    def fibo(self, n):
        prev, next = 0, 1
        for i in range(n):
            current = prev+next
            prev = next
            next = current
        return current