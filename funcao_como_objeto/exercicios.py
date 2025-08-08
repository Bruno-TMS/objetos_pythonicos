alunos = [
    ('joão', 0),
    ('carlos', 8),
    ('ana claudia', 7),
    ('arlindo', 5),
    ('tobias', 10),
    ('ramom', 10),
    ('kiko', 8),
    ('laura', 9),
    ('alice', 8)
    ]


def funcao_ordenacao(aluno):
    nome, nota = aluno

    return (nota, nome)


print(sorted(alunos, key=funcao_ordenacao, reverse=True))