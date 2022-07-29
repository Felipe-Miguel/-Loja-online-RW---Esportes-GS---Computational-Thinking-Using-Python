senha = 'RW@aDmin'
cods_prod = [] #codigos dos produtos
descs_prod = [] #Descriçoes dos produtos
set_val = ['ACADEMIA E FITNESS', 'BOX E ARTES MARCIAIS', 'CICLISMO']#Parametros para setor
sets_prod = [] # setores dos produtos
precs_prod = [] # preço dos produtos
quants_prod = [] # quantidade do produto
cods_comp = [] #cods comprados
prec_comp = [] # precos comprados
quants_comp = [] # quantidade comprada
descs_comp = [] #descricao do prod comrpado
total_comp = [] # total comprado
set_comp = [] # setor comprado
indices_sug = []
while True:
    print("|--------- Menu de Opções ---------|")
    print("1 - Cadastrar produto \n 2 - Alterar produto \n 3 - Comprar produto \n 4 - Relatório de produtos cadastrados \n 5 - Relatório de produtos comprados \n 6 - Sair")
    esc = int(input("--> "))
    while esc not in range (1,7):
        print("Digite uma opção válida")
        esc = int(input("--> "))
    if esc == 1:
         print("Digite a senha")
         senha_usu = input("--> ")
         while senha_usu != senha:
             print("Você errou a senha, digite novamente")
             senha_usu = input("--> ")
        print("Pronto, vamos cadastrar o produto")
        print("Digite o código do produto")
        cod_p = int(input("--> "))
        if cod_p not in cods_prod:
            cods_prod.append(cod_p)
            print("Digite a descrição do produto")
            desc_p = input("--> ")
            descs_prod.append(desc_p)
            print("Digite o setor do produto")
            set_p = input("--> ")
            while set_p not in set_val:
                print("São aceitos apenas os setores: ACADEMIA E FITNESS, BOX E ARTES MARCIAIS e CICLISMO, digite um setor válida")
                set_p = input("--> ")
            sets_prod.append(set_p)
            print("Digite o preço do produto")
            prec_p = float(input("--> "))
            while prec_p <= 0:
                print("Digite um valor válido")
                prec_p = float(input("--> "))
            precs_prod.append(prec_p)
            print("Digite a quantidade do produto")
            quant_p = int(input("--> "))
            while quant_p < 0:
                print("Você digitou uma quantidade inválida")
                quant_p = int(input("--> "))
            quants_prod.append(quant_p)
        else:
            print("Infelizmente esse código já esta cadastrado")
    if esc == 2:
        if len(cods_prod) >= 1:
            print("Digite a senha")
            senha_usu = input("--> ")
            while senha_usu != senha:
                print("Você errou a senha, digite novamente")
                senha_usu = input("--> ")
            print("Digite o código")
            cod_p = int(input("--> "))
            if cod_p not in cods_prod:
                print("Código de produto inexistente")
            elif cod_p in cods_prod:
                for i in range(len(cods_prod)):
                    if cod_p == cods_prod[i]:
                        print("Digite o novo preço do produto")
                        prec_p = float(input("--> ")) 
                        while prec_p <= 0:
                            print("Digite um valor válido")
                            prec_p = float(input("--> "))
                        precs_prod.insert(i,prec_p)
                        print("Digite a quantidade do produto em estoque")
                        quant_p = int(input("--> "))
                        while quant_p < 0:
                            print("Você digitou uma quantidade inválida")
                            quant_p = int(input("--> "))
                        quants_prod.insert(i,quant_p)
        else:
            print("Infelizmente não há produtos cadastrados ainda")
    
    if esc == 3:
        print("Digite o nome do produto que deseja comprar")
        nm_prod = input("--> ")
        if nm_prod in descs_prod:
            for i in range(len(descs_prod)):
                if nm_prod == descs_prod[i]:
                    print(cods_prod[i], " - ", descs_prod[i])
                    print("Digite o código do produto que deseja")
                    cod_p = int(input("--> "))
                    if cod_p in cods_prod:
                        for f in range(len(cods_prod)):
                            if cod_p == cods_prod[f]:
                                indice_p = f
                                if quants_prod[indice_p] > 0:
                                    print("Qual quantidade deseja comprar?")
                                    quant_p = int(input("--> "))
                                    verif = quants_prod[indice_p]
                                    while quant_p < 0:
                                        print("Digite uma quantidade válida")
                                        quant_p = int(input("--> "))
                                    while quant_p > verif:
                                        print("Infelizmente essa quantidade ultrapassa nosso estoque, temos apenas ", quants_prod(indice_p), " em estoque, digite um valor válido")
                                        quant_p = int(input("--> "))
                                    sobra = quant_p - quants_prod[indice_p]
                                    tot_comp = precs_prod[indice_p] * quant_p
                                    cods_comp.append(cod_p)
                                    descs_comp.append(descs_prod[indice_p])
                                    prec_comp.append(precs_prod[indice_p])
                                    quants_comp.append(quant_p)
                                    set_comp.append(sets_prod[indice_p])
                                    total_comp.append(tot_comp)
                                    quants_prod.insert(indice_p, sobra)
                                    print("Temos outros produtos que podem te interessar")
                                    set_comprado = sets_prod[indice_p]
                                    for f in range(len(sets_prod)):
                                        if set_comprado == sets_prod[f]:
                                            indices_sug.append(f)
                                        print(cods_prod[indices_sug[f]], " - " ,descs_prod[indices_sug[f]] )

                                else:
                                    print("Sem produto em estoque")
                    else:
                        print("Produto não cadastrado")
    if esc == 4:
        for f in range(len(cods_prod)):
            print(cods_prod[f], " - ", descs_prod[f], " - ", sets_prod[f], " - ", precs_prod[f], " - ", quants_prod[f])
    if esc ==5:
        for f in range(len(cods_comp)):
            print(cods_comp[f], " - ", descs_comp[f], " - ", prec_comp[f], " - ", quants_comp[f], " - ", total_comp[f])
    if esc == 6:
        print("Programa encerrado")
        break
