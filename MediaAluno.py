#media aluno
totalNotas = int (input ("Digite a quantidade de notas: "))
SomaTotal = 0
cont = 0
while cont < totalNotas:
    nota = float (input("Digite as notas: "))
    SomaTotal += nota
    cont += 1


media = SomaTotal / totalNotas
print (f"A média das notas é: {media:.2f}")
