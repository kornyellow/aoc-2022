def solution1(inputs):
    total = 0
    for inp in inputs:
        range1, range2 = inp.split(",")
        range1 = list(map(int, range1.split("-")))
        range2 = list(map(int, range2.split("-")))

        total += int((range1[0] >= range2[0] and range1[1] <= range2[1]) or \
                    (range2[0] >= range1[0] and range2[1] <= range1[1]))
    return total

def solution2(inputs):
    total = 0
    for inp in inputs:
        range1, range2 = inp.split(",")
        range1 = list(map(int, range1.split("-")))
        range2 = list(map(int, range2.split("-")))

        total += int(not(range1[0] < range2[0] and range1[1] < range2[0]) and \
                not(range1[0] > range2[1] and range1[1] > range2[1]))
    return total

def main():
    inputs = read_input()
    print("Solution 1: " + str(solution1(inputs)))
    print("Solution 2: " + str(solution2(inputs)))

def read_input():
    f = open("input.txt", "r")
    return f.read().splitlines()

if __name__ == "__main__":
    main()
