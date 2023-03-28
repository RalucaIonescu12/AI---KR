
import sys
# informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
class NodParcurgere:
   def __init__(self, info,g=0, h=0,  parinte=None):
       self.info = info  # eticheta nodului, de exemplu: 0,1,2...
       self.parinte = parinte  # parintele din arborele de parcurgere
       self.g=g
       self.h=h
       self.f=g+h

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

   def afisSolFisier(self,fisier):
       f = open(fisier,"w")
       drum = []
       nod = self
       while nod:
           drum.insert(0, nod)
           nod = nod.parinte

       for nod in drum:
           stive=nod.info
           maxx=-sys.maxsize
           for s in stive:
               if len(s)>maxx:
                   maxx=len(s)
           for j in range(maxx-1,-1,-1):
               i=0
               while(i<len(stive)):
                   if j>= len(stive[i]):
                       f.write("  ")
                   else:
                       f.write(stive[i][j])
                       f.write(" ")
                   i+=1
               f.write("\n")
           f.write("----\n")
           f.write("Cost partial: ")
           f.write(str(nod.g))
           f.write("\n")
       nod=self
       f.write("\n\nCost: ")
       f.write(str(nod.g))
       f.write("\nLungime: ")
       f.write(str(len(drum)))

   def __str__(self):
       return str(self.info)
   def __repr__(self):
       sir = str(self.info) + "("
       drum = self.drumRadacina()
       sir += ("->").join([str(n.info) for n in drum])
       sir += ")"
       return sir




import copy
class Graph:  # graful problemei

   def __init__(self, start, scopuri):
       self.start = start  # informatia nodului de start
       self.scopuri = scopuri  # lista cu informatiile nodurilor scop


   # va genera succesorii sub forma de noduri in arborele de parcurgere
   def succesori(self, nodCurent):
       listaSuccesori = []
       for istiva, stiva in enumerate(nodCurent.info):
           copieStiva = copy.deepcopy(nodCurent.info)
           if len(copieStiva[istiva]) == 0:
               continue
           else:
               bloc = copieStiva[istiva].pop()
           for istiva2,stiva2 in enumerate(copieStiva):
               if istiva==istiva2:
                   continue
               stareNoua = copy.deepcopy(copieStiva)
               stareNoua[istiva2].append(bloc)
               nodNou = NodParcurgere(stareNoua,nodCurent.g + ord(bloc)-ord("a")+1, self.estimeaza_h(stareNoua,"banala"),parinte= nodCurent)
               if not nodNou.vizitat():
                    listaSuccesori.append(nodNou)
       return listaSuccesori

   def scop(self, infoNod):
       return infoNod in self.scopuri

   def estimeaza_h(self, infoNod,euristica):
       if euristica == "banala":
           if infoNod not in self.scopuri:
               return 1
           else:
               return 0
       elif euristica == "euristica mutari":
           if infoNod in self.scopuri:
               return 0
           else:
               return calc_nr_min_mutari(infoNod)
       elif euristica=="euristica costuri":
           return calc_cost_min_mutari(infoNod)
       elif euristica == "euristica inadmisibila":
           return calc_cost_max_mutari()+10
       # return self.lista_h[infoNod]
       #  return 0 #deocamdata

   def valideaza(self):
       conditie1 = all([len(start)==len(scop) for scop in self.scopuri])
       multimeStart =set(sum(self.start,start=[]))
       conditie2 = all([set(sum(scop,start=[])) for scop in self.scopuri])
       return conditie1 and conditie2





def bin_search(listaNoduri, nodNou, ls, ld):
   if len(listaNoduri)==0:
       return 0
   if ls==ld:
       if nodNou.f<listaNoduri[ls].f:
           return ls
       elif nodNou.f>listaNoduri[ls].f:
           return ld+1
       else: # f-uri egale
           if nodNou.g < listaNoduri[ls].g:
               return ld + 1
           else:
               return ls
   else:
       mij=(ls+ld)//2
       if nodNou.f<listaNoduri[mij].f:
           return bin_search(listaNoduri, nodNou, ls, mij)
       elif nodNou.f>listaNoduri[mij].f:
           return bin_search(listaNoduri, nodNou, mij+1, ld)
       else:
           if nodNou.g < listaNoduri[mij].g:
               return bin_search(listaNoduri, nodNou, mij + 1, ld)
           else:
               return bin_search(listaNoduri, nodNou, ls, mij)




