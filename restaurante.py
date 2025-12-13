cliente = input("Bem Vindo ao nosso sistema!! Digite seu nome: ") #Identificação do cliente
print(f"Olá, {cliente.strip()}! Seja bem-vindo ao nosso restaurante.")

def exibir_menu(): #Função para exibir o menu do restaurante
    print("Menu do Restaurante:")
    print("Pratos:")
    print("1. Macarrão")
    print("2. Pizza")
    print("3. Panqueca")
    print("Bebidas:")
    print("1. Refrigerante")
    print("2. Suco")
    print("3. Água")
    print("4. Cerveja")
exibir_menu()    
# Definição dos pratos e bebidas disponíveis com seus preços
pratos = ("Macarrão, Pizza, Panqueca")
bebidas = ("Refrigerante", "Suco", "Água", "Cerveja")
refrigerante = {'Coca-Cola': 8.00, 'Guaraná': 7.00,'Fanta': 7.00}
suco = {'Suco de Laranja': 7.50, 'Suco de Uva': 6.00,'Suco de Abacaxi': 6.00}
agua = {'Água Sem Gás': 3.00, 'Água Com Gás': 4.50}
cerveja = {'Skol': 6.00, 'Brahma': 6.00,'Heineken': 8.00}
pizza = {'Pizza Grande': 40.00, 'Pizza Media': 30.00,'Pizza Pequena': 20.00}
macarrão = {'Macarrão À Bolonhesa': 40.00, 'Macarrão Penne': 35.00,'Macarrão ao Molho Branco': 32.00}
panqueca = {'Doce': 25.00, 'Salgada': 30.00}
pedido_lista = []
conta = 0.0
primeiro_pedido = True

while True: #Loop principal para fazer pedidos
    if primeiro_pedido: 
        pedido = input("Deseja fazer um pedido? (sim/não): ")
        primeiro_pedido = False
        if pedido not in ["Sim", "sim", "Não", "não"]:
            print("Resposta inválida!")
            break
    else:
        pedido = input("Deseja adicionar mais itens ao seu pedido? (sim/não): ")
    if pedido.lower().strip() == "não":
        print("Obrigado por visitar nosso restaurante. Volte sempre!")
        break
    if pedido not in ["Sim", "sim", "Não", "não"]:
        print("Resposta inválida!")
        break
    if pedido.lower().strip() == "sim":
     print("Pratos disponíveis: ", pratos) 
    prato = input("Qual prato deseja: ")
    match prato.lower().strip():
        case "macarrão":
            print("Tipos de macarrão disponíveis: ", macarrão)
            tipo_macarrao = input("Qual tipo de macarrão deseja: ")
            if tipo_macarrao in macarrão:
                pedido_lista.append(tipo_macarrao)
                conta += macarrão[tipo_macarrao]
                print("Adicionado ao pedido:", {tipo_macarrao})
            else:
                print("Tipo de macarrão não disponível.")    
        case "pizza":
            print("Tamanhos de pizza disponíveis: ", pizza)
            tamanho_pizza = input("Qual tamanho de pizza deseja: ")
            if tamanho_pizza in pizza:
                pedido_lista.append(tamanho_pizza)
                conta += pizza[tamanho_pizza]
                print(f"Adicionado ao pedido:", {tamanho_pizza})
            else:
                print("Tamanho de pizza não disponível.")
        case "panqueca":
            print("Tipos de panqueca disponíveis: ", panqueca)
            tipo_panqueca = input("Qual tipo de panqueca deseja: ")
            if tipo_panqueca in panqueca:
                pedido_lista.append(tipo_panqueca)
                conta += panqueca[tipo_panqueca]
                print(f"Adicionado ao pedido:", {tipo_panqueca})
            else:
                print("Tipo de panqueca não disponível.")
        case _:
            print("Prato não disponível.")
    print("Bebidas disponíveis: ", bebidas)
    bebida = input("Qual bebida deseja: ")
    match bebida.lower().strip():
        case "refrigerante":
            print("Tipos de refrigerante disponíveis: ", refrigerante)
            tipo_refrigerante = input("Qual tipo de refrigerante deseja: ")
            if tipo_refrigerante in refrigerante: 
                pedido_lista.append(tipo_refrigerante)
                conta += refrigerante[tipo_refrigerante]
                print(f"Adicionado ao pedido:", {tipo_refrigerante})
            else:
                print("Tipo de refrigerante não disponível.")
        case "suco":
            print("Tipos de suco disponíveis: ", suco)
            tipo_suco = input("Qual tipo de suco deseja: ")
            if tipo_suco in suco:
                pedido_lista.append(tipo_suco)
                conta += suco[tipo_suco]
                print(f"Adicionado ao pedido:", {tipo_suco})
            else:
                print("Tipo de suco não disponível.")
        case "água":
            print("Tipos de água disponíveis: ", agua)
            tipo_agua = input("Qual tipo de água deseja: ")
            if tipo_agua in agua:
                pedido_lista.append(tipo_agua)
        case "cerveja":
            print("Tipos de cerveja disponíveis: ", cerveja)
            tipo_cerveja = input("Qual tipo de cerveja deseja: ")
            if tipo_cerveja in cerveja:
                pedido_lista.append(tipo_cerveja)
                conta += cerveja[tipo_cerveja]
                print(f"Adicionado ao pedido:", {tipo_cerveja})
            else:
                print("Tipo de cerveja não disponível.")
        case _:
            print("Bebida não disponível.")
    print("Seu pedido até agora: ", pedido_lista)
# Exibição do resumo do pedido e total da conta    
print("Resumo do pedido:")
for item in pedido_lista:
    print("-", item)
print(f"Total a pagar: R$ {conta:.2f}")    
 
            

    





