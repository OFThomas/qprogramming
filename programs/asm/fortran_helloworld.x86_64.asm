	.file	"fortran_helloworld.f90"
	.section	.rodata
.LC0:
	.string	"fortran_helloworld.f90"
.LC1:
	.ascii	"Hello World!"
	.text
	.type	MAIN__, @function
MAIN__:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$480, %rsp
	movq	$.LC0, -472(%rbp)
	movl	$4, -464(%rbp)
	movl	$128, -480(%rbp)
	movl	$6, -476(%rbp)
	leaq	-480(%rbp), %rax
	movq	%rax, %rdi
	call	_gfortran_st_write
	leaq	-480(%rbp), %rax
	movl	$12, %edx
	movl	$.LC1, %esi
	movq	%rax, %rdi
	call	_gfortran_transfer_character_write
	leaq	-480(%rbp), %rax
	movq	%rax, %rdi
	call	_gfortran_st_write_done
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	MAIN__, .-MAIN__
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-16(%rbp), %rdx
	movl	-4(%rbp), %eax
	movq	%rdx, %rsi
	movl	%eax, %edi
	call	_gfortran_set_args
	movl	$options.1.3386, %esi
	movl	$9, %edi
	call	_gfortran_set_options
	call	MAIN__
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.section	.rodata
	.align 32
	.type	options.1.3386, @object
	.size	options.1.3386, 36
options.1.3386:
	.long	68
	.long	1023
	.long	0
	.long	0
	.long	1
	.long	1
	.long	0
	.long	0
	.long	31
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
