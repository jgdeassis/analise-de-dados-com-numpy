# Importação da biblioteca NumPy
import numpy as np

# Criação da matriz(3x4) da turma  
turma = np.array([[7.5 , 6.0, 8.0, 9.5], [7.7, 9.5, 4.5 , 10.0] , [4.2, 2.0 , 3.5 , 2.0]])

# Estatísticas da turma 
somat = turma.sum()
meant = turma.mean().round(2)

print(f"Nota da turma:\n{turma}")
print(f"Soma da nota da turma:\n{somat}")
print(f"Média da nota da turma:\n{meant}")

if meant>= 7:
    print("Rendimento esperado atingido.")
else:
    print("Turma abaixo do rendimento esperado.")

# Estatísticas das provas 
pmedia = turma.mean(axis= 0).round(2)
pmax = turma.max(axis= 0)
pmin = turma.min(axis= 0)

print(f"\nMédia das provas: {pmedia}")
print(f"\nMaior nota das provas: {pmax}")
print(f"\nMenor nota das provas: {pmin}") 

# Iteração de estatísticas dos alunos individualmente(linhas)
x = 1
for aluno in turma:
    name = str(x) + "°"
    print(f"\nNota do aluno {name}: {aluno}")
    total = aluno.sum()
    media = aluno.mean()
    almax = aluno.max()
    almin = aluno.min()
    print(f"Nota total do {name} aluno: {total}")
    print(f"\nMédia do {name} aluno: {media:.2f}")
    print(f"\nMaior nota do {name} aluno: {almax}")
    print(f"\nMenor nota do {name} aluno: {almin}")
    if media < 7:
        print(f"{name} Aluno reprovado.")
    else: 
        print(f"{name}Aluno aprovado.")
    x += 1