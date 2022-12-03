def solution1(inputs):
    total = 0
    for inp in inputs:
        sack1 = {}
        sack2 = {}
        half = int(len(inp) // 2)
        for i in range(half):
            if inp[i] not in sack1:
                sack1[inp[i]] = 1
            if inp[i+half] not in sack2:
                sack2[inp[i+half]] = 1
        for k in sack1:
            if k in sack2:
                ans = k
                break
        if ans >= "a" and ans <= "z":
            total += ord(ans) - ord("a") + 1
        else:
            total += ord(ans) - ord("A") + 1 + 26
    return total

def solution2(inputs):
    total = 0
    for i in range(0, len(inputs), 3):
        sack1 = {}
        sack2 = {}
        sack3 = {}
        for j in range(len(inputs[i])):
            if inputs[i][j] not in sack1:
                sack1[inputs[i][j]] = 1
        for j in range(len(inputs[i+1])):
            if inputs[i+1][j] not in sack2:
                sack2[inputs[i+1][j]] = 1
        for j in range(len(inputs[i+2])):
            if inputs[i+2][j] not in sack3:
                sack3[inputs[i+2][j]] = 1
        for k in sack1:
            if k in sack2 and k in sack3:
                ans = k
                break
        if ans >= "a" and ans <= "z":
            total += ord(ans) - ord("a") + 1
        else:
            total += ord(ans) - ord("A") + 1 + 26
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
