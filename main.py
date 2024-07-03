#Fórmula de juros compostos: FV/montante = PV/inicial * (1 + taxa) ** tempo

def informacoes_usuario():
    global nome
    nome = input("Qual é o seu nome?: ")
    print(f"Olá {nome}, seja muito bem-vindo a calculadora de juros compostos!")

def calculo_juros_compostos():    
    valor_inicial = float(input("Digite a quantidade de dinheiro inicial do investimento: "))
    tempo = int(input("Digite quanto tempo você deixará o dinheiro investido. Digite apenas números: "))
    metodo_tempo = int(input("O período é anual ou mensal? Digite 1 para anual ou 2 para mensal: "))
    taxa = float(input("Digite, em percentual, a taxa de retorno do seu investimento: "))
    metodo_taxa = int(input("A taxa é anual ou mensal? Digite 1 para anual ou 2 para mensal: "))
    
    conversao_taxa = (taxa / 100)

    if metodo_tempo != metodo_taxa:
            
        if metodo_taxa == 1:
            conversao_taxa = ((1 + conversao_taxa) ** (1/12)) - 1
            
        elif metodo_tempo == 1:
            tempo = tempo * 12

    montante = round(valor_inicial * ((1 + conversao_taxa) ** tempo), 2)
    juros = round((montante - valor_inicial), 2)
    
    resultado_calculo(montante=montante, juros=juros)

def resultado_calculo(montante, juros):
        print(f"O seu montante final será de R$ {montante} e você terá ganho R$ {juros}")        

def recomecar():
    novo_calculo = int(input("Quer fazer outro cálculo? Digite 1. Caso não, digite 0: "))
    if novo_calculo != 1:
        return False
    return True

def main():
    global nome
    desejaCalcular = True
    informacoes_usuario()
    while desejaCalcular:
        calculo_juros_compostos()
        desejaCalcular = recomecar()

    print(f"Fim do programa, {nome}!")


main()