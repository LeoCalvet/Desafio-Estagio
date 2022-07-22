"""
h) Os resultados da enquete foram compilados em um arquivo CSV com o seguinte cabeçalho:
    dia, codigo-pergunta, matricula, curso-codigo, opcao-codigo

i) As perguntas foram compiladas em outro arquivo CSV com o seguinte cabeçalho:
    curso-codigo, curso-nome, pergunta-codigo, pergunta-descricao

j) As opções possíveis das perguntas encontram-se em outro arquivo CSV com o seguinte cabeçalho:
    pergunta-codigo, opcao-codigo, opcao-descricao

Primeira tarefa seria compilar essas informações e apresentar o resultado da pesquisa. 

Para isso você deve seguir as seguintes regras:  
1. Utilizar qualquer linguagem de programaçãoqualquer linguagem de programação que tenha as estruturas necessárias;
    - Python
2. Apresentar o resultado da pesquisa em texto, sendo que, uma possível solução seria imprimir no terminal;
3. Informar o total de nome_cursos participantes;
4. Informar o total de perguntas;
5. Informar o total de entrevistados para cada um dos dias da enquete; e
6. Apresentar os resultados das perguntas em apenas um dos formatos abaixo
        2 - Resultado por Curso: **Formato utilizado**
            
            Código do Curso - Nome do Curso

            Perguntas:

            Código da Pergunta - Descrição da Pergunta
            
            Total de entrevistados:                  xxx
            Total de entrevistados do curso:         xxx
            Total de entrevistados de outros nome_cursos: xxx
            
            Resultado       | Porcentagem
            A - Descrição   | xx
            B - Descrição   | xx
            C - Descrição   | xx
            D - Descrição   | xx
            Não Respondida  | xx

Para poder fazer a saida como desejado tem que:
1. Separar por curso
    - Usar a tabela de 'respostas.csv'
    - Só tem 3 nome_cursos
        - c001 (Computação)
        - m010 (Medicina)
        - p100 (Psicologia)
2. Pegar cada perguntas
3. Entrevistatos
    1. Total
    2. Do curso
    3. Resto
"""


import csv
from os import close
from readline import append_history_file

def perguntas_cada_curso():
    with open("perguntas.csv", 'r') as info:
        arquivo_perguntas_csv = csv.reader(info, delimiter=',')
        
        for n, linha in enumerate(arquivo_perguntas_csv):
            if n != 0:
                if linha[0] not in cod_curso:
                    cod_curso.append(f"{linha[0]}")
                if linha[1] not in nome_cursos:    
                    nome_cursos.append(f"{linha[1]}")
                if linha[2] not in pergunta:
                    # quando a pergunta for colocar a sua posição na lista + 1
                    # será o número da questão
                    pergunta.append(f"{linha[3]}")
                # if 1 <= n < 6:
                #     perguntas_comp.append(f"{linha[2]}")
                # elif 6 <= n < 15:
                #     perguntas_med.append(f"{linha[2]}")
                # elif 15 <= n < 23:
                #     perguntas_psic.append(f"{linha[2]}")

def opcoes_cada_pergunta():
    with open("opcoes.csv", "r") as info:
        arquivo_opcoes_csv = csv.reader(info, delimiter=',')
        for _ in range(22):
            # criação de 22 espaços para as opções
            opcao_pergunta.append([])

        for n, linha in enumerate(arquivo_opcoes_csv):
            if n != 0:
            # if necessário para pular o cabeçalho
                num = int(linha[0])
                num = num - 1 
                opcao_pergunta[num].append(f"{linha[1]},{linha[2]}")

def resps_cada_pergunta():
    # fazer uma lista com o tamanho da qtd de questões
    # cada posisão representa uma questão
    for _ in range(22):
        resp_perguntas.append([])
        # criar para cada questão uma lista para cada alternativa que tiver
        qtd_opcoes_na_questao = len(opcao_pergunta[_])
        for __ in range(qtd_opcoes_na_questao):
            resp_perguntas[_].append([])
    with open("respostas.csv", "r") as info:
        arquivo_resps_csv = csv.reader(info, delimiter=',')
        for n, linha in enumerate(arquivo_resps_csv):
            if n != 0:
                questao_em_analise = int(linha[1])
                qtd_opcoes_na_questao = len(opcao_pergunta[questao_em_analise-1])
                resp_da_questao_em_analise = linha[4]
                match resp_da_questao_em_analise:
                    # como as questões são multipla escolha sempre terá as opções A e B
                    case 'A':
                        resp_perguntas[questao_em_analise-1][0].insert(0,resp_da_questao_em_analise)
                    case 'B':
                        resp_perguntas[questao_em_analise-1][1].insert(0,resp_da_questao_em_analise)
                    case 'C':
                        resp_perguntas[questao_em_analise-1][2].insert(0,resp_da_questao_em_analise)
                    case 'D':
                        resp_perguntas[questao_em_analise-1][3].insert(0,resp_da_questao_em_analise)

