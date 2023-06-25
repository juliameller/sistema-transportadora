#importar dados da biblioteca csv
import csv
from menu_trabalho import mostrar_menu
from menu_trabalho import mostrar_submenu

#indicação do arquivo que esta sendo manipulado, as delimitações, criação dicionário vazio para distância. 
with open('DNIT-Distancias-Modificado.csv') as csvfile:
    planilha = csv.reader(csvfile, delimiter=';')
    cidades = next(planilha)[1:]  
    distancias = {cidade: {} for cidade in cidades}  
    for linha in planilha:
        cidade = linha[0]
        for i, d in enumerate(linha[1:]):
            distancias[cidade][cidades[i]] = int(d)

#Dados do porte de caminhão e custo
porte_caminhao = {'PEQUENO': 6.47, 'MÉDIO': 12.24,'GRANDE': 23.48}
capacidade_caminhao = {'PEQUENO': 1000, 'MÉDIO': 5000, 'GRANDE': 10000}

mostrar_menu()
opcao_menu_principal = None

while opcao_menu_principal not in [1, 2, 3, 4]:
    try:
        opcao_menu_principal = int(input("Digite sua opção: "))
    except ValueError:
        print("Opção inválida. Digite apenas números.")

# opção 1 do menu principal.
def consulta_cidades():

    #lista enumerada das cidades      
    for i, cidade in enumerate(cidades):
        print(f"{i+1}. {cidade}")

# opção 2 do menu principal. 
def consultar_valores():
    print('---------------VALORES----------------')
    print(f'PORTE\t\tCAPACIDADE(Kg)\tCUSTO')
    for porte in porte_caminhao:
        custo = porte_caminhao[porte]
        capacidade = capacidade_caminhao[porte]
        print(f"{porte}\t\t{capacidade}\t\t{custo}")

dicionario_itens = {"celular": 0.5, "geladeira": 60.0, "freezer": 100.0, "cadeira": 5.0, "luminária": 0.8, "lavadora de roupa": 120.0}

#opção 3 menu principal:
def orcamento():
    
    mostrar_submenu()
    opcao_submenu = None
    while opcao_submenu not in [1, 2, 3]:
        try:
            opcao_submenu = int(input("Digite sua opção: "))
            
        except ValueError:
            print("Opção inválida. Digite apenas números.")

#opção 1 do submenu
    if opcao_submenu == 1:
        print('\nLista de itens cadastrados: ')
        for nome_item, peso_item in dicionario_itens.items():
            print(f"{nome_item} - {peso_item} kg")

#opção 2 do submenu                    
    elif opcao_submenu == 2:
        nome_item = input("Nome do item: ")
        peso_item = float(input("Peso do item (em Kg): "))
        print("Itens cadastrados com sucesso!")
        dicionario_itens[nome_item] = peso_item
        novos_itens = input("Deseja cadastrar novos itens? (S/N) ")

        while True:
            if novos_itens.upper() == "S":
                nome_item = input("Nome do item: ")
                peso_item = float(input("Peso do item (em Kg): "))
                print("Itens cadastrados com sucesso!")
                dicionario_itens[nome_item] = peso_item


                novos_itens = input("Deseja cadastrar mais itens? (S/N) ")
            
            elif novos_itens.upper() == "N":
                orcamento()
                break
                
            else:
                print("Opção inválida. Tente novamente.")
                novos_itens = input("Deseja cadastrar mais itens? (S/N) ")
                continue


