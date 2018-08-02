# Fortran compile to asm
gfortran -S fortran_helloworld.f90 -o fortran_helloworld.asm
# compile and assemble, link
gfortran fortran_helloworld.f90 -o fortran_helloworld.out

# C compile to asm
gcc -S c_helloworld.c -o c_helloworld.asm
# compile and assemble, link
gcc c_helloworld.c -o c_helloworld.out

# C++ compile to asm
g++ -S cpp_helloworld.cpp -o cpp_helloworld.asm
# compile and assemble, link
g++ cpp_helloworld.cpp -o cpp_helloworld.out
