class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        len_s = len(s)
        letter_count = s.count(letter)
        return int(letter_count / len_s * 100)

if __name__ == '__main__':
    s = 'foobar'
    letter = 'o'
    result = Solution().percentageLetter(s, letter)
    print(result)