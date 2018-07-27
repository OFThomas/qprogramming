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
objdump -Dj .text program.o >> $outfile
objdump -sj .data program.o >> $outfile

# linker
ld -o program program.o

# then disassemble linker file
echo $'\n\n#################################' >> $outfile
echo $'objectdump linked asm' >> $outfile
objdump -Dj .text program >> $outfile
objdump -sj .data program >> $outfile

# run the program...
# .. because reasons
./program
# let's see what this did
echo 'Program return value: '$?

#vim $outfile 
