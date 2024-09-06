#Define variáveis constantes com valores booleanos
ALFABETICO = False
NUMERICO = False
ESPECIAL = False
INVALID = False

#Entrada da senha
senha = input('Digite um senha: ')

#Declara uma l-string com caracteres especiais
CARACTERES_ESPECIAIS = r"!#$%&()*+,-./:;<=>?@[\]^_`{|}~" #o 'r' transforma a l-string em uma string bruta (raw string)

#Um loop para verificar quantos tipos de caracteres diferentes contém na senha
for caracter in senha:
	if (ord(caracter) >= ord('a') and ord(caracter) <= ord('z')) or (ord(caracter) >= ord('A') and ord(caracter) <= ord('Z')):
		ALFABETICO = True
	elif ord(caracter) >= ord('0') and ord(caracter) <= ord('9'):
		NUMERICO = True
	elif caracter in CARACTERES_ESPECIAIS:
		ESPECIAL = True
	else:
		INVALID = True

#Verifica se a senha possui caracteres inválidos
if INVALID:
	print('SENHA INVALIDA')
	
else:
	VERIFY = [ALFABETICO, NUMERICO, ESPECIAL]
	tipos = 0
	
	#Conta quantos tipos de caracteres diferentes possui a senha
	for verificar in VERIFY:
		if verificar:
			tipos += 1
			
	#Imprime para o usuário o nível da senha
	if tipos == 1:
		print('SENHA FRACA')
	elif tipos == 2:
		print('SENHA MÉDIA')
	else:
		print('SENHA FORTE')
