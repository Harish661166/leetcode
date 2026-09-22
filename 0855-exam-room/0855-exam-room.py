class ExamRoom:

    def __init__(self, n: int):
        self.n, self.room = n, []


    def seat(self) -> int:
        if not self.room: ans = 0                           # sit at 0 if empty room 

        else:
            dist, prev, ans = self.room[0], self.room[0], 0 # set best between door and first student   

            for curr in self.room[1:]:                      # check between all pairs of students  
                d = (curr - prev)//2                        # to improve on current best

                if dist < d: dist, ans = d, (curr + prev)//2
                prev = curr

            if dist < self.n - prev-1: ans = self.n - 1     # finally, check whether last seat is best

        insort(self.room, ans)                              # sit down in best seat

        return ans

    def leave(self, p: int) -> None:
        self.room.remove(p)
# param_1 = obj.seat()
# obj.leave(p)