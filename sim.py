n1 = float(input("digite um valor: "))
n2 = float (input("digite outro"))
op = input ("escolha a operacao: ( + - * /)")

if op == "+" :
    result = n1 + n2
    print (f"o resultado é {result}")

elif op == "-" :
    result = n1 - n2
    print (f"o resultado é {result}")

elif op == "*" :
    result = n1 * n2
    print (f"o resultado é {result}")
else :
    result = n1 / n2
    print (f"o resultado é {result}")








