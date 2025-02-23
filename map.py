#https://www.google.com/maps/place/


#C.+de+Rodríguez+Jaén,+26,+Madrid

import re
import webbrowser
import json
from difflib import get_close_matches



def user_interaction():
    while True:
        user_input: str = input('Which country are you exploring? ')
        if user_input.lower()=='quit':
            print('I hope you found your place! Have a good day <3')
            break
        else:
            country=user_input
            country=country.title()

        user_input: str = input('Which city are you exploring? ')
        if user_input.lower()=='quit':
            print('I hope you found your place! Have a good day <3')
            break
        else:
            city=user_input
            
        user_input: str = input('Insert the address you wish to consult on Google Maps: ')
        address = user_input

        if user_input.lower()=='quit':
            print('I hope you found your place! Have a good day <3')
            break

        if country=="Spain":
            clean_address=clean_up_str_spain(address, city)
            url = "https://www.google.com/maps/place/" + clean_address
            webbrowser.open(url)

            print("I hope this is what you are looking for!")
        
        if country == "USA" or country == "Estados Unidos" or country == "United States Of America" or country== "Usa"  or country== "United States":
            user_input: str = input('Which State is it in? ')
            state = user_input

            clean_address=clean_up_str_usa(address, city, state, country)
            url_usa = "https://www.google.com/maps/place/" + str(clean_address)
            webbrowser.open(url_usa)

        else:
            print("I'm sorry, but I can't provide information on this country")

def get_state_abbreviation(state_name, json_file='/Users/elisacascudo/Desktop/Universidad/4º-2S/idkd/experiment/Map Project/states.json'):
    try:
        # Open and load the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # Access the 'states' list from the loaded JSON data
        states_data = data.get("states", [])
        
        # Check if states_data is a list of dictionaries
        if isinstance(states_data, list):
            for state in states_data:
                if isinstance(state, dict) and 'state' in state and 'abbreviation' in state:
                    if state['state'].lower() == state_name.lower():
                        return state['abbreviation']
        else:
            print("Error: The 'states' data is not in the expected format.")
    
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")

    # If no match is found, return None
    return None




def clean_up_str_usa(address, city, state, country):
    address = address.title()
    city = city.title()
    state = state.title()

    #adding the pluls in the address
    words = address.split()
    for i in range(1, len(words)):
        words[i] = '+' + words[i][0] + words[i][1:]
    almost_address = ''.join(words)

    #adding the pluls in the city
    words = city.split()
    for i in range(0, len(words)):
        words[i] = '+' + words[i][0] + words[i][1:]
    almost_city = ''.join(words)

    address_and_city =  almost_address + "," + almost_city

    #obtaining state abbreviation
    
    state_abbreviation = get_state_abbreviation(state)

    #replacing country adequately
    country = country.replace('Estados Unidos', ',+USA')
    country = country.replace('United States Of America', ',+USA')
    country = country.replace('Usa', ',+USA')
    country = country.replace('United States', ',+USA')

    #final address
    final_address = address_and_city + ",+" + state_abbreviation + country

    return final_address


def clean_up_str_spain(address, city):
    address = address.title()
    city = city.title()

    #possible typos
    address = address.replace('Calle', 'C.')
    address = address.replace('Cale', 'C.')
    address = address.replace('Paza', 'Plaza')
    address = address.replace('Avenida', 'Av.')
    address = address.replace('Aenida', 'Av.')
    address = address.replace('Aveida', 'Av.')

    #adding necessary commas 
    address = re.sub(r'(\d+)', r',\1', address)
    
    #add the plus sign before each word
    words = address.split()
    for i in range(1, len(words)):
        words[i] = '+' + words[i][0] + words[i][1:]
    almost_address = ''.join(words)
    
    #add city name into address
    cleaned_address = almost_address + ",+" + city
    
    print(cleaned_address)
    return cleaned_address


if __name__ =='__main__':
    user_interaction()

