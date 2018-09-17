import time
from pprint import pprint

import requests

from conf import *

class Resposta:
    def __init__(self, res):
        self.res = res.json()
    def result(self):
        try:
            return self.res[0][u'command_result'][0][u'result']
        except:
            return self.res
    def eh_sucesso(self):
        return u'success' == self.result()
    def route_id(self):
        return self.res[0][u'command_result'][0][u'details'][-2]
        
def post_sw(s):
    post_add(s)
    post_routes(s)
    pprint(s)
    
def post_add(s):
    for address in s.addresses.values():
        res = requests.post(s.url, address)
        pprint(res.json())

def post_routes(s):
    for porta, rota in s.routes.items():
        res = requests.post(s.url, data=rota['route'])
        r = Resposta(res)
        try:
            if r.eh_sucesso():            
                s.routes[porta]['route_id'] = r.route_id()
        except: raise
        pprint(res.json())
        
def post():
    post_sw(s1)
    '''for address in s1.addresses.values():
        res = requests.post(s1.url, address)
        pprint(res.json())
    
    for porta, rota in s1.routes.items():
        res = requests.post(s1.url, data=rota['route'])
        r = Resposta(res)
        try:
            if r.eh_sucesso():            
                s1.routes[porta]['route_id'] = r.route_id()
        except: raise
    pprint(s1)'''
    
    time.sleep(10)
    
    for s in [s2, s3, s4]:
        post_add(s)
        '''for address in s.addresses.values():
            res = requests.post(s.url, address)
            pprint(res.json())'''
    
    for s in [s2, s3, s4]:
        post_routes(s)
        '''for porta, rota in s.routes.items():
            res = requests.post(s.url, data=rota['route'])
            r = Resposta(res)
            try:
                if r.eh_sucesso():            
                    s.routes[porta]['route_id'] = r.route_id()
            except: raise'''
        pprint(s)
        
def post_route(switch_number, route):
    url = switches[switch_number-1].url
    pprint('posting to:.......%s' % url)
    pprint('route:............%s' % route)
    res = requests.post(url, route)
    pprint(res.content)
    print

def delete(rrs_trs):
    "1,3 - 3,2 / 1,4 - 3,3"
    "3,2 - 1,3 / 3,3 - 1,4"
    "sw1, p3 e sw3, p3"
    l1, l2 = rrs_trs
    t1, t2 = sorted(l1)
    t3, t4 = sorted(l2)
    
    sb1, portaA = t1
    sb2, portaB = t4

    delete_route(sb1, portaA)
    post_route(sb1, '{"destination": "10.0.0.0/8", "gateway": "172.16.1.2"}')
    
    delete_route(sb2, portaB)
    post_route(sb2, '{"destination": "10.0.0.0/8", "gateway": "172.17.1.2"}')
    
    alll()


def delete_route(switch_number, porta_number):
    route_id = switches[switch_number-1].routes[porta_number]['route_id']

    pprint('...............DELETING ROUTING...............')
    url     = switches[switch_number-1].url
    payload = '{"route_id": "%s"}' % route_id
    res = requests.delete(url, data=payload)
    pprint(res.content)
    print

def alll():   
    res = requests.get('http://localhost:8080/router/all/all')
    pprint(res.json())
    return res

def x():
    import sys
    sys.exit()
    
 
