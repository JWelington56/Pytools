#primeiramente instale o pacote pytube com um pip intall yptube
#carrege a biblioteca
from pytube import YouTube

#variavel para receber o link do video do Youtube
url = input("Digite a url do video: ")
video = YouTube(url)

#escolhendo a melhor resolução
stream = video.streams.get_highest_resolution()

#indicando o local que o arquivo vai ser armazenado
stream.download(output_path = '<local do arquivo>')