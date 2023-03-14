from flask import Flask, jsonify, request
import json



app = Flask(__name__)


animes = [
    {
        'id': 1,
        'titulo': 'One Piece',
        'autor': 'Echiro Oda',
        'sobre': 'A série foca em Monkey D. Luffy, um jovem feito de borracha, que, inspirado em seu ídolo de infância, o poderoso pirata Shanks, o Ruivo, parte em uma jornada do mar do East Blue para encontrar o tesouro mítico, o One Piece, e proclamar-se o Rei dos Piratas.'

    },
    {
        'id': 2,
        'titulo': 'Pokemon',
        'autor': 'Satoshi Tajiri',
        'sobre': 'O nome Pokémon é uma abreviação da marca japonesa Pocket Monsters (ポケットモンスター Poketto Monsutā?).[10] O termo Pokémon, além de se referir a própria franquia Pokémon, também se refere às mais de 900 espécies de ficção que aparecem na mídia de Pokémon. A palavra "Pokémon" é usada no singular e plural para o nome individual de cada espécie; a gramática correta é "um Pokémon" e "muitos Pokémon", bem como "um Pikachu" e "muitos Pikachu".[11] (no entanto, em Pokémon Red, Blue e Yellow, alguns NPCs se referiam a Clefairy e Diglett no plural, mostrando "CLEFAIRYs" and "DIGLETTs", respectivamente. Isso foi arrumado em FireRed e LeafGreen.)'

    },
    {
        'id': 3,
        'titulo': 'Naruto',
        'autor': 'Masashi Kishimoto',
        'sobre': 'Naruto (ナルト) é uma série de mangá escrita e ilustrada por Masashi Kishimoto, que conta a história de Naruto Uzumaki, um jovem ninja que constantemente procura por reconhecimento e sonha em se tornar Hokage, o ninja líder de sua vila.'

    },

]

@app.route('/animes',methods=['GET'])
def obter_animes():
    return json.dumps(animes, indent=4)


@app.route('/animes/<int:id>',methods=['GET'])
def obter_id(id):
    for anime in animes:
        if anime.get('id') == id:
            return json.dumps(animes, indent=4)
        


@app.route('/animes/<int:id>',methods=['PUT'])        
def editar_anime(id):
    anime_alterado = request.get_json()
    for indice,anime in enumerate(animes):
        if anime.get('id') == id:
            animes[indice].update(anime_alterado)
            return json.dumps(animes[indice], indent=4)
        
@app.route('/animes',methods=['POST']) 
def incluir_anime():
    novo_anime = request.get_json()
    animes.append(novo_anime)
    return json.dumps(animes, indent=4)


@app.route('/animes/<int:id>',methods=['DELETE'])
def excluir_anime(id):
    for indice, anime in enumerate(animes):
        if anime.get('id') == id:
           del animes[indice]
    return json.dumps(animes, indent=4)       



app.run(port=5000,host='localhost',debug=True)