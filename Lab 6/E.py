import sys
import heapq
from collections import defaultdict, deque

def solve_alien_order(n, words):
    indeg = {chr(c): 0 for c in range(ord('a'), ord('z')+1)}
    graph = defaultdict(set)
    present = set()
    
    for w in words:
        for ch in w:
            present.add(ch)

    for i in range(n-1):
        w1, w2 = words[i], words[i+1]
        minlen = min(len(w1), len(w2))
        if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
            print(-1)
            return
        for j in range(minlen):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indeg[w2[j]] += 1
                break
    heap = []
    for ch in present:
        if indeg[ch] == 0:
            heapq.heappush(heap, ch)

    order = []
    while heap:
        ch = heapq.heappop(heap)
        order.append(ch)
        for nei in sorted(graph[ch]):
            indeg[nei] -= 1
            if indeg[nei] == 0:
                heapq.heappush(heap, nei)

    if len(order) != len(present):
        print(-1)
    else:
        print("".join(order))


input = sys.stdin.readline
n = int(input())
words = [input().strip() for j in range(n)]
solve_alien_order(n, words)
