
from enum import Enum, auto

class CommandType(Enum):
    C_ARITHMETIC = auto()
    C_PUSH = auto()
    C_POP = auto()
    C_LABEL = auto()
    C_GOTO = auto()
    C_IF = auto()
    C_FUNCTION = auto()
    C_RETURN = auto()
    C_CALL = auto()

    def __str__(self):
            return self.name.lower().replace('c_', '')

class Parser():
    def __init__(self, fp):
        self.lines = self._process_input(fp)
        self.current_index = -1

    @property
    def current_command(self) -> str:
        return self.lines[self.current_index]

    def _process_input(self, fp):
        with open(fp, 'rt') as f:
            lines = f.readlines()
        # ignroe space line
        lines = [line for line in lines if line != '\n']
        # ignroe comments
        lines = [line for line in lines if line[:2] != '//']
        # ignore line command after command
        lines = [line.split('//')[0] for line in lines]
        # ignore 2 space and more 
        lines = [line.strip() for line in lines]

        return lines

    def hasMoreCommands(self) -> bool:
        if self.current_index < len(self.lines) - 1:
            return True
        return False

    def advance(self):
        self.current_index += 1

    def commandType(self) -> CommandType:
        command_type = self.current_command.split(' ')[0]
        if command_type in 'add,sub,neg,eq,gt,lt,and,or,not'.split(','):
            return CommandType.C_ARITHMETIC
        if command_type == 'pop':
            return CommandType.C_POP
        if command_type == 'push':
            return CommandType.C_PUSH
        if command_type == 'label':
            return CommandType.C_LABEL
        if command_type == 'goto':
            return CommandType.C_GOTO
        if command_type == 'if-goto':
            return CommandType.C_IF
        if command_type == 'function':
            return CommandType.C_FUNCTION
        if command_type == 'call':
            return CommandType.C_CALL
        if command_type == 'return':
            return CommandType.C_FUNCTION
        raise ValueError()


    def arg1(self) -> str:
        split_s = self.current_command.split(' ')
        if self.commandType() == CommandType.C_RETURN:
            raise ValueError()
        if self.commandType() == CommandType.C_ARITHMETIC:
            return split_s[0]
        return split_s[1]

    def arg2(self) -> int:
        if self.commandType() not in [CommandType.C_PUSH, CommandType.C_POP, CommandType.C_FUNCTION, CommandType.C_CALL]:
            raise ValueError()
        return int(self.current_command.split(' ')[2])


