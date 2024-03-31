
class Parser:
    def 
    pass
class Code:
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
        raise Exception("Assemble Error!")
    print(out)
    return out

def read_file():
    return "@100"
    pass

def write_file():
    pass

def main():
    print("read file")
    code_file = read_file()
    outs = []
    for instruction in code_file:
        out = assemble(instruction)
        outs.append(out)
    write_file(outs)
    print("done")
    

if __name__ == '__main__':
    main()
