num = input("Digite um número em binário: ")

def binario_para_decima(num):
    if num == "":
        return 0
    else:
        return int(num[0]) * (2 ** (len(num)-1)) + binario_para_decima(num[1:])

decimal = binario_para_decima(num)
print(f"Número Decimal: {decimal}")
