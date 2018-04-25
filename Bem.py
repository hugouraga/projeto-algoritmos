class Bem:
    def __init__(self, codigoTipoBem, descTipoBem, descDetalhadoBem, valorBem):
        self.__codigoBem = codigoTipoBem
        self.__descTipoBem = descTipoBem
        self.__descDetalhadoBem = descDetalhadoBem
        self.__valorBem = valorBem

    def __str__(self):
        return "\n{} -- {} -- {} \n\n Descrição:{}".format(self.__codigoBem, self.__descTipoBem, self.__descDetalhadoBem,self.__valorBem)

    def __repr__(self):
        return "\n{} -- {} -- {} \n Descrição:{}".format(self.__codigoBem, self.__descTipoBem , self.__descDetalhadoBem, self.__valorBem)

    def comparacaoBens(self): # metodo de comparação atráves dos bens
        pass  # comparar os valores dos bens de acordo com o paramentro passado pelo usuario

