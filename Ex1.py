"""
- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato
"""
import os

def adicionar_contatos(contatos, nome_contato, numero_contato, email_contato): 
    #Estou adicionando um contato, salvando ele num dicionario com lista
    contato = {'Contato: ': nome_contato, 'Número: ': numero_contato, 'Email: ': email_contato, 'favorito': False}
    contatos.append(contato)
    print(f'O contato {nome_contato} foi adicionado com sucesso')
    return

def visualizar_contatos(contatos):
    print('\nLista de contatos')
    for indice, contato in enumerate(contatos, start=1):
        visu_contato = contato["Contato: "]
        visu_numero = contato["Número: "]
        visu_email = contato["Email: "]
        # visualizar os contatos favoritos
        status = "☆" if contato['favorito'] else ' '
        print(f'[{status}] {indice}º. Contato:  {visu_contato}  Número:  {visu_numero}  E-mail:  {visu_email}.')

def editar_contato(contatos, indice_contato, novo_nome_contato, novo_numero_contato, novo_email):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["Contato: "] = novo_nome_contato
        contatos[indice_contato_ajustado]["Número: "] = novo_numero_contato
        contatos[indice_contato_ajustado]["Email: "] = novo_email
        print(f'Contato {novo_nome_contato} atualizado com sucesso.')
    return

def marcar_favorito(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1 
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f'Contato {indice_contato} marcado como favorito com sucesso.')
    return

def desmarcar_favorito(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    contatos[indice_contato_ajustado]["favorito"] = False
    print(f'Contato {indice_contato} desmarcado como favorito com sucesso.')
    return

def visualizar_favoritos(contatos):
    print('Lista de contatos favoritos')
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            visu_contato = contato["Contato: "]
            visu_numero = contato["Número: "]
            visu_email = contato["Email: "]
            status = "☆" if contato['favorito'] else ' '
            print(f'[{status}] {indice}º. Contato:  {visu_contato}  Número:  {visu_numero}  E-mail:  {visu_email}.')
    return
def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato >= 0 and indice_contato_ajustado < len(contatos):
        contatos.remove(contatos[indice_contato_ajustado])
    
    return

contatos = []
while True:
    try:
        print('\nApp de contatos')
        print()
        print('1. Cadastrar contato')
        print('2. Visualisar contatos.')
        print('3. Editar contatos.')
        print('4. marcar/desmarcar um contato como favorito.')
        print('5. Visualisar contatos favoritos.')
        print('6. Apagar contatos.')
        print('7. Fechar app.')
        escolha = int(input('Escolha um número: (1/2/3/4/5/6/7): '))
        print()

        if escolha == 1:
            nome_contato = input('Nome do contato: ')
            numero_contato = int(input('Número do contato: '))
            email_contato = input('Email do contato: ')
            adicionar_contatos(contatos,nome_contato, numero_contato, email_contato)

        elif escolha == 2:
            visualizar_contatos(contatos)       

        elif escolha == 3:
            visualizar_contatos(contatos)
            indice_contato = int(input('Digite o número do contato que deseja editar: '))
            novo_nome_contato = input('Novo nome do contato: ')
            novo_numero_contato = int(input('Novo número do contato: '))
            novo_email = input('Novo E-mail do contato: ')
            editar_contato(contatos, indice_contato, novo_nome_contato, novo_numero_contato, novo_email)

        elif escolha == 4:        
            print('1. MARCAR COMO FAVORITO')
            print('2. DESMARCAR COMO FAVORITO')
            escolha_desmarcar_marcar = int(input('Digite um número: '))
            if escolha_desmarcar_marcar == 1:
                visualizar_contatos(contatos)
                indice_contato = int(input('Qual contato deseja marcar como favorito: '))
                marcar_favorito(contatos, indice_contato)
            elif escolha_desmarcar_marcar == 2:
                visualizar_contatos(contatos)
                indice_contato = int(input('Qual contato deseja desmarcar como favorito: '))
                desmarcar_favorito(contatos, indice_contato)
            else:
                print('Digite um número.')

        elif escolha == 5:
            visualizar_favoritos(contatos)
        
        elif escolha == 6:
            visualizar_contatos(contatos)
            indice_contato = int(input('Qual contato deseja apagar: '))
            apagar_contato(contatos, indice_contato)

        elif escolha == 7:
            print('Saindo do app...')
            #limpando o terminal
            os.system('cls')
            break

    except ValueError:
        # caso o cliente erre ao digitar 
        print('Por favor, digite corretamente.')