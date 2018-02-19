#!/usr/bin/python
# -*- coding: utf -*-
import re, os

def nome():
	NOM = raw_input ("Digite seu nome. (Form Alan): ")
	if re.search(r'^[a-zA-Z ]+$', NOM):
		return "nom"

while (True):
	os.system("clear")
	resultado = nome()
	if resultado == "nom":
		print ("Nome Válido")
		os.system("sleep 3")
		break
	else:
		print ("Nome Inválido")
	 	os.system("sleep 3")



def mail():
	EMA = raw_input ("Digite seu e-mail.(Contendo @ e .com ou .com.br): ")
	if re.search(r'.+@.+\.(com)+((.br)*)?$', EMA):
		return "ema"

while (True):
	os.system("clear")
	resultado = mail()
	if resultado == "ema":
		print ("E-mail Válido")
	 	os.system("sleep 3")
		break
	else:
		print ("E-mail Inválido")
	 	os.system("sleep 3")



def telf():
	TEL = raw_input ("Digite seu telefone. (Form 9999-9999): ")
	if re.search('^([0-9]{4})-([0-9]{4})$', TEL):
		return "tel"

while (True):
	os.system("clear")
	resultado = telf()
	if resultado == "tel":
		print ("Telefone Válido")
		os.system("sleep 3")
		break
	else:
		print ("Telefone Inválido")
	 	os.system("sleep 3")



def rg():
	NRG = raw_input ("Digite seu número de RG. (Form 99.999.999-9): ")
	if re.search(r'^([0-9]{2})\.([0-9]{3})\.([0-9]{3})-([0-9]|[x])$', NRG):
		return "nrg"

while (True):
	os.system("clear")
	resultado = rg()
	if resultado == "nrg":
		print ("RG Válido")
		os.system("sleep 3")
		break
	else:
		print ("RG Inválido")
	 	os.system("sleep 3")



def ncpf():
	CPF = raw_input ("Digite seu número de CPF. (Form 111.111.111-11): ")
	if re.search(r'^([0-9]{3})\.([0-9]{3})\.([0-9]{3})-([0-9]{2})$', CPF):
		return "cpf"

while (True):
	os.system("clear")
	resultado = ncpf()
	if resultado == "cpf":
		print ("CPF Válido")
		os.system("sleep 3")
		break
	else:
		print ("CPF Inválido")
	 	os.system("sleep 3")



def nasc():
	NAC = raw_input ("Digite a data de seu nascimento. (Form dd/mm/aaaa): ")
	if re.search(r'(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19|20)[0-9]{2}$', NAC):
		return "nac"

while (True):
	os.system("clear")
	resultado = nasc()
	if resultado == "nac":
		print ("Data Válida")
		os.system("sleep 3")
		break
	else:
		print ("Data Inválida")
	 	os.system("sleep 3")



def edip():
	EIP = raw_input ("Digite seu endereço IP. (Form 192.168.10.1): ")
	if re.search(r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$', EIP):
		return "eip"

while (True):
	os.system("clear")
	resultado = edip()
	if resultado == "eip":
		print ("IP Válido")
		os.system("sleep 3")
		break
	else:
		print ("IP Inválido")
		os.system("sleep 3")



def mask():
	MSK = raw_input ("Digite sua netmask. (Form 255.255.255.255): ")
	if re.search(r'^(254|252|248|240|224|192|128)(.0){3}$|^255(.255|.254|.252|.248|.240|.224|.192|.128|.0){3}$', MSK):
		return "msk"

while (True):
	os.system("clear")
	resultado = mask()
	if resultado == "msk":
		print ("Netmask Válido")
		os.system("sleep 3")
		break
	else:
		print ("Netmask Inválido")
	 	os.system("sleep 3")


os.system("clear")
