Dockerized Mindspore
-------------------

# Current version

* ubuntu 18.04
* python 3.7
* mindspore 0.5.0



# Installation
```shell script
docker pull yarenty/mindspore
```

# Run
```shell script
docker run -it yarenty/mindspore
```

You should be in /opt directory, and you should be able to run:
```shell script
python3.7 test_mul.py
```

Output:
```text
[ 4. 10. 18.]
``` 


## LeNet5 test

Added new LeNet5 test:
```shell script
python lenet.py
```


Output:
```shell script
epoch: 1 step: 1872, loss is 0.0793872
epoch: 1 step: 1873, loss is 0.07211199
epoch: 1 step: 1874, loss is 0.079631396
epoch: 1 step: 1875, loss is 0.31805548
============== Starting Testing ==============
============== Accuracy:{'Accuracy': 0.9702524038461539} ==============
```

Also you can check that after run there will be fen new files/directories:
 - MNIST_Data directory 
 - checkpoint_... files with latest train checkpoints
 - ms_output_... files with train and eval outputs



# Build
```shell script
docker build --tag mindspore:latest .  
docker tag mindspore:latest <your docker name>/midspore:latest   
docker push <your docker name>/mindspore:latest  
```

# Input
`https://github.com/mindspore-ai/mindspore`

# Changelog

## 0.5.0
* change from alpha to beta - investigation in progress what is new

## 0.3.0 - added functional and operations test 
* mindspore 0.3.0
* still, CPU lots missing operators i.e: AddN, TensorAdd - see [Supported Operator list](https://www.mindspore.cn/docs/zh-CN/0.3.0-alpha/operator_list.html)

## 0.2.0 - initial start version
* ubuntu 18.04
* python 3.7
* mindspore 0.2.0

