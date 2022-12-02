def solution1(inputs):
    elfs = []
    total = 0
    for inp in inputs:
        if inp != '':
            total += int(inp)
        else:
            elfs.append(total)
            total = 0
    return max(elfs)

def solution2(inputs):
    elfs = []
    total = 0
    for inp in inputs:
        if inp != '':
            total += int(inp)
        else:
            elfs.append(total)
            total = 0
    top_elfs = []
    for _ in range(3):
        top_elfs.append(elfs.pop(elfs.index(max(elfs))))
    return sum(top_elfs)

def main():
    inputs = read_input()
    print("Solution 1: " + str(solution1(inputs)))
    print("Solution 2: " + str(solution2(inputs)))

def read_input():
    f = open("input.txt", "r")
    return f.read().splitlines()

if __name__ == "__main__":
    main();
