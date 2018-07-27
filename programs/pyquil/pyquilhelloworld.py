from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import X
from pyquilcompiler import compiletoquil
import binascii


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)


def textstring(text):
    # separate chars from string
    charlist = []
    for letter in string:
        charlist.append(letter)

    # get binary of chars in bytes
    binarylets = []
    for i in range(0, len(charlist)):
        binarylets.append(text_to_bits(charlist[i]))
    return charlist, binarylets


def get_binary_from_byte(byte):
    bits = []
    for char in bytelist[0]:
        bits.append(int(char))
    return bits


string = "Hello World!"
print('string:,', string, '\n', text_to_bits(string))

# break into letters with corresponding bytes
charlist, bytelist = textstring(string)

# print letters and bytes
for i in range(0, len(charlist)):
    print(charlist[i], bytelist[i])

# get bits from each byte
b = get_binary_from_byte(bytelist[0])
print(b)

# Do quantum stuff now we have our bit string
qvm = QVMConnection()
prog = Program()

# empty list for results for each letter
res = []

bit = [None] * 8
for j in range(0, 8):
    print(charlist[j], bytelist[j])
    bit[:] = get_binary_from_byte(bytelist[j])

    for i in range(0, len(bit)):
        print('bit[i]=', bit[i])
        if bit[i] == 1:
            prog.inst(X(i))
            print('x on qubit', i)
        else:
            print('no x on qubit', i)
        prog.measure(i, i)
    cr = []
    results = (qvm.run(prog, cr, 1))

    print(results)
    print(type(results))
    #avg = sum(results)
    #print(avg)
    res.append(results)
print(res[0])

print(res)
#
#
#
#
