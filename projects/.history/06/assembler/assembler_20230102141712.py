
class Parser:
    line = 0
    def __init__(self, instruction):
        print(instruction)
        pass
    def comp(self):
        pass
    def dest(self):
        pass
    def jump(self):
        pass
    def value(self):
        pass
    def instruction_type(self):
        pass

class Code:
    def __init__(self):
        pass
    def comp(self):
        pass
    def dest(self):
        pass
    def jump(self):
        pass
    def value(self):
        pass

class SymbolTable:
    pass

def assemble(instruction):
    code = Code()
    parser = Parser(instruction)
    if parser.instruction_type() == 'c':
        c = parser.comp()
        d = parser.dest()
        j = parser.jump()
        cc = code.comp(c)
        dd = code.dest(d)
        jj = code.jump(j)
        out = '111' + cc + dd + jj 
    elif parser.instruction_type() == 'a':
        v = parser.value()
        out = '0' + code.value(v)
    else:
        # for comment and white line
        out = None
    print(out)
    return out

def read_file():
    return "@100"
    pass

def write_file(outs):
    print(outs)
    pass

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
