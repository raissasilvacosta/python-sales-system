from funcoes import (
    cadastrar_venda,
    mostrar_vendas,
    calcular_faturamento,
    produto_mais_vendido,
    salvar_csv,
    ler_csv
)

while True:

    print("\n===== SISTEMA DE VENDAS =====")

    print("1 - Cadastrar venda")
    print("2 - Mostrar vendas")
    print("3 - Faturamento total")
    print("4 - Produto mais vendido")
    print("5 - Salvar CSV")
    print("6 - Ler CSV")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_venda()

    elif opcao == "2":
        mostrar_vendas()

    elif opcao == "3":
        calcular_faturamento()

    elif opcao == "4":
        produto_mais_vendido()

    elif opcao == "5":
        salvar_csv()

    elif opcao == "6":
        ler_csv()

    elif opcao == "7":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")