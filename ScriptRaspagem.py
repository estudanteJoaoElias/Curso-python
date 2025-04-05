import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site de exemplo
url = "https://semalt.com/pt/qa/ferramenta-de-raspagem-de-dados.htm"

try:
    # Fazendo a requisição HTTP
    response = requests.get(url)
    response.raise_for_status()  # Verifica se houve erro na requisição

    # Extraindo o conteúdo da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrando os elementos desejados (exemplo: títulos e descrições)
    titles = [title.text.strip() for title in soup.find_all('h3')]
    descriptions = [desc.text.strip() for desc in soup.find_all('p')]

    # Verificando os tamanhos das listas
    print(f"Tamanho de 'titles': {len(titles)}")
    print(f"Tamanho de 'descriptions': {len(descriptions)}")

    # Ajustando os tamanhos das listas para evitar erros
    min_length = min(len(titles), len(descriptions))
    titles = titles[:min_length]
    descriptions = descriptions[:min_length]

    # Criando um DataFrame com os dados raspados
    df = pd.DataFrame({'Título': titles, 'Descrição': descriptions})

    # Exibindo o DataFrame
    #print(df)

except requests.exceptions.RequestException as e:
    print(f"Erro durante a requisição: {e}")
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")
