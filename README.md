# WFlow
Uma Solução para o Monitoramento In-band de Redes Definidas por Software

1. Módulos de setup do WFlow:

MiniNet.py - É inicializado por < sudo python MiniNet >. É utilizado para configurar as conexões entre hosts e switches

conf.py - Módulo para a configuração de interfaces e rotas dos switches;


2. Módulos do WFlow:

wflow.py - Módulo para agregação das APIs de switching, routing e monitoramento do RYU;

extract.py - Módulo para cálculo do throughput dos links;

dbmon.py - Módulo para disparo dos modos proativo e adaptativo do WFlow;

setconf.py - Módulo para a modificação das regras dos switches; e

db.py - Módulo de carga para a base de dados.
