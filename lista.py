class No:
    def __init__(self, dado, anterior = None, proximo = None):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo

class ListaDuplamenteEncadeada:
    def __init(self):
        pass
    def listaVazia(self):
        self.anterior = self.proximo = self.dado = No(None,None,None)
    cabeca = None
    rabo = None

    def pesquisa(self, index):
        contador = 0
        no_atual = self.cabeca
        if index == 0:
            if contador == index:
                if no_atual.dado != None:
                    return no_atual.dado
                    contador += 1

        while contador <= index:
            no_atual = no_atual.proximo
            if contador == index:
                if no_atual.dado != None:
                    return no_atual.dado
            contador += 1
    def adicionar(self,dado):

        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.rabo = novo_no

        else:
            novo_no.anterior = self.rabo
            novo_no.proximo = None
            self.rabo.proximo = novo_no
            self.rabo = novo_no
    def adicionarPosicao(self, index, teste):
        novo_no = No(teste)
        contador = 0
        no_atual = self.cabeca
        if index == 0:
            if contador == index:
                if no_atual.dado != None:
                    no_atual.dado = novo_no
                    contador += 1

        while contador <= index:
            no_atual = no_atual.proximo
            if contador == index:
                if no_atual.dado != None:
                    no_atual.dado = novo_no
            contador += 1
    def adicionarAuxiliar(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.rabo = novo_no

        else:
            novo_no.anterior = self.rabo
            novo_no.proximo = None
            self.rabo.proximo = novo_no
            self.rabo = novo_no
        if dado == True:
            self.anterior = self.proximo = self.dado = self.cabeca = self.rabo = None
    def adicionarInicio(self, dado):

        novo_no = No(dado)
        if self.cabeca == None:
            self.cabeca = novo_no
            self.rabo = novo_no
        else:
            novo_no.proximo = self.cabeca
            novo_no.anterior = None
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no
    def remove(self, dado):
        no_atual = self.cabeca

        while no_atual != None:
           if no_atual.dado == dado:
                if no_atual.anterior == None:
                    self.cabeca = no_atual.prox
                    no_atual.proximo.anterior = None
                else:
                    no_atual.anterior.proximo = no_atual.proximo
                    no_atual.proximo.anterior = no_atual.anterior
           no_atual = no_atual.proximo
    def removeInicio(self):
        no_atual = self.cabeca
        if self.cabeca == None:
            x = "lista vazia"
            return x
        else:
            self.cabeca = no_atual.prox
            no_atual.proximo.anterior = None
    def removeFinal(self):
        no_atual = self.rabo
        if self.cabeca == None:
            x = "lista Vazia"
            return x
        else:
            no_atual.anterior = None
            no_atual.anterior.proximo = None
    def mostrar(self):
        no_atual = self.cabeca
        while no_atual != None:
            print(no_atual.dado)
            no_atual = no_atual.proximo
        print("=" * 80)
    def acessar(self, index):
        contador = 1
        no_atual = self.cabeca

        while contador <= index:
            no_atual = no_atual.proximo
            if contador == index:
               return no_atual.dado
            contador += 1

lista = ListaDuplamenteEncadeada()


