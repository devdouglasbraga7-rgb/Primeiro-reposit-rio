# Esse codigo faz um mini sistema de lista para treinar e consolidar o conhecimento das listas

cadastro = []

loop = 0

while loop == 0:
    print("=" * 40)
    print("1 - Cadastrar novo cliente\n"
        "2 - Atualizar cliente existente\n"
        "3 - Mostrar lista de clientes\n"
        "4 - Deletar cliente existente")
    print("="* 40)
#Mostra as opções que o usuário pode fazer na lista

    escolha = int(input("Escolha uma das opções digitando o número correspondente: ")) #Pede pro usuário escolher a opção desejada no menu

    if escolha == 1:
        clientes = input("Digite o nome do cliente: ")
        cadastro.append(clientes)
        print(f"Esse aqui é o  cadastro do cliente: {clientes}")
    elif escolha == 2:
        for i, nome in enumerate(cadastro, start=1):
            print(i, "-" , nome)
        opcao = int(input("Escolha a opção: "))
        novo_nome = input("Digite o novo nome: ")
            
        cadastro[opcao - 1] = novo_nome

        for nome in cadastro:
            print("-", nome)
    elif escolha == 3:
        for i, nome in enumerate(cadastro, start=1):
            print(i, "-",nome)
    else:
        for nome in cadastro:
            print("-", nome)
        opcao = input("Digite a opção que deseja excluir: ")
        
        cadastro.remove(opcao)
        for nome in cadastro:
            print("-", nome)

 #Percorre a escolha do usuário           

    loop = int(input("Digite 0 para continuar e 1 para sair: "))
print("Obrigado por utilizar este programa!")