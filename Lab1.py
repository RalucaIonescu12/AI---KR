# #
# # # informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
# # class NodParcurgere:
# #     def __init__(self, info, parinte=None):
# #         self.info = info  # eticheta nodului, de exemplu: 0,1,2...
# #         self.parinte = parinte  # parintele din arborele de parcurgere
# #
# #     def drumRadacina(self):
# #         l = []
# #         nod = self
# #         while nod:
# #             l.insert(0, nod)
# #             nod = nod.parinte
# #         return l
# #
# #
# #     def vizitat(self): #verifică dacă nodul a fost vizitat (informatia lui e in propriul istoric)
# #         nodDrum = self.parinte
# #         while nodDrum:
# #             if (self.info == nodDrum.info):
# #                 return True
# #             nodDrum = nodDrum.parinte
# #
# #         return False
# #
# #     def __str__(self):
# #         return str(self.info)
# #     def __repr__(self):
# #         sir = str(self.info) + "("
# #         drum = self.drumRadacina()
# #         sir += ("->").join([str(n.info) for n in drum])
# #         sir += ")"
# #         return sir
# #
# #
# # class Graph:  # graful problemei
# #
# #     def __init__(self, matrice, start, scopuri):
# #         self.matrice = matrice
# #         self.nrNoduri = len(matrice)
# #         self.start = start  # informatia nodului de start
# #         self.scopuri = scopuri  # lista cu informatiile nodurilor scop
# #
# #
# #     # va genera succesorii sub forma de noduri in arborele de parcurgere
# #     def succesori(self, nodCurent):
# #         listaSuccesori = []
# #         for i in range(self.nrNoduri):
# #             if self.matrice[nodCurent.info][i] == 1:
# #                 nodNou = NodParcurgere(info=i, parinte=nodCurent)
# #                 if not nodNou.vizitat():
# #                     listaSuccesori.append(nodNou)
# #         return listaSuccesori
# #
# #     def scop(self, infoNod):
# #         return infoNod in self.scopuri;
# #
# #
# #
# # ##############################################################################################
# # #                                 Initializare problema                                      #
# # ##############################################################################################
# #
# # m = [
# #     [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
# #     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
# #     [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
# #     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# #     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
# #     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
# #     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
# #     [0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
# #     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
# #     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# # ]
# #
# # start = 0
# # scopuri = [5, 9]
# # gr = Graph(m, start, scopuri)
# #
# #
# # #### algoritm BF
# # # presupunem ca vrem mai multe solutii (un numar fix) prin urmare vom folosi o variabilă numită nrSolutiiCautate
# # # daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# # # si doar oprim algoritmul la afisarea primei solutii
# #
# # def breadth_first(gr, nrSolutiiCautate=1):
# #     # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
# #     c = [NodParcurgere(gr.start)]
# #
# #     while len(c) > 0:
# #         #print("Coada actuala: " + str(c))
# #         #input()
# #         nodCurent = c.pop(0)
# #
# #         if gr.scop(nodCurent.info):
# #             print("Solutie:")
# #             drum = nodCurent.drumRadacina()
# #             print(("->").join([str(n.info) for n in drum]))
# #             print("\n----------------\n")
# #             #input()
# #             nrSolutiiCautate -= 1
# #             if nrSolutiiCautate == 0:
# #                 return
# #         c+=gr.succesori(nodCurent)
# #
# #
# # def depth_first(gr, nrSolutiiCautate=1):
# #     # vom simula o stiva prin relatia de parinte a nodului curent
# #     df(NodParcurgere(gr.start), nrSolutiiCautate)
# #
# #
# # def df(nodCurent, nrSolutiiCautate):
# #     if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
# #         return nrSolutiiCautate
# #     #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
# #     #input()
# #     if gr.scop(nodCurent.info):
# #         print("Solutie: ", end="")
# #         drum = nodCurent.drumRadacina()
# #         print(("->").join([str(n.info) for n in drum]))
# #         print("\n----------------\n")
# #         #input()
# #         nrSolutiiCautate -= 1
# #         if nrSolutiiCautate == 0:
# #             return nrSolutiiCautate
# #     lSuccesori = gr.succesori(nodCurent)
# #     for sc in lSuccesori:
# #         if nrSolutiiCautate != 0:
# #             nrSolutiiCautate = df(sc, nrSolutiiCautate)
# #
# #     return nrSolutiiCautate
# #
# #
# # # df(a)->df(b)->df(c)->df(f)
# # #############################################
# #
# #
# # def df_nerecursiv(nrSolutiiCautate):
# #     stiva = [NodParcurgere(gr.start)]
# #     #consider varful stivei in dreapta
# #     while stiva: #cat timp stiva nevida
# #         nodCurent=stiva.pop() #sterg varful
# #         if gr.scop(nodCurent.info):
# #             print("Solutie:")
# #             drum = nodCurent.drumRadacina()
# #             print(("->").join([str(n.info) for n in drum]))
# #             print("\n----------------\n")
# #             #input()
# #             nrSolutiiCautate -= 1
# #             if nrSolutiiCautate == 0:
# #                 return
# #         stiva+=gr.succesori(nodCurent)[::-1] #adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf
# #
# # """
# # Mai jos puteti comenta si decomenta apelurile catre algoritmi. Pentru moment e apelat doar breadth-first
# # """
# #
# # print("====================================================== \nBreadthfirst")
# # breadth_first(gr, nrSolutiiCautate=4)
# # print("====================================================== \nDepthFirst recursiv")
# # depth_first(gr, nrSolutiiCautate=4)
# # print("====================================================== \nDepthFirst nerecursiv")
# # df_nerecursiv(nrSolutiiCautate=4)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
#  #lab 3
# # informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
# class Nod:
#     def __init__(self, info, parinte=None,g=0, h=0):
#         self.info=info
#         self.parinte=parinte
#         self.g=g  #suma muchiilor de la start la nodul curent
#         self.h=h   #estimarea
#         self.f=self.g+self.h
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
#         return str(self.info)
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
#     def __init__(self,estimari, matrice, start, scopuri):
#         self.matrice = matrice
#         self.nrNoduri = len(matrice)
#         self.estimari = estimari
#         self.start = start  # informatia nodului de start
#         self.scopuri = scopuri  # lista cu informatiile nodurilor scop
#
#     def estimeaza_h(self,nod):
#         return self.estimari[nod]
#
#     # va genera succesorii sub forma de noduri in arborele de parcurgere
#     def succesori(self, nodCurent):
#         listaSuccesori = []
#         for i in range(self.nrNoduri):
#             if self.matrice[nodCurent.info][i] != 0:
#                 nodNou = Nod(info=i, parinte=nodCurent)
#                 if not nodNou.vizitat():
#                     nodNou.g = nodCurent.g + self.matrice[nodCurent.info][i]
#                     nodNou.h = self.estimeaza_h(nodNou.info)
#                     nodNou.f = nodNou.g + nodNou.h
#                     listaSuccesori.append(nodNou)
#         return listaSuccesori
#
#     def scop(self, infoNod):
#         return infoNod in self.scopuri;
#
#
#
# ##############################################################################################
# #                                 Initializare problema                                      #
# ##############################################################################################
#
# # estimariAdmis=[-1,1,5,1,0,4,0]
# # estimariAdmis=[-1,100,100,1,0,100,0]
# # start = 0
# # scopuri = [5, 9]
# # gr = Graph(m, start, scopuri)
#
#
# #### algoritm BF
# # presupunem ca vrem mai multe solutii (un numar fix) prin urmare vom folosi o variabilă numită nrSolutiiCautate
# # daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# # si doar oprim algoritmul la afisarea primei solutii
#
# # def breadth_first(gr, nrSolutiiCautate=1):
# #     # in coada vom avea doar noduri de tip Nod (nodurile din arborele de parcurgere)
# #     c = [Nod(gr.start)]
# #
# #     while len(c) > 0:
# #         #print("Coada actuala: " + str(c))
# #         #input()
# #         nodCurent = c.pop(0)
# #
# #         if gr.scop(nodCurent.info):
# #             print("Solutie:")
# #             drum = nodCurent.drumRadacina()
# #             print(("->").join([str(n.info) for n in drum]))
# #             print("\n----------------\n")
# #             #input()
# #             nrSolutiiCautate -= 1
# #             if nrSolutiiCautate == 0:
# #                 return
# #         c+=gr.succesori(nodCurent)
# #
# #
# # def depth_first(gr, nrSolutiiCautate=1):
# #     # vom simula o stiva prin relatia de parinte a nodului curent
# #     df(Nod(gr.start), nrSolutiiCautate)
# #
# #
# # def df(nodCurent, nrSolutiiCautate):
# #     if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
# #         return nrSolutiiCautate
# #     #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
# #     #input()
# #     if gr.scop(nodCurent.info):
# #         print("Solutie: ", end="")
# #         drum = nodCurent.drumRadacina()
# #         print(("->").join([str(n.info) for n in drum]))
# #         print("\n----------------\n")
# #         #input()
# #         nrSolutiiCautate -= 1
# #         if nrSolutiiCautate == 0:
# #             return nrSolutiiCautate
# #     lSuccesori = gr.succesori(nodCurent)
# #     for sc in lSuccesori:
# #         if nrSolutiiCautate != 0:
# #             nrSolutiiCautate = df(sc, nrSolutiiCautate)
# #
# #     return nrSolutiiCautate
# #
# #
# # # df(a)->df(b)->df(c)->df(f)
# # #############################################
# #
# #
# # def df_nerecursiv(nrSolutiiCautate):
# #     stiva = [Nod(gr.start)]
# #     #consider varful stivei in dreapta
# #     while stiva: #cat timp stiva nevida
# #         nodCurent=stiva.pop() #sterg varful
# #         if gr.scop(nodCurent.info):
# #             print("Solutie:")
# #             drum = nodCurent.drumRadacina()
# #             print(("->").join([str(n.info) for n in drum]))
# #             print("\n----------------\n")
# #             #input()
# #             nrSolutiiCautate -= 1
# #             if nrSolutiiCautate == 0:
# #                 return
# #         stiva+=gr.succesori(nodCurent)[::-1] #adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf
# #
# # """
# # Mai jos puteti comenta si decomenta apelurile catre algoritmi. Pentru moment e apelat doar breadth-first
# # """
# #
# # print("====================================================== \nBreadthfirst")
# # breadth_first(gr, nrSolutiiCautate=4)
# # print("====================================================== \nDepthFirst recursiv")
# # depth_first(gr, nrSolutiiCautate=4)
# # print("====================================================== \nDepthFirst nerecursiv")
# # df_nerecursiv(nrSolutiiCautate=4)
#
# from queue import PriorityQueue
# import time
#
# def aStarSolMultiple (graf, sol):
#
#     pq= PriorityQueue()
#     st=Nod(graf.start)
#     pq.put((st.f,st.g,st))
#
#     while pq.empty()==0:
#         nodCurent= pq.get()
#         if graf.scop(nodCurent[2].info):
#             print("Solutie:")
#             drum = nodCurent[2].drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print(f"Cost total: {nodCurent[2].g}")
#             print("\n----------------\n")
#             sol-=1
#             if sol==0:
#                 return
#         succesori = graf.succesori(nodCurent[2])
#         for s in succesori:
#             pq.put((s.f,s.g,s))
#
#
#
# m = [
#     [0, 3, 5, 10, 0, 0,100],
#     [0,0,0,4,0,0,0],
#     [0,0,0,4,9,3,0],
#     [0,3,0,0,2,0,0],
#     [0,0,0,0,0,0,0],
#     [0, 0, 0, 0, 4, 0, 5],
#     [0,0,3,0,0,0,0]
# ]
# estimari=[-1,1,6,2,0,5,0]
# start=0
# scopuri=[4,6]
# g = Graph(estimari,m,start,scopuri)
#
# aStarSolMultiple(g,5)
#
#
# # informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
# class NodParcurgere:
#     def _init_(self, info, parinte=None, g=0, h=0):
#         self.info = info  # eticheta nodului, de exemplu: 0,1,2...
#         self.parinte = parinte  # parintele din arborele de parcurgere
#         self.g = g
#         self.h = h
#         self.f = g + h
#
#     def drumRadacina(self):
#         l = []
#         nod = self
#         while nod:
#             l.insert(0, nod)
#             nod = nod.parinte
#         return l
#
#     def vizitat(self):  # verifică dacă nodul a fost vizitat (informatia lui e in propriul istoric)
#         nodDrum = self.parinte
#         while nodDrum:
#             if (self.info == nodDrum.info):
#                 return True
#             nodDrum = nodDrum.parinte
#         return False
#
#     def _str_(self):
#         return str(self.info)
#
#     def _repr_(self):
#         sir = str(self.info) + "("
#         drum = self.drumRadacina()
#         sir += ("->").join([str(n.info) for n in drum])
#         sir += ")"
#         return sir
#
#
# class Graph:  # graful problemei
#
#     def _init_(self, matrice, start, scopuri, lista_h):
#         self.matrice = matrice
#         self.nrNoduri = len(matrice)
#         self.start = start  # informatia nodului de start
#         self.scopuri = scopuri  # lista cu informatiile nodurilor scop
#         self.lista_h = lista_h
#
#     # va genera succesorii sub forma de noduri in arborele de parcurgere
#     def succesori(self, nodCurent):
#         listaSuccesori = []
#         for i in range(self.nrNoduri):
#             if self.matrice[nodCurent.info][i] != 0:
#                 nodNou = NodParcurgere(info=i, parinte=nodCurent, g=nodCurent.g + self.matrice[nodCurent.info][i],
#                                        h=self.estimeaza_h(i))
#                 if not nodNou.vizitat():
#                     listaSuccesori.append(nodNou)
#         return listaSuccesori
#
#     def scop(self, infoNod):
#         return infoNod in self.scopuri
#
#     def estimeaza_h(self, infoNod):
#         return self.lista_h[infoNod]
#
#
# ##############################################################################################
# #                                 Initializare problema                                      #
# ##############################################################################################
#
# m = [
#     [0, 3, 5, 10, 0, 0, 100],
#     [0, 0, 0, 4, 0, 0, 0],
#     [0, 0, 0, 4, 9, 3, 0],
#     [0, 3, 0, 0, 2, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 4, 0, 5],
#     [0, 0, 3, 0, 0, 0, 0],
# ]
#
# start = 0
# scopuri = [4, 6]
# lista_h = [0, 1, 6, 2, 0, 3, 0]
# gr = Graph(m, start, scopuri, lista_h)
#
#
# def bin_search(listaNoduri, nodNou, ls, ld):
#     if ld <= 0:  # lista vida
#         return 0
#     if ls == ld:  # e doar un sg element in lista
#         if nodNou.f < listaNoduri[ls].f:
#             return ls
#         elif nodNou.f > listaNoduri[ls].f:
#             return ls + 1
#         else:  # f-uri egale
#             if nodNou.g < listaNoduri[ls].g:
#                 return ls + 1
#             else:
#                 return ls
#     else:
#         mij = int((ls + ld) / 2)
#         if nodNou.f < listaNoduri[mij].f:
#             return bin_search(listaNoduri, nodNou, ls, mij)
#         elif nodNou.f > listaNoduri[mij].f:
#             return bin_search(listaNoduri, nodNou, mij + 1, ld)
#         else:  # f-uri egale deci verific g-urile
#             if nodNou.g < listaNoduri[mij].g:
#                 return bin_search(listaNoduri, nodNou, ls, mij)
#             else:
#                 return bin_search(listaNoduri, nodNou, mij + 1, ld)
#
#
# def aStarSolMultiple(gr, nrSolutiiCautate=1):
#     # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#     c = [NodParcurgere(gr.start)]
#
#     while len(c) > 0:
#         # print("Coada actuala: " + str(c))
#         # input()
#         nodCurent = c.pop(0)
#
#         if gr.scop(nodCurent.info):
#             print("Solutie:")
#             drum = nodCurent.drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print("Cost: ", str(nodCurent.g))
#             print("\n----------------\n")
#             # input()
#             nrSolutiiCautate -= 1
#             if nrSolutiiCautate == 0:
#                 return
#         for s in gr.succesori(nodCurent):
#             indice = bin_search(c, s, 0, len(c) - 1)
#             if indice == len(c):
#                 c.append(s)
#             else:
#                 c.insert(indice, s)
#
#
# #### algoritm BF
# # presupunem ca vrem mai multe solutii (un numar fix) prin urmare vom folosi o variabilă numită nrSolutiiCautate
# # daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# # si doar oprim algoritmul la afisarea primei solutii
#
# def breadth_first(gr, nrSolutiiCautate=1):
#     # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#     c = [NodParcurgere(gr.start)]
#
#     while len(c) > 0:
#         # print("Coada actuala: " + str(c))
#         # input()
#         nodCurent = c.pop(0)
#
#         if gr.scop(nodCurent.info):
#             print("Solutie:")
#             drum = nodCurent.drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print("\n----------------\n")
#             # input()
#             nrSolutiiCautate -= 1
#             if nrSolutiiCautate == 0:
#                 return
#         c += gr.succesori(nodCurent)
#
#
# def depth_first(gr, nrSolutiiCautate=1):
#     # vom simula o stiva prin relatia de parinte a nodului curent
#     df(NodParcurgere(gr.start), nrSolutiiCautate)
#
#
# def df(nodCurent, nrSolutiiCautate):
#     if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
#         return nrSolutiiCautate
#     # print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
#     # input()
#     if gr.scop(nodCurent.info):
#         print("Solutie: ", end="")
#         drum = nodCurent.drumRadacina()
#         print(("->").join([str(n.info) for n in drum]))
#         print("\n----------------\n")
#         # input()
#         nrSolutiiCautate -= 1
#         if nrSolutiiCautate == 0:
#             return nrSolutiiCautate
#     lSuccesori = gr.succesori(nodCurent)
#     for sc in lSuccesori:
#         if nrSolutiiCautate != 0:
#             nrSolutiiCautate = df(sc, nrSolutiiCautate)
#
#     return nrSolutiiCautate
#
#
# # df(a)->df(b)->df(c)->df(f)
# #############################################
#
#
# def df_nerecursiv(nrSolutiiCautate):
#     stiva = [NodParcurgere(gr.start)]
#     # consider varful stivei in dreapta
#     while stiva:  # cat timp stiva nevida
#         nodCurent = stiva.pop()  # sterg varful
#         if gr.scop(nodCurent.info):
#             print("Solutie:")
#             drum = nodCurent.drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print("\n----------------\n")
#             # input()
#             nrSolutiiCautate -= 1
#             if nrSolutiiCautate == 0:
#                 return
#         stiva += gr.succesori(nodCurent)[
#                  ::-1]  # adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # ////////////////////////////////////////////////////////////////////////////////////////////
# # informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
# class NodParcurgere:
#     def _init_(self, info, parinte=None, g=0, h=0):
#         self.info = info  # eticheta nodului, de exemplu: 0,1,2...
#         self.parinte = parinte  # parintele din arborele de parcurgere
#         self.g = g
#         self.h = h
#         self.f = g + h
#
#     def drumRadacina(self):
#         l = []
#         nod = self
#         while nod:
#             l.insert(0, nod)
#             nod = nod.parinte
#         return l
#
#     def vizitat(self):  # verifică dacă nodul a fost vizitat (informatia lui e in propriul istoric)
#         nodDrum = self.parinte
#         while nodDrum:
#             if (self.info == nodDrum.info):
#                 return True
#             nodDrum = nodDrum.parinte
#         return False
#
#     def _str_(self):
#         return str(self.info)
#
#     def _repr_(self):
#         sir = str(self.info) + "("
#         drum = self.drumRadacina()
#         sir += ("->").join([str(n.info) for n in drum])
#         sir += ")"
#         return sir
#
#
# class Graph:  # graful problemei
#
#     def _init_(self, matrice, start, scopuri, lista_h):
#         self.matrice = matrice
#         self.nrNoduri = len(matrice)
#         self.start = start  # informatia nodului de start
#         self.scopuri = scopuri  # lista cu informatiile nodurilor scop
#         self.lista_h = lista_h
#
#     # va genera succesorii sub forma de noduri in arborele de parcurgere
#     def succesori(self, nodCurent):
#         listaSuccesori = []
#         for i in range(self.nrNoduri):
#             if self.matrice[nodCurent.info][i] != 0:
#                 nodNou = NodParcurgere(info=i, parinte=nodCurent, g=nodCurent.g + self.matrice[nodCurent.info][i],
#                                        h=self.estimeaza_h(i))
#                 if not nodNou.vizitat():
#                     listaSuccesori.append(nodNou)
#         return listaSuccesori
#
#     def scop(self, infoNod):
#         return infoNod in self.scopuri
#
#     def estimeaza_h(self, infoNod):
#         return self.lista_h[infoNod]
#
#
# ##############################################################################################
# #                                 Initializare problema                                      #
# ##############################################################################################
#
# m = [
#     [0, 3, 5, 10, 0, 0, 100],
#     [0, 0, 0, 4, 0, 0, 0],
#     [0, 0, 0, 4, 9, 3, 0],
#     [0, 3, 0, 0, 2, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 4, 0, 5],
#     [0, 0, 3, 0, 0, 0, 0],
# ]
#
# start = 0
# scopuri = [4, 6]
# lista_h = [0, 1, 6, 2, 0, 3, 0]
# gr = Graph(m, start, scopuri, lista_h)
#
#
# def bin_search(listaNoduri, nodNou, ls, ld):
#     if ld <= 0:  # lista vida
#         return 0
#     if ls == ld:  # e doar un sg element in lista
#         if nodNou.f < listaNoduri[ls].f:
#             return ls
#         elif nodNou.f > listaNoduri[ls].f:
#             return ls + 1
#         else:  # f-uri egale
#             if nodNou.g < listaNoduri[ls].g:
#                 return ls + 1
#             else:
#                 return ls
#     else:
#         mij = int((ls + ld) / 2)
#         if nodNou.f < listaNoduri[mij].f:
#             return bin_search(listaNoduri, nodNou, ls, mij)
#         elif nodNou.f > listaNoduri[mij].f:
#             return bin_search(listaNoduri, nodNou, mij + 1, ld)
#         else:  # f-uri egale deci verific g-urile
#             if nodNou.g < listaNoduri[mij].g:
#                 return bin_search(listaNoduri, nodNou, ls, mij)
#             else:
#                 return bin_search(listaNoduri, nodNou, mij + 1, ld)
#
#
# def aStarSolMultiple(gr, nrSolutiiCautate=1):
#     # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#     c = [NodParcurgere(gr.start)]
#
#     while len(c) > 0:
#         # print("Coada actuala: " + str(c))
#         # input()
#         nodCurent = c.pop(0)
#
#         if gr.scop(nodCurent.info):
#             print("Solutie:")
#             drum = nodCurent.drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print("Cost: ", str(nodCurent.g))
#             print("\n----------------\n")
#             # input()
#             nrSolutiiCautate -= 1
#             if nrSolutiiCautate == 0:
#                 return
#         for s in gr.succesori(nodCurent):
#             indice = bin_search(c, s, 0, len(c) - 1)
#             if indice == len(c):
#                 c.append(s)
#             else:
#                 c.insert(indice, s)
#
#
# #### algoritm BF
# # presupunem ca vrem mai multe solutii (un numar fix) prin urmare vom folosi o variabilă numită nrSolutiiCautate
# # daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# # si doar oprim algoritmul la afisarea primei solutii
#
# def breadth_first(gr, nrSolutiiCautate=1):
#     # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
#     c = [NodParcurgere(gr.start)]
#
#     while len(c) > 0:
#         # print("Coada actuala: " + str(c))
#         # input()
#         nodCurent = c.pop(0)
#
#         if gr.scop(nodCurent.info):
#             print("Solutie:")
#             drum = nodCurent.drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print("\n----------------\n")
#             # input()
#             nrSolutiiCautate -= 1
#             if nrSolutiiCautate == 0:
#                 return
#         c += gr.succesori(nodCurent)
#
#
# def depth_first(gr, nrSolutiiCautate=1):
#     # vom simula o stiva prin relatia de parinte a nodului curent
#     df(NodParcurgere(gr.start), nrSolutiiCautate)
#
#
# def df(nodCurent, nrSolutiiCautate):
#     if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
#         return nrSolutiiCautate
#     # print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
#     # input()
#     if gr.scop(nodCurent.info):
#         print("Solutie: ", end="")
#         drum = nodCurent.drumRadacina()
#         print(("->").join([str(n.info) for n in drum]))
#         print("\n----------------\n")
#         # input()
#         nrSolutiiCautate -= 1
#         if nrSolutiiCautate == 0:
#             return nrSolutiiCautate
#     lSuccesori = gr.succesori(nodCurent)
#     for sc in lSuccesori:
#         if nrSolutiiCautate != 0:
#             nrSolutiiCautate = df(sc, nrSolutiiCautate)
#
#     return nrSolutiiCautate
#
#
# # df(a)->df(b)->df(c)->df(f)
# #############################################
#
#
# def df_nerecursiv(nrSolutiiCautate):
#     stiva = [NodParcurgere(gr.start)]
#     # consider varful stivei in dreapta
#     while stiva:  # cat timp stiva nevida
#         nodCurent = stiva.pop()  # sterg varful
#         if gr.scop(nodCurent.info):
#             print("Solutie:")
#             drum = nodCurent.drumRadacina()
#             print(("->").join([str(n.info) for n in drum]))
#             print("\n----------------\n")
#             # input()
#             nrSolutiiCautate -= 1
#             if nrSolutiiCautate == 0:
#                 return
#         stiva += gr.succesori(nodCurent)[
#                  ::-1]  # adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf

prime = [n for n in range(2, 100) if all([n % d != 0 for d in range(2, n//2)])][:10]
print(prime)