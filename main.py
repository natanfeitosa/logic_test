"""
Teste de Lógica de Programação

zax.gupy.io
"""

"""
Problema

Existem 5 motoboys, cada motoboy ganha uma comissão diferente por pedido coletado, e alguns motoboys possuem exclusividade com algumas lojas na qual fazem coletas.

Os motoboys não podem reclamar que ficaram sem pedidos.

Os motoboys que possuem exclusividade com as lojas, possuem prioridade.

Os motoboys podem ter exclusividade com as lojas, mas as lojas não possuem exclusividade com os motoboys.

Hoje existem 10 pedidos para serem retirados em 3 lojas.

Quando eu executar o script passando apenas o motoboy ou não passando nenhum motoboy, preciso ver:
Quem é o motoboy e quantos pedidos terá?
De qual loja é?
Quanto vai ganhar?

Dados do teste

Motoboys
Moto 1 - cobra R$2 reais por entrega e atende todas as lojas
Moto 2 - cobra R$2 reais por entrega e atende todas as lojas
Moto 3 - cobra R$2 reais por entrega e atende todas as lojas
Moto 4 - cobra R$2 reais por entrega e atende apenas a loja 1
Moto 5 - cobra R$3 reais por entrega e atende todas as lojas

Lojas
Loja 1 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50) e paga 5% do valor pedido por entrega fora o valor fixo.
Loja 2 - 4 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50, PEDIDO 4 R$50) e paga 5% do valor pedido por entrega fora o valor fixo.
Loja 3 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$100) e paga 15% do valor pedido por entrega fora o valor fixo.

O Moto 1 atende todas as lojas
O Moto 2 atende todas as lojas
O Moto 3 atende todas as lojas
O Moto 4 atende apenas a loja 1
O Moto 5 atende todas as lojas
"""

stores = [
    { 'requests': [ 50, 50, 50 ], 'tax': 5, },
    { 'requests': [ 50, 50, 50, 50 ], 'tax': 5, },
    { 'requests': [ 50, 50, 100 ], 'tax': 15, }
]

motoboys = [
    { 'price': 2, 'store': 'todas', 'pedidos': 0 },
    { 'price': 2, 'store': 'todas', 'pedidos': 0 },
    { 'price': 2, 'store': 'todas', 'pedidos': 0 },
    { 'price': 2, 'store': 1, 'pedidos': 0 },
    { 'price': 3, 'store': 'todas', 'pedidos': 0 },
]

def calcule(motoboy:int=-1):
    
    def calcule_earns(store):
        if len(store['requests']) > 0:
            return store['requests'].pop() * (store['tax'] / 100)
        else:
            return 0
            
    def format_real(val):
        val = 'R$ {:.2f}'.format(float(val))
        
        return str(val).replace('.', ',')
            
    earn = 0
    loja = 0
    output = "Moto {0}\n{1} Pedidos\n{2}\nVai ganhar {3}\n"
    
    if motoboy == -1:
        for mi in range(len(motoboys)):
            moto = motoboys[mi]
            
            if moto['store'] == 'todas':
                for si in range(len(stores)):
                    moto['pedidos'] += 1
                    earn += calcule_earns(stores[si])
            
            else:
                earn += calcule_earns(stores[moto['store']])
                moto['pedidos'] += 1

            print(output.format(
                mi + 1,
                moto['pedidos'],
                'Todas as lojas' if moto['store'] == 'todas' else 'Loja %i' % moto['store'],
                format_real(earn + moto['price'])
            ))
    else:
        moto = motoboys[motoboy - 1]
        for si in range(len(stores)):
            moto['pedidos'] += 1
            earn += calcule_earns(stores[si])
        
        print(output.format(
                motoboy,
                moto['pedidos'],
                'Todas as lojas' if moto['store'] == 'todas' else 'Loja %i' % moto['store'],
                format_real(earn + moto['price'])
            ))


if __name__ == '__main__':
    calcule(4)
