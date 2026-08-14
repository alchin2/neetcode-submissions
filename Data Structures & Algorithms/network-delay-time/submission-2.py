import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        all_nodes = set(i for i in range(1, n+1))
        visited = set()

        heap = [(0, k)]  # (time, node)
        ans = 0

        while heap:
            time, curr = heapq.heappop(heap)
            
            if curr in visited:
                continue
                
            visited.add(curr)
            
            print(curr, time)
            ans = max(ans, time)

            for query in times:
                u, v, t = query
                # look for u --> v
                if u == curr and v not in visited:
                    heapq.heappush(heap, (time+t, v))

        return ans if (visited == all_nodes) else -1
