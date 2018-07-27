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
    #return int2bytes(n).decode(encoding, errors)
    return n.to_bytes(
        (n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


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
    for char in byte:
        bits.append(int(char))
    return bits


string = "Hello World!"

string = str(input('Enter a message to be printed by a quantum computer: \n'))

stringsize = len(string)
print('string:', string, '\n', 'In binary this is\n', text_to_bits(string))

# how many measurement samples to perform for each character
samples = 1
# show compiler steps :p
explicitprinting = 0

# break into letters with corresponding bytes
charlist, bytelist = textstring(string)

# get bits from each byte

# empty list for results for each letter
res = []

# 8 bits in 1 byte
bit = [None] * 8
for j in range(0, len(charlist)):
    # Do quantum stuff now we have our bit string
    qvm = QVMConnection()
    prog = Program()
    # make 8 individual bits for the 8 qubits
    bit = get_binary_from_byte(bytelist[j])
    # don't what this is for...
    cr = []
    for i in range(0, len(bit)):
        # do x rotation to get 1
        if bit[i] == 1:
            prog.inst(X(i))
        # measure the i-th qubit
        prog.measure(i, i)
    # store measurement outcomes, can change number of shots
    results = (qvm.run(prog, cr, samples))
    # use list for results for each char
    res.append(results[0])
    if explicitprinting == 1:
        print(compiletoquil(prog))

# write quantum measurements to a bitstring
outputbitstring = [''] * stringsize
for i in range(0, len(res)):
    for element in res[i]:
        # concatenate the bits
        outputbitstring[i] += str(element)

print('\nMeasurement results, %d samples for each char\n' % (samples),
      outputbitstring)

# translate bitstring into acsii again
quantumstring = ''
for i in range(0, len(outputbitstring)):
    quantumstring += str(text_from_bits(outputbitstring[i]))

print('\nThis is your quantum computer (simulator), your message was:\n',
      quantumstring)