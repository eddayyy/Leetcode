class Leaderboard:

    def __init__(self):
        self.leaderboard = defaultdict(int)
    
    def addScore(self, playerId: int, score: int) -> None: 
        self.leaderboard[playerId] += score
 
    def top(self, K: int) -> int:
        return sum(sorted(self.leaderboard.values(), reverse=True) [:K])

    def reset(self, playerId: int) -> None:
        self.leaderboard.pop(playerId)
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)