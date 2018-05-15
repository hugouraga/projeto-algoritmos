from operator import attrgetter
class No:
    def __init__(self,chave=None,valor=None):
        self.__chave = chave
        self.__valor = valor
        self.__proximo = [None] * 10

class Arvore:
    def __init__(self):
        self.__raiz = No()
        self.__contador = 0
        
    def adicionar(self, chave=None, valor=None):
        novoNo = self.__raiz
        for elementos in chave:
            if novoNo._No__proximo[int(elementos)] == None:
                novoNo._No__proximo[int(elementos)] = No()
            novoNo = novoNo._No__proximo[int(elementos)]
        if not novoNo._No__chave is None:
            novoNo._No__chave = chave
            return
        novoNo._No__chave = chave
        novoNo._No__valor = valor
        self.__contador += 1
                
    def __getitem__(self, chave):
        buscaNo = self.__raiz
        for elementos in chave:
            #print(buscaNo.proximo)
            if buscaNo._No__proximo[int(elementos)] == None:
                pass
				#raise keyError
            buscaNo = buscaNo._No__proximo[int(elementos)]
        if not buscaNo._No__chave is None:
            return buscaNo._No__valor

    def __setitem__(self, chave, valor):
        #[nodo._No__chave,nodo._No__valor][chave]=[valor]
        nodo = self.__raiz
        for elementos in chave:
            if nodo._No__proximo[int(elementos)] == None:
                nodo._No__proximo[int(elementos)] = No()
            nodo = nodo._No__proximo[int(elementos)]
        if not nodo._No__chave is None:
            nodo._No__chave = chave
            return
        nodo._No__chave = chave
        nodo._No__valor = valor
         