def aStarSolMultiple(gr, nrSolutiiCautate=1):
   # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
   c = [NodParcurgere(gr.start)]

   while len(c) > 0:
       #print("Coada actuala: " + str(c))
       #input()
       nodCurent = c.pop(0)

       if gr.scop(nodCurent.info):

           nodCurent.afisSolFisier("output.txt")
           print("Solutie:")
           drum = nodCurent.drumRadacina()
           print(("->").join([str(n.info) for n in drum]))
           print("cost:", nodCurent.g)
           print("\n----------------\n")
           #input()
           nrSolutiiCautate -= 1
           if nrSolutiiCautate == 0:
               return
       #[2,4,7,8,10,14]
       # c+=gr.succesori(nodCurent)
       for s in gr.succesori(nodCurent):
           indice=bin_search(c, s, 0, len(c)-1)
           if indice==len(c):
               c.append(s)
           else:
               c.insert(indice, s)


def calc_nr_min_mutari(stiveStare):
    minim = sys.maxsize

    for Scop in gr.scopuri:
        minn = 0
        for j in range(0,len(stiveStare)):
            i=0
            while(i<len(stiveStare[j]) and i<len(Scop[j])):
                if stiveStare[j][i] != Scop[j][i]:
                    minn+=1
                i+=1
            if (len(stiveStare[j])!= len(Scop[j]) and len(stiveStare[j])<len(Scop[j])):
                minn+= len(Scop[j]) - len(stiveStare[j])
        if minn<minim:
            minim = minn
    return minim

def calc_cost_min_mutari(stiveStare):
    minim = sys.maxsize

    for Scop in gr.scopuri:
        minn = 0
        for j in range(0, len(stiveStare)):
            i = 0
            while (i < len(stiveStare[j]) and i < len(Scop[j])):
                if stiveStare[j][i] != Scop[j][i]:
                    minn += ord(Scop[j][i])-ord('a')+1
                i += 1
            if (len(stiveStare[j]) != len(Scop[j]) and len(stiveStare[j]) < len(Scop[j])):
                for i in range(i,len(Scop[j])):
                    minn+=ord(Scop[j][i])-ord('a')+1

        if minn < minim:
            minim = minn
    return minim

def calc_cost_max_mutari(stiveStare):
    maxim = -sys.maxsize
    for Scop in gr.scopuri:
        maxx = 0
        for j in range(0, len(stiveStare)):
            i = 0
            while (i < len(stiveStare[j]) and i < len(Scop[j])):
                if stiveStare[j][i] != Scop[j][i]:
                    maxx += ord(Scop[j][i])-ord('a')+1
                i += 1
            if (len(stiveStare[j]) != len(Scop[j]) and len(stiveStare[j]) < len(Scop[j])):
                for i in range(i,len(Scop[j])):
                    maxx += ord(Scop[j][i])-ord('a')+1

        if maxx > maxim:
            maxim = maxx
    return maxim

