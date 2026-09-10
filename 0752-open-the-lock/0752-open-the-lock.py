class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead or target in dead: return -1
        front, back = {'0000'}, {target}
        steps = 0
        while front and back:
            if len(front) > len(back): front, back = back, front
            nxt = set()
            for code in front:
                if code in back: return steps
                if code in dead: continue
                dead.add(code)
                for i in range(4):
                    digit = int(code[i])
                    for move in (-1, 1):
                        neighbor = code[:i] + str((digit + move) % 10) + code[i+1:]
                        if neighbor not in dead:
                            nxt.add(neighbor)
            front = nxt
            steps += 1
        return -1