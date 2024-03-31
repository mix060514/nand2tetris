import re 
class Parser:
    line = 0
    def __init__(self, instruction):
        print(f"instruction: {instruction}")
        self.instruction = instruction
    def comp(self):
        pass
    def dest(self):
        pass
    def jump(self):
        pass
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
        pass
    def comp(self):
        pass
    def dest(self):
        pass
    def jump(self):
        pass
    def value(self, v):
        return bin(v)[2:]
    

class SymbolTable:
    pass

def assemble(instruction):
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

def read_file():
    return ["@100"]

def write_file(outs):
    print(f"outs: {outs}")

def main():
    print("read file")
    code_file = read_file()
    outs = []
    for instruction in code_file:
        out = assemble(instruction)
        if out:
            outs.append(out)
    write_file(outs)
    print("done")
    

if __name__ == '__main__':
    main()
