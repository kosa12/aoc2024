if __name__ == '__main__':
    with open('input.txt', 'r') as puzzle_input:
        lines = puzzle_input.readlines()
        A = int(lines[0].strip().split(' ')[-1])
        B = int(lines[1].strip().split(' ')[-1])
        C = int(lines[2].strip().split(' ')[-1])
        P = lines[4].strip().split(' ')[-1].split(',')

    instruction_pointer = 0
    output = []

    while instruction_pointer < len(P):
        opcode = int(P[instruction_pointer])
        operand = int(P[instruction_pointer + 1])

        dict_combo = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: A,
            5: B,
            6: C,
            7: 'invalid'
        }

        if opcode == 0:  # adv
            A = A // (2 ** dict_combo[operand])
        elif opcode == 1:  # bxl
            B = B ^ operand
        elif opcode == 2:  # bst
            B = dict_combo[operand] % 8
        elif opcode == 3:  # jnz
            if A != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:  # bxc
            B = B ^ C
        elif opcode == 5:  # out
            output.append(str(dict_combo[operand] % 8))
        elif opcode == 6:  # bdv
            B = A // (2 ** dict_combo[operand])
        elif opcode == 7:  # cdv
            C = A // (2 ** dict_combo[operand])

        instruction_pointer += 2

    print(','.join(output))
