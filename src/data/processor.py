from data.instruction import NAME_FROM_OPCODE
from data.instruction_r import NAME_FROM_FUNCT
from util.util import *

HI, LO = 0, 0

MEMORY = {}

NAME_FROM_REGISTER = [
    'zero', 'at', 'v0', 'v1', 'a0', 'a1', 'a2', 'a3',
    't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7',
    's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
    't8', 't9', 'k0', 'k1', 'gp', 'sp', 's8', 'ra'
]

REGISTERS = {key: 0 for key in NAME_FROM_REGISTER}  # TODO: May need to clear the values later.

START_PC = 0x00100008


class Processor(object):
    @staticmethod
    def process(instructions):
        i = 0

        while i < len(instructions):
            instruction = instructions[i]

            print('PC:', i, '  Instruction:', instruction)

            if instruction.is_nop():
                i += 1
                continue

            if instruction.is_syscall():
                if REGISTERS['v0'] == 1:  # Print Integer
                    print('SYSCALL - Print Integer:', REGISTERS['a0'])
                elif REGISTERS['v0'] == 10:  # Exit Program
                    print('SYSCALL - Exit Program')
                    return

                i += 1
                continue

            opcode = instruction.get_opcode()

            if opcode == 0x02:  # Jump
                i = instruction.get_jump_address() - START_PC
                continue

            if opcode == 0x03:  # Jump and Link
                REGISTERS['ra'] = i + 2
                i = instruction.get_jump_address() - START_PC
                continue

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
                elif name == 'div' or name == 'divu':
                    Processor.LO = REGISTERS[rs] / REGISTERS[rt]
                    Processor.HI = REGISTERS[rs] % REGISTERS[rt]
                elif name == 'jr':
                    i = REGISTERS[rs]
                    continue
                elif name == 'mfhi':
                    REGISTERS[rd] = Processor.HI
                elif name == 'mflo':
                    REGISTERS[rd] = Processor.LO
                elif name == 'mult' or name == 'multu':
                    product = REGISTERS[rs] * REGISTERS[rt]

                    Processor.HI = (product >> 32) & ((2 ** 32) - 1)
                    Processor.LO = product & ((2 ** 32) - 1)
                elif name == 'nor':
                    REGISTERS[rd] = ~(REGISTERS[rs] | REGISTERS[rt])
                elif name == 'or':
                    REGISTERS[rd] = REGISTERS[rs] | REGISTERS[rt]
                elif name == 'slt' or name == 'sltu':
                    REGISTERS[rd] = 1 if REGISTERS[rs] < REGISTERS[rt] else 0
                elif name == 'sll':
                    REGISTERS[rd] = REGISTERS[rt] << shamt
                elif name == 'sra':
                    REGISTERS[rd] = REGISTERS[rt] >> shamt
                elif name == 'srl':
                    REGISTERS[rd] = Util.logical_right_shift(REGISTERS[rt], shamt)
                elif name == 'sub' or name == 'subu':
                    REGISTERS[rd] = REGISTERS[rs] - REGISTERS[rt]
            else:  # I-Type
                name = NAME_FROM_OPCODE[opcode]
                immediate = instruction.get_immediate()
                sign_extended_immediate = Util.sign_extend(immediate, 15)

                if name == 'addi' or name == 'addiu':
                    REGISTERS[rt] = REGISTERS[rs] + sign_extended_immediate
                elif name == 'andi':
                    REGISTERS[rt] = REGISTERS[rs] & immediate  # TODO: Zero-extend immediate
                elif name == 'beq':
                    if REGISTERS[rs] == REGISTERS[rt]:
                        i += sign_extended_immediate + 1
                        continue
                elif name == 'bne':
                    if REGISTERS[rs] != REGISTERS[rt]:
                        i += sign_extended_immediate + 1
                        continue
                elif name == 'lbu':
                    REGISTERS[rt] = (MEMORY[REGISTERS[rs] + sign_extended_immediate]) & 255
                elif name == 'lhu':
                    REGISTERS[rt] = (MEMORY[REGISTERS[rs] + sign_extended_immediate] & 65535)
                elif name == 'lui':
                    REGISTERS[rt] = immediate << 16
                elif name == 'll' or name == 'lw':
                    REGISTERS[rt] = MEMORY[REGISTERS[rs] + sign_extended_immediate]
                elif name == 'ori':
                    REGISTERS[rt] = REGISTERS[rs] | immediate  # TODO: Zero-extend immediate
                elif name == 'sb':
                    value = MEMORY[REGISTERS[rs] + sign_extended_immediate]
                    value &= ~0xFF
                    value |= (REGISTERS[rt] & 255)
                    MEMORY[REGISTERS[rs] + sign_extended_immediate] = value
                elif name == 'sh':
                    value = MEMORY[REGISTERS[rs] + sign_extended_immediate]
                    value &= ~0xFFFF
                    value |= (REGISTERS[rt] & 65535)
                    MEMORY[REGISTERS[rs] + sign_extended_immediate] = value
                elif name == 'slti' or name == 'sltiu':
                    REGISTERS[rt] = 1 if REGISTERS[rs] < sign_extended_immediate else 0
                elif name == 'sw':
                    MEMORY[REGISTERS[rs] + sign_extended_immediate] = REGISTERS[rt]

            print('\tRegisters:', REGISTERS)
            print('\tMemory:', MEMORY)

            i += 1