def calculo_porcentagem_alternativas():
    for a in range(len(resp_perguntas)):
        # criacão da lista que receberá as porcentagens
        porcentagem_resp_perguntas.append([])
        qtd_alternativas = len(resp_perguntas[a])
        for _ in range(qtd_alternativas):
            porcentagem_resp_perguntas[a].append([])
        match qtd_alternativas:
            case 2:
                qtd_a = len(resp_perguntas[a][0])
                qtd_b = len(resp_perguntas[a][1])
                total_marcadas = qtd_a+qtd_b
                porcento_a = round((qtd_a*100)/total_marcadas,1)
                porcento_b = round((qtd_b*100)/total_marcadas,1)
                porcentagem_resp_perguntas[a][0].insert(0, porcento_a)
                porcentagem_resp_perguntas[a][1].insert(0, porcento_b)
            case 3:
                qtd_a = len(resp_perguntas[a][0])
                qtd_b = len(resp_perguntas[a][1])
                qtd_c = len(resp_perguntas[a][2])
                total_marcadas = qtd_a + qtd_b + qtd_c
                porcento_a = round((qtd_a*100)/total_marcadas,1)
                porcento_b = round((qtd_b*100)/total_marcadas,1)
                porcento_c = round((qtd_c*100)/total_marcadas,1)
                porcentagem_resp_perguntas[a][0].insert(0, porcento_a)
                porcentagem_resp_perguntas[a][1].insert(0, porcento_b)
                porcentagem_resp_perguntas[a][2].insert(0, porcento_c)
            case 4:
                qtd_a = len(resp_perguntas[a][0])
                qtd_b = len(resp_perguntas[a][1])
                qtd_c = len(resp_perguntas[a][2])
                qtd_d = len(resp_perguntas[a][3])
                total_marcadas = qtd_a + qtd_b + qtd_c + qtd_d
                porcento_a = round((qtd_a*100)/total_marcadas,1)
                porcento_b = round((qtd_b*100)/total_marcadas,1)
                porcento_c = round((qtd_c*100)/total_marcadas,1)
                porcento_d = round((qtd_d*100)/total_marcadas,1)
                porcentagem_resp_perguntas[a][0].insert(0, porcento_a)
                porcentagem_resp_perguntas[a][1].insert(0, porcento_b)
                porcentagem_resp_perguntas[a][2].insert(0, porcento_c)
                porcentagem_resp_perguntas[a][3].insert(0, porcento_d)
    # print(porcentagem_resp_perguntas)

                



def imprimir():
    print("__________________________________________________________________________")
    print(f"{cod_curso[0]} - {nome_cursos[0]}")
    print("\n")
    print("Perguntas:")
    print("\n")
    for k in range(len(pergunta)):
        print("\n")
    # k começará em 0, logo caso queira que pega a pergunta 3 o valor real de k será 2
    # k será o representante da pergunta que estou analizando
        print(f"{k+1} - {pergunta[k]}")
        print("\n")
        print(f"Total de entrevistados:                  {total_entrevistados}")
        print(f"Total de entrevistados do curso:         {total_curso_comp}")
        print(f"Total de entrevistados de outros cursos: {total_entrevistados - total_curso_comp}")
        print("\n")
        print(f"Resultado          |          Porcentagem")
        for _ in range(len(opcao_pergunta[k])):
            saida = opcao_pergunta[k][_]
            alternativa = saida[:1]
            texto_alternativa = saida[2:]
            porcentagem_resp_perguntas_bonito = porcentagem_resp_perguntas[k][_]
            porcentagem_resp_perguntas_bonito = str(porcentagem_resp_perguntas_bonito)[1:-1]
            print(f"{alternativa} - {texto_alternativa}   |   {porcentagem_resp_perguntas_bonito}")
    print("__________________________________________________________________________")
    print(f"{cod_curso[1]} - {nome_cursos[1]}")
    print("\n")
    print("Perguntas:")
    print("\n")
    for k in range(len(pergunta)):
        print(f"{k+1} - {pergunta[k]}")
        print("\n")
        print(f"Total de entrevistados:                  {total_entrevistados}")
        print(f"Total de entrevistados do curso:         {total_curso_med}")
        print(f"Total de entrevistados de outros cursos: {total_entrevistados - total_curso_med}")
        print("\n")
        print(f"Resultado          |          Porcentagem")
        for _ in range(len(opcao_pergunta[k])):
            saida = opcao_pergunta[k][_]
            alternativa = saida[:1]
            texto_alternativa = saida[2:]
            porcentagem_resp_perguntas_bonito = porcentagem_resp_perguntas[k][_]
            porcentagem_resp_perguntas_bonito = str(porcentagem_resp_perguntas_bonito)[1:-1]
            print(f"{alternativa} - {texto_alternativa}   |   {porcentagem_resp_perguntas_bonito}")
    
    print("__________________________________________________________________________")
    print(f"{cod_curso[2]} - {nome_cursos[2]}")
    print("\n")
    print("Perguntas:")
    print("\n")
    for k in range(len(pergunta)):
        print(f"{k+1} - {pergunta[k]}")
        print("\n")
        print(f"Total de entrevistados:                  {total_entrevistados}")
        print(f"Total de entrevistados do curso:         {total_curso_psic}")
        print(f"Total de entrevistados de outros cursos: {total_entrevistados - total_curso_psic}")
        print("\n")
        print(f"Resultado          |          Porcentagem")
        for _ in range(len(opcao_pergunta[k])):
            saida = opcao_pergunta[k][_]
            alternativa = saida[:1]
            texto_alternativa = saida[2:]
            porcentagem_resp_perguntas_bonito = porcentagem_resp_perguntas[k][_]
            porcentagem_resp_perguntas_bonito = str(porcentagem_resp_perguntas_bonito)[1:-1]
            print(f"{alternativa} - {texto_alternativa}   |   {porcentagem_resp_perguntas_bonito}")
        print("\n")





nome_cursos = []
cod_curso = []
pergunta = []
opcao = []

total_entrevistados = 101
total_curso_comp = 38
total_curso_med = 38
total_curso_psic = 25

opcao_pergunta = []

resp_perguntas = []
porcentagem_resp_perguntas = []

perguntas_cada_curso()
opcoes_cada_pergunta()
resps_cada_pergunta()
calculo_porcentagem_alternativas()
imprimir()