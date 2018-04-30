from operator import *

import Candidato
import Bem
import lista
tamanhoLista = 0
tamanhoListaBens = 0
listaAux = lista.ListaDuplamenteEncadeada()
listaTeste = lista.ListaDuplamenteEncadeada()
listaCarregamentoCandidatos = lista.ListaDuplamenteEncadeada()

listaBens = lista.ListaDuplamenteEncadeada()
listaDesBens = lista.ListaDuplamenteEncadeada()
listaGeral = lista.ListaDuplamenteEncadeada()
listaDetalhadaBens = lista.ListaDuplamenteEncadeada()
listaGeralBens = lista.ListaDuplamenteEncadeada()



acessoArquivoBens = "bem_candidato_2014"
acessoListasBens = "bem_candidato_2014_"
acessoArquivoConsulta = "consulta_cand_2014"
acessoListasConsulta =  "consulta_cand_2014_"
UFs = ["AC"]
#, "AM", "AP", "BA", "BR", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO", "ZZ"]

class Controle:
    def __init__(self):
        pass
    def carregamentoCandidatos(self, acessoListas):
        global tamanhoLista
        carregamentoCandidatos = open(acessoListas,"r")
        arquivo = carregamentoCandidatos.readlines()
        for lista in arquivo:
            parametro = ""
            for dados in lista:
                if dados != ";":
                    parametro += dados
                else:
                    listaCarregamentoCandidatos.adicionarAuxiliar(parametro)
                    parametro = ""
            candidatos = Candidato.Candidato()

            candidatos.setAnoEleixao(listaCarregamentoCandidatos.acessar(2))
            candidatos.setSiglaUF(listaCarregamentoCandidatos.acessar(5))
            candidatos.setCodigoCargo(listaCarregamentoCandidatos.acessar(8))
            candidatos.setDescricaoCargo(listaCarregamentoCandidatos.acessar(9))
            candidatos.setNomeCandidato(listaCarregamentoCandidatos.acessar(10))
            candidatos.setIdCandidato(listaCarregamentoCandidatos.acessar(11))
            candidatos.setNumeroUrna(listaCarregamentoCandidatos.acessar(12))
            candidatos.setCPF(listaCarregamentoCandidatos.acessar(13))
            candidatos.setNomeUrna(listaCarregamentoCandidatos.acessar(14))
            candidatos.setNumeroPartido(listaCarregamentoCandidatos.acessar(17))
            candidatos.setNomePartido(listaCarregamentoCandidatos.acessar(19))
            candidatos.setSiglaPartido(listaCarregamentoCandidatos.acessar(18))
            candidatos.setCodigoOcupacao(listaCarregamentoCandidatos.acessar(24))
            candidatos.setDescricaoOcupacao(listaCarregamentoCandidatos.acessar(25))
            candidatos.setDataNascimento(listaCarregamentoCandidatos.acessar(26))
            candidatos.setSexoCandidato(listaCarregamentoCandidatos.acessar(30))
            candidatos.setGrauInstituicao(listaCarregamentoCandidatos.acessar(31))
            candidatos.setEstadoCivil(listaCarregamentoCandidatos.acessar(34))
            candidatos.setUFNacimento(listaCarregamentoCandidatos.acessar(39))
            candidatos.setMunicipioNasc(listaCarregamentoCandidatos.acessar(41))
            candidatos.setSitCandiPosEleito(listaCarregamentoCandidatos.acessar(44))
            candidatos.setSitCandidatura(listaCarregamentoCandidatos.acessar(16))
            candidatos.setListaBens(listaBens)

            listaGeral.adicionar(candidatos)
            listaCarregamentoCandidatos.adicionarAuxiliar(True)
            tamanhoLista += 1
        tamanhoLista -= 1
        carregamentoCandidatos.close()

    def carregamentoBensCandidatos(self, caminhoArquivo):
        carregamentoBens = open(caminhoArquivo,"r")
        arquivoBens = carregamentoBens.readlines()
        print(tamanhoLista)
        for listaBens in arquivoBens:
           parametro = ""
           for elementos in listaBens:
                if elementos != ";":
                    parametro += elementos
                else:
                    listaDetalhadaBens.adicionarAuxiliar(parametro)
                    parametro = ""

           idCandidato = listaDetalhadaBens.acessar(5)

           bens = Bem.Bem(listaDetalhadaBens.acessar(6), listaDetalhadaBens.acessar(7), listaDetalhadaBens.acessar(8).replace('"', ""),float(listaDetalhadaBens.acessar(9).replace('"', "")))
           listaGeralBens.adicionar(bens)
           index = 0
           entrei = False
           while index < tamanhoLista:
               verificador = listaGeral.pesquisa(index)._Candidato__idCandidato

               if idCandidato == verificador:
                   adicionandoBens = listaGeral.pesquisa(index)
                   if listaGeral.pesquisa(index)._Candidato__listaBens == [None,None]:
                       valor = bens._Bem__valorBem
                       descricao = bens._Bem__descDetalhadoBem

                       bem = [valor, descricao]
                       listaGeral.pesquisa(index).incluirBem(bem)
                       index += 50000
                       entrei = True
                   else:
                       valor = bens._Bem__valorBem
                       descricao = bens._Bem__descDetalhadoBem
                       adicionando = listaGeral.pesquisa(index)._Candidato__listaBens
                       adicionando[0] += valor
                       adicionando[1] += descricao
                       bem = [adicionando[0], adicionando[1]]
                       listaGeral.pesquisa(index).incluirBem(bem)
                       entrei = True

               index += 1
           if entrei == False:
               bem = [None,None]
               listaGeral.pesquisa(index - 1).incluirBem(bem)

           listaDetalhadaBens.adicionarAuxiliar(True)
        carregamentoBens.close()

    def recuperandoUsuarios(self,entrada):
        index = 0
        if entrada == "1":
            verificacao = input("Forneça o nome do partido a ser analisado: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__nomePartido
                verificador = verificador.replace('"',"")
                if verificacao == verificador:
                    print(listaGeral.pesquisa(index))
                verificador = ""
                index += 1

        elif entrada == "2":
            verificacao = input("Forneça o nome do estado a ser analisado: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__siglaUF
                verificador = verificador.replace('"',"")
                if verificacao == verificador:
                    print(listaGeral.pesquisa(index))
                verificador = ""
                index += 1
        elif entrada == "3":
            verificacao = input("Forneça o nome da cidade a ser analisada: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__municipioNasc
                verificador = verificador.replace('"',"")
                if verificacao == verificador:
                     print(listaGeral.pesquisa(index))
                verificador = ""
                index += 1
        elif entrada == "4":
            verificacao = input("Forneça o nome do cargo a ser analisado: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__descricaoCargo
                verificador = verificador.replace('"',"")
                if verificacao == verificador:
                    print(listaGeral.pesquisa(index))
                verificador = ""
                index += 1
        elif entrada == "5":
            verificacao = float(input("Forneça um valor base -> "))
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__listaBens
                verificador = verificador[0]
                if verificador != None:
                    if verificacao < verificador:
                        print(listaGeral.pesquisa(index))
                index += 1
        elif entrada == "6":
            verificacao = "ELEITO"
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__sitCandiPosEleito
                verificador = verificador.replace('"',"")

                if verificacao == verificador:
                    print(listaGeral.pesquisa(index))
                verificador = ""
                index += 1
        elif entrada == "7":
            verificacao = "NÃO ELEITO"
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__sitCandidatura
                verificador = verificador.replace('"',"")
                if verificacao == verificador:
                    print(verificacao)
                verificador = ""
                index += 1
        else:
            print("entrada inválida")

    def mediaTotalBens(self, entrada):
        valorTotal = 0
        media = 0
        contador = 0
        index = 0
        if entrada == "1":
            verificacao = input("Forneça o nome do cargo a ser analisado: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                acessoTipo = listaGeral.pesquisa(index)._Candidato__descricaoCargo
                acessoTipo = acessoTipo.replace('"', "")
                if verificacao == acessoTipo:
                    objetoValor = listaGeral.pesquisa(index)._Candidato__listaBens
                    valor = objetoValor[0]
                    if valor != None:
                        valorTotal += valor
                    contador += 1
                index += 1
            if contador != 0:
                media = valorTotal / contador
                print("valor total:" +str(valorTotal))
                print("media: " +str(media))
                return media
        elif entrada == "2":

            verificacao = input("Forneça a sigla do Estado a ser analisado: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                acessoTipo = listaGeral.pesquisa(index)._Candidato__siglaUF
                acessoTipo = acessoTipo.replace('"', "")
                if verificacao == acessoTipo:
                    objetoValor = listaGeral.pesquisa(index)._Candidato__listaBens
                    valor = objetoValor[0]
                    if valor != None:
                        valorTotal += valor
                    contador += 1
                index += 1
            if contador != 0:
                media = valorTotal / contador
                print("valor total:" +str(valorTotal))
                print("media: " +str(media))
                return media
        elif entrada == "3":
            verificacao = input("Forneça a ocupação dos candidatos a serem analisados: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                acessoTipo = listaGeral.pesquisa(index)._Candidato__descricaoOcupacao
                acessoTipo = acessoTipo.replace('"', "")
                if verificacao == acessoTipo:
                    objetoValor = listaGeral.pesquisa(index)._Candidato__listaBens
                    valor = objetoValor[0]
                    if valor != None:
                        valorTotal += valor
                        contador += 1
                index += 1
            if contador != 0:
                media = valorTotal / contador
                print("valor total:" + str(valorTotal))
                print("media: " + str(media))
                return media
        elif entrada == "4":
            index = 0

            verificacao = input("Forneça a data de nascimento a ser analisada: dia/mês/ano")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                acessoTipo = listaGeral.pesquisa(index)._Candidato__dataNascimento
                acessoTipo = acessoTipo.replace('"', "")
                if verificacao == acessoTipo:
                    print("entrei")
                    objetoValor = listaGeral.pesquisa(index)._Candidato__listaBens
                    valor = objetoValor[0]
                    if valor != None:
                        valorTotal += valor
                        contador += 1
                index += 1
            if contador != 0:
                media = valorTotal / contador
                print("valor total:" + str(valorTotal))
                print("media: " + str(media))
                return media
    def excluirCandidato(self, removeCandidato):
        #print("- Eleito \n - Não eleito \n - Indeferido - \n + \n- deferido\n- deferido com  recurso  \n- indeferido"
         #    + "\n- indeferido com recurso  \n- renúnica  \n- cancelado\n  ")
        contador = 0
        for elemento in listaGeral:
            teste = elemento._Candidato__municipioNasc
            if teste == removeCandidato:
                print(teste ," == ", removeCandidato)
                listaGeral.remove(elemento)
            contador += 1
for uf in UFs:
    candidatosConsulta = str(acessoArquivoConsulta + "/" + acessoListasConsulta + uf +".txt")
    candidatosBens = str(acessoArquivoBens + "/" + acessoListasBens + uf +".txt")

    candidatos = Controle()

    candidatos.carregamentoCandidatos(candidatosConsulta)
    candidatos.carregamentoBensCandidatos(candidatosBens)

print("################ Banco de dados Justiça Eleitorial 2014 ################")
print("########################################################################\n")
print("# 1 - Análise específica no banco de dados")
print("# 2 - Análise ordenada dos elementos do banco de dados")
print("# 3 - Análise específica das médias totais")
print("# 4 - Remover candidatos específicos")
opcao = input("\nForneça a numeração de acordo com a atividade desejada -> ")

if opcao == "1":
    print("\n#   1 - Análide por partido")
    print("#   2 - Análise por Estado")
    print("#   3 - Análise por cidade de nascimento")
    print("#   4 - Análise de candidatos a um determinado cargo")
    print("#   5 - Análise do Valor total de bens declarado")
    print("#   6 - Análise dos que foram eleitos")
    print("#   7 - Análise dos que não foram eleitos")
    entrada = input("\nForneça a numeração de acordo com a atividade desejada -> ")
    x = candidatos.recuperandoUsuarios(entrada)
    print(x)

elif opcao == "2":
    print("\nAinda não ta pronto")
elif opcao == "3":
    print("\n#   1 - Análise da média total de bens por cargo")
    print("#   2 - Análise da média total de bens por Estado")
    print("#   3 - Análise da média total de bens por ocupação")
    print("#   4 - Análise da média total de bens por ano de nascimento")
    entrada = input("\nForneça a numeração de acordo com a atividade desejada -> ")
    x = candidatos.mediaTotalBens(entrada)
elif opcao == "4":
    entrada = input("Forneça um critério para exclução de candidatos do banco de dados ex: eleitos, não eleitos, indeferidos e etc-> ")
    x = candidatos.excluirCandidato(entrada)

