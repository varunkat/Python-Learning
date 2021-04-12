inp1 = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
inp2 = [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

final = []
board = []
res = []
sum = 0
class Leaderboard:


    def addScore(self, playerId: int, score: int):
        self.playerid = playerId
        self.score = score
        board.append([self.playerid, self.score])
        board.sort(key = lambda x:x[0])

    def top(self, K: int) -> int:
        sum = 0
        for i in range(K):
            sum += board[i][1]
        return sum

    def reset(self, playerId: int) -> None:
        for i in board:
            if i[0] == playerId:
                board.remove(i)

for i in range(len(inp1)):
    T = (inp1[i], inp2[i])
    final.append(T)


print(final)


for func in final:
    if func[0] == 'Leaderboard':
        obj = Leaderboard()
        res.append('null')
    elif func[0] == 'addScore':
        obj.addScore(func[1][0], func[1][1])
        res.append('null')
    elif func[0] == 'top':
        param = obj.top(func[1][0])
        res.append(param)
    elif func[0] == 'reset':
        obj.reset(func[1][0])
        res.append('null')


print(board)
print(res)
