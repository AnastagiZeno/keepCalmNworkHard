# -*- coding: utf-8 -*-
import redis


class RedisHelper:
    def __init__(self, host='localhost', port=6379, name_space='', partition=''):
        if not (name_space and partition):
            raise AttributeError('namespace and partition is required.')
        self.__redis = redis.StrictRedis(host, port)
        self.namespace = name_space + partition

    def get(self, key, with_namespace=False):
        if not with_namespace:
            key = self.namespace + key
        else:
            if not self.namespace in key:
                key = self.namespace + key
            pass

        if self.__redis.exists(key):
            num = self.__redis.get(key)
            assert num.isdigit(), 'value of key %s should be a number, but %s' % (key, type(num))
            return int(num)
        else:
            return 0

    def set(self, key, value=1):
        key = self.namespace + key
        if not isinstance(value, int):
            if isinstance(value, basestring) and value.isdigit():
                value = int(value)
            elif isinstance(value, float):
                value = int(value)
            else:
                raise ValueError('value should be a number, but %s given' % (type(value)))
        self.__redis.set(key, value)
        return value

    def vote(self, key):
        num = self.get(key)
        return self.set(key, num + 1)

    def scan(self):
        return {key: self.get(key, with_namespace=True) for key in self.__redis.scan_iter(match="%s*" % self.namespace)}


if __name__ == '__main__':
    r = RedisHelper(name_space='lagou-python::', partition='jobdetail-des::')
    for k, v in r.scan().iteritems():
        print k, '- ', v
