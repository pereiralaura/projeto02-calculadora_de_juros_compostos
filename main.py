#Fórmula de juros compostos: FV/montante = PV/inicial * (1 + taxa) ** tempo

#descobrindo o montante ao mês
valor_inicial = float(input("Qual o seu valor inicial?: "))
taxa = float(input("Qual a taxa de juros mensais?: "))
tempo = float(input("Qual a ser resgatado? Insira em meses: "))
taxa_convertida = taxa / 100
montante = valor_inicial * ((1 + taxa_convertida) ** tempo)

print(f"O seu montante final será de: R$ {montante:.2f}")