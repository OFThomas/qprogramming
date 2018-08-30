	.file	"fortran_helloworld.f90"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"fortran_helloworld.f90"
	.section	.rodata
.LC1:
	.ascii	"Hello World!"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB2:
	.text
.LHOTB2:
	.p2align 4,,15
	.type	MAIN__, @function
MAIN__:
.LFB0:
	.cfi_startproc
	subq	$488, %rsp
	.cfi_def_cfa_offset 496
	movq	%rsp, %rdi
	movq	$.LC0, 8(%rsp)
	movl	$4, 16(%rsp)
	movl	$128, (%rsp)
	movl	$6, 4(%rsp)
	call	_gfortran_st_write
	movq	%rsp, %rdi
	movl	$12, %edx
	movl	$.LC1, %esi
	call	_gfortran_transfer_character_write
	movq	%rsp, %rdi
	call	_gfortran_st_write_done
	addq	$488, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE0:
	.size	MAIN__, .-MAIN__
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.section	.text.unlikely
.LCOLDB3:
	.section	.text.startup,"ax",@progbits
.LHOTB3:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	call	_gfortran_set_args
	movl	$options.1.3386, %esi
	movl	$9, %edi
	call	_gfortran_set_options
	call	MAIN__
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE3:
	.section	.text.startup
.LHOTE3:
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
