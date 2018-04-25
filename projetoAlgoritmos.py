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
#, "AL"]
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
            candidatos = Candidato.Candidato(listaCarregamentoCandidatos.acessar(2),  listaCarregamentoCandidatos.acessar(5),  listaCarregamentoCandidatos.acessar(8),
                                             listaCarregamentoCandidatos.acessar(9),  listaCarregamentoCandidatos.acessar(10), listaCarregamentoCandidatos.acessar(11),
                                             listaCarregamentoCandidatos.acessar(12), listaCarregamentoCandidatos.acessar(13), listaCarregamentoCandidatos.acessar(14),
                                             listaCarregamentoCandidatos.acessar(17), listaCarregamentoCandidatos.acessar(19), listaCarregamentoCandidatos.acessar(18),
                                             listaCarregamentoCandidatos.acessar(24), listaCarregamentoCandidatos.acessar(25), listaCarregamentoCandidatos.acessar(26),
                                             listaCarregamentoCandidatos.acessar(30), listaCarregamentoCandidatos.acessar(31), listaCarregamentoCandidatos.acessar(34),
                                             listaCarregamentoCandidatos.acessar(39), listaCarregamentoCandidatos.acessar(41), listaCarregamentoCandidatos.acessar(44),
                                             listaCarregamentoCandidatos.acessar(16), listaBens)
            listaGeral.adicionar(candidatos)
            listaCarregamentoCandidatos.adicionarAuxiliar(True)
            tamanhoLista += 1
        tamanhoLista -= 1
        carregamentoCandidatos.close()

    def carregamentoBensCandidatos(self, caminhoArquivo):
        carregamentoBens = open(caminhoArquivo,"r")
        arquivoBens = carregamentoBens.readlines()
        tamanhoLista = 620
        for listaBens in arquivoBens:
           index = 0
           parametro = ""
           for elementos in listaBens:
                if elementos != ";":
                    parametro += elementos
                else:
                    listaDetalhadaBens.adicionarAuxiliar(parametro)
                    parametro = ""

           idCandidato = listaDetalhadaBens.acessar(5)

           bens = Bem.Bem(listaDetalhadaBens.acessar(6), listaDetalhadaBens.acessar(7), float(listaDetalhadaBens.acessar(9).replace('"', "")), listaDetalhadaBens.acessar(8))
           listaGeralBens.adicionar(bens)
           print(listaGeralBens.adicionar(bens))
           while index < tamanhoLista:
               verificador = listaGeral.pesquisa(index)._Candidato__idCandidato

               if idCandidato == verificador:
                   # listaGeral.pesquisa(index)._Bem__listaBens.adicionar(bens)
                   candidatosAtualizando = Candidato.Candidato(listaGeral.pesquisa(index)._Candidato__anoEleicao,
                                                               listaGeral.pesquisa(index)._Candidato__siglaUF,
                                                               listaGeral.pesquisa(index)._Candidato__codigoCargo ,
                                                               listaGeral.pesquisa(index)._Candidato__descricaoCargo,
                                                               listaGeral.pesquisa(index)._Candidato__nomeCandidato,
                                                               listaGeral.pesquisa(index)._Candidato__idCandidato,
                                                               listaGeral.pesquisa(index)._Candidato__numeroUrna,
                                                               listaGeral.pesquisa(index)._Candidato__cpf,
                                                               listaGeral.pesquisa(index)._Candidato__nomeUrna,
                                                               listaGeral.pesquisa(index)._Candidato__numeroPartido,
                                                               listaGeral.pesquisa(index)._Candidato__nomePartido,
                                                               listaGeral.pesquisa(index)._Candidato__siglaPartido,
                                                               listaGeral.pesquisa(index)._Candidato__codigoOcupacao,
                                                               listaGeral.pesquisa(index)._Candidato__descricaoOcupacao,
                                                               listaGeral.pesquisa(index)._Candidato__dataNascimento,
                                                               listaGeral.pesquisa(index)._Candidato__sexoCandidato,
                                                               listaGeral.pesquisa(index)._Candidato__grauInstituicao,
                                                               listaGeral.pesquisa(index)._Candidato__estadoCivil,
                                                               listaGeral.pesquisa(index)._Candidato__UFNascimento,
                                                               listaGeral.pesquisa(index)._Candidato__municipioNasc,
                                                               listaGeral.pesquisa(index)._Candidato__sitCandiPosEleito,
                                                               listaGeral.pesquisa(index)._Candidato__sitCandidatura, listaBens)
                   candidatosAtualizando.incluirBem(bens)
                   listaGeral.adicionarPosicao(index,candidatosAtualizando)

                   index += 50000
               index += 1
           listaDetalhadaBens.adicionarAuxiliar(True)

        carregamentoBens.close()


      #      contando = 0
    #        for contador in range(tamanhoLista -1):
      #          verificador = listaGeral.pesquisa(contador)._Candidato__idCandidato

                #if verificador == idCandidato:
                #    acessoCandidato = listaGeralBens.pesquisa(0)
                    #if acessoCandidato.rabo.anterior == None:
                    #    print("sim")
                    #valor = acessoCandidato.adicionarAuxiliarBens(listaGeralBens.pesquisa(0))
                    #escricao = acessoCandidato.adicionarAuxiliarBens(listaGeralBens.pesquisa(0))

                    #teste =  listaGeral.pesquisa(index)
                   # x = teste._Candidato__listaBens



                    #if convertendo != None:
                     #   convertendo._Candidato__listaBens.replace('"',"")
                    #    convertendo += float(convertendo)
                    #if teste == None:
                     #   verificadorBensTotal = listaGeral.adicionar(teste)._Candidato__listaBens
                     #   varificadorBensDescricao = listaGeral.adicionar(1)._Candidato__descDetalhadoBem
                    #istaBens =  listaGeralBens.adicionar(teste)
                    #listaGeral.adicionar(index)._Candidato__listaBens = contando
     #       index += 1
           # print(idCandidato)
            #print(listaBens.mostrar())

            #print(listaGeralBens.pesquisa(0)._Bem__valorBem)

    #    listaDetalhadaBens.adicionarAuxiliarBens(True)

        #codigoId = listaDetalhadaBens.pesquisa(index)._Candidato__idCandidato
        #print(codigoId)
    def recuperandoUsuarios(self,entrada):
        index = 0
        if entrada == "1":
            verificacao = input("Forneça o nome do partido a ser analisado: ")
            verificacao = verificacao.upper()
            semAspas = ""
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__nomePartido
                verificador.replace('"',"")
                if verificacao == verificador:
                    print(listaGeral.pesquisa(index))
                verificador = ""
                index += 1

        elif entrada == "2":
            verificacao = input("Forneça o nome do estado a ser analisado: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__siglaUF
                verificador.replace('"',"")
                if verificacao == verificador:
                    print(verificacao)
                verificador = ""
                index += 1
        elif entrada == "3":
            verificacao = input("Forneça o nome da cidade a ser analisada: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__municipioNasc
                verificador.replace('"',"")
                if verificacao == verificador:
                    print(verificacao)
                verificador = ""
                index += 1
        elif entrada == "4":
            verificacao = input("Forneça o nome do cargo a ser analisado: ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__descricaoCargo
                verificador.replace('"',"")
                if verificacao == verificador:
                    print(verificacao)
                verificador = ""
                index += 1
        elif entrada == "5":
            verificacao = float(input("Forneça um valor base -> "))
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__valorBem[0]
                verificador.replace('"',"")
                if verificacao == verificador:
                    print(verificacao)
                verificador = ""
                index += 1
        elif entrada == "6":
            print("\n - Eleito \n - Não eleito \n - Suplente \n - Eleito por qp \n - Eleito por média \n")
            verificacao = input("situação pós eleito: ")

            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__sitCandiPosEleito
                verificador.replace('"',"")
                if verificacao == verificador:
                    print(verificacao)
                verificador = ""
                index += 1
        elif entrada == "7":
            verificacao = input("\nSituação candidatura:"
                                + "\n- deferido\n- deferido com  recurso  \n- indeferido"
                                + "\n- indeferido com recurso  \n- renúnica  \n- cancelado\n -> ")
            verificacao = verificacao.upper()
            while index < tamanhoLista:
                verificador = listaGeral.pesquisa(index)._Candidato__sitCandidatura
                verificador.replace('"',"")
                if verificacao == verificador:
                    print(verificacao)
                verificador = ""
                index += 1

        else:
            print("entrada inválida")

'''
    def mediaTotalBens(self, entrada):
        valorTotal = 0
        media = 0
        contador = 0
        if entrada == "1":
            verificacao = input("Forneça o nome do cargo a ser analisado: ")
            verificacao = verificacao.upper()
            for elementos in listaGeral:
                acessoTipo = elementos._Candidato__descricaoOcupacao
                if verificacao == acessoTipo:
                    valor = elementos._Candidato__listaBens[0]
                    if valor != []:
                        valor = valor[0]
                        valorTotal += valor
                        contador += 1
            if contador != 0:
                print(valorTotal)
                media = valorTotal / contador
        elif entrada == "2":
            contador = 0
            verificacao = input("Forneça a sigla do Estado a ser analisado: ")
            verificacao = verificacao.upper()
            for elementos in listaGeral:
                acessoTipo = elementos._Candidato__siglaUF
                acessoTipo = acessoTipo.replace('"', "")
                if verificacao == acessoTipo:
                    valor = elementos._Candidato__listaBens[0]
                    if valor != []:
                        valor = valor[0]
                        valorTotal += valor

                        contador += 1
            if contador != 0:
                print(valorTotal)
                media = valorTotal / contador
        elif entrada == "3":
            verificacao = input("Forneça a ocupação dos candidatos a serem analisados: ")
            verificacao = verificacao.upper()
            for elementos in listaGeral:
                acessoTipo = elementos._Candidato__descricaoOcupacao
                if verificacao == acessoTipo:
                    valor = elementos._Candidato__listaBens[0]
                    if valor != []:
                        valor = valor[0]
                        valorTotal += valor
                        contador += 1
            if contador != 0:
                media = valorTotal / contador
        elif entrada == "4":
            verificacao = input("Forneça a data de nascimento a ser analisada: dia/mês/ano")
            verificacao = verificacao.upper()
            for elementos in listaGeral:
                acessoTipo = elementos._Candidato__descricaoOcupacao
                if verificacao == acessoTipo:
                    valor = elementos._Candidato__listaBens[0]
                    if valor != []:
                        valor = valor[0]
                        valorTotal += valor
                        contador += 1
            if contador != 0:
                media = valorTotal / contador
        print(media)
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
'''
for uf in UFs:
    candidatosConsulta = str(acessoArquivoConsulta + "/" + acessoListasConsulta + uf +".txt")
    candidatosBens = str(acessoArquivoBens + "/" + acessoListasBens + uf +".txt")

    candidatos = Controle()

    candidatos.carregamentoCandidatos(candidatosConsulta)
    candidatos.carregamentoBensCandidatos(candidatosBens)


#print(listaGeral.mostrar())
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

