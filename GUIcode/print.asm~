	# -- Printing to the console --	
	# Compile and run:
	#	
	#  as -o program.o print.asm && ld -o program program.o && objdump -D program && ./program
	#
	# Comments:
	# 	The `hello world' sentence is stored as a constant and passed directly to eax as a
	#	string literal, hence there is no memory access associated with getting the string.
	#	For some reason the literal value of the `Hello world' constant is 0x0 which is a
	#	bit of an odd address. Maybe Intel assigns address space with some offset so that
	#	the accessible memory always starts from zero.
	#
	# 	The write system call returns the number of bytes written in %eax. In the following,
	#	13 characters are printed and 0x30 is added to the result, which gives 0x3d, the ASCII
	#       character for a = (the idea was to print a number, but that only works if the number
	#       is less than 10).
	#
	#	Passing a value in a memory location specified by a label var: is
	#	done by passing $(var)
	#
	#       I don't know what information %ebx is supposed to contain in sys_write calls. 
	#
	#       In the print macro, for some reason it's OK to pass Thing to str and then invoke
	#	"\str" inside the macro, but it isn't OK to pass "Thing" to str and then invoke
	#	\str. To be investigated. This causes a problem when passing sentences to print
	#	because it treats each word as a different argument
	#
	.section .data
var:	.byte 0x30
msg:	.ascii "Test\n"
	.set size, 5

	.section .text
	.global _start

	.macro quit
	movl $1, %eax
	movl $0, %ebx
	int $0x80
	.endm
	
	.macro write msg, size
	movl \msg, %ecx
	movl \size, %edx
	movl $4, %eax
	movl $0, %ebx
	int $0x80
	.endm

	.macro print str
	.section .data
0:	.ascii "\str"
1:	.set length, 1b-0b
	.section .text
	write $0b, $length
	.endm

_start:
	# print message
	write $msg, $size,

	# Print the number of bytes written
	addl %eax, (var)
	write $(var), $1

	print \nHello\n
	print "Hello Oli" 

	# quit
	quit
