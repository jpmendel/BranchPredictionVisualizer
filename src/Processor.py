from InstructionTypeR import *

REGISTERS = [0] * 32

NAME_FROM_REGISTER = [
    'zero', 'at', 'v0', 'v1', 'a0', 'a1', 'a2', 'a3',
    't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7',
    's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
    't8', 't9', 'k0', 'k1', 'gp', 'sp', 's8', 'ra'
]


def process(instructions):
    i = 0

    while i < len(instructions):
        instruction = instructions[i]

        if instruction.is_nop() or instruction.is_syscall():  # TODO: Handle syscall (for fun?)
            i += 1
            continue

        opcode = instruction.get_opcode()

        if opcode == 0x02 or opcode == 0x03:  # TODO: Handle j and jal (change i)
            raise NotImplementedError('j and jal are not handled!')

        rs = instruction.get_rs()
        rt = instruction.get_rt()

        if opcode == 0x00:  # R-Type
            name = NAME_FROM_FUNCT[instruction.get_funct()]
            rd = instruction.get_rd()
            shamt = instruction.get_shamt()

            if name == 'add' or name == 'addu':
                REGISTERS[rd] = REGISTERS[rs] + REGISTERS[rt]
            elif name == 'and':
                REGISTERS[rd] = REGISTERS[rs] & REGISTERS[rt]
            elif name == 'jr':
                pass  # TODO: Set i accordingly.
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
            elif name == 'beq' or name == 'bne':
                pass  # TODO: Handle branching
            elif name == 'ori':
                REGISTERS[rt] = REGISTERS[rs] | immediate  # TODO: Zero-extend immediate
            elif name == 'slti' or name == 'sltiu':
                REGISTERS[rt] = 1 if REGISTERS[rs] < immediate else 0


        print(instruction)
        print('Registers:', REGISTERS)

        i += 1
