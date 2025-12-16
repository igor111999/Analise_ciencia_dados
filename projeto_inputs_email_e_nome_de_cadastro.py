
cpf = input('insira seu cpf')


if len(cpf) == 11 and cpf.isnumeric() == True:
    print(cpf)
    
else :
    print('Digite seu CPF corretamente e digite apenas números')


pf = input('insira seu cpf')



if len(cpf) == 11 and cpf.isnumeric() == True:
    print(cpf)
    
else :
    print('Digite seu CPF corretamente e digite apenas números')


nome = input('insira o nome para cadastro ')
email = input('insira o email para cadastro ')

if  nome.isalpha() and '@' in email:
    print(nome, email)
    
elif '' :
    print('preencha todos os dados corretamente')
    
else:
     print('preencha todos os dados corretamente')
    

print(email.find('@'))
