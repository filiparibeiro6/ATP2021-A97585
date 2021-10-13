# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:46:02 2021

@author: Utilizador
"""

from random import randint
def jogo():
    lugar=input("Deseja jogar em 1º lugar (1), em 2º lugar (2) ou fechar o jogo (3):")
    x=21
    vantagem=0
    if(lugar == "1"):
        while(x>1):
            a=input("Introduza o valor que deseja retirar:")
            b=int(a)
            while(b>4 or b<0):
                print("O valor terá que ser menor ou igual a 4!")
                a=input("Introduza o valor que deseja retirar:")
                b=int(a)
            if (b>0 and b<=4):
                x=x-b
                y=5-b
                print("O outro jogador retirou o valor:",y)
                x=x-y
                print("O resultado final é:",x)
                
        print("Perdeu o jogo!")
        jogo()
    elif(lugar == "2"):
        c=randint(1,4)
        print("O outro jogador retirou o valor:", c)
        x=x-c
        
        while(x>1):
            
            a=input("Introduza o valor que deseja retirar:")
            b=int(a)
            x=x-b
            print("O resultado final é :", x)
            
            if(b>0 and b<=4):
                soma=c+b
        
                if(vantagem==0):
                    if (x<=1):
                        print("Ganhou o jogo!")
                        jogo()
                    elif(soma>5):
                        y=10-soma
                        print("O outro jogador retirou o valor:",y)
                        x=x-y
                        vantagem=1
                        if (x<=1):
                            print("Perdeu o jogo!")
                            jogo()
                    elif(soma<5):
                        y=5-soma
                        print("O outro jogador retirou o valor:",y)
                        x=x-y
                        vantagem=1
                        if (x<=1):
                            print("Perdeu o jogo!")
                            jogo()
                    elif(soma==5):
                        c=randint(1,4)
                        print("O outro jogador retirou o valor:",c)
                        x=x-c
                           
                else:
                    while(b>4 or b<0):
                        print("O valor terá que ser menor ou igual a 4!")
                        a=input("Introduza o valor que deseja retirar:")
                        b=int(a)
                        
                    if (b>0 and b<=4):
                        y=5-b
                        print("O outro jogador retirou o valor:",y)
                        x=x-y
                        
                    if(x<=1):
                        print("Perdeu o jogo!")
                        jogo()
                    
            else:
                print("O valor terá que ser menor ou igual a 4!") 

    elif(lugar == "3"):
        print("Obrigada por ter jogado!")
        SystemExit()
        
    else:
        print("Não selecionou nenhuma das opções!")

jogo()