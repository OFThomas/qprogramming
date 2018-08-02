	.file	"fortran_helloworld.f90"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"fortran_helloworld.f90"
	.section	.rodata
.LC1:
	.ascii	"Hello World!"
	.text
	.p2align 4,,15
	.type	MAIN__, @function
MAIN__:
.LFB0:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	leaq	.LC0(%rip), %rax
	subq	$480, %rsp
	.cfi_def_cfa_offset 496
	movq	%rsp, %rbx
	movq	%rax, 8(%rsp)
	movabsq	$25769803904, %rax
	movq	%rbx, %rdi
	movq	%rax, (%rsp)
	movl	$4, 16(%rsp)
	call	_gfortran_st_write@PLT
	leaq	.LC1(%rip), %rsi
	movq	%rbx, %rdi
	movl	$12, %edx
	call	_gfortran_transfer_character_write@PLT
	movq	%rbx, %rdi
	call	_gfortran_st_write_done@PLT
	addq	$480, %rsp
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE0:
	.size	MAIN__, .-MAIN__
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	call	_gfortran_set_args@PLT
	leaq	options.1.3502(%rip), %rsi
	movl	$7, %edi
	call	_gfortran_set_options@PLT
	call	MAIN__
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.section	.rodata
	.align 16
	.type	options.1.3502, @object
	.size	options.1.3502, 28
options.1.3502:
	.long	68
	.long	1023
	.long	0
	.long	1
	.long	1
	.long	0
	.long	31
	.ident	"GCC: (Ubuntu 7.3.0-16ubuntu3) 7.3.0"
	.section	.note.GNU-stack,"",@progbits
