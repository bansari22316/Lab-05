'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
   # for poke in poke_info['results']:
    print(poke_info)
    #print(poke_info)
    #return

   # info = get_pokemon_info("Rockruff")
    #for i in info['results']:
     #   print(i['info'])

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    headers = {
        'Accept': 'application/json'  # To get joke in JSON formatted text
    }

    pokemon_name = str(pokemon_name).strip().lower()

    # TODO: Build a clean URL and use it to send a GET request
    print(f'Getting information for {pokemon_name}...', end='')
    url = POKE_API_URL + pokemon_name
    #resp_msg = requests.get(url, headers=headers)
    

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    try:
        resp_msg = requests.get(url, headers=headers)



        if resp_msg.status_code == requests.codes.ok:
            print('success')
            return resp_msg.json()

        
        

    # TODO: If the GET request failed, print the error reason and return None
        else:
            print('failure')
            print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')         
            return None
        
    except Exception as e:
        print("failure")
        print(f'Request error: {str(e)}')
        return None

if __name__ == '__main__':
    main()