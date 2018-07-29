# Run at your own risk!
#
#git clone https://github.com/Z3Prover/Z3
#cd Z3
#python scripts/mk_make.py
#cd build
#make
#sudo make install
#
# Now you need to clone the cirkit repository and run the following in it:
#
# 1) In file: addons/cirkit-addon-reversible/src/reversible/synthesis/exact_synthesis.cpp exact_synthesis.cpp:
#
# Replace the line:
#
#      #include <z3++.h>
#      
# with the lines:
#
#      #include <z3++.h>
#      typedef uint64_t __uint64;
#
# 3) In file addons/cirkit-addon-reversible/src/cli/commands/esopbs.cpp,
# comment out the function 'cubes_to_esop_ptr'.
#
rm -rf build
mkdir build
cd build
# Lookout for python 3.5!
# Change the path to python3.5
cmake -Dcirkit_ENABLE_PYTHON_API=ON -Denable_cirkit-addon-reversible=ON -Denable_cirkit-addon-formal=ON -DPYBIND11_PYTHON_VERSION=3.5 -DPYTHON_EXECUTABLE=/usr/local/bin/python3 ..
#make revkit_python
#make cirkit_python
# Need to add build/program (or something like that) to PYTHONPATH
