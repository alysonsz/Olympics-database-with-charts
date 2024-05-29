from validacoes import validacao_str
from design import linhas
from time import sleep
from BancodeDados import BDLinhas
import matplotlib.pyplot as plt

def grafLinhas():  #grafico de linhas
  print('Apresentaremos a seguir a evolucao da media do IMC (Indice de Massa Corporal) dos atletas do genero masculino (M) ou feminino (F), que ganharam medalhas em alguma das Olimpiadas.')
  print()
  sleep(1)

  while True:
    while True:
      genero = str(input('Por favor, escolha um dos generos. Digite M para masculino ou F para feminino: '))
      generoEsc = validacao_str.lerSTR(genero)
      if generoEsc == 'ERRO':
        continue
      
      else:
        break
        
    print()
          
    if generoEsc == 'M':
      generoDesejado = 'Masculino'
      print('Voce escolheu o genero Masculino')
      break
    elif generoEsc == 'F':
      generoDesejado = 'Feminino'
      print('Voce escolheu o genero Feminino')
      break 
    else:
      linhas.linha('=')
      print('ERRO! Tente novamente.')
      linhas.linha('=')

  dados = BDLinhas.bancoDadosLinhas(generoEsc)
  anoS = []
  dadosimc = []
  for c, v in dados.items():
    anoS.append(c)
    dadosimc.append(v)

  anos = anoS

  imc = dadosimc

  plt.plot(anoS, imc)
  plt.title('IMC dos atletas do genero {} que ganharam medalhas em alguma das Olimpiadas'.format((generoDesejado)))
  plt.xlabel('Anos')
  plt.ylabel('Media do IMC')
  plt.savefig('Linhas.png')
  plt.show()
