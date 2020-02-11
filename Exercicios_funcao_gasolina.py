print('=-=' * 20)
print('Bom dia Humano')
km = 0
litros = 0

def carro(km, litros):
    km = int(input("Humano, quantos kilometros voce rodou? "))
    litros = int(input("Humano, quantos litros o carro consumiu? "))
    total = km / litros
    if total <= 8:
        print(f'Humano, esse carro consumiu {total}, venda esse lixo!!!')
    elif total >= 8 and total <= 12:
        print(f"Humano, esse carro consumiu {total}, é até economico ")
    elif total > 12:
        print(f'Humano, esse carro consumiu {total}, é super economico , parabens')


carro(km, litros)
