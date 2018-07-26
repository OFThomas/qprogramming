# set output file path
infile='exitingasm.asm'
outfile='programobj.txt'

infile=$1
# print code to file
echo $'#################################' > $outfile
echo 'asm program' >> $outfile
cat $infile >> $outfile

#create object file
as -o program.o $infile

# objectdump disassemble
echo $'\n\n#################################' >> $outfile
echo 'objectdump compiled asm' >> $outfile
objdump -d program.o >> $outfile

# linker
ld -o program program.o

# then disassemble linker file
echo $'\n\n#################################' >> $outfile
echo $'objectdump linked asm' >> $outfile
objdump -d program >> $outfile

# run the program...
# .. because reasons
./program
# let's see what this did 
echo $?

vim programobj.txt
