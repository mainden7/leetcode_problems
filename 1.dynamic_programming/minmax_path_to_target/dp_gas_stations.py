# https://leetcode.com/problems/minimum-number-of-refueling-stops
import heapq
from typing import List

class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        if target <= startFuel:
            return 0
        else:
            if not stations:
                return -1
        last_station = stations[-1]
        if last_station[0] < target:
            stations.append([target, 0])

        queue = []
        p = result = 0
        print(f"START: {startFuel=}")
        for i, (dest, gas) in enumerate(stations):

            startFuel -= dest - p
            print(f"{dest=}, {gas=}, {p=}, {startFuel=}, {queue=}")
            while queue and startFuel < 0:
                startFuel += -heapq.heappop(queue)
                result += 1
                print(f"FILLED TANK {result=}, {startFuel=}")
            if startFuel < 0:
                return -1
            heapq.heappush(queue, -gas)
            p = dest

        return result




if __name__ == "__main__":
    print(
        Solution().minRefuelStops(
            100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]
        )
    )
