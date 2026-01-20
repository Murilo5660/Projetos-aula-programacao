notas = []

while True:
    opcoes = input("Escolha a opção desejada: \n1) Inserir uma nova nota. \n2) Ver as notas lançadas. \n3) Calcular a média final. \nOpção: ")
    
    if opcoes == "1":
        inserir_notas = float(input("Digite as notas que deseja inserir: "))
        notas.append(inserir_notas)
    
    elif opcoes == "2":
        print(f"Notas presentes na lista: {notas}")

    elif opcoes == "3":
        
         if len(notas) == 0:
             print("Nenhum elemento na lista, insira algumas notas primeiro.")
         
         else:   
            soma = sum(notas)
            media = soma / len(notas)
            print(f"A média das notas é: {media}")
    
    elif opcoes == "0":
         print("Encerrando o programa...")
         break
    
    else:
        print("Opção inválida, tente novamente.")
