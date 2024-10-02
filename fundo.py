import os
from rembg import remove
from PIL import Image

# Define o caminho da pasta onde as imagens estão
pasta = 'imgFundo'

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    # Verifica se o arquivo é uma imagem com extensão .jpg, .png, etc.
    if nome_arquivo.endswith(('.jpg', '.JPG', '.jpeg', '.JPEG')):
        # Exibe o nome do arquivo
        print(nome_arquivo)

        # Constrói o caminho completo para o arquivo de entrada
        img_entrada = os.path.join(pasta, nome_arquivo)

        # Define o caminho completo para o arquivo de saída
        img_saida = os.path.join(pasta, 'sFundo', f'{os.path.splitext(nome_arquivo)[0]}.PNG')

        # Abre a imagem e processa com o rembg
        input = Image.open(img_entrada)
        output = remove(input)
        output.save(img_saida)

