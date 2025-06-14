class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)

        for n in num:   # replace to get max_value
            if n != '9':
                max_ = int(num.replace(n, '9'))
                break
        else:
            max_ = int(num)
        
        for n in num:   # replace to get min_value
            if n != '0':
                min_ = int(num.replace(n, '0'))
                break
        else:
            min_ = int(num)


        return max_ - min_
