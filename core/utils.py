import requests
import random
from bs4 import BeautifulSoup as b
import numpy as np

def get_jokes():
    URL = 'https://www.anekdot.ru/last/good'
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    list_of_jokes = [c.text for c in anekdots]
    main_array = np.array(list_of_jokes)
    random.shuffle(main_array)
    return main_array[0]
    
