class Solution:
    def maximalRectangle(self, matrix: list[list[str]]):
        index_list = []
        for i in matrix:
            for j in range(len(i)):
                if i[j] == '1':
                    index_list.append(j)
        for i in range(len(index_list) - 1):
            if i == 0 or len(index_list) -1:
                pass
            else:
                pass



if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    result = Solution().maximalRectangle(matrix)
    print(result)