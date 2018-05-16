class No:
    def __init__(self,chave=None,valor=None):
        self.chave = chave
        self.valor = valor
        self.proximo = [None] * 10

class Arvore:
    def __init__(self):
        self.raiz = No()
        
    def adicionar(self, chave=None, valor=None):
        novoNo = self.raiz
        for elementos in chave:
            if novoNo.proximo[int(elementos)] == None:
                novoNo.proximo[int(elementos)] = No(elementos)
            novoNo = novoNo.proximo[int(elementos)]
            ultimo = elementos
        novoNo.proximo[int(ultimo)] = No(ultimo, valor)
        """if not novoNo._No__chave is None:
            novoNo._No__chave = chave
            return
        novoNo._No__chave = chave
        novoNo._No__valor = valor
        self.__contador += 1"""
                
    def __getitem__(self, chave):
        buscaNo = self.raiz
        for elementos in chave:
            #print(chave)
            #print(buscaNo.proximo)
            if buscaNo.proximo[int(elementos)] == None:
                raise KeyError
            buscaNo = buscaNo.proximo[int(elementos)]
            ultimo = elementos
        if not buscaNo.chave is None:
            return buscaNo.proximo[int(ultimo)].valor
        raise KeyError

    def __setitem__(self, chave, valor):
        self.adicionar(chave,valor)
