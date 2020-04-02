#!/usr/bin/env bash

docker run\
    --gpus all\
    --privileged\
    --user $(id -u):$(id -g)\
    -p 8888:8888\
    -v "/home/weiwang/Desktop/master-thesis/BBextractor/poseEstPipeline":/mmdetection/poseEstPipeline\
    -v "/media/weiwang/Elements/h36m-fetch/processed":/mmdetection/human36m\
    -v "/media/weiwang/Elements/export":/mmdetection/export\
    --rm -it\
    weiwang/bbextractor\