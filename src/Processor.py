from InstructionTypeR import *

NAME_FROM_REGISTER = [
    'zero', 'at', 'v0', 'v1', 'a0', 'a1', 'a2', 'a3',
    't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7',
    's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
    't8', 't9', 'k0', 'k1', 'gp', 'sp', 's8', 'ra'
]

REGISTERS = {key: 0 for key in NAME_FROM_REGISTER}


def sign_extend(value, bits):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)


def process(instructions):
    i = 0

    while i < len(instructions):
        instruction = instructions[i]

        if instruction.is_nop():
            i += 1
            continue

        if instruction.is_syscall():
            if REGISTERS['v0'] == 1:  # Print Integer
                print(REGISTERS['a0'])
            elif REGISTERS['v0'] == 10:  # Exit Program
                print('Terminating...')
                return

            i += 1
            continue

        opcode = instruction.get_opcode()

        if opcode == 0x02 or opcode == 0x03:  # TODO: Handle j and jal (change i)
            raise NotImplementedError('j and jal are not handled!')

        rs = NAME_FROM_REGISTER[instruction.get_rs()]
        rt = NAME_FROM_REGISTER[instruction.get_rt()]

        if opcode == 0x00:  # R-Type
            name = NAME_FROM_FUNCT[instruction.get_funct()]
            rd = NAME_FROM_REGISTER[instruction.get_rd()]
            shamt = instruction.get_shamt()

            if name == 'add' or name == 'addu':
                REGISTERS[rd] = REGISTERS[rs] + REGISTERS[rt]
            elif name == 'and':
                REGISTERS[rd] = REGISTERS[rs] & REGISTERS[rt]
            elif name == 'jr':
                i = REGISTERS[rs]
                continue
            elif name == 'nor':
                REGISTERS[rd] = ~(REGISTERS[rs] | REGISTERS[rt])
            elif name == 'or':
                REGISTERS[rd] = REGISTERS[rs] | REGISTERS[rt]
            elif name == 'slt' or name == 'sltu':
                REGISTERS[rd] = 1 if REGISTERS[rs] < REGISTERS[rt] else 0
            elif name == 'sll':
                REGISTERS[rd] = REGISTERS[rt] << shamt
            elif name == 'srl':
                REGISTERS[rd] = REGISTERS[rt] >> shamt
            elif name == 'sub' or name == 'subu':
                REGISTERS[rd] = REGISTERS[rs] - REGISTERS[rt]
        else:  # I-Type
            name = NAME_FROM_OPCODE[opcode]
            immediate = instruction.get_immediate()

            if name == 'addi' or name == 'addiu':
                REGISTERS[rt] = REGISTERS[rs] + immediate
            elif name == 'andi':
                REGISTERS[rt] = REGISTERS[rs] & immediate  # TODO: Zero-extend immediate
            elif name == 'beq':
                if REGISTERS[rs] == REGISTERS[rt]:
                    i += sign_extend(immediate, 15)
                    continue
            elif name == 'bne':
                if REGISTERS[rs] != REGISTERS[rt]:
                    i += sign_extend(immediate, 15)
                    continue
            elif name == 'lui':
                REGISTERS[rt] = immediate << 16
            elif name == 'ori':
                REGISTERS[rt] = REGISTERS[rs] | immediate  # TODO: Zero-extend immediate
            elif name == 'slti' or name == 'sltiu':
                REGISTERS[rt] = 1 if REGISTERS[rs] < immediate else 0

        print(instruction)
        print('Registers:', REGISTERS)

        i += 1
