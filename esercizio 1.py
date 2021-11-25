#scrivi un programma python per estrarre un dato numero di elementi (preso in input) selezionati casualmente da una data lista
import random

def random_select_nums(n_list, n):
    return random.sample (n_list, n)

l = []
n = int(input("inserisci quanti elementi vuoi inserire nella lista: "))
while n > len(l):
    e = input ("inserisci elemento nella lista: ")
    l.append(e)

casual_elem = int(input("quanti elementi casuali vuoi estrarre? "))
if casual_elem > len(l):
    print ("numero più alto del numero di elementi nella lista. Riprova")
    casual_elem = int(input("quanti elementi casuali vuoi estrarre? "))



result = random_select_nums(l,casual_elem)
print (result)












