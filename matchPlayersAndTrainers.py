class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        i, j= 0, 0
        matched = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i+=1
                j+=1
                matched += 1
            else:
                j+=1

        return matched
