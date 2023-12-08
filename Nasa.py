import requests 
import pathlib
import os
import os.path
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint


def get_nasa_img(img_folder_path):
    api_token = os.getenv('A')

    url_nasa   = 'https://api.nasa.gov/planetary/apod'
    
    params = {
        'count': 3,
        'hd':'True',
        'api_key': api_token
    }

    response = requests.get(url_nasa, params=params)
    response = response.json()
  
    for number, img in enumerate (response, 1):
        nasa_apod_path = Path(img_folder_path, f'nasa_apod_{number}.jpeg') 
        response = requests.get(img['url'])
        with open(nasa_apod_path, "wb") as file:
            file.write(response.content)
    text = 'Картинка дня от Nasa'
    return text 
