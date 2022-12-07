def solution1(inputs):
    insts, stacks = tuple(inputs)

    for inst in insts:
        _, times, _, move_from, _, move_to = inst.split()
        for _ in range(int(times)):
            stacks[int(move_to)-1].append(stacks[int(move_from)-1].pop())

    res = ""
    for stack in stacks:
        res += stack.pop()
    return res

def solution2(inputs):
    insts, stacks = tuple(inputs)

    for inst in insts:
        _, times, _, move_from, _, move_to = inst.split()
        for i in range(int(times)):
            stacks[int(move_to)-1].append(stacks[int(move_from)-1].pop(-int(times)+i))

    res = ""
    for stack in stacks:
        res += stack.pop()
    return res

def main():
    print("Solution 1: " + str(solution1(read_input())))
    print("Solution 2: " + str(solution2(read_input())))

def read_input():
    f = open("input.txt", "r")
    all_lines = f.read().splitlines()

    height = 0
    for line in all_lines:
        height += 1
        if line == "":
            break

    towers = 0
    for c in all_lines[height-2]:
        if c != " ":
            towers += 1

    insts = all_lines[height:]

    stacks = []
    for _ in range(towers):
        stacks.append([])

    stack_pictures = all_lines[:height-2]
    for stack_picture in stack_pictures:
        for i in range(towers):
            if stack_picture[(i*4)+1].isalpha():
                stacks[i].insert(0, stack_picture[(i*4)+1])
    return [insts, stacks]

if __name__ == "__main__":
    main()
