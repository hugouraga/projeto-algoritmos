class Candidato:
    def __init__(self, anoEleicao, siglaUF, codigoCargo, descricaoCargo, nomeCandidato, idCandidato, numeroUrna, cpf,
                 nomeUrna, numeroPartido, nomePartido, siglaPartido, codigoOcupacao, descricaoOcupacao, dataNascimento
                 , sexoCandidato, grauInstituicao, estadoCivil, UFNascimento, municipioNasc, sitCandiPosEleito,
                 sitCandidatura,  listaBens):
        self.__anoEleicao = anoEleicao
        self.__siglaUF = siglaUF
        self.__codigoCargo = codigoCargo
        self.__descricaoCargo = descricaoCargo
        self.__nomeCandidato = nomeCandidato
        self.__idCandidato = idCandidato
        self.__numeroUrna = numeroUrna
        self.__cpf = cpf
        self.__nomeUrna = nomeUrna
        self.__numeroPartido = numeroPartido
        self.__nomePartido = nomePartido
        self.__siglaPartido = siglaPartido
        self.__codigoOcupacao = codigoOcupacao
        self.__descricaoOcupacao = descricaoOcupacao
        self.__dataNascimento = dataNascimento
        self.__sexoCandidato = sexoCandidato
        self.__grauInstituicao = grauInstituicao
        self.__estadoCivil = estadoCivil
        self.__UFNascimento = UFNascimento
        self.__municipioNasc = municipioNasc
        self.__sitCandiPosEleito = sitCandiPosEleito
        self.__sitCandidatura = sitCandidatura
        self.__listaBens = listaBens

    def __str__(self):
        return "\n{} -- {} -- {}\n{}\n{}\nResumo dos bens:\n  -  Total declado: {}\n  -  Total por tipo de bem: {}\n".format(
            self.__nomeUrna, self.__numeroUrna, self.__siglaPartido, self.__descricaoOcupacao, self.__municipioNasc,
            self.__listaBens.mostrar(), self.__listaBens.mostrar())

    def __repr__(self):
        return "\n{} -- {} -- {}\n{}\n{}\nResumo dos bens:\n  -  Total declado: {}\n  -  Total por tipo de bem: {}\n".format(
            self.__nomeUrna, self.__numeroUrna, self.__siglaPartido, self.__descricaoOcupacao, self.__municipioNasc,
            self.__listaBens, self.__listaBens)

    def exibirBens(self):
        pass

    def getAnoEleicao(self):
        return self.__anoEleicao

    def getSiglaUF(self):
        return self.__siglaUF

    def getCodigoCargo(self):
        return self.__codigoCargo

    def getDescricaoCargo(self):
        return self.__descricaoCargo

    def getNomeCandidato(self):
        return self.__nomeCandidato

    def getIdCandidato(self):
        return self.__idCandidato

    def getNumeroUrna(self):
        return self.__numeroUrna

    def getCPF(self):
        return self.__cpf

    def getNomeUrna(self):
        return self.__nomeUrna

    def getNumeroPartido(self):
        return self.__numeroPartido

    def getNomePartido(self):
        return self.__nomePartido

    def getSiglaPartido(self):
        return self.__siglaPartido

    def getCodigoOcupacao(self):
        return self.__codigoOcupacao

    def getDescricaoOcupacao(self):
        return self.__descricaoOcupacao

    def getDataNascimento(self):
        return self.__dataNascimento

    def getSexoCandidato(self):
        return self.__sexoNascimento

    def getGrauInstituicao(self):
        return self.__grauInstituicao

    def getEstadoCivil(self):
        return self.__estadoCivil

    def getUFNacimento(self):
        return self.__UFNascimento

    def getMunicipioNasc(self):
        return self.__municipioNasc

    def getSitCandiPosEleito(self):
        return self.__sitCandidatoPosEleito

    def getSitCandidatura(self):
        return self.__sitCanditarura

    def getListaBens(self):
        return self.__listasBens

    # MÉTODO PARA ALTERAR OBJETO
    def setAnoEleixao(self, anoEleicao):
        self.__anoEleicao = anoEleicao

    def setSiglaUF(self, siglaUF):
        self.__siglaUF = siglaUF

    def setCodigoCargo(self, codigoCargo):
        self.__codigoCargo = codigoCargo

    def setDescricaoCargo(self, descricaoCargo):
        self.__descricaoCargo = descricaoCargo

    def setNomeCandidato(self, nomeCandidato):
        self.__nomeCandidato = nomeCandidato

    def setIdCandidato(self, idCandidato):
        self.__idCandidato = idCandidato

    def setNumeroUrna(self, numeroUrna):
        self.__numeroUrna = numeroUrna

    def setCPF(self, cpf):
        self.__cpf = cpf

    def setNomeUrna(self, nomeUrna):
        self.__nomeUrna = nomeUrna

    def setNumeroPartido(self, numeroPartido):
        self.__numeroPartido = numeroPartido

    def setNomePartido(self, nomePartido):
        self.__nomePartido = nomePartido

    def setSiglaPartido(self, siglaPartido):
        self.__siglaPartido = siglaPartido

    def setCodigoOcupacao(self, codigoOcupacao):
        self.__codigoOcupacao = codigoOcupacao

    def setDescricaoOcupacao(self, descricaoOcupacao):
        self.__descricaoOcupacao = descricaoOcupacao

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def setSexoCandidato(self, sexoNascimento):
        self.__sexoNascimento = sexoNascimento

    def setGrauInstituicao(self, grauInstituicao):
        self.__grauInstituicao = grauInstituicao

    def setEstadoCivil(self, estadoCivil):
        self.__estadoCivil = estadoCivil

    def setUFNacimento(self, UFNacimento):
        self.__UFNascimento = UFNacimento

    def setMunicipioNasc(self, municipioNasc):
        self.__municipioNasc = municipioNasc

    def setSitCandiPosEleito(self, sitCandidaturaPosEleito):
        self.__sitCandidatoPosEleito = sitCandidaturaPosEleito

    def setSitCandidatura(self, sitCandidatura):
        self.__sitCanditarura = sitCandidatura

    def setListaBens(self, listasBens):
        self.__listasBens = listasBens

    def incluirBem(self, bens):
        self.__listaBens = bens


    def comparacaoCandidatos(self):
        tamanhoLista = len(listaGeral)
        for candidatos in range(tamanhoLista):
            primeiroCandidato = listaGeral[candidatos]
            nomeCompletoPrimeiro = primeiroCandidato._Candidato__nomeCompleto
            cpfPrimeiro = primeiroCandidato._Candidato__cpf
            for candidatos2 in range(candidatos + 1, tamanhoLista):
                segundoCandidato = listaGeral[candidatos2]
                nomeCompletoSegundo = segundoCandidato._Candidato__nomeCompleto
                cpfSegundo = segundoCandidato._Candidato__cpf
                if nomeCompletoPrimeiro == nomeCompletoSegundo and cpfPrimeiro == cpfSegundo :
                    print("encontrei")


    def bensDeclaradosCandidato(self):
        pass