#opção 3 do submenu
    elif opcao_submenu == 3:
       
       print('\n---------Calcular transporte-----------')      
       cidade_partida = input('\nDigite a cidade de partida: ')
       cidade_partida_upper = cidade_partida.upper()
       while cidade_partida_upper not in cidades:
            print(f"\n A cidade '{cidade_partida_upper}' não está na lista.") 
            cidade_partida = input('\nDigite a cidade de partida: ')
            cidade_partida_upper = cidade_partida.upper()

            
       cidade_chegada = input('\nDigite a cidade de chegada: ')
       cidade_chegada_upper = cidade_chegada.upper()
       while cidade_chegada_upper not in cidades:
            print(f"\n A cidade '{cidade_chegada_upper}' não está na lista.")  
            cidade_chegada = input('\nDigite a cidade de chegada: ')
            cidade_chegada_upper = cidade_chegada.upper() 
    
       peso_total = 0
       peso_total_final = 0
       itens_transportados = []
       dicionario_itens_qtds = {}

       while True:
            item_transportado = input('\nDigite o item que será transportado: ')
            item_transportado_lower = item_transportado.lower()
            while item_transportado_lower not in dicionario_itens.keys():
                print(f"\n O item '{item_transportado_lower}' não está na lista.")
                item_transportado = input('\nDigite o item que será transportado: ')
                item_transportado_lower = item_transportado.lower()
            itens_transportados.append(item_transportado_lower)
            quantidade_item = int(input('\nDigite a quantidade de unidades deste item: '))
            dicionario_itens_qtds[item_transportado_lower] = quantidade_item

            peso_item = dicionario_itens[item_transportado_lower] * quantidade_item
            peso_total += peso_item
            peso_total_final += peso_item

            while True:
                novos_itens = input("\nDeseja inserir mais itens? (S/N) ")
                if novos_itens.upper() == "S":
                    break
                elif novos_itens.upper() == "N":
                    break
                else:
                    print("\n Opção inválida. Tente novamente.")
                    continue

            if novos_itens.upper() == "N":
                break

       distancia = distancias[cidade_partida_upper][cidade_chegada_upper]
       contagem_pequeno = 0
       contagem_medio = 0
       contagem_grande = 0
       custo_total = 0
    
       while peso_total > 0:
            if peso_total <= 1000:
                custo = distancia * porte_caminhao['PEQUENO']
                contagem_pequeno += 1
                custo_total += custo
                peso_total -= 1000
            elif peso_total > 1000 and peso_total <= 5000:
                custo = distancia * porte_caminhao['MÉDIO']
                contagem_medio += 1
                custo_total += custo
                peso_total -= 5000
            elif peso_total > 5000:
                custo = distancia * porte_caminhao['GRANDE']
                contagem_grande += 1
                custo_total += custo
                peso_total = peso_total - 10000
               
        
       print('\n-----------------------COTAÇÃO---------------------------')
       print(f'\nDe {cidade_partida_upper} para {cidade_chegada_upper}, a distância é de {distancia} km')
       print('\nOs itens transportados e quantidades são: ')
       for item, quantidade in dicionario_itens_qtds.items():
           print(f'{item} - {quantidade}') 
       print(f'\nO peso total é: {peso_total_final:.2f} quilos')
       print(f'\nPara transporte dos produtos será necessário: ')
       print(f'{contagem_pequeno} caminhão(ões) de porte PEQUENO')
       print(f'{contagem_medio} caminhão(ões) de porte MÉDIO')
       print(f'{contagem_grande} caminhão(ões) de porte GRANDE')
       print(f'\nO valor total do transporte dos itens é R$ {custo_total:.2f}.')

                  

# MENU PRINCIPAL
while opcao_menu_principal != 4:
    if opcao_menu_principal == 1:
        print('\nVocê selecionou "Consultar trechos disponíveis", abaixo são as cidades disponiveis:')
        consulta_cidades()
        while True:
            voltar_menu_principal = input("\nDigite '0' para voltar ao menu inicial: ")
            if voltar_menu_principal == '0':
                break  
            else:
                print("Opção inválida. Tente novamente.")

    elif opcao_menu_principal == 2:
        print('\n Consultar valores:')
        consultar_valores()
        while True:
            voltar_menu_principal = input("\nDigite '0' para voltar ao menu inicial: ")
            if voltar_menu_principal == '0':
                break  
            else:
                print("Opção inválida. Tente novamente.")

    elif opcao_menu_principal == 3:
        orcamento()
        while True:
            voltar_menu_principal = input("\nDigite '0' para voltar ao menu principal: ")
            if voltar_menu_principal == '0':
                break 
            else:
                print("Opção inválida. Tente novamente.")
    
    elif opcao_menu_principal != int:
        print('Opção inválida')
        
    mostrar_menu()
    opcao_menu_principal = int(input('Digite sua opção: '))
print('\nPrograma encerrado')

