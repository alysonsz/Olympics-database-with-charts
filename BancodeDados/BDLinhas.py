from funcionalidades import arquivo

def ordenarListaIMC(listaIMC):
  
  temp = []
  dadosIMC = {}
  for ano,imc in listaIMC.items():
    imc = '%.2f' % imc
    temp.append((ano, imc))

  temp.sort(reverse = True)

  for i in temp:
    dadosIMC[i[0]] = i[1]
 
  return dadosIMC

def imc(generoEscolhido):
  arquivoAtleta = 'athlete_events.csv'
  arq = arquivo.abrirArquivo(arquivoAtleta)
  dadosIMC = {}
  contLinhas = 0
  imcTotal = 0

  for dados in arq:
    contLinhas += 1
    
    if contLinhas == 1:
      continue
    altura = dados[4]
    peso = dados[5]
    genero = dados[2]
    ano = int(dados[9])

    try:
      imc = float(peso) / float(altura) ** 2
    
    except:
      imc = 0
    
    if genero == generoEscolhido:
      if ano in dadosIMC:
        imcTotal = imc + dadosIMC[ano]
        dadosIMC[ano] = imcTotal
      else:
        imcTotal = imc
        dadosIMC[ano] = imcTotal

  dadosDeIMC = ordenarListaIMC(dadosIMC)
  return dadosDeIMC 

def bancoDadosLinhas(generoEscolhido):
  dadosLinhas = imc(generoEscolhido)
  return dadosLinhas