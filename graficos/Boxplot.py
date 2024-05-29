from validacoes import validacao_str
from design import linhas
from time import sleep
from BancodeDados import BDBoxplot
import matplotlib.pyplot as plt
from funcionalidades import ordenacao
from funcionalidades import arquivo
import csv

def grafBoxplot(): #boxplot   

  while True:
    while True:
      tipoOlimpiada = str(input('Escolha o tipo de Olimpiada. Digite V para Verao ou I para Inverno: '))
      tipodeOlimpiada = validacao_str.lerSTR(tipoOlimpiada) 
      if tipodeOlimpiada == 'ERRO':
        continue
      else:
        break
    print()
          
    if tipodeOlimpiada == 'V':
      tipodeOlimpiadaEsc = 'Verao'
      tipodeOlimpiada = 'Summer'
      break
    elif tipodeOlimpiada == 'I':
      tipodeOlimpiadaEsc = 'Inverno'
      tipodeOlimpiada = 'Winter'
      break 
    else:
      linhas.linha('=')
      print('ERRO! Tente novamente.')
      linhas.linha('=')

  sleep(1)      
  print('Apresentaremos a seguir a quantidade de atletas de cada pais nas Olimpiadas de {} ao decorrer dos anos.'.format(tipodeOlimpiadaEsc))

  boxplot = BDBoxplot.bancoDadosBoxPlot(tipodeOlimpiada)
  arquivoAtleta = 'athlete_events.csv'
  arquivos = arquivo.abrirArquivo(arquivoAtleta)

  anos = []
  c = 0
  for dado in arquivos:
    c += 1
    if c == 1:
      continue
    if dado[9] not in anos:
      anos.append(dado[9])
  
  listaAtletas = {}
  atletas = []
  for ano in boxplot:
    
    anos.append(int(ano[0]))
    atletas = [boxplot[ano]]
    listaAtletas[ano] = atletas
  
  plt.boxplot(list(listaAtletas.values()), labels = list(listaAtletas.keys()))
  plt.xlabel('ANOS')
  plt.ylabel('ATLETAS')
  plt.savefig('Boxplot.png')  
  plt.show()
  plt.close()