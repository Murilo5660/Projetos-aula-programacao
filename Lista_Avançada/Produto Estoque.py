estoque = [
{'nome':'Teclado','preço':150.00,'quantidade':5},
{'nome':'Mouse','preço':80.00,'quantidade':12},
{'nome':'Monitor','preço':700.00,'quantidade':3},
{'nome':'Headset','preço':250.00,'quantidade':8}
]
for iten in estoque:
    if iten['quantidade'] < 10:
        print(iten['nome'])
