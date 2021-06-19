from datetime import datetime
from functools import reduce

class Pessoa:
    def __init__(self, nome, idade=None):
        self.nome = nome
        self.idade = idade
        self.adulto = 18

    def __str__(self):
        return f'{self.nome} - Idade: {self.idade}'

    def is_adult(self):
        return (self.idade or 0) >= self.adulto


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


# Receberá a compra e retornará a data da compra
#def get_data(compra):
#    return compra.data


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    # A compra recebida como parâmetro é adicionada a lista self.compras
    def registrar_compra(self, compra):
        self.compras.append(compra)

    # Retornará a data da última compra
    #def get_data_ultima_compra(self):
    #    return int(None if not self.compras else sorted(self.compras, key=lambda compra: compra.data)[-1].data)

    # O tamanho da lista self.compras indicará o total de compras
    def total_compras(self):
        return reduce(lambda c1,c2: c1 + c2, (compra.valor for compra in self.compras))


class Compra():
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = datetime
        self.valor = valor


def main():
    fulano = Cliente('Fulano',idade=24)
    sicrano = Vendedor('Sicrano', 27, 5000)

    compra1 = Compra(sicrano, datetime.now(), 512)
    compra2 = Compra(sicrano, datetime(2021, 5, 5), 256)
    fulano.registrar_compra(compra1)
    fulano.registrar_compra(compra2)

    print(f'Cliente: {fulano}', '(Adulto)' if fulano.is_adult() else '')
    print(f'Vendedor: {sicrano}')
    print(f'Total: {fulano.total_compras()} em {len(fulano.compras)} compras')
    #print(f'Última compra: {fulano.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
