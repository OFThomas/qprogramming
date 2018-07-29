# -- AS syntax --
	# Function: do nothing and exit
	# Compile and run:
	#   as -o program.o exiting.asm && objdump -d program.o && ld -o program program.o && ./program; echo $?
	#
	.section .text
	.global _start
_start:
	# Store code number for system call (on interrupt 0x80)
	movl $1, %eax	# 1 in %eax corresponds to request for program to exit
	movl $2, %ebx	# %ebx specifies the return value
	int $0x80	# OS syscall software interrupt
