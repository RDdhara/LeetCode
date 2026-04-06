class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        st = set()

        for obs in obstacles:
            key = str(obs[0]) + "_" + str(obs[1])
            st.add(key)
        
        x = 0
        y = 0
        max_dis = 0
        dir_ = [0, 1]

        for i in range(len(commands)):
            if commands[i] == -2:   # turn 90 degree left
                dir_ = [-dir_[1], dir_[0]]
            elif commands[i] == -1: # turn 90 degree right
                dir_ = [dir_[1], -dir_[0]]
            else:                   # move step by step
                for step in range(commands[i]):
                    new_x = x + dir_[0]
                    new_y = y + dir_[1]

                    next_key = str(new_x) + "_" + str(new_y)

                    if next_key in st:
                        break
            
                    x = new_x
                    y = new_y
            
            max_dis = max(max_dis, x*x + y*y)
        
        return max_dis
