import csv

from utils.validacoes import validar_numero

vendas = []


def cadastrar_venda():

    produto = input("Digite o nome do produto: ")

    quantidade = validar_numero(
        input("Digite a quantidade: ")
    )

    preco = validar_numero(
        input("Digite o preço: ")
    )

    venda = {
        "produto": produto,
        "quantidade": int(quantidade),
        "preco": float(preco)
    }

    vendas.append(venda)

    print("Venda cadastrada com sucesso!")


def mostrar_vendas():

    if not vendas:
        print("Nenhuma venda cadastrada.")
        return

    for venda in vendas:

        print("-" * 30)

        print(f"Produto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Preço: R${venda['preco']}")


def calcular_faturamento():

    faturamento = 0

    for venda in vendas:

        total = venda['quantidade'] * venda['preco']

        faturamento += total

    print(f"Faturamento total: R${faturamento:.2f}")


def produto_mais_vendido():

    if not vendas:
        print("Nenhuma venda cadastrada.")
        return

    maior_quantidade = 0
    produto = ""

    for venda in vendas:

        if venda['quantidade'] > maior_quantidade:

            maior_quantidade = venda['quantidade']
            produto = venda['produto']

    print(f"Produto mais vendido: {produto}")


def salvar_csv():

    with open(
        "vendas.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([
            "produto",
            "quantidade",
            "preco"
        ])

        for venda in vendas:

            escritor.writerow([
                venda['produto'],
                venda['quantidade'],
                venda['preco']
            ])

    print("Dados salvos com sucesso!")


def ler_csv():

    try:

        with open(
            "vendas.csv",
            "r",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.reader(arquivo)

            next(leitor)

            for linha in leitor:
                print(linha)

    except FileNotFoundError:
        print("Arquivo não encontrado.")