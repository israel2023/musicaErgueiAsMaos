def lista_animais(posicao): # Definição da função lista_animais, que recebe a posição como argumento
    animais = ["passarinhos","pinguins", "sapinhos"] # Lista de animais disponíveis
    print(f"E os {animais[posicao]},como os filhos do Senhor\n") # Exibição do animal na posição especificada, formatado na frase
    
        
def primeira_parte(troca, estrofe): # Definição da função primeira_parte, que recebe troca e estrofe como argumento
    print(f'{"Por isso...!" if troca else ""}') # Expressão condicional que imprime "Por isso...!" se a variável troca for verdadeira, senão, imprime uma string vazia
    for i in range(estrofe): # Loop que executa a quantidade de vezes especificada pelo argumento estrofe
        for j in range(2): # Loop aninhado que executa duas vezes para cada iteração de i
            print(f"Erguei as mãos e dai glória a Deus") # Impressão do verso "Erguei as mãos e dai glória a Deus"
        print("Erguei as mãos") # Após o loop interno, imprime a linha "Erguei as mãos"
        print("E cantai como os filhos do Senhor\n") # Em seguida, imprime "E cantai como os filhos do Senhor\n"

def segunda_parte(posicao = 0): # Definição da função segunda_parte com um argumento opcional posicao
    animais = ["elefante","minhoquinha","canguru"] # Lista de animais
    for i in range(2):  # Loop para imprimir a linha duas vezes
        print("Os animaizinhos subiram de dois em dois")
    print(f"O {animais[posicao]}") # Imprime o animal correspondente à posição na lista
    lista_animais(posicao) # Chama a função lista_animais com o argumento posicao
    if posicao < 2: # Verifica se posicao é menor que 2 para continuar chamando a função segunda_parte com a próxima posição
        segunda_parte(posicao + 1)


def terceira_parte(): # Definição da função terceira_parte
    for i in range(2): # Loop para imprimir uma frase duas vezes
        print("Deus disse a Noé: Constrói uma arca")
    print("Que seja feita") # Imprime duas linhas adicionais
    print("De madeira para os filhos do Senhor\n")
                     
def quarta_parte(teste, vezes): # Definição da função quarta_parte que recebe dois argumentos: teste e vezes
    for i in range(vezes): # Loop para imprimir o bloco de texto 'vezes' vezes
        # Imprime o texto dependendo do valor de 'teste'
        print(f"""
{"E atenção agora,porque" if teste else ""}
O senhor tem muitos filhos
{"Muitos" if teste else "Muitos"} filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor""")
        if teste: # Condicional para imprimir uma linha adicional caso 'teste' seja verdadeiro
            print("Braço direito, braço esquerdo")

def quinta_parte(teste, vezes): # Definição da função quinta_parte que recebe dois argumentos: teste e vezes
    for i in range(vezes): # Loop para imprimir o bloco de texto 'vezes' vezes
        # Imprime o texto dependendo do valor de 'teste'
        print(f"""
O senhor tem muitos filhos
{"Muitos" if teste else "Muitos"} filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor""")
        if teste: # Condicional para imprimir uma linha adicional caso 'teste' seja verdadeiro
            print("Braço direito, braço esquerdo\nPerna direita")

def sexta_parte(): # Definição da função sexta_parte
    print("Braço direito, braço esquerdo\nPerna direita, Perna esquerda") # Imprime uma mensagem

def setima_parte(): # Definição da função setima_parte
    print("\nBraço direito, braço esquerdo\nPerna direita, Perna esquerda ") # Imprime uma mensagem


def oitava_parte(teste, vezes): # Definição da função oitava_parte que recebe dois argumentos: teste e vezes
    for i in range(vezes): # Loop para imprimir o bloco de texto 'vezes' vezes
        # Imprime o texto dependendo do valor de 'teste'
        print(f"""
{"Balança a cabeça" if teste else ""}
O senhor tem muitos filhos
{"Muitos" if teste else "Muitos"} filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor""")
        if teste: # Condicional para imprimir uma linha adicional caso 'teste' seja verdadeiro
            print("\nBraço direito, braço esquerdo\nPerna direita, Perna esquerda")
            print("Balança a cabeça, dá uma voltinha")


def nona_parte(): # Definição da nona_parte
    # Imprime as mensagens
    print("Balança a cabeça, dá uma voltinha")
    print("Dá um pulinho e abraça o irmão")
    

def cantar_musica(): # Definição da função cantar_musica
    #False porque não quero pegar a primeira parte "por isso!" e esse 1 é a quantidade de vezes que vou repetir a frase
    primeira_parte(False, 1) # Executa a primeira parte da música com argumento False e 1 para quantidade de vezes
    segunda_parte() # Executa a segunda parte da música
    terceira_parte()# Executa a terceira parte da música
    primeira_parte(True, 3) # Executa a primeira parte da música True e 3 para quantidade de vezes
    quarta_parte(True, 1) # Executa a quarta parte da música True e 3 para quantidade de vezes
    quinta_parte(True, 1) # Executa a quinta parte da música com argumento True e 1 para quantidade de vezes
    quinta_parte(False, 1) # Executa a quinta parte da música com argumento False e 1 para quantidade de vezes
    sexta_parte()
    oitava_parte(True,1)
    quinta_parte(False, 1)
    oitava_parte(True, 0)
    setima_parte()
    nona_parte()
    
cantar_musica()
