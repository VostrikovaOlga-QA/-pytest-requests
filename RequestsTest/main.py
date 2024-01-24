
"""
Kolorado test Api

"""
import requests


URL='https://api.pokemonbattle.me:9104'

HEADER = {"Content-type": "application/json", 
         "trainer_token": "5305af55c6f00f16b23dc8e02d4ddc8b"
         }

#body= {
    #"name": "generate",
    #"photo": "https://dolnikov.ru/pokemons/albums/012.png"
    #}

#response=requests.post(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение {response.json()["message"]}')

#body = {
    #"pokemon_id": "28136",
    #"name": "Тушакутуша",
    #"photo": "https://dolnikov.ru/pokemons/albums/009.png"
#}

#response=requests.put(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение {response.json()["message"]}')

#body = {
 #   "pokemon_id": "28136"
#}

#response=requests.post(url=f'{URL}/trainers/add_pokeball',json=body,headers=HEADER,timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение {response.json()["message"]}')


response=requests.get(url=f'{URL}/trainers', timeout=5)
print(f'Статус код: {response.status_code}.')
        

