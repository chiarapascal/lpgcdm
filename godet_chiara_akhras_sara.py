import generateur_map
import sys
import os
import time


def max_square(mat : list[list])-> dict:
    nrows, ncols = len(mat), (len(mat[0]) if mat else 0)
    if not (nrows and ncols):
        return 0 # empty matrix or rows
    counts = [[0]*ncols for _ in range(nrows)]
    for i in reversed(range(nrows)):
        # assert len(mat[i]) == ncols # matrix must be rectangular
        for j in reversed(range(ncols)):
            if mat[i][j] != '0':
                if i < (nrows - 1) and j < (ncols - 1) :
                    counts[i][j] = (1 + min(counts[i][j+1], counts[i+1][j], counts[i+1][j+1] ))
                else  :
                     counts[i][j] = 1
    max = counts[0][0]
    x = 0
    y = 0
    for i in range(0,len(counts)) :
        for j in range(0,len(counts[0])) :
            if counts[i][j] > max :
                max = counts[i][j]
                x = i
                y = j
    return {'max' : max,'x' : x,'y': y}

def create_liste_map(map:list[str])-> list[list] :
    liste = []
    for i in range(0,len(map)) :
        tmp = map[i].replace('o', '0')
        tmp = tmp.replace('.', '1')
        tmp = tmp.replace('\n', '')
        tmp = tmp.replace(' ', '')
        liste.append(tmp)

    return liste

def modif_map(map:list[str],res:dict,nomFichier:str) -> None:
    new = []
    for i in range(0,len(map)) :
        tmp = ''
        for j in range(0,len(map[0])) :
            if (i >= res['x']) and (i<res['x']+res['max']) and  (j >= 2*res['y']) and (j<2*res['y']+2*res['max']-1) :
                if (map[i][j]== ' ') :
                    tmp += ' '
                else :
                    tmp += 'x'
            else :
                tmp += map[i][j]
        new.append(tmp)

    filin = open(nomFichier, "w")
    for rows in new :
        filin.write(rows)

    return None

def solution(nomFichier:str)-> dict:
    tmp1= generateur_map.create_map(nomFichier)
    nomFichier += ".map"
    file = open(nomFichier, "r+")
    Map = file.readlines()
    file.close()

    liste_map = create_liste_map(Map)
    res = max_square(liste_map)

    modif_map(Map,res, nomFichier)
    tmp2=time.time()
    print("Temps : " + str(tmp2-tmp1)+ " s")
    return res

def parametres(p: str)-> None:
    if (p == '-f') or (p == '--file'):

        if (sys.argv[2]== None): nomFichier="file1"
        else: nomFichier=sys.argv[2]

        solution(nomFichier)

    elif (p == '-p') or (p == '--project'):
        os.system("cat godet_chiara_akhras_sara.py")

    elif (p == '-a') or (p == '--authors'):
        print("Auteur 1 : Chiara Godet")
        print("Auteur 2 : Sara Akhras")

    elif (p == '-v') or (p == '--verbose'):
        os.system("cat godet_chiara_akhras_sara.py")
        print("Auteur 1 : Chiara Godet")
        print("Auteur 2 : Sara Akhras")

    elif (p == '-h') or (p == '--help'):
        print("tapez la commande :\n python3 godet_chiara_akhras_sara \n Avec comme parametres:\n -r (ou) --print-result\n et cela affichera le plus grand carre")

    elif (p == '-r') or (p == '--print-result'):
        nomFichier= "file1"
        solution(nomFichier)
        os.system("cat %s.map"%(nomFichier))

    elif (p == '-c') or (p == '--print-coordinates'):
        res=solution("file1")
        print("%d %d %d %d"%(res['x'],res['y'],res['x']+ res['max']-1,res['y']+ res['max']-1))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        solution("file1")
    else:
        parametres(sys.argv[1])


