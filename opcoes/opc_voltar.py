from menu import listaMenu
from opcoes import opc_graficos
from design import linhas
from time import sleep
def voltar():

  print()
  print(' '* 15, 'PROCESSANDO...', ' '* 15)
  sleep(2)
  linhas.linha('=')
  print(' ' * 12, 'Bem vindo de volta! :)')

  listaOpc = ['De linha', 'De barras', 'Boxplot', 'Textual','Questionario', 'Fechar programa']
    
  listaMenu.menu(listaOpc)
      
    #GRAFICOS:
  opc_graficos.posEscolha()
  