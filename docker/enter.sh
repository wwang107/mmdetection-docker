#!/usr/bin/env bash
sudo docker run --gpus all\
  --privileged\
  -it\
  -p 8888:8888\
  weiwang/bbextractor\
  /bin/bash