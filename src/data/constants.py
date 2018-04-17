class Constants:
    NAME_FROM_REGISTER = [
        'zero', 'at', 'v0', 'v1', 'a0', 'a1', 'a2', 'a3',
        't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7',
        's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
        't8', 't9', 'k0', 'k1', 'gp', 'sp', 's8', 'ra'
    ]
    NAME_FROM_OPCODE = {
        8:  'addi',   9: 'addiu',
        12: 'andi',   4: 'beq',
        5:  'bne',    2: 'j',
        3:  'jal',   36: 'lbu',
        37: 'lhu',   48: 'll',
        15: 'lui',   35: 'lw',
        13: 'ori',   10: 'slti',
        11: 'sltiu', 40: 'sb',
        41: 'sh',    43: 'sw'
    }
    NAME_FROM_FUNCT = {
        3:  'sra',
        16: 'mfhi', 18: 'mflo',
        24: 'mult', 25: 'multu',
        26: 'div',  27: 'divu',
        32: 'add',  33: 'addu',
        36: 'and',   8:  'jr',
        39: 'nor',  37: 'or',
        42: 'slt',  43: 'sltu',
        0:  'sll',   2:  'srl',
        34: 'sub',  35: 'subu'
    }
