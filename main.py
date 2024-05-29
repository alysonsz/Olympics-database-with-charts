import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
from menu import listaMenu
from opcoes import opc_graficos

listaOpc = ['De Linhas', 'De Barras', 'Boxplot', 'Textual', 'Questionario','Fechar programa']
arquivoNoc = 'noc_regions.csv'
arquivoAtleta = 'athlete_events.csv'
arquivoContinente = 'countries-continents.csv'

listaMenu.menu(listaOpc)

opc_graficos.posEscolha()
