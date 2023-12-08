import requests 
import os
import os.path
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint

def get_spacex_img(img_folder_path):
    url = "https://api.spacexdata.com/v3/launches"

    response = requests.get(url)
    response = response.json()
    

    for launch in reversed(response):
        
        links_img = launch["links"]['flickr_images']
        
        if links_img != []:
            for number, link_img  in enumerate(links_img, 1):
                response = requests.get(link_img)
                path_SpaceX_img = Path(img_folder_path, f'spacex_{number}.jpeg')
                launch_date = launch["launch_date_local"] 
                with open(path_SpaceX_img, "wb") as file:
                    file.write(response.content)
            text = f'Запуск ракеты SpaceX.Совершен {launch_date}'
            return text
    