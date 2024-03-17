from copy import deepcopy

liste=[]
f = open("frenchssaccent.dic",'r')
for ligne in f:
    liste.append(ligne[0:len(ligne)-1])
f.close()

points=[['?','0',0],['a','e','i','l','n','o','r','s','t','u',1],['d','g','m',2],['b','c','p',3],['f','h','v',4],['j','q',8],['k','w','x','y','z',10]]
alphabet='abcdefghijklmnopqrstuvwxyz'

def score(mot):
    mot=str(mot)
    score=0
    for i in range(len(mot)):
        for j in range(len(points)):
            if mot[i] in points[j]:
                score=score+points[j][-1]
    return score

def verif(mot, tirage):
    if mot[0] in tirage:
        t=deepcopy(tirage)
        t.remove(mot[0])
        x=mot
        j=1
        while j<len(x) and x[j] in t:
            t.remove(x[j])
            j=j+1
        if j==len(x):
            return True
        else:
            return False

def scrabble(tirage):
    mots_possibles=[]
    solution=0
    for i in range(len(liste)):
        if verif(liste[i], tirage):
            mots_possibles.append(liste[i])
    for z in range(len(mots_possibles)):
        if score(mots_possibles[z])>score(solution):
            solution=mots_possibles[z]
    #print(mots_possibles, solution)
    return mots_possibles, solution
    
def scrabble2(tirage):
    if '?' in tirage:
        potentiel=[]
        solution=0
        intero=0
        for j in range(len(tirage)):
            if tirage[j]=='?':
                intero=j
        for i in range(len(alphabet)):
            t=deepcopy(tirage) 
            t[intero]=alphabet[i]
            mot=scrabble(t)[1]
            if alphabet[i] in tirage:                    #gestion cas si lettre prise par '?' est déjà dans le tirage pour le comptage des points
                num=0
                for j in range(len(tirage)):
                    if tirage[j]==alphabet[i]:
                        num=num+1                 
                potentiel.append((mot, alphabet[i],num))
            else:
                potentiel.append((mot,alphabet[i],0)) 
        for z in range(len(potentiel)):
            if potentiel[z][2]==0:
                if score(potentiel[z])-score(potentiel[z][1])>score(solution):
                    solution=potentiel[z][0]
            else:                                       #cas lettre prise par '?' est déjà dans le tirage
                num=potentiel[z][2]
                for h in range(len(potentiel[z][0])):
                    if potentiel[z][0][h]==potentiel[z][1]:
                        num=num-1
                        if score(potentiel[z])-abs(num)*score(potentiel[z][1])>score(solution):
                            solution=potentiel[z][0]
        print(solution)                
        return solution
    else:
        print(scrabble(tirage)[1])
        return scrabble(tirage)[1]

scrabble2(['c','a','v','e','l','y','o','?'])
