# =====================================
# BOLETIM UNIVERSITÁRIO SEMESTRAL
# =====================================

def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))

            if 0 <= nota <= 10:
                return nota
            else:
                print("ERRO: a nota deve estar entre 0 e 10.")

        except ValueError:
            print("ERRO: digite um número válido.")


def ler_frequencia():
    while True:
        try:
            frequencia = float(input("Digite a frequência (%): "))

            if 0 <= frequencia <= 100:
                return frequencia
            else:
                print("ERRO: a frequência deve estar entre 0 e 100.")

        except ValueError:
            print("ERRO: digite um número válido.")


def verificar_situacao(media, frequencia):

    if media >= 7 and frequencia > 70:
        return "APROVADO"
    elif media >= 7 and frequencia <= 70:
        return "REPROVADO"
    elif media >= 4 and media < 7 and frequencia > 70:
        return "RECUPERACAO"
    elif media >= 4 and media < 7 and frequencia <= 70:
        return "REPROVADO"
    else:
        return "REPROVADO"


# CONTADORES DA TURMA
total_alunos = 0
total_aprovados = 0
total_reprovados = 0
alunos_em_recuperacao = 0

relatorio = []

# CADASTRO DOS ALUNOS
while True:

    print("\n=================================")
    print("CADASTRO DE ALUNO")
    print("=================================")

    nome = input("Digite o nome do aluno: ")

    while not nome.replace(" ", "").isalpha():
        print("Nome inválido.")
        nome = input("Digite o nome do aluno: ")

    av1 = ler_nota("Digite a nota da AV1: ")
    av2 = ler_nota("Digite a nota da AV2: ")

    frequencia = ler_frequencia()

    media = (av1 + av2) / 2

    situacao = verificar_situacao(media, frequencia)

    # RECUPERAÇÃO
    if situacao == "RECUPERACAO":
        alunos_em_recuperacao += 1
        print("\nAluno em recuperação.")
        nota_rec = ler_nota("Digite a nota da recuperação: ")
        media_final = (media + nota_rec) / 2

        if media_final >= 6:
            situacao = "APROVADO"
        else:
            situacao = "REPROVADO"

        media = media_final

    # BOLETIM
    print("\n=================================")
    print("BOLETIM UNIVERSITÁRIO")
    print("=================================")

    print(f"Aluno: {nome}")
    print(f"AV1: {av1:.1f}")
    print(f"AV2: {av2:.1f}")
    print(f"Média Final: {media:.1f}")
    print(f"Frequência: {frequencia:.1f}%")
    print(f"Situação: {situacao}")

    print("=================================")

    # ESTATÍSTICAS
    total_alunos += 1

    if situacao == "APROVADO":
        total_aprovados += 1
    else:
        total_reprovados += 1

    relatorio.append([nome, media, frequencia, situacao])

    continuar = input(
        "\nDeseja cadastrar outro aluno? (S/N): "
    ).upper()

    if continuar != "S":
        break

# RELATÓRIO FINAL
print("\n")
print("==============================================")
print("RELATÓRIO FINAL DA TURMA")
print("==============================================")

print(
    f"{'Aluno':20} {'Média':10} {'Freq.':10} {'Situação'}"
)

for aluno in relatorio:

    print(
        f"{aluno[0]:20} "
        f"{aluno[1]:<10.1f} "
        f"{aluno[2]:<10.1f} "
        f"{aluno[3]}"
    )

print("\n==============================================")
print("ESTATÍSTICAS")
print("==============================================")

print(f"Total de alunos: {total_alunos}")
print(f"Aprovados: {total_aprovados}")
print(f"Reprovados: {total_reprovados}")
print(f"Alunos que fizeram recuperação: {alunos_em_recuperacao}")

percentual_aprovacao = (
    total_aprovados / total_alunos
) * 100

print(
    f"Percentual de aprovação: "
    f"{percentual_aprovacao:.1f}%"
)

print("==============================================")