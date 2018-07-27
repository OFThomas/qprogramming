# set output file path
infile='exitingasm.asm'
#outfile='programobj.txt'

infile=$1

outfile=${infile::-4}
outfile=$outfile'obj.txt'
#echo 'outfile' $outfile

# print code to file
echo $'#################################' > $outfile
echo 'asm program' >> $outfile
cat $infile >> $outfile

#create object file
as -o program.o $infile

# objectdump disassemble
echo $'\n\n#################################' >> $outfile
echo 'objectdump compiled asm' >> $outfile
objdump -dsj .data program.o >> $outfile

# linker
ld -o program program.o

# then disassemble linker file
echo $'\n\n#################################' >> $outfile
echo $'objectdump linked asm' >> $outfile
objdump -dsj .data program >> $outfile

# run the program...
# .. because reasons
./program
# let's see what this did 
echo $?

vim programobj.txt
