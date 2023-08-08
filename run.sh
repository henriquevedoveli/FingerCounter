#!/bin/bash

image="$1"

sudo docker run -it --privileged --network="host" --device /dev/video0 --env="DISPLAY=$DISPLAY" -v src:/app $image
