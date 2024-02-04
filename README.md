# Python-Assignment
Leetcode problem 130: Surrounded regions
(link:- https://leetcode.com/problems/surrounded-regions/)
The goal of this problem is to capture all regions surrounded by 'X' on a 2D board. Any 'O' that is not on the border and is not connected to an 'O' on the border (directly or via other 'O's) should be flipped to 'X'. Any 'O' on the border or connected to an 'O' on the border should not be flipped.
Approach
The solution uses a Depth-First Search (DFS) algorithm with the following steps:
1) Identify 'O's on the Border: The first step is to traverse the border of the board. For each 'O' found on the border, the algorithm performs a DFS to mark all 'O's connected to it (directly or indirectly) as '#'. This marking process identifies the 'O's that should not be flipped because they are connected to the border.
2) DFS Traversal: The dfs function is used to recursively traverse the board. For each cell that is an 'O' and not yet visited (not marked as '#'), the function marks it as '#' and then recurses to its neighboring cells (up, down, left, right) to mark connected 'O's.
3) Flip the Captured Regions: After marking, the board is traversed again. Cells marked with '#' are changed back to 'O' since they represent 'O's connected to the border and should not be flipped. All other 'O's (not marked) are flipped to 'X' as they are surrounded by 'X's.
4) Time Complexity: O(N*M), where N is the number of rows and M is the number of columns in the board. Each cell is visited at most twice: once during the initial DFS to mark border-connected 'O's and once during the final traversal to flip the cells. Therefore, the time complexity is linear with respect to the total number of cells in the board.
