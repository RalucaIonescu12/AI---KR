# class Nod:
#
#     def __init__(self,informatie  ,parinte = None):
#         self.informatie = informatie
#         self.parinte = parinte
#
#         # mal curent = mal cu barca
#         # mal opus= mal fara barca
#     def drumRadacina(self):
#         nod = self
#         l = [self]
#
#         while nod.parinte != None:
#             l.append(nod.parinte)
#             nod = nod.parinte
#         return l
#
#     def vizitat(self):
#         nod = self
#         while nod.parinte != None:
#             if self.informatie == nod.parinte.informatie:
#                return True #informatia se gaseste in drum
#             nod = nod.parinte
#         return False #am ajuns la radacina deci nu a fost vizitat
#
#     def __repr__(self):
#         drum = [nod.informatie for nod in self.drumRadacina()]
#         drum_str = '->'.join(str(informatie) for informatie in drum)
#         return f"{self.informatie} ({drum_str})"
#
#     def __str__(self):
#         return str(self.informatie)
#
#
#
# class Graf:
#     def __init__(self, listaAdiacenta, nodStart, scopuri):
#         self.listaAdiacenta = listaAdiacenta
#         self.nodStart = nodStart
#         self.scopuri = scopuri
#
#         # mal curent = mal cu barca
#         # mal opus= mal fara barca
#
#     def scop(self, informatieNod):
#
#
#         nod = Nod (informatieNod)
#
#         if nod.info[2] == 1:  # mal stang(initial)
#             self.NCmal_curent = nod.info[0]
#             self.NMmal_curent = nod.info[1]
#             self.NCmal_opus = Graf.N - self.NCmal_curent
#             self.NMmal_opus = Graf.N - self.NMmal_curent
#         else:
#             # mis barca
#             maxMisionariBarca = min(Graf.M, self.NMmal_curent)
#             for mb in range(maxMisionariBarca + 1):
#                 if mb == 0:
#                     minCanB = 1
#                     maxCanBarca = min(Graf.M, self.NCmal_curent)
#                 else:
#                     minCanB = 0
#                     maxCanBarca = min(Graf.M - mb,self.NCmal_curent, mb)
#                 for cb in range(minCanB, maxCanBarca + 1):
#                     NCmal_curentNou = self.NCmal_curent - cb
#                     NMmal_curentNou = self.NMmal_curent - mb
#                     NCmal_opusNou = self.NCmal_opus + cb
#                     NMmal_opusNou = self.NMmal_opus + mb
#                     if NCmal_curentNou <= NMmal_curentNou and NCmal_opusNou <= NMmal_opusNou:
#                         Nod=(NC)
#
#                     # daca ok, atunci creez Nod(informatieNoua)
#         if informatieNod in self.scopuri:
#             return True
#         else:
#             return False
#
#
#
#     def succesori(self, nod):
#         listaSuccesori = []
#         indexNod = -1
#         for i in range(len(self.listaAdiacenta)):
#             if self.listaAdiacenta[i][0] == nod.informatie:
#                 indexNod = i
#                 break
#         if indexNod != -1:
#             for infoSuccesor in self.listaAdiacenta[indexNod][1:]:
#                 succesor = Nod(infoSuccesor, nod)
#                 if succesor.vizitat() == 0:
#                     listaSuccesori.append(succesor)
#         return listaSuccesori
#
#
#
# int f = open("fisier.in" , "r")
# Graf.N= f.readline()  #nr canibali
# Graf.M= f.readline()  #nr misionari
#


