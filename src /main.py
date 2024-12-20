import pandas as pd
import os as os


#### Opção  1 ###############################
carros = ["Gol", "Porsche", "Cantidad", "Ferrari", "Mustang", "Fiat", "Mazda", "Honda", "Chevrolet", "VW"]
anos = ["2004", "2005", "2006", "2007","2008","2009","2010","2011","2012","2013"]
valorDosCarros = [20,311,311,311,311,311,311,311,311,311]

def listar(): 
    for i in range(len(carros)):
        print (i+1, carros[i],"------------",anos[i],"------------",valorDosCarros[i],"000 U$")
    print ("============================================================")        
    print ("============================================================")        
    print ("============================================================")        
    print ("============================================================")        
    print ("============================================================")        

def comprar():
    print("Escolha qual carro você quer comprar:")
    a = int(input())
    print ("============================================================")        
    print ("============================================================")        
    print ("============================================================")        
    print ("============================================================")        
    print()
    print()
    print()
    
    print ("Você comprou o", carros[a-1],"!")
    print()
    print()
    print()
    print ("============================================================")        
    print("============================================================")
    print ("============================================================")        
    print ("============================================================")
    tecla = input("Aperter qualquer tecla para continuar")
    
    match(tecla):
        case _: main()
    
c = True

####################################################################

def adicionarCarro():
    os.system("clear")
    print ("Adicionar um novo carro:")
    carros.append(input("Nome do carro:"))
    anos.append(input("Ano do carro:"))
    valorDosCarros.append(int(input("Preço do carro em milhares:")))
    listar

########################################################################
def remove():
    os.system("clear")
    listar()
    print ("Escolha qual carro você quer remover:")
    a = int(input())
    del carros[a-1] 
    del anos[a-1]
    del valorDosCarros[a-1]
    listar()

########################################################################


def main():
    print ("BEM VINDO A SUA LOCADORA DE CARROS================================================================")

    print ("1. Listar todos os carros")
    print ("2. Adicionar um carro")
    print ("3. Remover um carro")
    print ("4. Sair")

    print ("==============================================================================================")

    print ("Estamos sempre com você")

    c = True

    while (c == True):
        opcao = int(input("Escolha uma opcao:"))

        if opcao == 1:
            c = False
            os.system("clear")
            print ("Você escolheu listar todos os carros")
            # código para listar os carros aqui
            listar()
            comprar()

        elif opcao == 2:
            c = False    
            os.system("clear")
            print ("Voce escolheu adicionar um carro")
            adicionarCarro()
            main()

        elif opcao == 3:
            c = False  # Para sair do loop
            os.system("clear")
            print ("Você escolher Remover um carro")
            remove()
            listar()
            main()

        elif opcao == 4:
            c = False
            os.system("clear")
            print ("Você Saiu")
            break

main()

