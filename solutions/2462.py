class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapify(head_workers)
        heapify(tail_workers)

        next_head, next_tail = candidates, len(costs) - 1 - candidates

        res = 0 
        for _ in range(k): 
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                res += heapq.heappop(head_workers)

                if next_head <= next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                res += heapq.heappop(tail_workers) 

                if next_head <= next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1 

        return res