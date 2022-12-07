def solution1(inputs):
    left = 0
    right = 1

    signal = inputs[0]
    while True:
        if signal[right] in signal[left:right]:
            left += 1
        else:
            right += 1
        if right - left == 4:
            return right
        if right == left:
            right += 1

def solution2(inputs):
    left = 0
    right = 1

    signal = inputs[0]
    while True:
        if signal[right] in signal[left:right]:
            left += 1
        else:
            right += 1
        if right - left == 14:
            return right
        if right == left:
            right += 1

def main():
    print("Solution 1: " + str(solution1(read_input())))
    print("Solution 2: " + str(solution2(read_input())))

def read_input():
    f = open("input.txt", "r")
    all_lines = f.read().splitlines()
    return all_lines

if __name__ == "__main__":
    main()
