"""
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by moving left, right, up, and down, is indicated in bold red
and is equal to 2297.

  131 673 234 103  18
  201  96 342 965 150
  630 803 746 422 111
  537 699 497 121 956
  805 732 524  37 331

Find the minimal path sum from the top left to the bottom right by moving
left, right, up, and down in matrix.txt, a 31K text file containing a 80 by 80
matrix.

link: https://projecteuler.net/problem=83
"""
import heapq
import math


def solution(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    distance = [[math.inf] * columns for _ in range(rows)]
    distance[0][0] = matrix[0][0]

    # Using Dijkstra's algorithm
    visited = set()
    heap = [(distance[0][0], 0, 0)]
    while heap:
        current_distance, row, column = heapq.heappop(heap)

        if (row, column) in visited:
            continue
        visited.add((row, column))

        # Relax neighbors
        for delta_row, delta_column in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_column = row + delta_row, column + delta_column
            if not(0 <= next_row < rows and 0 <= next_column < columns):
                continue

            new_distance = current_distance + matrix[next_row][next_column]
            if new_distance < distance[next_row][next_column]:
                distance[next_row][next_column] = new_distance
                heapq.heappush(heap, (new_distance, next_row, next_column))

    return distance[-1][-1]



def file_to_matrix(file_path):
    with open(file_path) as f:
        return [list(map(int, line.split(','))) for line in f]


# Test
if __name__ == '__main__':
    print(solution([[131, 673, 234, 103,  18],
                    [201,  96, 342, 965, 150],
                    [630, 803, 746, 422, 111],
                    [537, 699, 497, 121, 956],
                    [805, 732, 524,  37, 331]]))  # 2297

    print(solution(file_to_matrix('resources/0083_matrix.txt')))  # 425185
