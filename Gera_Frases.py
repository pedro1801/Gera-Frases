import random
class geraFrases():
    def __init__(self):
        self.confirma = False
        self.prod = {
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
        print('Foi Inicializado')

    def insertProd(self,PessoaM,PessoaF,PessoaMP,PessoaFP,LocasM,LocasF,Verbo1,Verbo2,Verbo3,Verbo4):
        if self.confirma == False:
            self.prod = {
            'Começo'       : [('ARTDEFSING',),('ARTDEFPLUR',),('PronomeSING',)],
            'Final'        : [('no','LocalM'),('na','LocalF')],
            'ARTDEFSING'   : [('o','PessoasSINGM'),('a','PessoasSINGF')],
            'ARTDEFPLUR'   : [('os','PessoasPLURM'),('as','PessoasPLURF'),],
            'PronomeSING'  : [('eu','Verbo1SING'),('voce','Verbo2SING'),('ele','Verbo2SING'),('ela','Verbo2SING')],
            'PronomePLUR'  : [('nos','Verbo1PLUR'),('eles','Verbo2PLUR'),('elas','Verbo2PLUR'),],
            'PessoasSINGM' : [],
            'PessoasSINGF' : [],
            'PessoasPLURM' : [],
            'PessoasPLURF' : [],
            'LocalF'       : [],
            'LocalM'       : [],
            'Verbo1SING'   : [],
            'Verbo2SING'   : [],
            'Verbo1PLUR'   : [],
            'Verbo2PLUR'   : []
            }
            self.confirma = True
        self.prod['PessoasSINGM'].append((PessoaM,'Verbo2SING'))
        self.prod['PessoasSINGF'].append((PessoaF,'Verbo2SING'))
        self.prod['PessoasPLURM'].append((PessoaMP,'Verbo2PLUR'))
        self.prod['PessoasPLURF'].append((PessoaFP,'Verbo2PLUR'))
        self.prod['LocalF'].append((LocasF,))
        self.prod['LocalM'].append((LocasM,))
        self.prod['Verbo1SING'].append((Verbo1,'Final'))
        self.prod['Verbo2SING'].append((Verbo2,'Final'))
        self.prod['Verbo1PLUR'].append((Verbo3,'Final'))
        self.prod['Verbo2PLUR'].append((Verbo4,'Final'))

    def gen_random(self,symbol):
        """ Generate a random sentence from the
            grammar, starting with the given
            symbol.
        """
        sentence = ''
        # select one production of this symbol randomly
        rand_prod = random.choice(self.prod[symbol])

        if len(rand_prod) == 1 and rand_prod in self.prod:
            rand_prod = random.choice(self.prod[rand_prod[0]])

        for palavra in rand_prod:
            if palavra in self.prod:
                sentence += self.gen_random(palavra)
            else:
                sentence += palavra + ' '
        return sentence
