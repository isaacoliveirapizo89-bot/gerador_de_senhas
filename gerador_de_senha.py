import secrets
import string


def gerar_senha(tamanho, incluir_maiusculas=True, incluir_minusculas=True,
                incluir_numeros=True, incluir_simbolos=True):
    """Gera uma senha aleatória com os caracteres selecionados."""
    if tamanho <= 0:
        raise ValueError("O tamanho da senha deve ser maior que zero.")

    caracteres = ""

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase

    if incluir_minusculas:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Selecione pelo menos um tipo de caractere.")

    return "".join(secrets.choice(caracteres) for _ in range(tamanho))


def main():
    print("=" * 40)
    print("      GERADOR DE SENHAS")
    print("=" * 40)

    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha: "))
            if tamanho <= 0:
                print("Digite um número maior que 0.")
                continue
            break
        except ValueError:
            print("Digite apenas números.")

    maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().upper() == "S"
    minusculas = input("Incluir letras minúsculas? (S/N): ").strip().upper() == "S"
    numeros = input("Incluir números? (S/N): ").strip().upper() == "S"
    simbolos = input("Incluir símbolos? (S/N): ").strip().upper() == "S"

    try:
        senha = gerar_senha(
            tamanho,
            incluir_maiusculas=maiusculas,
            incluir_minusculas=minusculas,
            incluir_numeros=numeros,
            incluir_simbolos=simbolos,
        )
    except ValueError as erro:
        print(f"\n{erro}")
        return

    print("\n" + "=" * 40)
    print(f"Sua senha é:\n\n{senha}")
    print("=" * 40)


if __name__ == "__main__":
    main()
