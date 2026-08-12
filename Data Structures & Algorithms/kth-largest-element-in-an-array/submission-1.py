class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a PQ and keep track of largest
        pq = []

        for num in nums:
            heapq.heappush(pq, num)

            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]