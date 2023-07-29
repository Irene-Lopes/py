meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def converter_para_K(matriz):
    lista = []
    for i, linha in enumerate(matriz):
        if 'C' in linha:
            celsius = matriz[i][0]
            kelvin = round(celsius + 273.15, 2), 'K'
            lista.append(kelvin)
        elif 'F' in linha:
            fahrenheit = matriz[i][0]
            kelvin = round(((fahrenheit - 32) * 5/9) + 273.15, 2), 'K'
            lista.append(kelvin)
        else:
            lista.append(linha)

    return lista

def temp_med_anual(matriz):
    soma = 0
    for i, _ in enumerate(matriz):
        temperatura = matriz[i][0]
        soma += temperatura
    media = round(soma/12, 2)

    return media

def acima_media(matriz, media):
    for i, _ in enumerate(matriz):
        temperatura = matriz[i][0]
        if temperatura > media:
            print(f'{meses[i]}: {temperatura}K')

def main():
    ano = []
    for _ in range(12):
        temperatura = float(input().strip())
        escala = input().strip().upper()
        mes = temperatura, escala
        ano.append(mes)

    escalas_convertidas = converter_para_K(ano)
    med_temp = temp_med_anual(escalas_convertidas)

    print('TEMPERATURA MÉDIA ANUAL')
    print(f'{med_temp}K')
    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    acima_media(escalas_convertidas, med_temp)

if __name__ == '__main__':
   main()
