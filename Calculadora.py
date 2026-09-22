from Custos import*

orcamento = dict()
print('-' *27)
print('ORÇAMENTO PERSIANAS SOUZA')
print('-' *27)

def linha_separa():
    print('-' *27)
def lista_persinas():
    for c, modelo in enumerate(custo_persianas, start=1):
        print(f'[{c}] {modelo}')
def lista_tecidos(modelo):
    for c, tecido in enumerate(custo_persianas[modelo], start=1):
        print(f'[{c}] {tecido}')
def lista_acess():
    for c, modelo in enumerate(custo_acess, start=1):
        print(f'[{c}] {modelo}')
    print('[0] Sair')
def calcula_acess(acessorio, larg):
    if larg < med_min:
        return custo_acess[acessorio] * med_min * tx_wpp
    else:
        return  custo_acess[acessorio] * larg * tx_wpp
def mostra_orcamento(persiana,tecido,medida_larg,medida_alt,total_acess, valor):
    print(f'{persiana} {tecido} Largura {medida_larg:.2f} x {medida_alt:.2f} com ', end='')
    for v in total_acess:
        print(v, end=' ')
    print(f': R$ {valor:.2f}')

orcamento['Cliente'] = input(str('Nome do Cliente: '))
lista_persinas()

mod_persiana = str(input('Modelo da Persiana: '))
while True:
    if mod_persiana in ['1', '2', '3']:
        if mod_persiana == '1':
            mod_persiana = 'Rolo'
        elif mod_persiana == '2':
            mod_persiana = 'Romana'
        else:
            mod_persiana = 'Double'
        break
    linha_separa()
    print('Opção invalida, digite novamente')
    lista_persinas()
    mod_persiana = str(input('Modelo da Persiana: '))

linha_separa()
if mod_persiana == 'Rolo' or mod_persiana == 'Romana':
    lista_tecidos(mod_persiana)
    mod_tecido = str(input('Modelo do Tecido: '))

    while True:
        if mod_tecido in ['1', '2', '3' , '4']:
            if mod_tecido == '1':
                mod_tecido = 'Blackout'
            elif mod_tecido == '2':
                mod_tecido = 'Tela Solar 1%'
            elif mod_tecido == '3':
                mod_tecido = 'Tela Solar 3%'
            else:
                mod_tecido = 'Tela Solar 5%'
            break
        linha_separa()
        print('Opção invalida, digite novamente')
        lista_tecidos(mod_persiana)
        mod_tecido = str(input('Modelo do Tecido: '))


if mod_persiana == 'Rolo' or mod_persiana == 'Romana':
    linha_separa()
    larg = float(input('Largura(cm): ' ))/ 100
    alt = float(input('Altura(cm): '))/ 100

    if larg * alt > med_min:
        valor_persiana = larg * alt * custo_persianas[mod_persiana][mod_tecido] * tx_wpp
    else:
        valor_persiana = med_min * custo_persianas[mod_persiana][mod_tecido] * tx_wpp

    print(f'Persiana {mod_persiana}: {mod_tecido} Largura {larg:.2f} x {alt:.2f} Altura')
    print(f'R$ {valor_persiana:.2f}')

    linha_separa()
    lista_acess()
    acessorios_incluidos = list()
    while True:
        acessorio = str(input('Acessorio: '))
        if acessorio == '0':
            break
        else:
            if acessorio == '1':
                acessorios_incluidos.append('Bando Rolo')
                valor_acess = calcula_acess(acessorios_incluidos[-1], larg)
                valor_persiana += valor_acess
                mostra_orcamento(mod_persiana,mod_tecido,larg,alt,acessorios_incluidos,valor_persiana)
            elif acessorio == '2':
                acessorios_incluidos.append('Bando Double')
                valor_acess = calcula_acess(acessorios_incluidos[-1], larg)
                valor_persiana += valor_acess
                mostra_orcamento(mod_persiana,mod_tecido,larg,alt,acessorios_incluidos,valor_persiana)
            elif acessorio == '3':
                acessorios_incluidos.append('Base Cônica')
                valor_acess = calcula_acess(acessorios_incluidos[-1], larg)
                valor_persiana += valor_acess
                mostra_orcamento(mod_persiana,mod_tecido,larg,alt,acessorios_incluidos,valor_persiana)
            elif acessorio == '4':
                acessorios_incluidos.append('Guias Laterais')
                if mod_persiana != 'Rolo' or mod_tecido != 'Blackout':
                    print('Guias Laterias são apenas para o Modelo Rolo Blackout')
                else:
                    valor_acess = ((custo_acess[acessorios_incluidos[-1]] * larg * 2) + (custo_acess[acessorios_incluidos[-1]] * alt * 2)) * tx_wpp
                    valor_persiana += valor_acess
                    mostra_orcamento(mod_persiana,mod_tecido,larg,alt,acessorios_incluidos,valor_persiana)
            elif acessorio == '5':
                acessorios_incluidos.append('Motor')
                valor_acess = custo_acess[acessorios_incluidos[-1]] * tx_wpp
                valor_persiana += valor_acess
                mostra_orcamento(mod_persiana,mod_tecido,larg,alt,acessorios_incluidos,valor_persiana)
            else:
                acessorios_incluidos.append('Motor Wi-Fi')
                valor_acess = custo_acess[acessorios_incluidos[-1]] * tx_wpp
                valor_persiana += valor_acess
                mostra_orcamento(mod_persiana,mod_tecido,larg,alt,acessorios_incluidos,valor_persiana)

    orcamento['Persiana'] = mod_persiana
    orcamento['Tecido'] = mod_tecido
    orcamento['largura'] = larg
    orcamento['Altura'] = alt
    orcamento['Acessórios'] = acessorios_incluidos
else:
    print('Modelo Double ainda ainda em desenvolvimento')