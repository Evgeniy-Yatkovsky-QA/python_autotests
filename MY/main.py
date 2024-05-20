import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
POKEMON_ID = '3221'
body_registration = {
    "trainer_token": TOKEN,
    "email": "email",
    "password": "password"
} 
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбач",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_pokeball = {
    "pokemon_id": "3221"
}

body_name = {
    "pokemon_id": POKEMON_ID ,
    "name": "BULBA",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

'''responce = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json =  ) 
print(responce.text)'''


'''responce_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(responce_confirmation.text)'''

'''responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text)'''

'''responce_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER , json = body_pokeball)
print(responce_pokeball.text)'''

responce_name = requests.put(url = f'{URL}/pokemons' , headers = HEADER , json = body_name)
print(responce_name.text)
