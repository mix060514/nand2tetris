import re 
import sys
class Parser:
    line = 0
    def __init__(self, instruction):
        print(f"instruction: {instruction}")
        self.instruction = instruction
    def comp(self):
        ins = self.instruction
        if ins.find(';') != -1:
            pos = ins.find(';')
            ins = ins[:pos]
        if ins.find('=') != -1:
            pos = ins.find('=')
            ins = ins[pos+1:]
        return ins.strip()
    def dest(self):
        ins = self.instruction
        if ins.find('//') != -1:
            pos = ins.find('//') 
            ins = ins[:pos]
        if ins.find('=') != -1:
            pos = ins.find('=') 
            ins = ins[:pos]
        else:
            ins = 'null'
        return ins.strip()
    def jump(self):
        ins = self.instruction
        if ins.find('//') != -1:
            pos = ins.find('//') 
            ins = ins[:pos]
        if ins.find(';') != -1:
            pos = ins.find(';') 
            ins = ins[pos+1:]
        else:
            ins = 'null'
        return ins.strip()
    def value(self):
        m = re.search("@\s*(?P<value>\d+)", self.instruction)
        return m.group('value')
    def instruction_type(self):
        if len(self.instruction) == 0:
            return None
        elif self.instruction[:2] == '//':
            return None
        elif self.instruction[0] == '@':
            return 'a'
        else:
            return 'c'

class Code:
    def __init__(self):
        self.comp_table = {
            '0': '0101010',
            '1': '0111111',
            '-1': '0111010',
            'D': '0001100',
            'A': '0110000',
            '!D': '0001101',
            '!A': '0110001',
            '-D': '0001111',
            '-A': '0110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'D+A': '0000010',
            'D-A': '0010011',
            'A-D': '0000111',
            'D&A': '0000000',
            'D|A': '0010101',
            'M': '1110000',
            '!M': '1110001',
            '-M': '1110011',
            'M+1': '1110111',
            'M-1': '1110010',
            'D+M': '1000010',
            'D-M': '1010011',
            'M-D': '1000111',
            'D&M': '1000000',
            'D|M': '1010101',
        }
        self.dest_table = {
            'null' : '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111',
        }
        self.jump_table = {
            'null': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
        }
    def comp(self, c):
        c = self.comp_table.get(c)
        if c:
            return c
        else: 
            raise Exception('comp value not found')
    def dest(self, d):
        d = self.dest_table.get(d)
        if d:
            return d
        else: 
            raise Exception('dest value not found')
    def jump(self, j):
        j = self.jump_table.get(j)
        if j:
            return j
        else: 
            raise Exception('jump value not found')
    def value(self, v):
        binary_value = bin(int(v), )[2:]
        return f"{binary_value:>015}"

class SymbolTable:
    pass

def assemble(instruction):
    if instruction.find('//') != -1:
        pos = instruction.find('//')
        instruction = instruction[:pos]
    instruction = instruction.strip()
    if len(instruction) == 0:
        return None
    
    code = Code()
    parser = Parser(instruction)
    print(f"instruction_type: {parser.instruction_type()}")
    if parser.instruction_type() == 'c':
        c = parser.comp()
        d = parser.dest()
        j = parser.jump()
        print(f"c = {c},d = {d},j = {j}")
        cc = code.comp(c)
        dd = code.dest(d)
        jj = code.jump(j)
        out = '111' + cc + dd + jj 
    elif parser.instruction_type() == 'a':
        v = parser.value()
        print(f"v = {v}")
        out = '0' + code.value(v)
    else:
        # for comment and white line
        out = None
    print(f"out: {out}")
    return out

def read_file(filename):
    return ["@100", "@ 50", "D=M+1","MD=D+1", "@R1", "(LOOP)", "(STOP)", "@R15", "D=M"]
    # with open(filename, 'rt') as f:
    #     w = f.readlines()
    # return w


def write_file(outs, filename):
    w = '\n'.join(outs)
    print(f"outs: {w}")
    # with open(filename, 'wt') as f:
        # f.write(w)
     

def main():
    print("read file")
    # filename = sys.argv[1]
    filename = ""
    print(filename)
    code_file = read_file(filename)
    # print(code_file)
    outs = []
    for instruction in code_file:
        print(instruction)
        out = assemble(instruction)
        if out:
            outs.append(out)
    write_file(outs, filename.split('.asm')[0]+'.hack')
    print("done")
    

if __name__ == '__main__':
    # filename = r'D:\nand2tetris\projects\06\assembler\Add.asm'
    main()
