# Randomizador Eficiente de Playlists Colaborativas do Spotify

## Descrição
Este projeto visa melhorar a experiência das playlists colaborativas do Spotify ao implementar uma randomização mais eficiente. Em vez de reproduzir músicas de forma totalmente aleatória, onde pode haver a possibilidade de tocar várias músicas consecutivas do mesmo colaborador, este randomizador garante uma alternância equilibrada entre os diferentes contribuintes da playlist. Por exemplo, em uma playlist colaborativa com 5 pessoas, a reprodução será organizada para que toque uma música de cada pessoa em sequência.

## Como utilizar?
Primeiramente, faça login em <https://developer.spotify.com/> e crie um projeto no dashboard, em **Redirect URIs"**, coloque: **http://127.0.0.1:8000/callback**

Após clonar o repositório, execute o comando:
pip install -r requirements.txt para instalar os pacotes necessários

No arquivo settings.env, insira as informações necessárias que se obtêm na API do Spotify.