# Clone the git repo
git clone https://github.com/epiqc/ScaffCC.git
cd ScaffCC
# No need to install binutils-gold now; the gold linker is part of the binutils package
sudo apt-get update 
sudo apt-get install -y  clang-3.9* libboost-all-dev libgmp-dev libgmpxx4ldbl libmpfr-dev cmake
sudo ln -s /usr/bin/clang-3.9 /usr/bin/clang
sudo ln -s /usr/bin/clang++-3.9 /usr/bin/clang++
sed -i -e 's/CLANG=g++/CLANG=clang++/g' Makefile
echo "-------------------------"
echo "ARE YOU READY FOR CLANG!?"
echo "-------------------------"
make

# Install!
sudo ln -s $PWD/scaffold.sh /usr/bin/scaffold
