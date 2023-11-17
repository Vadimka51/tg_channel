import requests 
import pathlib
import os
import os.path
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint

def get_spacex_img():
    url = "https://api.spacexdata.com/v3/launches/73"

    payload={}
    headers = {}

    response = requests.get( url,headers=headers,data=payload)
    response = response.json()['links']['flickr_images']
    directory = "SpaceX"
    dir_path = pathlib.Path.cwd()
    count = 0
    path = Path(dir_path,'SpaceX')

    if not os.path.exists(path):
            os.makedirs(path)  
            print("Directory '% s' created" % directory)

    for i in response:
        count += 1
        response = requests.get(i)
        path = Path(dir_path,'SpaceX', f'spacex_{count}.jpeg') 
        with open(path, "wb") as file:
            file.write(response.content)

    