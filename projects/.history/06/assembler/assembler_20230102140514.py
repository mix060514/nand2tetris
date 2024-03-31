
class Parser:
    pass
class Code:
    pass
class SymbolTable:
    pass

def read_file():
    pass

def write_file():
    pass

def main():
    code_file = read_file()
    code = Code()
    outs = []
    line = 0
    for instruction in code_file:
        parser, line = Parser(instruction, line)
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
        outs.append()
    write_file(outs)
    

if __name__ == '__main__':
    main()
