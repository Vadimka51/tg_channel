import os
import telegram
import pathlib
import time
from pathlib import Path
from Nasa import get_nasa_img
from SpaceX import get_spacex_img
from dotenv import load_dotenv
from pprint import pprint
from random import choice



def choosing_random_img(img_folder_path):
    list_img = os.listdir(img_folder_path) 
    random_path = Path(img_folder_path, choice(list_img))
    return random_path


def send_photo(random_path,text):
    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo = open(random_path,"rb") ,caption = text )


def delete_files_in_folder(img_folder_path):
    for filename in os.listdir(img_folder_path):
        file_path = os.path.join(img_folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')


if __name__ == '__main__':


    load_dotenv()


    api_token_nasa = os.getenv('A')
    TELEGRAM_BOT_TOKEN = os.getenv('B')
    TELEGRAM_CHAT_ID = '6541125634'
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    
    dir_path = pathlib.Path.cwd()
    img_folder_path = Path(dir_path, 'imgxn')

    if not os.path.exists(img_folder_path):
        os.makedirs(img_folder_path)

    while True:   
        func = choice([get_spacex_img, get_nasa_img])
        text = func(img_folder_path)
        random_path = choosing_random_img(img_folder_path)
        
        
        send_photo(random_path,text) 
        delete_files_in_folder(img_folder_path)

        time.sleep(7)
