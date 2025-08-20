def soma():   # Função para somar dois números
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resultado = n1 + n2
    print(f"A soma de {n1} e {n2} é {resultado}")

def subtracao(): # Função para subtrair dois números
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resultado = n1 - n2
    print(f"A subtração de {n1} e {n2} é {resultado}")  
    
def multiplicacao():   # Função para multiplicar dois números
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resultado = n1 * n2
    print(f"A multiplicação de {n1} e {n2} é {resultado}")
    
def divisao():   # Função para dividir dois números
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    if n2 == 0:   # Verifica se o divisor é zero
        print("Erro: Divisão por zero não é permitida.")
    else:    # Realiza a divisão se o divisor não for zero
        resultado = n1 / n2
        print(f"A divisão de {n1} por {n2} é {resultado}")
        
def calculadora():   # Função principal da calculadora
    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão\n")
    
    escolha = input("Digite o número da operação desejada (1/2/3/4): \n")
    # Verifica a escolha do usuário e chama a função correspondente
    if escolha == '1':
        soma()
    elif escolha == '2':
        subtracao()
    elif escolha == '3':
        multiplicacao()
    elif escolha == '4':
        divisao()
    else:  # Caso a escolha não seja válida
        print("Opção inválida! Por favor, escolha uma operação válida.")
        
if __name__ == "__main__":   # Verifica se o script está sendo executado diretamente
    calculadora()            # Chama a função principal da calculadora