class CodeWriter():
    def __init__(self, fp):
        self.fn = fp.split('/')[-1].split('\\')[-1].split('.')[0]
        self.fp = self.fn + '.asm'
        self.lines = []
        self.cnt = 0

    def writeArithmetic(self, command: str):
        self.lines.append('// ' + command)
        if command in ['neg','not']:
            if command == 'neg':
                self.lines.append('@SP')
                self.lines.append('A=M-1')
                self.lines.append('M=-M')
            elif command == 'not':
                self.lines.append('@SP')
                self.lines.append('A=M-1')
                self.lines.append('M=!M')
        else:
            self.lines.append('@SP')
            self.lines.append('A=M-1')
            self.lines.append('D=M')
            self.lines.append('A=A-1')
            if command == 'add':
                self.lines.append('M=M+D')
            elif command == 'sub':
                self.lines.append('M=M-D')

            elif command in ['eq', 'gt', 'lt']:
                self.lines.append('D=M-D')
                self.lines.append(f'@If_True_{self.cnt}')
                if command == 'eq':
                    self.lines.append('D;JEQ')
                elif command == 'gt':
                    self.lines.append('D;JGT')
                elif command == 'lt':
                    self.lines.append('D;JLT')
                # if false
                self.lines.append('D=0')
                # to end if
                self.lines.append(f'@End_If_{self.cnt}')
                self.lines.append('1;JMP')
                # if true
                self.lines.append(f'(If_True_{self.cnt})')
                self.lines.append('D=-1')
                # end if 
                self.lines.append(f'(End_If_{self.cnt})')
                self.lines.append('@SP')
                self.lines.append('A=M-1')
                self.lines.append('A=A-1')
                self.lines.append('M=D')

            elif command == 'and':
                self.lines.append('M=M&D')
            elif command == 'or':
                self.lines.append('M=M|D')
            self.lines.append('D=A+1')
            self.lines.append('@SP')
            self.lines.append('M=D')
            self.cnt += 1

    def writePushPop(self, command: str, segment: str, index: int):
        self.lines.append(f'// {command} {segment} {index}')
        if segment == 'constant':
            if command == CommandType.C_PUSH:
                self.lines.append(f'@{index}')
                self.lines.append('D=A')
                self.lines.append('@SP')
                self.lines.append('A=M')
                self.lines.append('M=D')
                self.lines.append('@SP')
                self.lines.append('M=M+1')
        elif segment in ['local', 'argument', 'this', 'that']:
            if segment == 'local':
                key = 'LCL'
            elif segment == 'argument':
                key = 'ARG'
            elif segment == 'this':
                key = 'THIS'
            elif segment == 'that':
                key = 'THAT'
            if command == CommandType.C_POP:
                # LCL = LCL + i
                self.lines.append(f'@{index}')
                self.lines.append('D=A')
                self.lines.append(f'@{key}')
                self.lines.append('M=M+D')
                # SP--
                self.lines.append('@SP')
                self.lines.append('M=M-1')
                # addr[SP]
                self.lines.append('A=M')
                self.lines.append('D=M')
                # addr[LCL] <- addr[SP]
                self.lines.append(f'@{key}')
                self.lines.append('A=M')
                self.lines.append('M=D')
                # LCL = LCL - i
                self.lines.append(f'@{index}')
                self.lines.append('D=A')
                self.lines.append(f'@{key}')
                self.lines.append('M=M-D')
            if command == CommandType.C_PUSH:
                # LCL = LCL + i
                self.lines.append(f'@{index}')
                self.lines.append('D=A')
                self.lines.append(f'@{key}')
                self.lines.append('M=M+D')
                # addr[LCL]
                self.lines.append('A=M')
                self.lines.append('D=M')
                # addr[SP] <- addr[LCL]
                self.lines.append('@SP')
                self.lines.append('A=M')
                self.lines.append('M=D')
                # SP++
                self.lines.append('@SP')
                self.lines.append('M=M+1')
                # LCL = LCL - i
                self.lines.append(f'@{index}')
                self.lines.append('D=A')
                self.lines.append(f'@{key}')
                self.lines.append('M=M-D')
        elif segment == 'static':
            if command == CommandType.C_POP:
                self.lines.append('@SP')
                self.lines.append('A=M-1')
                self.lines.append('D=M')
                self.lines.append(f'@{self.fn}.{index}')
                self.lines.append('M=D')
                self.lines.append('@SP')
                self.lines.append('M=M-1')
            if command == CommandType.C_PUSH:
                self.lines.append(f'@{self.fn}.{index}')
                self.lines.append('D=M')
                self.lines.append('@SP')
                self.lines.append('A=M')
                self.lines.append('M=D')
                self.lines.append('@SP')
                self.lines.append('M=M+1')
        elif segment == 'temp':
            if index > 7 or index < 0:
                raise ValueError()
            if command == CommandType.C_POP:
                self.lines.append('@SP')
                self.lines.append('A=M-1')
                self.lines.append('D=M')
                self.lines.append(f'@{index+5}')
                self.lines.append('M=D')
                self.lines.append('@SP')
                self.lines.append('M=M-1')
            if command == CommandType.C_PUSH:
                self.lines.append(f'@{index+5}')
                self.lines.append('D=M')
                self.lines.append('@SP')
                self.lines.append('A=M')
                self.lines.append('M=D')
                self.lines.append('@SP')
                self.lines.append('M=M+1')
        elif segment == 'pointer':
            if index == 0:
                key = 'THIS'
            elif index == 1:
                key = 'THAT'
            if command == CommandType.C_POP:
                self.lines.append('@SP')
                self.lines.append('A=M-1')
                self.lines.append('D=M')
                self.lines.append(f'@{key}')
                self.lines.append('M=D')
                self.lines.append('@SP')
                self.lines.append('M=M-1')
            if command == CommandType.C_PUSH:
                self.lines.append(f'@{key}')
                self.lines.append('D=M')
                self.lines.append('@SP')
                self.lines.append('A=M')
                self.lines.append('M=D')
                self.lines.append('@SP')
                self.lines.append('M=M+1')

    def close(self):
        print()
        print()
        print(self.fp)
        print()
        print('\n'.join(self.lines))
        with open(self.fp, 'wt') as f:
            f.write('\n'.join(self.lines))

class Main():
    def __init__(self, fp):
        parser = Parser(fp)
        code_writer = CodeWriter(fp)

        while parser.hasMoreCommands():
            parser.advance()
            command = parser.current_command
            command_type = parser.commandType()
            if command_type != CommandType.C_RETURN:
                arg1 = parser.arg1()
                if command_type in [CommandType.C_PUSH, CommandType.C_POP, CommandType.C_FUNCTION, CommandType.C_CALL]:
                    arg2 = parser.arg2()
            if command_type == CommandType.C_ARITHMETIC:
                code_writer.writeArithmetic(command)
            if command_type == CommandType.C_POP or command_type == CommandType.C_PUSH:
                code_writer.writePushPop(command_type, segment=arg1, index=arg2)
        code_writer.close()





if __name__ == '__main__':
    # fp = 'projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm'
    # fp = 'projects/07/StackArithmetic/StackTest/StackTest.vm'
    # fp = 'projects/07/MemoryAccess/StaticTest/StaticTest.vm'
    # fp = 'projects/07/MemoryAccess/BasicTest/BasicTest.vm'
    fp = 'projects/07/MemoryAccess/PointerTest/PointerTest.vm'
    Main(fp)
    # p = Parser(fp)
    # print(p.lines)
    # print(CommandType.C_CALL.name)

