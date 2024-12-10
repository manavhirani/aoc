import numpy as np
from collections import defaultdict
from itertools import combinations


class Solution:
    def calculate_antinodes(self, data: str):
        city_map = [list(row) for row in data.splitlines()]
        city_map = np.array(city_map)

        m, n = city_map.shape

        def inbounds(x, y):
            return x in range(m) and y in range(n)

        locations = np.argwhere(city_map != ".")
        nodes = defaultdict(list)

        for location in locations:
            x, y = location
            frequency = city_map[x, y]
            nodes[frequency].append(location)

        antinodes = 0
        antinode_pos = set()
        for frequency, positions in nodes.items():
            p = len(positions)
            for p1, p2 in combinations(positions, 2):
                x1, y1 = p1
                x2, y2 = p2
                dx = x2 - x1
                dy = y2 - y1
                antinode_pos.add((x1, y1))
                antinode_pos.add((x2, y2))

                x, y = x1 - dx, y1 - dy
                while inbounds(x, y):
                    antinode_pos.add((x, y))
                    x, y = x - dx, y - dy

                x, y = x2 + dx, y2 + dy
                while inbounds(x, y):
                    antinode_pos.add((x, y))
                    x, y = x + dx, y + dy

        print("\n".join([" ".join(row) for row in city_map]))

        return len(antinode_pos)


if __name__ == "__main__":
    data = open("input.in").read()
    s = Solution()
    result = s.calculate_antinodes(data)
    print(result)