def a_star(gr):
   # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
   l_open = [NodParcurgere(gr.start)]

   # l_open contine nodurile candidate pentru expandare (este echivalentul lui c din A* varianta neoptimizata)

   # l_closed contine nodurile expandate
   l_closed = []
   while len(l_open) > 0:
       # print("Coada actuala: " + str(l_open))
       # input()
       nodCurent = l_open.pop(0)
       l_closed.append(nodCurent)
       if gr.scop(nodCurent.info):

           print("Solutie:")
           drum = nodCurent.drumRadacina()
           print(("->").join([str(n.info) for n in drum]))
           print("cost:", nodCurent.g)
           return
       lSuccesori = gr.succesori(nodCurent)
       for s in lSuccesori:
           gasitC = False
           for nodC in l_open:
               if s.info == nodC.info:
                   gasitC = True
                   if s.f >= nodC.f:
                       lSuccesori.remove(s)
                   else:  # s.f<nodC.f
                       l_open.remove(nodC)
                   break
           if not gasitC:
               for nodC in l_closed:
                   if s.info == nodC.info:
                       if s.f >= nodC.f:
                           lSuccesori.remove(s)
                       else:  # s.f<nodC.f
                           l_closed.remove(nodC)
                       break
       for s in gr.succesori(nodCurent):
           indice=bin_search(l_open, s, 0, len(l_open)-1)
           if indice==len(l_open):
               l_open.append(s)
           else:
               l_open.insert(indice, s)




def breadth_first(gr, nrSolutiiCautate=1):
   # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
   c = [NodParcurgere(gr.start)]

   while len(c) > 0:
       #print("Coada actuala: " + str(c))
       #input()
       nodCurent = c.pop(0)

       if gr.scop(nodCurent.info):
           print("Solutie:")
           drum = nodCurent.drumRadacina()
           print(("->").join([str(n.info) for n in drum]))
           print("\n----------------\n")
           #input()
           nrSolutiiCautate -= 1
           if nrSolutiiCautate == 0:
               return
       c+=gr.succesori(nodCurent)


def depth_first(gr, nrSolutiiCautate=1):
   # vom simula o stiva prin relatia de parinte a nodului curent
   df(NodParcurgere(gr.start), nrSolutiiCautate)


def df(nodCurent, nrSolutiiCautate):
   if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
       return nrSolutiiCautate
   #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
   #input()
   if gr.scop(nodCurent.info):
       print("Solutie: ", end="")
       drum = nodCurent.drumRadacina()
       print(("->").join([str(n.info) for n in drum]))
       print("\n----------------\n")
       #input()
       nrSolutiiCautate -= 1
       if nrSolutiiCautate == 0:
           return nrSolutiiCautate
   lSuccesori = gr.succesori(nodCurent)
   for sc in lSuccesori:
       if nrSolutiiCautate != 0:
           nrSolutiiCautate = df(sc, nrSolutiiCautate)

   return nrSolutiiCautate



def df_nerecursiv(nrSolutiiCautate):
   stiva = [NodParcurgere(gr.start)]
   #consider varful stivei in dreapta
   while stiva: #cat timp stiva nevida
       nodCurent=stiva.pop() #sterg varful
       if gr.scop(nodCurent.info):
           print("Solutie:")
           drum = nodCurent.drumRadacina()
           print(("->").join([str(n.info) for n in drum]))
           print("\n----------------\n")
           #input()
           nrSolutiiCautate -= 1
           if nrSolutiiCautate == 0:
               return
       stiva+=gr.succesori(nodCurent)[::-1] #adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf



##############################################################################################
#                                 Initializare problema                                      #
##############################################################################################

def calculeaza_stive(sirStive):
    sirStive = sirStive.strip()
    listaStive = [stiva.strip().split(" ") if stiva!= "#" else [] for stiva in sirStive.split("\n")]
    return listaStive



f=open("input.txt")
continut =f.read().split("=========")
start = calculeaza_stive(continut[0])
stariFinale = continut[1].strip().split("---")
scopuri =[calculeaza_stive(st) for st in stariFinale ]

NodStart = NodParcurgere(start)
# print(NodStart)
gr = Graph(start, scopuri)

# # breadth_first(gr,4)
# print("----------RECURSIV----------")
# depth_first(gr,4)
#
#
# print("----------NERECURSIV----------")
# df_nerecursiv(1)
#
# print("----------A Star----------")
aStarSolMultiple(gr,1)


