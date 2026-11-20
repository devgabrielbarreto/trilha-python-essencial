forma_pagamento = input("Qual a forma de pagamento (pix, dinheiro ou cartao)? ")

if forma_pagamento == "pix" or forma_pagamento == "dinheiro":
    print("Você ganhou 10% de desconto no pagamento à vista!")
else:
    print("Preço normal, sem desconto.")