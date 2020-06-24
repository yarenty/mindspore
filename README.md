Dockerized Mindspore
-------------------

# Current version

* ubuntu 18.04
* python 3.7
* mindspore 0.3.0



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

# Build
```shell script
docker build --tag mindspore:latest .  
docker tag mindspore:latest <your docker name>/midspore:latest   
docker push <your docker name>/mindspore:latest  
```


# Changelog

## 0.3.0 - added functional and operations test 
* mindspore 0.3.0
* still, looks like functional is not working i.e: AddN, TensorAdd

## 0.2.0 - initial start version
* ubuntu 18.04
* python 3.7
* mindspore 0.2.0

