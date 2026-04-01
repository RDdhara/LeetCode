class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        order = sorted(range(n), key = lambda i: positions[i])

        h = healths[:]
        alive = [True] * n
        stack = []

        for i in order:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack:
                    top = stack[-1]

                    if h[top] < h[i]:
                        alive[top] = False
                        stack.pop()
                        h[i] -= 1
                    elif h[top] > h[i]:
                        alive[i] = False
                        h[top] -= 1
                        break
                    else:
                        alive[top] = False
                        alive[i] = False
                        stack.pop()
                        break
        
        return [h[i] for i in range(n) if alive[i]]