#
#
# # informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
# class NodParcurgere:
#     def __init__(self, info, parinte=None):
#         self.info = info  # eticheta nodului, de exemplu: 0,1,2...
#         self.parinte = parinte  # parintele din arborele de parcurgere
#
#     def drumRadacina(self):
#         l = []
#         nod = self
#         while nod:
#             l.insert(0, nod)
#             nod = nod.parinte
#         return l
#
#
#     def vizitat(self): #verifică dacă nodul a fost vizitat (informatia lui e in propriul istoric)
#         nodDrum = self.parinte
#         while nodDrum:
#             if (self.info == nodDrum.info):
#                 return True
#             nodDrum = nodDrum.parinte
#
#         return False
#
#     def __str__(self):
#         repr_barca = ":<barca>"
#         repr_fara_barca = ""
#         if self.info[2] == 1:
#             barcaMalInitial = repr_barca
#             barcaMalFinal = repr_fara_barca
#         else:
#             barcaMalInitial = repr_fara_barca
#             barcaMalFinal = repr_barca
#         return "(Stanga{}) {} canibali {} misionari  ......  (Dreapta{}) {} canibali  {} misionari\n\n".format(
#             barcaMalInitial, self.info[1], self.info[0], barcaMalFinal, Graph.N - self.info[1],
#             Graph.N - self.info[0])
#
#     def afisSolFisier(self, fis):  # returneaza si lungimea drumului
#         l = self.drumRadacina()
#         for nod in l:
#             if nod.parinte is not None:
#                 if nod.parinte.info[2] == 1:
#                     mbarca1 = "stang"
#                     mbarca2 = "drept"
#                 else:
#                     mbarca1 = "drept"
#                     mbarca2 = "stang"
#                 fis.write(
#                     ">>> Barca s-a deplasat de la malul {} la malul {} cu {} canibali si {} misionari.\n".format(mbarca1,
#                             mbarca2, abs( nod.info[1] - nod.parinte.info[1]), abs(nod.info[0] - nod.parinte.info[0])))
#             fis.write(str(nod))
#
#
#
#     def __repr__(self):
#         sir = str(self.info) + "("
#         drum = self.drumRadacina()
#         sir += ("->").join([str(n.info) for n in drum])
#         sir += ")"
#         return sir
#
#
# class Graph:  # graful problemei
#
#     def __init__(self,start, scopuri):
#         self.start = start  # informatia nodului de start
#         self.scopuri = scopuri  # lista cu informatiile nodurilor scop
#
#
#     # va genera succesorii sub forma de noduri in arborele de parcurgere
#     def succesori(self, nodCurent):
#
#         def conditie(mis, can):
#             return mis==0 or mis>=can
#
#         listaSuccesori = []
#         #(misionari mal initial, canibali mal initial, locatie barca) barca=1 daca mal initial si 0 daca final
#         #mal curent = mal cu barca; mal opus= mal fara barca
#         if nodCurent.info[2]==1: #mal initial = mal curent(cu barca)
#             misMalCurent=nodCurent.info[0]
#             canMalCurent=nodCurent.info[1]
#             misMalOpus=Graph.N-nodCurent.info[0]
#             canMalOpus=Graph.N-nodCurent.info[1]
#         else:
#             misMalCurent=Graph.N-nodCurent.info[0]
#             canMalCurent=Graph.N-nodCurent.info[1]
#             misMalOpus=nodCurent.info[0]
#             canMalOpus=nodCurent.info[1]
#         maxMisBarca=min(Graph.M, misMalCurent)
#         for misBarca in range(maxMisBarca+1):
#             if misBarca==0:
#                 minCanBarca=1
#                 maxCanBarca=min(Graph.M, canMalCurent)
#             else:
#                 minCanBarca = 0
#                 maxCanBarca = min(Graph.M-misBarca, canMalCurent, misBarca)
#             for canBarca in range(minCanBarca,maxCanBarca+1):
#                 misMalCurentNou=misMalCurent-misBarca
#                 canMalCurentNou=canMalCurent-canBarca
#                 misMalOpusNou=misMalOpus+misBarca
#                 canMalOpusNou=canMalOpus+canBarca
#                 if not conditie(misMalCurentNou,canMalCurentNou):
#                     continue
#                 if not conditie(misMalOpusNou,canMalOpusNou):
#                     continue
#                 if nodCurent.info[2] == 1:
#                     nodNou= NodParcurgere((misMalCurentNou,canMalCurentNou, 0), nodCurent)
#                 else:
#                     nodNou = NodParcurgere((misMalOpusNou, canMalOpusNou, 1), nodCurent)
#                 if not nodNou.vizitat():
#                     listaSuccesori.append(nodNou)
#         return listaSuccesori
#
#     def scop(self, infoNod):
#         return infoNod in self.scopuri
#
#
#
# ##############################################################################################
# #                                 Initializare problema                                      #
# ##############################################################################################
#
#
#
#
#
#
# #### algoritm BF
# # presupunem ca vrem mai multe solutii (un numar fix) prin urmare vom folosi o variabilă numită nrSolutiiCautate
# # daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# # si doar oprim algoritmul la afisarea primei solutii
#
# def breadth_first(gr, nrSolutiiCautate=1, fis=None):
#     # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#     c = [NodParcurgere(gr.start)]
#
#     while len(c) > 0:
#         #print("Coada actuala: " + str(c))
#         #input()
#         nodCurent = c.pop(0)
#
#         if gr.scop(nodCurent.info):
#             print("Solutie:")
#             drum = nodCurent.drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print("\n----------------\n")
#             if fis:
#                 nodCurent.afisSolFisier(fis)
#                 fis.write("\n----------------\n")
#             #input()
#             nrSolutiiCautate -= 1
#             if nrSolutiiCautate == 0:
#                 return
#         c+=gr.succesori(nodCurent)
#
#
# def depth_first(gr, nrSolutiiCautate=1, fis=None):
#     # vom simula o stiva prin relatia de parinte a nodului curent
#     df(NodParcurgere(gr.start), nrSolutiiCautate, fis)
#
#
# def df(nodCurent, nrSolutiiCautate, fis):
#     if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
#         return nrSolutiiCautate
#     #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
#     #input()
#     if gr.scop(nodCurent.info):
#         print("Solutie: ", end="")
#         drum = nodCurent.drumRadacina()
#         print(("->").join([str(n.info) for n in drum]))
#         print("\n----------------\n")
#         if fis:
#             nodCurent.afisSolFisier(fis)
#             fis.write("\n----------------\n")
#         #input()
#         nrSolutiiCautate -= 1
#         if nrSolutiiCautate == 0:
#             return nrSolutiiCautate
#     lSuccesori = gr.succesori(nodCurent)
#     for sc in lSuccesori:
#         if nrSolutiiCautate != 0:
#             nrSolutiiCautate = df(sc, nrSolutiiCautate, fis)
#
#     return nrSolutiiCautate
#
#
# # df(a)->df(b)->df(c)->df(f)
# #############################################
#
#
# def df_nerecursiv(nrSolutiiCautate, fis=None):
#     stiva = [NodParcurgere(gr.start)]
#     #consider varful stivei in dreapta
#     while stiva: #cat timp stiva nevida
#         nodCurent=stiva.pop() #sterg varful
#         if gr.scop(nodCurent.info):
#             print("Solutie:")
#             drum = nodCurent.drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print("\n----------------\n")
#             if fis:
#                 nodCurent.afisSolFisier(fis)
#                 fis.write("\n----------------\n")
#             #input()
#             nrSolutiiCautate -= 1
#             if nrSolutiiCautate == 0:
#                 return
#         stiva+=gr.succesori(nodCurent)[::-1] #adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf
#
# """
# Mai jos puteti comenta si decomenta apelurile catre algoritmi. Pentru moment e apelat doar breadth-first
# """
#
# f=open("input.txt", "r")
# continut=f.read().split() #["3","2"]
# Graph.N= int(continut[0])
# Graph.M= int(continut[1])
#
# start = (Graph.N, Graph.N,1)
# scopuri = [ (0,0,0) ]
# gr = Graph(start, scopuri)
#
#
# # print("====================================================== \nBreadthfirst")
# f=open("output_bf.txt", "w")
# breadth_first(gr, nrSolutiiCautate=2,fis=f)
# f.close()
# # print("====================================================== \nDepthFirst recursiv")
# f=open("output_df.txt", "w")
# depth_first(gr, nrSolutiiCautate=4,fis=f)
# f.close()
# # print("====================================================== \nDepthFirst nerecursiv")
# f=open("output_df_nerec.txt", "w")
# df_nerecursiv(nrSolutiiCautate=4,fis=f)
# f.close()