# ex 3
def a_star_blocuri(gr):
   # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
   l_open = [NodParcurgere(gr.start)]

   # l_open contine nodurile candidate pentru expandare (este echivalentul lui c din A* varianta neoptimizata)

   # l_closed contine nodurile expandate
   l_closed = []
   while len(l_open) > 0:
       # print("Coada actuala: " + str(l_open))
       # input()
       nodCurent = l_open.pop(0)
       l_closed.append(nodCurent)
       if gr.scop(nodCurent.info):
           print("Solutie:")
           drum = nodCurent.drumRadacina()
           print(("->").join([str(n.info) for n in drum]))
           print("cost:", nodCurent.g)
           return
       lSuccesori = gr.succesori(nodCurent)
       for s in lSuccesori:
           gasitC = False
           for nodC in l_open:
               if s.info == nodC.info:
                   gasitC = True
                   if s.f >= nodC.f:
                       lSuccesori.remove(s)
                   else:  # s.f<nodC.f
                       l_open.remove(nodC)
                   break
           if not gasitC:
               for nodC in l_closed:
                   if s.info == nodC.info:
                       if s.f >= nodC.f:
                           lSuccesori.remove(s)
                       else:  # s.f<nodC.f
                           l_closed.remove(nodC)
                       break
       for s in gr.succesori(nodCurent):
           indice=bin_search(l_open, s, 0, len(l_open)-1)
           if indice==len(l_open):
               l_open.append(s)
           else:
               l_open.insert(indice, s)


# print(calc_cost_min_mutari(start))






















