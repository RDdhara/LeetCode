class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        columns = n // rows

        result = ""

        for i in range(columns):
            for j in range(i, n, columns + 1):
                result += encodedText[j]
        
        return result.rstrip()
