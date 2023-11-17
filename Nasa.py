import requests 
import pathlib
import os
import os.path
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint


def get_nasa_img(api_token):
#возращфет ссылки на картинки
    

    url_nasa   = 'https://api.nasa.gov/planetary/apod'
    
    directory = "nasa_apod"
    dir_path = pathlib.Path.cwd()
     

    params = {
        'count': 10,
        'hd':'True',
        'api_key': api_token
    }

    response = requests.get(url_nasa, params=params)
    response = response.json()
    
    count = 0
    path = Path(dir_path,'nasa_apod')

    if not os.path.exists(path):
        os.makedirs(path)  

    for i in response:
        count += 1
        path = Path(dir_path,'nasa_apod', f'nasa_apod_{count}.jpeg') 
        # response = requests.get(i['hdurl'])
        # with open(path, "wb") as file:
        #     file.write(response.content)
    

