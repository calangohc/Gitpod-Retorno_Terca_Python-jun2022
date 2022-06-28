import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-mistas/cmo/Indicacoes-para-execucao-orcamentaria-em-RP9_LOA-2022')

pagina_processada = BeautifulSoup(pagina.text, 'html.parser')

tags_a = pagina_processada.find_all('a')

print("Encontrei %d links" % len(tags_a))

planilhas = []

for a in tags_a:
    if a.get('href'):
        url = a.get('href')
        if url[-4:] == 'xlsx':
            planilhas.append(url)

for url in planilhas:
    nome_arquivo = url.split('/')[-1]
    conteudo = requests.get(url)

    # arquivo = open(nome_arquivo, 'wb')
    with open('planilhas/' + nome_arquivo, 'wb') as arquivo:
        arquivo.write(conteudo.content)





#list()
