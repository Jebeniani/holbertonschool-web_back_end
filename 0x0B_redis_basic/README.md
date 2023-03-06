# Redis basic

![alt text](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230306%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230306T090827Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1311444435f53db896b75001a8618f040efcb30e6244aa3ff0dfaed91e5c23b6)

in this project we'll learn how to:
```python
- use redis for basic operations
- use redis as a simple cache
```


how to install Redis on Ubuntu:
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```