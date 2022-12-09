import time

def get_adjacent_cells(matrix, col, row):
    result = []

    top = []
    at = row
    while at != 0:
        at -= 1
        top.append(matrix[at][col])

    bottom = []
    at = row
    while at != len(matrix)-1:
        at += 1
        bottom.append(matrix[at][col])

    left = []
    at = col
    while at != 0:
        at -= 1
        left.append(matrix[row][at])

    right = []
    at = col
    while at != len(matrix[row])-1:
        at += 1
        right.append(matrix[row][at])

    result.append(top)
    result.append(bottom)
    result.append(left)
    result.append(right)
    return result

def get_scenic_score(matrix, col, row):
    center = matrix[row][col]

    top = []
    at = row
    while at != 0:
        at -= 1
        other = matrix[at][col]
        top.append(other)
        if top[-1] >= center:
            break
    if len(top) == 0:
        return 0

    bottom = []
    at = row
    while at != len(matrix)-1:
        at += 1
        other = matrix[at][col]
        bottom.append(other)
        if bottom[-1] >= center:
            break
    if len(bottom) == 0:
        return 0

    left = []
    at = col
    while at != 0:
        at -= 1
        other = matrix[row][at]
        left.append(other)
        if left[-1] >= center:
            break
    if len(left) == 0:
        return 0

    right = []
    at = col
    while at != len(matrix[row])-1:
        at += 1
        other = matrix[row][at]
        right.append(other)
        if right[-1] >= center:
            break
    if len(right) == 0:
        return 0

    return len(top) * len(bottom) * len(left) * len(right)

def solution1(inputs):
    matrix = []
    for inp in inputs:
        matrix.append(list(map(int, inp)))

    trees_visible = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            adjacents = get_adjacent_cells(matrix, col, row)
            is_visible = False
            for adj in adjacents:
                if len(adj) == 0 or max(adj) < matrix[row][col]:
                    trees_visible += 1
                    break

    return trees_visible

def solution2(inputs):
    matrix_score = []
    matrix = []
    for inp in inputs:
        matrix.append(list(map(int, inp)))
        matrix_score.append([0] * len(inp))

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix_score[row][col] = get_scenic_score(matrix, col, row)

    max_score = 0
    for all_score in matrix_score:
        for score in all_score:
            if score > max_score:
                max_score = score
    return max_score

def main():
    print("Solution 1: " + str(solution1(read_input())))
    print("Solution 2: " + str(solution2(read_input())))

def read_input():
    f = open("input.txt", "r")
    all_lines = f.read().splitlines()
    return all_lines

if __name__ == "__main__":
    main()
