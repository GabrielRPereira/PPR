#/bin/bash
clear

nome(){ 
	echo "Digite seu nome, com a primeira letra maiuscula: "
	read NOM
RNOM='^[a-zA-Z ]+$'

if [[ $NOM =~ $RNOM ]]; then
	echo 'Nome Válido'
	sleep 3
	mail
else
	echo 'Nome Inválido'
	sleep 3
	clear
	nome
fi
}



mail(){
	clear
	echo "Digite seu e-mail (que contenha @; .com ou .com.br): "
	read EMA
REMA='.+@.+\.(com)+((.br)*)?$'

if [[ $EMA =~ $REMA ]]; then
	echo 'E-mail Válido'
	sleep 3
	telf
else
	echo 'E-mail Inválido'
	sleep 3
	mail
fi
}



telf(){
	clear
	echo "Digite seu telefone. (Formato 9999-9999): "
	read TLF 
RTLF='^[0-9]{4}+-[0-9]{4}$'

if [[ $TLF =~ $RTLF ]]; then
 	echo 'Telefone Válido' 
	sleep 3
	rg
else
 	echo 'Telefone inválido' 
	sleep 3
	telf
fi
}



rg(){
	clear
	echo "Digite seu RG. (Formato 11.111.111-x): "
	read NRG
RNRG='^([0-9]{2})\.([0-9]{3})\.([0-9]{3})-([0-9]|[x])$'

if [[ $NRG =~ $RNRG ]]; then
	echo 'Número de RG válido'	
	sleep 3
	cpf
else
	echo 'Número de RG inválido'
	sleep 3
	rg
fi
}



cpf(){
	clear
	echo "Digite seu CPF.(Formato 123.456.789-11): "
	read CPF
RCPF='^([0-9]{3})\.([0-9]{3})\.([0-9]{3})-([0-9]{2})$'

if [[ $CPF =~ $RCPF ]]; then
	echo 'Número de CPF válido'	
	sleep 3
	nasc
else
	echo 'Número de CPF inválido'
	sleep 3
	cpf
fi
}



nasc(){
	clear
	echo "Digite a data de seu nascimento.(Formato dd/mm/aaaa): "
	read NAC
RNAC='(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19|20)[0-9]{2}$'

if [[ $NAC =~ $RNAC ]]; then
	echo 'Data de nascimento válida'	
	sleep 3
	edip	
else
	echo 'data de nascimento inválida'
	sleep 3
	nasc
fi
}



edip(){
	clear
	echo "Digite o seu endereço IP. (Formato 192.168.10.1): "
	read EIP
REIP='^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'

if [[ $EIP =~ $REIP ]]; then
	echo 'IP válido'	
	sleep 3
	mask
else
	echo 'IP inválido'
	sleep 3
	edip
fi
}



mask(){
	clear
	echo "Digite sua netmask. (Formato 255.255.255.255): "
	read MSK
RMSK='^(254|252|248|240|224|192|128)(.0){3}$|^255(.255|.254|.252|.248|.240|.224|.192|.128|.0){3}$'

if [[ $MSK =~ $RMSK ]]; then
	echo 'Máscara válida'	
	sleep 3
else
	echo 'Máscara inválida'
	sleep 3
	mask
fi
}

nome

clear
echo "Seus dados são: "  
echo "NOME: $NOM"; echo "EMAIL: $EMA"; echo "TELEFONE: $TLF"; echo "RG: $NRG"; echo "CPF: $CPF"; echo "DATA NASC.: $NAC"; echo "END. IP: $EIP"; echo "NETMASK: $MSK"
