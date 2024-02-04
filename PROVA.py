'''Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e 
um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e 
utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado 
pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o 
usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.'''

senha_cadastrada = "S1234"
email_cadastrado = "email@email.com.br"
login_bem_sucedido = False

while True:
    email_digitado = input("Digite seu email: ")
    senha_digitada = input("Digite sua senha: ")

    if email_digitado == email_cadastrado and senha_digitada == senha_cadastrada:
        print("Login bem-sucedido!")
        login_bem_sucedido = True
    else:
        print("Email ou senha incorretos. Tente novamente.")