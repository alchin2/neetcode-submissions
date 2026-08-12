class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        count = list(Counter(tasks).items())
        pq = []
        for task in count:
            heapq.heappush(pq, -task[1])
            

        max_freq = -heapq.heappop(pq)
        same_max = 1
        

        for freq in pq:
            if -freq == max_freq:
                same_max += 1
                

        ans = (max_freq - 1) * (n + 1) + same_max

        return max(len(tasks), ans)
