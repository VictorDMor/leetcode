'''
DAILY PROBLEM
Leetcode problem 886

Possible Bipartition
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.
Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible 
to split everyone into two groups in this way.

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.
'''

class Solution:
    def possibleBipartition(self, n, dislikes):
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
        color = {}
        for i in range(1, n+1):
            color[i] = 0
        for i in range(1, n+1):
            if color[i] == 0:
                color[i] = 1
                queue = [i]
                while queue:
                    node = queue.pop(0)
                    for neighbor in graph[node]:
                        if color[neighbor] == 0:
                            color[neighbor] = -color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
    print(solution.possibleBipartition(3, [[1,2],[1,3],[2,3]]))
    print(solution.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
    print(solution.possibleBipartition(10, [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]))