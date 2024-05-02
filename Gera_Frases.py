import random

PROD = {

    'Começo'       : [('ARTDEFSING',),('ARTDEFPLUR',),('PronomeSING',)],
    'Final'        : [('no','LocalM'),('na','LocalF')],
    'ARTDEFSING'   : [('o','PessoasSINGM'),('a','PessoasSINGF')],
    'ARTDEFPLUR'   : [('os','PessoasPLURM'),('as','PessoasPLURF'),],
    'PronomeSING'  : [('eu','Verbo1SING'),('voce','Verbo2SING'),('ele','Verbo2SING'),('ela','Verbo2SING')],
    'PronomePLUR'  : [('nos','Verbo1PLUR'),('eles','Verbo2PLUR'),('elas','Verbo2PLUR'),],
    'PessoasSINGM' : [('pedro','Verbo2SING'),('senhor','Verbo2SING')],
    'PessoasSINGF' : [('Maria','Verbo2SING'),('mae','Verbo2SING'),('senhora','Verbo2SING')],
    'PessoasPLURM' : [('garotos','Verbo2PLUR')],
    'PessoasPLURF' : [('meninas','Verbo2PLUR')],
    'LocalF'       : [('praça',),('escola',),('sala',),('casa',),('quadra',),('esquina',),],
    'LocalM'       : [('parque',),('restaurante',),('apartamento',),('correio',),('vizinho',),],
    'Verbo1SING'   : [('estudei','Final'),('brinquei','Final'),('matei','Final'),],
    'Verbo2SING'   : [('estudou','Final'),('brincou','Final'),('matou','Final')],
    'Verbo1PLUR'   : [('estudamos','Final'),('brincamos','Final'),('matamos','Final'),],
    'Verbo2PLUR'   : [('estudaram','Final'),('brincaram','Final'),('mataram','Final')]

}

def gen_random(symbol):
    
    """ Generate a random sentence from the
        grammar, starting with the given
        symbol.
    """

    sentence = ''
    # select one production of this symbol randomly
    rand_prod = random.choice(PROD[symbol])

    if len(rand_prod) == 1 and rand_prod in PROD:
        rand_prod = random.choice(PROD[rand_prod[0]])

    for palavra in rand_prod:
        if palavra in PROD:
            sentence += gen_random(palavra)
        else:
            sentence += palavra + ' '
    return sentence
