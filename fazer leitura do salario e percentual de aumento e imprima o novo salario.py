s = float(input('salario: '))
p = float(input('aumento%:'))
aumento = s * p /100
novo = s + aumento
print(f'Aumento: rR$ `{aumento:.2f}')
print(f'Novo salario: R$ {novo:.2f}')