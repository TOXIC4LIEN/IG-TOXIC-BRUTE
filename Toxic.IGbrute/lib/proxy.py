# Date: 23/04/2022
# Author: ALTHAF
# Description: Proxy


class Proxy(object):

    def __init__(self, proxy):
        self.proxy = proxy

    @property
    def ip(self):
        return self.proxy['ip']

    @property
    def port(self):
        return self.proxy['port']

    @property
    def country(self):
        return self.proxy['country']

    @property
    def addr(self):
        addr = '{}:{}'.format(self.proxy['ip'], self.proxy['port'])
        return {'http': f'http://{addr}', 'https': f'http://{addr}'}
