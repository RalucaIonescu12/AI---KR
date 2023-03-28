# informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
class NodParcurgere:
    def __init__(self, info,g=0,h=0, parinte=None):
        self.info = info  # eticheta nodului, de exemplu: 0,1,2...
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g= g
        self.h= h
        self.f= self.g+self.h


    def drumRadacina(self):
        l = []
        nod = self
        while nod:
            l.insert(0, nod)
            nod = nod.parinte
        return l


    def vizitat(self): #verifică dacă nodul a fost vizitat (informatia lui e in propriul istoric)
        nodDrum = self.parinte
        while nodDrum:
            if (self.info == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte
        return False

    def __str__(self):
        return str(self.info)
    def __repr__(self):
        sir = str(self.info) + "("
        drum = self.drumRadacina()
        sir += ("->").join([str(n.info) for n in drum])
        sir += ")"
        return sir


class Graph:  # graful problemei

    def __init__(self, matrice, start, scopuri,lista_h):
        self.matrice = matrice
        self.nrNoduri = len(matrice)
        self.start = start  # informatia nodului de start
        self.scopuri = scopuri  # lista cu informatiile nodurilor scop
        self.lista_h=lista_h

    # va genera succesorii sub forma de noduri in arborele de parcurgere
    def succesori(self, nodCurent):
        listaSuccesori = []
        for i in range(self.nrNoduri):
            if self.matrice[nodCurent.info][i] != 0:
                nodNou = NodParcurgere(info=i, parinte=nodCurent)
                if not nodNou.vizitat():
                    nodNou.g = nodCurent.g + self.matrice[nodCurent.info][i]
                    nodNou.h = self.estimeaza_h(nodNou.info)
                    nodNou.f = nodNou.g + nodNou.h
                    listaSuccesori.append(nodNou)
        return listaSuccesori

    def scop(self, infoNod):
        return infoNod in self.scopuri
    def estimeaza_h(self,nod):
        return self.lista_h[nod]


def binary_search(listaNoduri,nodDeInserat,ls,ld):
    if ld<=0:  #lista vida
        return 0;
    if ls == ld:
        if listaNoduri[ls].f < nodDeInserat.f:
            return ls+1
        elif listaNoduri[ls].f > nodDeInserat.f:
            return ls
        else: # if listaNoduri[ls].f == nodDeInserat.f: #f uri egale
            if listaNoduri[ls].g > nodDeInserat.g:
                return ls + 1
            else:
                return ls
    else:
        mij = int((ls+ld) // 2)
        if nodDeInserat.f < listaNoduri[mij].f:
            return binary_search(listaNoduri, nodDeInserat, ls, mij)
        elif nodDeInserat.f > listaNoduri[mij].f:
            return binary_search(listaNoduri, nodDeInserat, mij + 1, ld)
        else:  # f-uri egale deci verific g-urile
            if nodDeInserat.g < listaNoduri[mij].g:
                return binary_search(listaNoduri, nodDeInserat, ls, mij)
            else:
                return binary_search(listaNoduri, nodDeInserat, mij + 1, ld)


def aStarSolMultiple(gr, nrSolutiiCautate):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start,0,gr.estimeaza_h(gr.start))]

    while len(c) > 0:
        #print("Coada actuala: " + str(c))
        #input()
        nodCurent = c.pop(0)

        if gr.scop(nodCurent.info):
            print("Solutie:")
            drum = nodCurent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print(f"Cost total: {nodCurent.g}")
            print("\n----------------\n")
            #input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        for s in gr.succesori(nodCurent):
            indice = binary_search(c,s,0,len(c)-1)

            if indice == len(c):
                c.append(s)
            else:
                c.insert(indice, s)

def este_in_lista(lista,nod):
    # returneaza nodul din lista daca exista, altfel False
    for i in range(len(lista)):
        if lista[i].info == nod.info:
            return lista[i]
    return False


def a_star(graf):
    open=[NodParcurgere(graf.start,0,graf.estimeaza_h(graf.start))]
    closed=[]
    gasit=0
    while len(open) != 0:
        nod_curent=open.pop(0)
        if graf.scop(nod_curent.info):
            gasit = 1
            print("Solutie:")
            drum = nod_curent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print(f"Cost total: {nod_curent.g}")
            print("\n----------------\n")
            # input()
            return
        succesori=graf.succesori(nod_curent)
        closed.append(nod_curent)
        for s in succesori:
            nod_nou = None
            nod_in_open=este_in_lista(open,s)
            if nod_in_open != False:
                if nod_in_open.f> s.f or (nod_in_open.f == s.f and nod_in_open.g < s.g):
                    open.remove(nod_in_open)
                    nod_nou = NodParcurgere(s.info,s.g,s.h,nod_curent)
            else:
                nod_in_closed = este_in_lista(closed,s) #returneaza ori nodul daca exista ori false daca nu e
                if nod_in_closed != False:
                    if nod_in_closed.f > s.f or (nod_in_closed.f == s.f and nod_in_closed.g < s.g):
                        closed.remove(nod_in_closed)
                        nod_nou = NodParcurgere(s.info, s.g, s.h, nod_curent)
                else:
                    nod_nou = s
            if nod_nou != None:
                indice = binary_search(open, nod_nou, 0, len(open) - 1)

                if indice == len(open):
                    open.append(nod_nou)
                else:
                    open.insert(indice, nod_nou)
    if gasit==0:
        print("Nu exista drum de la start la scop")



m = [
    [0,3,5,10,0,0,100],
    [0,0,0,4,0,0,0],
    [0,0,0,4,9,3,0],
    [0,3,0,0,2,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,4,0,5],
    [0,0,3,0,0,0,0]
]
estimari=[0,1,6,2,0,5,0]
start=0
scopuri=[4,6]
g = Graph(m,start,scopuri,estimari)
# aStarSolMultiple(g,30)
a_star(g)



