class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        st = set()

        d = (n+1) // 2
        start = 10 ** (d-1)
        end = (10 ** d) - 1

        for num in range(start, end+1):
            left_half = str(num)
            full = ""
            if n % 2 == 0:
                right_half = left_half
                full = left_half + right_half[::-1]
            else:
                right_half = left_half[:-1]
                full = left_half + right_half[::-1]

            number = int(full)
            if number % k != 0:
                continue
            st.add(''.join(sorted(full)))

        factorial = [1]
        for i in range(1, 11):
            factorial.append(factorial[-1] * i)

        result = 0
        for s in st:
            count = [0] * 10
            for i in s:
                count[int(i)] += 1
            total_digit = len(s)
            zeros = count[0]
            non_zeros = total_digit - zeros

            perm = (non_zeros * factorial[total_digit - 1])
            for i in range(10):
                perm //= factorial[count[i]]
            result += perm

        return result
