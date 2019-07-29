#!/usr/bin/python
# -*- coding: utf-8 -*-
# Autor: Luciano Silva
# O objetivo desse script é verificar quantos dias faltam para a expiração de um X.509 certificado no formtato .pem

import datetime
import commands
import sys
import os
import re

# Abaixo, onde se encontra escrito "nome_ou_caminho_do_arquivo.pem, deve-se substituir pelo nome do arquivo do certificado
# Caso o script esteja salvo em um diretório diferente do certificado, coloque o caminho completo do arquivo

ANO = int(commands.getoutput("openssl x509 -noout -in nome_ou_caminho_do_arquivo.pem -dates | grep ""notAfter"" | cut -c26-29"))
MES = (commands.getoutput("openssl x509 -noout -in nome_ou_caminho_do_arquivo.pem -dates | grep ""notAfter"" | cut -c10-12"))
DIA = int(commands.getoutput("openssl x509 -noout -in nome_ou_caminho_do_arquivo.pem -dates | grep ""notAfter"" | cut -c14-15"))

# Como o openssl retorna o mês com o nome abreviado ao invés de número, é necessário converte-lo

meses = {"Jan":1, "Feb":2, "Mar":3, "Abr":4, "May":5, "June":6, "July":7, "Aug":8, "Sep":7, "Oct":10, "Nov":11, "Dec":12 }

MES = meses[MES]  
   
EXPIRACAO = datetime.datetime( ANO, MES, DIA)
HOJE = datetime.datetime.today()
RESULTADO = EXPIRACAO - HOJE
DIAS_RESTANTES=RESULTADO.days


# Os prints abaixo são para testes, pode-se usa-los ou adaptalos conforme necessidade
print RESULTADO
print "Data de validade:", EXPIRACAO
print "Hoje:", HOJE
print "Dias restantes:", DIAS_RESTANTES

sys.exit()