#
# # ex 5
#
# import sys
# # informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
# class NodParcurgere:
#    def __init__(self, info,g=0, h=0,  parinte=None):
#        self.info = info  # eticheta nodului, de exemplu: 0,1,2...
#        self.parinte = parinte  # parintele din arborele de parcurgere
#        self.g=g
#        self.h=h
#        self.f=g+h
#
#    def drumRadacina(self):
#        l = []
#        nod = self
#        while nod:
#            l.insert(0, nod)
#            nod = nod.parinte
#        return l
#
#
#    def vizitat(self): #verifică dacă nodul a fost vizitat (informatia lui e in propriul istoric)
#        nodDrum = self.parinte
#        while nodDrum:
#            if (self.info == nodDrum.info):
#                return True
#            nodDrum = nodDrum.parinte
#
#        return False
#
#    def afisSolFisier(self,fisier):
#        f = open(fisier,"w")
#        drum = []
#        nod = self
#        while nod:
#            drum.insert(0, nod)
#            nod = nod.parinte
#
#        for nod in drum:
#            stive=nod.info
#            maxx=-sys.maxsize
#            for s in stive:
#                if len(s)>maxx:
#                    maxx=len(s)
#            for j in range(maxx-1,-1,-1):
#                i=0
#                while(i<len(stive)):
#                    if j>= len(stive[i]):
#                        f.write("  ")
#                    else:
#                        f.write(stive[i][j])
#                        f.write(" ")
#                    i+=1
#                f.write("\n")
#            f.write("----\n")
#            f.write("Cost partial: ")
#            f.write(str(nod.g))
#            f.write("\n")
#        nod=self
#        f.write("\n\nCost: ")
#        f.write(str(nod.g))
#        f.write("\nLungime: ")
#        f.write(str(len(drum)))
#
#    def __str__(self):
#        return str(self.info)
#    def __repr__(self):
#        sir = str(self.info) + "("
#        drum = self.drumRadacina()
#        sir += ("->").join([str(n.info) for n in drum])
#        sir += ")"
#        return sir
#
#
#
#
# import copy
# class Graph:  # graful problemei
#
#    def __init__(self, start, scopuri):
#        self.start = start  # informatia nodului de start
#
#    def verificare_exista_scop(self):
#        stive = self.start.info
#        nrElem = 0
#        for stiva in stive:
#            nrElem += len(stiva)
#        if nrElem % len(stive) == 0:
#            return 1
#        else:
#            return 0
#
#    # va genera succesorii sub forma de noduri in arborele de parcurgere
#    def succesori(self, nodCurent):
#        listaSuccesori = []
#        for istiva, stiva in enumerate(nodCurent.info):
#            copieStiva = copy.deepcopy(nodCurent.info)
#            if len(copieStiva[istiva]) == 0:
#                continue
#            else:
#                bloc = copieStiva[istiva].pop()
#            for istiva2,stiva2 in enumerate(copieStiva):
#                if istiva==istiva2:
#                    continue
#                stareNoua = copy.deepcopy(copieStiva)
#                if bloc not in stareNoua[istiva2]: #schimbare
#                    stareNoua[istiva2].append(bloc)  #schimbare jos
#                    nodNou = NodParcurgere(stareNoua,nodCurent.g + len(stareNoua[istiva2]), self.estimeaza_h(stareNoua,"banala"),parinte= nodCurent)
#                    if not nodNou.vizitat():
#                         listaSuccesori.append(nodNou)
#        return listaSuccesori
#
#    def scop(self, infoNod):
#        for i in range(1,len(infoNod)):
#             if len(infoNod[i])!=len(infoNod[0]):
#                 return 0
#        return 1
#
#    def estimeaza_h(self, infoNod,euristica):
#        if euristica == "banala":
#            if infoNod.scop():
#                return 1
#            return 0
#
#
#    def valideaza(self):
#        conditie1 = all([len(start)==len(scop) for scop in self.scopuri])
#        multimeStart =set(sum(self.start,start=[]))
#        conditie2 = all([set(sum(scop,start=[])) for scop in self.scopuri])
#        return conditie1 and conditie2
#
#
#
#
#
# def bin_search(listaNoduri, nodNou, ls, ld):
#    if len(listaNoduri)==0:
#        return 0
#    if ls==ld:
#        if nodNou.f<listaNoduri[ls].f:
#            return ls
#        elif nodNou.f>listaNoduri[ls].f:
#            return ld+1
#        else: # f-uri egale
#            if nodNou.g < listaNoduri[ls].g:
#                return ld + 1
#            else:
#                return ls
#    else:
#        mij=(ls+ld)//2
#        if nodNou.f<listaNoduri[mij].f:
#            return bin_search(listaNoduri, nodNou, ls, mij)
#        elif nodNou.f>listaNoduri[mij].f:
#            return bin_search(listaNoduri, nodNou, mij+1, ld)
#        else:
#            if nodNou.g < listaNoduri[mij].g:
#                return bin_search(listaNoduri, nodNou, mij + 1, ld)
#            else:
#                return bin_search(listaNoduri, nodNou, ls, mij)
#
#
#
#
# def aStarSolMultiple(gr, nrSolutiiCautate=1):
#    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#    c = [NodParcurgere(gr.start)]
#
#    while len(c) > 0:
#        #print("Coada actuala: " + str(c))
#        #input()
#        nodCurent = c.pop(0)
#
#        if gr.scop(nodCurent.info):
#
#            nodCurent.afisSolFisier("output.txt")
#            print("Solutie:")
#            drum = nodCurent.drumRadacina()
#            print(("->").join([str(n.info) for n in drum]))
#            print("cost:", nodCurent.g)
#            print("\n----------------\n")
#            #input()
#            nrSolutiiCautate -= 1
#            if nrSolutiiCautate == 0:
#                return
#        #[2,4,7,8,10,14]
#        # c+=gr.succesori(nodCurent)
#        for s in gr.succesori(nodCurent):
#            indice=bin_search(c, s, 0, len(c)-1)
#            if indice==len(c):
#                c.append(s)
#            else:
#                c.insert(indice, s)
#
#
# def calc_nr_min_mutari(stiveStare):
#     minim = sys.maxsize
#
#     for Scop in gr.scopuri:
#         minn = 0
#         for j in range(0,len(stiveStare)):
#             i=0
#             while(i<len(stiveStare[j]) and i<len(Scop[j])):
#                 if stiveStare[j][i] != Scop[j][i]:
#                     minn+=1
#                 i+=1
#             if (len(stiveStare[j])!= len(Scop[j]) and len(stiveStare[j])<len(Scop[j])):
#                 minn+= len(Scop[j]) - len(stiveStare[j])
#         if minn<minim:
#             minim = minn
#     return minim
#
# def calc_cost_min_mutari(stiveStare):
#     minim = sys.maxsize
#
#     for Scop in gr.scopuri:
#         minn = 0
#         for j in range(0, len(stiveStare)):
#             i = 0
#             while (i < len(stiveStare[j]) and i < len(Scop[j])):
#                 if stiveStare[j][i] != Scop[j][i]:
#                     minn += ord(Scop[j][i])-ord('a')+1
#                 i += 1
#             if (len(stiveStare[j]) != len(Scop[j]) and len(stiveStare[j]) < len(Scop[j])):
#                 for i in range(i,len(Scop[j])):
#                     minn+=ord(Scop[j][i])-ord('a')+1
#
#         if minn < minim:
#             minim = minn
#     return minim
#
# def calc_cost_max_mutari(stiveStare):
#     maxim = -sys.maxsize
#     for Scop in gr.scopuri:
#         maxx = 0
#         for j in range(0, len(stiveStare)):
#             i = 0
#             while (i < len(stiveStare[j]) and i < len(Scop[j])):
#                 if stiveStare[j][i] != Scop[j][i]:
#                     maxx += ord(Scop[j][i])-ord('a')+1
#                 i += 1
#             if (len(stiveStare[j]) != len(Scop[j]) and len(stiveStare[j]) < len(Scop[j])):
#                 for i in range(i,len(Scop[j])):
#                     maxx += ord(Scop[j][i])-ord('a')+1
#
#         if maxx > maxim:
#             maxim = maxx
#     return maxim
#
# def a_star(gr):
#    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#    l_open = [NodParcurgere(gr.start)]
#
#    # l_open contine nodurile candidate pentru expandare (este echivalentul lui c din A* varianta neoptimizata)
#
#    # l_closed contine nodurile expandate
#    l_closed = []
#    while len(l_open) > 0:
#        # print("Coada actuala: " + str(l_open))
#        # input()
#        nodCurent = l_open.pop(0)
#        l_closed.append(nodCurent)
#        if gr.scop(nodCurent.info):
#
#            print("Solutie:")
#            drum = nodCurent.drumRadacina()
#            print(("->").join([str(n.info) for n in drum]))
#            print("cost:", nodCurent.g)
#            return
#        lSuccesori = gr.succesori(nodCurent)
#        for s in lSuccesori:
#            gasitC = False
#            for nodC in l_open:
#                if s.info == nodC.info:
#                    gasitC = True
#                    if s.f >= nodC.f:
#                        lSuccesori.remove(s)
#                    else:  # s.f<nodC.f
#                        l_open.remove(nodC)
#                    break
#            if not gasitC:
#                for nodC in l_closed:
#                    if s.info == nodC.info:
#                        if s.f >= nodC.f:
#                            lSuccesori.remove(s)
#                        else:  # s.f<nodC.f
#                            l_closed.remove(nodC)
#                        break
#        for s in gr.succesori(nodCurent):
#            indice=bin_search(l_open, s, 0, len(l_open)-1)
#            if indice==len(l_open):
#                l_open.append(s)
#            else:
#                l_open.insert(indice, s)
#
#
#
#
# def breadth_first(gr, nrSolutiiCautate=1):
#    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#    c = [NodParcurgere(gr.start)]
#
#    while len(c) > 0:
#        #print("Coada actuala: " + str(c))
#        #input()
#        nodCurent = c.pop(0)
#
#        if gr.scop(nodCurent.info):
#            print("Solutie:")
#            drum = nodCurent.drumRadacina()
#            print(("->").join([str(n.info) for n in drum]))
#            print("\n----------------\n")
#            #input()
#            nrSolutiiCautate -= 1
#            if nrSolutiiCautate == 0:
#                return
#        c+=gr.succesori(nodCurent)
#
#
# def depth_first(gr, nrSolutiiCautate=1):
#    # vom simula o stiva prin relatia de parinte a nodului curent
#    df(NodParcurgere(gr.start), nrSolutiiCautate)
#
#
# def df(nodCurent, nrSolutiiCautate):
#    if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
#        return nrSolutiiCautate
#    #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
#    #input()
#    if gr.scop(nodCurent.info):
#        print("Solutie: ", end="")
#        drum = nodCurent.drumRadacina()
#        print(("->").join([str(n.info) for n in drum]))
#        print("\n----------------\n")
#        #input()
#        nrSolutiiCautate -= 1
#        if nrSolutiiCautate == 0:
#            return nrSolutiiCautate
#    lSuccesori = gr.succesori(nodCurent)
#    for sc in lSuccesori:
#        if nrSolutiiCautate != 0:
#            nrSolutiiCautate = df(sc, nrSolutiiCautate)
#
#    return nrSolutiiCautate
#
#
#
# def df_nerecursiv(nrSolutiiCautate):
#    stiva = [NodParcurgere(gr.start)]
#    #consider varful stivei in dreapta
#    while stiva: #cat timp stiva nevida
#        nodCurent=stiva.pop() #sterg varful
#        if gr.scop(nodCurent.info):
#            print("Solutie:")
#            drum = nodCurent.drumRadacina()
#            print(("->").join([str(n.info) for n in drum]))
#            print("\n----------------\n")
#            #input()
#            nrSolutiiCautate -= 1
#            if nrSolutiiCautate == 0:
#                return
#        stiva+=gr.succesori(nodCurent)[::-1] #adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf
#
#
#
# ##############################################################################################
# #                                 Initializare problema                                      #
# ##############################################################################################
#
# def calculeaza_stive(sirStive):
#     sirStive = sirStive.strip()
#     listaStive = [stiva.strip().split(" ") if stiva!= "#" else [] for stiva in sirStive.split("\n")]
#     return listaStive
#
#
#
# f=open("input.txt")
# continut =f.read().split("=========")
# start = calculeaza_stive(continut[0])
# stariFinale = continut[1].strip().split("---")
# scopuri =[calculeaza_stive(st) for st in stariFinale ]
#
# NodStart = NodParcurgere(start)
# # print(NodStart)
# gr = Graph(start, scopuri)
#
# # # breadth_first(gr,4)
# # print("----------RECURSIV----------")
# # depth_first(gr,4)
# #
# #
# # print("----------NERECURSIV----------")
# # df_nerecursiv(1)
# #
# # print("----------A Star----------")
# aStarSolMultiple(gr,1)
#
#
# # ex 3
# def a_star_blocuri(gr):
#    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#    l_open = [NodParcurgere(gr.start)]
#
#    # l_open contine nodurile candidate pentru expandare (este echivalentul lui c din A* varianta neoptimizata)
#
#    # l_closed contine nodurile expandate
#    l_closed = []
#    while len(l_open) > 0:
#        # print("Coada actuala: " + str(l_open))
#        # input()
#        nodCurent = l_open.pop(0)
#        l_closed.append(nodCurent)
#        if gr.scop(nodCurent.info):
#            print("Solutie:")
#            drum = nodCurent.drumRadacina()
#            print(("->").join([str(n.info) for n in drum]))
#            print("cost:", nodCurent.g)
#            return
#        lSuccesori = gr.succesori(nodCurent)
#        for s in lSuccesori:
#            gasitC = False
#            for nodC in l_open:
#                if s.info == nodC.info:
#                    gasitC = True
#                    if s.f >= nodC.f:
#                        lSuccesori.remove(s)
#                    else:  # s.f<nodC.f
#                        l_open.remove(nodC)
#                    break
#            if not gasitC:
#                for nodC in l_closed:
#                    if s.info == nodC.info:
#                        if s.f >= nodC.f:
#                            lSuccesori.remove(s)
#                        else:  # s.f<nodC.f
#                            l_closed.remove(nodC)
#                        break
#        for s in gr.succesori(nodCurent):
#            indice=bin_search(l_open, s, 0, len(l_open)-1)
#            if indice==len(l_open):
#                l_open.append(s)
#            else:
#                l_open.insert(indice, s)
#
#
# # print(calc_cost_min_mutari(start))
#






















































