from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid):
        rows, cols = len(grid), len(grid[0])

        start_row = start_col = 0
        target_mask = 0

        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]

                if cell == "@":
                    start_row, start_col = row, col

                elif "a" <= cell <= "f":
                    target_mask |= 1 << (ord(cell) - ord("a"))

        queue = deque([(start_row, start_col, 0, 0)])
        visited = {(start_row, start_col, 0)}

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            row, col, key_mask, steps = queue.popleft()

            if key_mask == target_mask:
                return steps

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue

                cell = grid[new_row][new_col]

                if cell == "#":
                    continue

                new_mask = key_mask

                if "a" <= cell <= "f":
                    new_mask |= 1 << (ord(cell) - ord("a"))

                if "A" <= cell <= "F":
                    if not (new_mask & (1 << (ord(cell) - ord("A")))):
                        continue

                state = (new_row, new_col, new_mask)

                if state not in visited:
                    visited.add(state)
                    queue.append((new_row, new_col, new_mask, steps + 1))

        return -1