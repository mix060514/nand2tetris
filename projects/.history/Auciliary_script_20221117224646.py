#%%
import pyperclip

s = ''

for i in range(16):
    # pass
    # if i == 0:
        # s += f'Or(a=in[{i}], b=in[{i+1}], out=out1);\n\t'
    # else:
        # s += f'Or(a=out{i}, b=in[{i+1}], out=out{i+1});\n\t'
    # s += f'Or(a=a[{i}], b=b[{i}], out=out[{i}]);\n\t'
    # s += f'Mux16(a=a, b=b, sel=sel[0], out=outab);\n\t'
    # s += f'And(a=a[{i}], b=b[{i}], out=out[{i}]);\n'
    # s+=f"Not(in=in[{i}], out=out[{i}]);\n"
    # s += f'FullAdder(a=a[{i}], b=b[{i}], c=carry{i-1}, sum=out[{i}], carry=carry{i});'
    # s += f'    Bit(in=in[{i}], load=load, out=out[{i}]);'
    s += f'    Register(in=in, load=DMux{i}, out=Registerout{i});'
    s += '\n'
# s += f'Mux16(a=a, b=b, sel=sel[0], out=outab);\n\t'
# s += f'Mux16(a=c, b=d, sel=sel[0], out=outcd);\n\t'
# s += f'Mux16(a=outab, b=outcd, sel=sel[1], out=out);\n\t'
print(s)

pyperclip.copy(s)
