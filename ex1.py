centenas = {
    1: "cento",
    2: "duzentos",
    3: "trezentos",
    4: "quatrocentos",
    5: "quinhentos",
    6: "seiscentos",
    7: "setecentos",
    8: "oitocentos",
    9: "novecentos"
}

dezenas = {
    2: "vinte",
    3: "trinta",
    4: "quarenta",
    5: "cinquenta",
    6: "sessenta",
    7: "setenta",
    8: "oitenta",
    9: "noventa"
}

unidades = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove"
}

especiais = {
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "quatorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezessete",
    18: "dezoito",
    19: "dezenove",
    100: "cem"
}

def get_cdu(numero):
    if numero in especiais:
        return "{}".format(especiais[numero])

    extenso = ""
    c, numero = divmod(numero, 100)
    if c:
        extenso += "{}{}".format(centenas[c], " e " if numero else "")
    if numero in especiais:
        extenso += "{}".format(especiais[numero])
    else:
        d, u = divmod(numero, 10)
        if d:
            extenso += "{}{}".format(dezenas[d], " e " if u else "")
        if u:
            extenso += "{}".format(unidades[u])
    
    return extenso
        

def get_milhao(numero):
    milhao, numero = divmod(numero, 1000000)
    if milhao:
        return "{} {}".format(get_cdu(milhao), "milhão" if milhao == 1 else "milhões"), numero
    return "", numero


def get_mil(numero):
    mil, numero = divmod(numero, 1000)
    if mil:
        return "{} mil".format(get_cdu(mil)) if mil > 1 else "mil", numero
    return "", numero


def get_reais(numero):
    if numero == 1:
        return "um real"
    if numero == 0:
        return ""

    milhoes, numero = get_milhao(numero)
    milhares, numero = get_mil(numero)
    resto = get_cdu(numero)

    return "{}{}{}{}{} reais".format(
        milhoes, 
        " e " if milhoes and milhares else "",
        milhares, 
        " e " if milhares and resto else "",
        resto)


def get_centavos(numero):
    if numero == 1:
        return "um centavo"
    if numero == 0:
        return ""
    
    return "{} centavos".format(get_cdu(numero))



valor = input("Digite um valor ou 0 para sair:")
while valor != "0":
    # nao digitou um valor com casa decimal
    if valor.find(',') < 0:   
        valor = input("Digite um valor válido:")
    else:
        reais, centavos = valor.split(',')
        # aceitar apenas valores com dois digitos após a virgula e com até 9 dígitos antes da vírgula
        if len(centavos) != 2 or len(reais) < 1 or len(reais) > 9:
            valor = input("Digite um valor válido:")
        else:
            # reais
            reais = get_reais(int(reais))
            # centavos
            centavos = get_centavos(int(centavos))

            print("{}{}{}".format(reais, " e " if reais and centavos else "", centavos))
            
            valor = input("Digite um valor ou 0 para sair:")