def solution1(inputs):
    elf_code = "ABC"
    my_code = "XYZ"

    total_score = 0
    for inp in inputs:
        elf, me = inp.split()
        total_score += my_code.index(me) + 1
        if elf_code.index(elf) == my_code.index(me):
            total_score += 3
        elif (elf == "A" and me == "Z") or \
            (elf == "B" and me == "X") or \
            (elf == "C" and me == "Y"):
            total_score += 0
        else:
            total_score += 6
    return total_score

def solution2(inputs):
    elf_code = "ABC"
    my_code = "XYZ"

    total_score = 0
    for inp in inputs:
        elf, me = inp.split()
        total_score += 3 * my_code.index(me)
        if me == "Y":
            total_score += elf_code.index(elf) + 1
        elif me == "X":
            if elf == "A": total_score += my_code.index("Z") + 1
            elif elf == "B": total_score += my_code.index("X") + 1
            elif elf == "C": total_score += my_code.index("Y") + 1
        elif me == "Z":
            if elf == "A": total_score += my_code.index("Y") + 1
            elif elf == "B": total_score += my_code.index("Z") + 1
            elif elf == "C": total_score += my_code.index("X") + 1
    return total_score

def main():
    inputs = read_input()
    print("Solution 1: " + str(solution1(inputs)))
    print("Solution 2: " + str(solution2(inputs)))

def read_input():
    f = open("input.txt", "r")
    return f.read().splitlines()

if __name__ == "__main__":
    main();
