class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)

        left_close_R = [-1] * n
        right_close_L = [-1] * n

        # check left to right for closest R in left side
        for i in range(n):
            if dominoes[i] == 'L':
                left_close_R[i] = -1
            elif dominoes[i] == 'R':
                left_close_R[i] = i
            else:
                left_close_R[i] = left_close_R[i-1] if i > 0 else -1
            
        # check right to left for closest L in right side
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'R':
                right_close_L[i] = -1
            elif dominoes[i] == 'L':
                right_close_L[i] = i
            else:
                right_close_L[i] = right_close_L[i+1] if i < (n-1) else -1

        # check distance from both side and place dominoes
        dom = ""
        for i in range(n):
            if left_close_R[i] == right_close_L[i]:
                dom += "."
            elif left_close_R[i] == -1:
                dom += "L"
            elif right_close_L[i] == -1:
                dom += "R"
            else:
                dist_r = abs(i - right_close_L[i])
                dist_l = abs(i - left_close_R[i])
                
                if dist_r == dist_l:
                    dom += '.'
                elif dist_r < dist_l:
                    dom += "L"
                else:
                    dom += "R"
            
        return dom
