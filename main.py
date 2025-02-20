import pandas as pd

def recommendation(products: list) -> dict:
     excel = pd.read_excel('./loja.xlsx')

     removeCategoryDups = excel.drop_duplicates(subset=['Sub-Category','Order ID'],keep='first') #Remove Duplicates

     table = pd.crosstab(removeCategoryDups['Order ID'],removeCategoryDups['Sub-Category']) #Transforming in binary

     filteredTable = table[(table[products] > 0).all(1)] #Filtring
     
     values = {} #Category:Probability

     sumProducts = 0

     if max(filteredTable.count()) == 0: #Case probability with cart products are 0
          OthersProducts = table.drop(columns=products) 

          for c in OthersProducts:
               sumProducts += OthersProducts[c].sum()

          for i in OthersProducts:
               sum = OthersProducts[i].sum()
               values.update({i:(sum/sumProducts)*100})

          return values
     else:
          allProductsWithoutCartProducts = filteredTable.drop(columns=products) #drop the columns with the products that are in the car

          for c in allProductsWithoutCartProducts:
               sumProducts += allProductsWithoutCartProducts[c].sum()

          for i in allProductsWithoutCartProducts: #Calculate the probability
               sum = allProductsWithoutCartProducts[i].sum()
               values.update({i:(sum/sumProducts)*100})
          return values


def choosingRecomended(products: dict) -> dict:
     
     df = pd.DataFrame(list(products.items()), columns=['Category', 'Value'])

     bestProducts = df.sort_values(by=['Value'], ascending=False).head(3)

     productsRec = {}
     
     for i in bestProducts['Category'].values:
          productsRec.update({i:products[i]})

     return productsRec
     

def menu():
    print("\nBem-vindo à loja! Escolha um ou mais produtos para adicionar ao carrinho.")
    excel = pd.read_excel('./loja.xlsx')
    categorias = excel['Sub-Category'].unique()  # Pega as categorias únicas
    print("Escolha uma opção: \n")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i} - {categoria}")
    while True:
        print("\n\n1 - Adicionar produto no carrinho: ")
        print("2 - não comprar nada ")
        print("3 - sair da loja \n")
        opcao = int(input("Digite sua opção: "))
        if(opcao == 1):
            carrinho = str(input("\n\ndigite o seu carrinho"))
            print(carrinho)
            array = carrinho.split(", ")
            produtoo = recommendation(array)
            proximo_produto = choosingRecomended(produtoo)
            print(proximo_produto)
        elif(opcao == 2):
            print("não comprar nada, suas recomendaçoes iniciais serão: ")
            produtoo = recommendation([])
            proximo_produto = choosingRecomended(produtoo)
            print(proximo_produto)
        elif(opcao == 3):
            print("Saindo...")
            break
        else:
            print("de 1 a 2")





menu()