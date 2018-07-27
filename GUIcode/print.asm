	# -- Printing to the console --	
	#

	# This is a memory section
	.section .data
msg:	.ascii "\nHello World\n"
	.set size, 13

	.section .text
	.global _start
_start:
	# print msg
	movl $msg, %ecx
	movl $size, %edx
	movl $4, %eax
	movl $0, %ebx
	int $0x80
	
	# quit with exit code 0
	movl $1, %eax
	movl $0, %ebx
	int $0x80
