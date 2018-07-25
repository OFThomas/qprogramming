git clone --recursive https://github.com/msoeken/cirkit.git
cd cirkit
mkdir build
cd build
cmake -Denable_cirkit-addon-reversible=ON -Denable_cirkit-addon-formal=ON ..
make external
make revkit
cd ..
