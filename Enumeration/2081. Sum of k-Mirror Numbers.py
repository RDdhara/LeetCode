class Solution:
    def convert_base_k(self, num, k):
        if num == 0:
            return '0'
        result = ""
        while num > 0:
            result += str(num % k)
            num //= k
        return result

    def kMirror(self, k: int, n: int) -> int:
        sum_ = 0
        l = 1 # lenght of palindrom

        while n > 0:
            half_len = (l+1) // 2
            min_num = 10**(half_len - 1)
            max_num = 10**half_len - 1

            for num in range(min_num, max_num + 1):
                first_half = str(num)
                second_half = first_half[::-1]

                pal = ""
                if l % 2 == 0:
                    pal = first_half + second_half
                else:
                    pal = first_half + second_half[1:]

                pal_num = int(pal)
                base_k  = self.convert_base_k(pal_num, k)

                if base_k == base_k[::-1]:
                    sum_ += pal_num
                    n -= 1
                    if n == 0:
                        break
            l += 1

        return sum_
                
