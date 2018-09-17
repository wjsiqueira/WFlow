from pprint import pformat

#CAMINHO_PARA_O_BANCO = '/home/wilson_siqueira/ryu/module.db'

INTERVALO = 1

class Switch:
    def __repr__(self):
        fmt = '\n' + 'nome: ' + self.nome
        fmt += '\n' + 'ip: ' + self.ip
        fmt += '\n' + 'url: ' + self.url
        fmt += '\n' + 'addresses: '
        fmt += '\n' + pformat(self.addresses, indent=4)
        fmt += '\n' + 'routes: '
        fmt += '\n' + pformat(self.routes, indent=4)
        return fmt


# sw, porta <-> 1, 2 <-> switches[0].routes[2]['route_id'] <-> switches[sw].routes[porta]['route_id']


s1 = Switch()
s1.nome = 's1'
s1.ip = '0.0.0.0'
s1.url = 'http://localhost:8080/router/0000000000000001'
s1.addresses = {
        4: '{"address": "10.0.0.2/8"}',
        2: '{"address": "172.16.1.1/24"}',
        3: '{"address": "172.18.1.1/24"}',
        5: '{"address": "172.20.1.1/24"}',
    }
s1.routes = {
        2: {'route': '{"destination": "20.0.0.0/8", "gateway": "172.16.1.2"}', 'route_id': None}, 
        3: {'route': '{"destination": "30.0.0.0/8", "gateway": "172.18.1.3"}', 'route_id': None}, #<<<<<<<<<<<
        5: {'route': '{"destination": "40.0.0.0/8", "gateway": "172.20.1.4"}', 'route_id': None},
    }


s2 = Switch()
s2.nome = 's2'
s2.ip = '0.0.0.0'
s2.url = 'http://localhost:8080/router/0000000000000002'
s2.addresses = {
        3: '{"address": "20.0.0.2/8"}',
        1: '{"address": "172.16.1.2/24"}',
        2: '{"address": "172.17.1.2/24"}',
    }
s2.routes = {  
        1: {'route': '{"destination": "10.0.0.0/8", "gateway": "172.16.1.1"}', 'route_id': None},
        2: {'route': '{"destination": "30.0.0.0/8", "gateway": "172.17.1.3"}', 'route_id': None},
        1: {'route': '{"destination": "40.0.0.0/8", "gateway": "172.16.1.1"}', 'route_id': None},
    }

s3 = Switch()
s3.nome = 's3'
s3.ip = '0.0.0.0'
s3.url = 'http://localhost:8080/router/0000000000000003'
s3.addresses = {
        2: '{"address": "30.0.0.2/8"}',
        1: '{"address": "172.17.1.3/24"}',
        3: '{"address": "172.18.1.3/24"}',
        4: '{"address": "172.19.1.3/24"}',
    }
s3.routes = { 
        3: {'route': '{"destination": "10.0.0.0/8", "gateway": "172.18.1.1"}', 'route_id': None}, #<<<<<<<<<<<
        1: {'route': '{"destination": "20.0.0.0/8", "gateway": "172.17.1.2"}', 'route_id': None},
        4: {'route': '{"destination": "40.0.0.0/8", "gateway": "172.19.1.4"}', 'route_id': None},
    }

s4 = Switch()
s4.nome = 's4'
s4.ip = '0.0.0.0'
s4.url = 'http://localhost:8080/router/0000000000000004'
s4.addresses = {
        2: '{"address": "40.0.0.2/8"}',
        1: '{"address": "172.19.1.4/24"}',
        3: '{"address": "172.20.1.4/24"}',
    }
s4.routes = { 
        3: {'route': '{"destination": "10.0.0.0/8", "gateway": "172.20.1.1"}', 'route_id': None},
        1: {'route': '{"destination": "30.0.0.0/8", "gateway": "172.19.1.3"}', 'route_id': None},
        1: {'route': '{"destination": "20.0.0.0/8", "gateway": "172.20.1.1"}', 'route_id': None},
    }


switches = [s1, s2, s3, s4]
