def validar_numero(valor):

    while not valor.replace(".", "").isdigit():

        print("Digite apenas números.")

        valor = input("Digite novamente: ")

    return valor