#----------------ex4-------------------------------------------


# informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
class NodParcurgere:
    def __init__(self, info, parinte=None):
        self.info = info  # eticheta nodului, de exemplu: 0,1,2...
        self.parinte = parinte  # parintele din arborele de parcurgere

    def drumRadacina(self):
        l = []
        nod = self
        while nod:
            l.insert(0, nod)
            # nod = nod.parinte
        return l


    def vizitat(self): #verifică dacă nodul a fost vizitat (informatia lui e in propriul istoric)
        nodDrum = self.parinte
        while nodDrum:
            if (self.info == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False

    def __str__(self):
        repr_barca = ":<barca>"
        repr_fara_barca = ""
        if self.info[2] == 1:
            barcaMalInitial = repr_barca
            barcaMalFinal = repr_fara_barca
        else:
            barcaMalInitial = repr_fara_barca
            barcaMalFinal = repr_barca
        return "(Stanga{}) {} canibali {} misionari  ......  (Dreapta{}) {} canibali  {} misionari\n\n".format(
            barcaMalInitial, self.info[1], self.info[0], barcaMalFinal, Graph.NC - self.info[1],
            Graph.NM - self.info[0])

    def afisSolFisier(self, fis):  # returneaza si lungimea drumului
        l = self.drumRadacina()
        for nod in l:
            if nod.parinte is not None:
                if nod.parinte.info[2] == 1:
                    mbarca1 = "stang"
                    mbarca2 = "drept"
                else:
                    mbarca1 = "drept"
                    mbarca2 = "stang"
                fis.write(
                    ">>> Barca s-a deplasat de la malul {} la malul {} cu {} canibali si {} misionari.\n".format(mbarca1,
                            mbarca2, abs( nod.info[1] - nod.parinte.info[1]), abs(nod.info[0] - nod.parinte.info[0])))
            fis.write(str(nod))



    def __repr__(self):
        sir = str(self.info) + "("
        drum = self.drumRadacina()
        sir += ("->").join([str(n.info) for n in drum])
        sir += ")"
        return sir


class Graph:  # graful problemei

    def __init__(self,start, scopuri):
        self.start = start  # informatia nodului de start
        self.scopuri = scopuri  # lista cu informatiile nodurilor scop


    # va genera succesorii sub forma de noduri in arborele de parcurgere
    def succesori(self, nodCurent):

        def conditie(mis, can):
            return mis==0 or mis>=can

        listaSuccesori = []
        #(misionari mal initial, canibali mal initial, locatie barca) barca=1 daca mal initial si 0 daca final
        #mal curent = mal cu barca; mal opus= mal fara barca
        if nodCurent.info[2]==1: #mal initial = mal curent(cu barca)
            misMalCurent=nodCurent.info[0]
            canMalCurent=nodCurent.info[1]
            misMalOpus=Graph.NM-nodCurent.info[0]
            canMalOpus=Graph.NC-nodCurent.info[1]
        else:
            misMalCurent=Graph.NM-nodCurent.info[0]
            canMalCurent=Graph.NC-nodCurent.info[1]
            misMalOpus=nodCurent.info[0]
            canMalOpus=nodCurent.info[1]
        maxMisBarca=min(Graph.M, misMalCurent)
        for misBarca in range(1,maxMisBarca+1):

            maxCanBarca = min(Graph.M-misBarca, canMalCurent, misBarca)
            for canBarca in range(maxCanBarca+1):
                misMalCurentNou=misMalCurent-misBarca
                canMalCurentNou=canMalCurent-canBarca
                misMalOpusNou=misMalOpus+misBarca
                canMalOpusNou=canMalOpus+canBarca

                #canibalii si misionarii se "bat" doar in barca si pe malul drept
                if nodCurent.info[2] == 1: #dacamalul curent e cel stang
                    if not conditie(misMalOpusNou, canMalOpusNou): #testez conditia pe malul opus care e cel drept
                        continue
                    nodNou= NodParcurgere((misMalCurentNou,canMalCurentNou, 0), nodCurent)
                else:
                    if not conditie(misMalCurentNou, canMalCurentNou):
                        continue
                    nodNou = NodParcurgere((misMalOpusNou, canMalOpusNou, 1), nodCurent)
                if not nodNou.vizitat():
                    listaSuccesori.append(nodNou)
        return listaSuccesori

    def scop(self, infoNod):
        return infoNod in self.scopuri



##############################################################################################
#                                 Initializare problema                                      #
##############################################################################################






#### algoritm BF
# presupunem ca vrem mai multe solutii (un numar fix) prin urmare vom folosi o variabilă numită nrSolutiiCautate
# daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# si doar oprim algoritmul la afisarea primei solutii

def breadth_first(gr, nrSolutiiCautate=1, fis=None):
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
            if fis:
                nodCurent.afisSolFisier(fis)
                fis.write("\n----------------\n")
            #input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        c+=gr.succesori(nodCurent)


def depth_first(gr, nrSolutiiCautate=1, fis=None):
    # vom simula o stiva prin relatia de parinte a nodului curent
    df(NodParcurgere(gr.start), nrSolutiiCautate, fis)


def df(nodCurent, nrSolutiiCautate, fis):
    if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
        return nrSolutiiCautate
    #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
    #input()
    if gr.scop(nodCurent.info):
        print("Solutie: ", end="")
        drum = nodCurent.drumRadacina()
        print(("->").join([str(n.info) for n in drum]))
        print("\n----------------\n")
        if fis:
            nodCurent.afisSolFisier(fis)
            fis.write("\n----------------\n")
        #input()
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return nrSolutiiCautate
    lSuccesori = gr.succesori(nodCurent)
    for sc in lSuccesori:
        if nrSolutiiCautate != 0:
            nrSolutiiCautate = df(sc, nrSolutiiCautate, fis)

    return nrSolutiiCautate


# df(a)->df(b)->df(c)->df(f)
#############################################


def df_nerecursiv(nrSolutiiCautate, fis=None):
    stiva = [NodParcurgere(gr.start)]
    #consider varful stivei in dreapta
    while stiva: #cat timp stiva nevida
        nodCurent=stiva.pop() #sterg varful
        if gr.scop(nodCurent.info):
            print("Solutie:")
            drum = nodCurent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print("\n----------------\n")
            if fis:
                nodCurent.afisSolFisier(fis)
                fis.write("\n----------------\n")
            #input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        stiva+=gr.succesori(nodCurent)[::-1] #adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf

"""
Mai jos puteti comenta si decomenta apelurile catre algoritmi. Pentru moment e apelat doar breadth-first
"""

f=open("input.txt", "r")
continut=f.read().split() #["3","2"]
Graph.NM= int(continut[0])
Graph.NC= int(continut[1])
Graph.M= int(continut[2])

start = (Graph.NM, 0 ,1)
scopuri = [ (0,Graph.NC,0) ]
gr = Graph(start, scopuri)


# print("====================================================== \nBreadthfirst")
f=open("output_bf.txt", "w")
breadth_first(gr, nrSolutiiCautate=2,fis=f)
f.close()
# print("====================================================== \nDepthFirst recursiv")
f=open("output_df.txt", "w")
depth_first(gr, nrSolutiiCautate=4,fis=f)
f.close()
# print("====================================================== \nDepthFirst nerecursiv")
f=open("output_df_nerec.txt", "w")
df_nerecursiv(nrSolutiiCautate=4,fis=f)
f.close()
