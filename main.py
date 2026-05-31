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

    match opcao:
        case "1":
            cadastrar_venda()
        case "2":
            mostrar_vendas()
        case "3":
            calcular_faturamento()
        case "4":
            produto_mais_vendido()
        case "5":
            salvar_csv()
        case "6":
            ler_csv()
        case "7":
            print("Sistema encerrado.")
            break
        case _:  
            print("Opção inválida.")