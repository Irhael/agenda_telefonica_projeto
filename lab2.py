# FUNÇÕES

# Crio o dicionáro que será usado pra armazenar os contatos(chaves do dicionário) e os respectivos telefones.
ag = {}

# Primeira função de incluir novo contato.
# 2 parâmetros, nome e número/números do contato, atrela esses números ao contato.
def incluirNovoNome(nome, numeros):
    ag[nome] = numeros

#Segunda função, incluir incluir telefone para um certo contato.
# Se o nome informado existir nas chaves(.keys) do dicionário, o número informado é adicionado ao contato.
# Se o nome informado não existir na agenda, pergunta ao usuário se quer incluí-lo na agenda.
# Se a resposta for 's'(sim) o programa adiciona o contato e o telefone à agenda.
# Se a resposta for 'n'(não) o telefone nem o contato são adicionados e retorna pro menu.
def incluirTelefone(nome, numero):
    if nome in ag.keys():
        ag[nome].append(numero)
    else:
        k = input('Contato não existente! Deseja incluí-lo ele na agenda? (s/n): ')
        if k == 's':
            numeros = [numero]
            incluirNovoNome(nome, numeros)
            print(ag)
        elif k == 'n':
            return

# Terceira função, exclui o contato informado da agenda(incluindo os telefones desse contato)
def excluirNome(nome):
    if nome in ag:
        del ag[nome]

# Quarta função, exclui um telefone específico atrelado à um contato.
# Se o contato informado só tiver 1 telefone atrelado à ele, o contato é apagado.
# Se ele tiver mais de 1 telefone, é verificado se o nome do contato existe,
# se existe, verifica se o número informado está atrelado à esse contato e remove o número.
def excluirTelefone(nome, numero):
    x = ag[nome]
    if len(x) == 1: # Contato com 1 telefone.
        del ag[nome] # Deletado.
    elif nome in ag.keys():
        if numero in ag[nome]:
            ag[nome].remove(numero)


# Quinta função, informa os telefones atrelados à um certo contato.
# Verifica se o nome informado consta nas chaves do dicionário
# Se tiver, informa os números desse contato
# Se não, informa que o contato não existe.
def consultarTelefone(nome):
    if nome in ag.keys():
        print(ag[nome])
    else:
        print('Contato inexistente!')

####################################################################################################################################
# INTERFACE

# Em um loop, ponho o input do menu com as opções.
# OBS: Adicionei 2 novas opções, uma pra ver toda agenda(6) e outra pra encerrar o programa(7).
while True:
    a = int(input('Menu: \n 1 - Adicionar Novo Contato \n 2 - Adicionar Telefone \n 3 - Excluir Contato\n 4 - Excluir '
                  'Telefone\n 5 - Consultar Telefone\n 6 - Ver agenda\n 7 - Encerrar Programa\n\nEscolha uma opção: '))
    # 1 - Usando a função de incluir novo nome. nome = nome e numeros = telefones.
    # Peço o nome e o telefone do contato
    # Guardo os telefones em um lista atrelada ao nome
    # Ponho um loop para pedir um novo número para o contato até quando o usuário pedir pra cancelar o loop(digitando 0)
    # Ponho uma varivável 'z' com um número negativo qualquer(não pode ser positivo pois se for pode ser um número que o usuário quer colocar)
    # Depois enquanto z não for 0, os telefones informados pelo usuário vão sendo adicionados à lista de telefones.
    if a == 1:
        nome = input("Nome: ")
        telefones = [int(input("Telefone: "))]
        z = -999
        while z != 0:
            z = int(input("Insira outro telefone(Digite 0 para sair): "))
            if z != 0:
                telefones.append(z)
        incluirNovoNome(nome, telefones)
    # 2 - Usando a função de incluir novo telefone
    # Peço o Nome e o Telefone que deseja adicionar ao contato
    # Se esse nome não existe acontece o processo explicado anteriormente na função
    elif a == 2:
        nome = input("Nome: ")
        telefone = int(input("Telefone: "))
        incluirTelefone(nome, telefone)
    # 3 - Usando a função de excluir nome para excluir o contato inteiro.
    # Peço o nome que o usuário deseja excluir.
    elif a == 3:
        nome = (input("Nome do contato que deseja excluir: "))
        excluirNome(nome)
    # 4 - Usando a função de excluir telefone de um contato
    # Peço o nome do contato e o telefone que o usuário deseja excluir .
    # Se o contato tiver só 1 telefone, contato é excluído.
    elif a == 4:
        nome = input("Nome: ")
        telefone = int(input("Telefone que deseja excluir: "))
        excluirTelefone(nome, telefone)
    # 5 - Usando a função de consular os telefones de certo cotnato
    # Peço o nome do contato que o usuário deseja saber os telefones.
    elif a == 5:
        consultarTelefone(input("Nome: "))
    # 6 - Printa toda a agenda.
    elif a == 6:
        print(ag)
    # 7 - Encerra o loop.
    elif a == 7:
        print("Programa encerrado!")
        break