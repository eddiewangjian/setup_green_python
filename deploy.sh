#! /bin/bash
VERSION=2.7.17

PROCESS_DIR=$(pwd)
# python压缩包的解压后路径
python_pkg=./Python-${VERSION}
# python部署路径
deploy_dir=$PROCESS_DIR/../python${VERSION}

# ------------ green python pkg ------------
cd ${python_pkg}
./configure --prefix=${deploy_dir} --with-ssl
make
make install
cd $PROCESS_DIR

# ------------ pip python pkg ------------
${deploy_dir}/bin/python get-pip.py

${deploy_dir}/bin/pip install requests
${deploy_dir}/bin/pip install ConfigParser
${deploy_dir}/bin/pip install logging
${deploy_dir}/bin/pip install mysql
${deploy_dir}/bin/pip install tornado
${deploy_dir}/bin/pip install protobuf
${deploy_dir}/bin/pip install tensorflow
${deploy_dir}/bin/pip install matplotlib
${deploy_dir}/bin/pip install numpy

${deploy_dir}/bin/python ./sofa-pbrpc/python/setup.py install



