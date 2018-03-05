#!/usr/bin/env bash
# installs the requirements
cd `dirname "$0"`
gdal-config --version > /dev/null
RC=$?
if [ "$RC" != "0" ]; then
  echo "[ERROR] looks you GDAL isn't installed as a system package. You need to do that first."
  echo "[INFO] On linux, try the 'libgdal-dev' package"
  exit $RC
fi

export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
pip install \
  numpy \
  GDAL==1.11.2
