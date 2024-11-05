# How To Install Python3.10 on CentOS 7 

## prepare required packages
* need root, not sure if Python3.10 can be installed properly without packages below
```
sudo yum -y update
sudo yum -y install openssl-devel bzip2-devel libffi-devel
sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

## install openssl
* python3.10 needs openssl version 1.1.1 or above, while CentOS 7 only have 1.0.2, need to install  manually
* download openssl
```
wget https://www.openssl.org/source/old/1.1.1/openssl-1.1.1.tar.gz
```
* uncompress
```
tar xf openssl-1.1.1.tar.gz
```
* change dir
```
cd openssl-1.1.1
```
* config
```
./config  --prefix=/home/myname/software --openssldir=/home/myname/software/ssl
```
* make and make installl
```
make
make install
```

## check if ssl is installed
```
openssl version
OpenSSL 1.1.1  11 Sep 2018
```
* cd /home/myname/software/lib64 and ls
```
$cd /home/myname/software/lib64 && ls
cmake/        engines-3/   libcrypto.so@      libcrypto.so.3*  libssl.so@      libssl.so.3*   pkgconfig/
engines-1.1/  libcrypto.a  libcrypto.so.1.1*  libssl.a         libssl.so.1.1*  ossl-modules/
```

## export LDFLAGS
```
export LDFLAGS="-L/home/myname/software/lib64"
```
* not sure if LD_LIBRARY_PATH and PKG_CONFIG_PATH will influence installation
```
export LD_LIBRARY_PATH=/home/myname/software/lib:/home/myname/software/lib64:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=/home/myname/software/lib/pkgconfig:/home/myname/software/lib64/pkgconfig:$PKG_CONFIG_PATH
```

## install python3.10
* download
```
wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz
```
* uncompress
```
tar xf Python-3.10.2.tgz
```

* cd
```
cd Python-3.10.2
```
* before configure
  *  for some unkown reason, `--with-openssl=/home/myname/software` doesn't work, you need to edit source file, edit file `Modules/Setup` with vim,  search for keyword `openssl`, uncomment line below，in my case, it start with line 211, save and exit

```
OPENSSL=/home/myname/software
_ssl _ssl.c \
    -I$(OPENSSL)/include -L$(OPENSSL)/lib \
    -lssl -lcrypto
```
* configure
  * option `--enable-optimizations` also not works for unknown reason on centos 7
```
./configure --prefix /home/myname/software
```

* make and make altinstall
```
make
make altinstall
```
* if make altinstall failed, and system keeps tell you 
```
./python: error while loading shared libraries: libssl.so.1.1: cannot open shared object file: No such file or directory
```

try
```
sudo bash -c "echo '/home/myname/software/lib64' >> /etc/ld.so.conf"
sudo ldconfig
```
and run ```make altinstall``` again

# test if python3.10 is properly installed
```
/home/myname/software/bin/python3.10
```
```
/home/myname/software/bin/python3.10 -m pip install pip --upgrade
```
* if both command is properly executed, python3.10 is likely successfully installed.
