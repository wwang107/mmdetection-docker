#!/usr/bin/env bash

if [ "$#" != 1 ]; then
    echo "Expect name of training script"
    exit 1
fi


./preprocessing.sh /home/user/BBextractor/exec $1


docker run\
    --gpus all\
    --shm-size="8g"\
    --privileged\
    -p 8888:8888
    -v "/home/weiwang/Desktop/BBextractor":/home/user/BBextractor:ro\
    -v "/home/media/Elements/h36m-fetch/human36m":/home/user/human36m:ro\
    -v "/home/media/Elements/export":/home/user/export\
    --rm -it\
    weiwang/bbextractor\
    /bin/bash /home/user/run.sh