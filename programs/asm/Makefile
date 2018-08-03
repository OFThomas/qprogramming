ARCH = $(shell arch)
CC = gcc
PP = g++
FF = gfortran

all: fortran_helloworld c_helloworld cpp_helloworld

fortran_helloworld: fortran_helloworld.f90 fortran_helloworld.asm 
	$(FF) fortran_helloworld.f90 -o fortran_helloworld.$(ARCH).out

fortran_helloworld.asm: fortran_helloworld.f90
	$(FF) -S fortran_helloworld.f90 -o fortran_helloworld.$(ARCH).asm
	$(FF) -S -O3 fortran_helloworld.f90 -o opt_fortran_helloworld.$(ARCH).asm

c_helloworld: c_helloworld.c c_helloworld.asm 
	$(CC) c_helloworld.c -o c_helloworld.$(ARCH).out

c_helloworld.asm: c_helloworld.c
	$(CC) -S c_helloworld.c -o c_helloworld.$(ARCH).asm
	$(CC) -S -O3 c_helloworld.c -o opt_c_helloworld.$(ARCH).asm

cpp_helloworld: cpp_helloworld.cpp cpp_helloworld.asm 
	$(PP) cpp_helloworld.cpp -o cpp_helloworld.$(ARCH).out

cpp_helloworld.asm: cpp_helloworld.cpp
	$(PP) -S cpp_helloworld.cpp -o cpp_helloworld.$(ARCH).asm
	$(PP) -S -O3 cpp_helloworld.cpp -o opt_cpp_helloworld.$(ARCH).asm

clean:
	rm -f *$(ARCH)* 




