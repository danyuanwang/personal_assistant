#!/bin/bash
if test -z $1
then
  image=danyuanwang/xuanwugame:assistant
else
  image=$1
fi
sudo docker run -it --entrypoint sh $image
