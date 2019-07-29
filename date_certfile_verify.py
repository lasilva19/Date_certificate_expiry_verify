#!/usr/bin/python
# -*- coding: utf-8 -*-
# Autor: Luciano Silva
# O objetivo desse script é verificar quantos dias faltam para a expiração de um X.509 certificado

import datetime
import commands
import sys
import os
import re

#Coloque abaixo, o nome ou o caminho completo do arquivo do certificado
Arquivo = "nome_ou_caminho_do_certificado"

ANO = int(commands.getoutput("openssl x509 -noout -in "+Arquivo+" -dates | grep ""notAfter"" | cut -c26-29"))
MES = (commands.getoutput("openssl x509 -noout -in "+Arquivo+" -dates | grep ""notAfter"" | cut -c10-12"))
DIA = int(commands.getoutput("openssl x509 -noout -in "+Arquivo+" -dates | grep ""notAfter"" | cut -c14-15"))

# Como o openssl retorna os mêses com os nomes abreviados ao invés de números, é necessário converte-los

meses = {"Jan":1, "Feb":2, "Mar":3, "Abr":4, "May":5, "June":6, "July":7, "Aug":8, "Sep":7, "Oct":10, "Nov":11, "Dec":12 }

MES = meses[MES]  
   
EXPIRACAO = datetime.datetime( ANO, MES, DIA)
HOJE = datetime.datetime.today()
RESULTADO = EXPIRACAO - HOJE
DIAS_RESTANTES=RESULTADO.days


# Os prints abaixo são para testes, pode-se usa-los ou adapta-los conforme necessidade
#print "Data de validade:", EXPIRACAO
#print "Hoje:", HOJE
#print "Dias restantes:", DIAS_RESTANTES
print(DIAS_RESTANTES)

sys.exit()
