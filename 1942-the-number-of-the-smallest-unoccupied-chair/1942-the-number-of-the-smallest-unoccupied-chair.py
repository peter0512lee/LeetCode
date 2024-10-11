class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        vals = []
        for i, (arrival, leaving) in enumerate(times): 
            vals.append((arrival, 1, i))
            vals.append((leaving, 0, i))
        
        k = 0 
        pq = [] # available seats 
        mp = {} # player-to-seat mapping 
        for _, arrival, i in sorted(vals): 
            if arrival: 
                if pq: s = heappop(pq)
                else: 
                    s = k
                    k += 1
                if i == targetFriend: return s
                mp[i] = s
            else: heappush(pq, mp[i]) # new seat available