import os
from Nasa import get_nasa_img
from SpaceX import get_spacex_img
from dotenv import load_dotenv




if __name__ == '__main__':
    load_dotenv()
    api_token = os.getenv('A')