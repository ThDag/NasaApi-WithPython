# TODO: use other functions of the api like cordinate image generator, nasa image galery, EPIC
import requests
from PIL import Image 
import urllib.request
import json

def apod():
    response = requests.request('GET', 'https://api.nasa.gov/planetary/apod?api_key=QMoyyZB2PMUVGv6VOSCYT2b8xxe9fKVgDXTB8X0j')
    urllib.request.urlretrieve(response.json()['url'], 'potd.jpg')
    img = Image.open('potd.jpg')
    img.show()

Criosity_cameras = {0: 'fhaz',
                    1: 'rhaz',
                    2: 'mast',
                    3: 'chemcam',
                    4: 'mahli',
                    5: 'mardi',
                    6: 'navcam'}

class Criosity:
    def __init__(self, camera: int, date: str, page: int):
        self.camera = Criosity_cameras.get(camera)
        self.date = date
        self.page = str(page)
        parametres = {'earth_date': self.date,'camera': self.camera,'page': self.page, 'api_key': 'QMoyyZB2PMUVGv6VOSCYT2b8xxe9fKVgDXTB8X0j'}
        self.response = requests.request('GET',params=parametres, url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos')
    

    def image_number(self):
        return len(self.response.json()['photos'])


    def show_image(self, image_idx: int):
        # print(json.dumps(parametres, indent=2))
        # response = requests.request('GET', url, params=parametres) 
        # print(response)

        image_data = self.response.json()['photos'][image_idx]
        # print(json.dumps(image_data, indent=2))

        image_url = image_data['img_src']
        # TODO: show the image
        return image_url     

rover = Criosity(camera=2, date='2022-03-23', page=1)

print('humber of images in the page: ',  rover.image_number())
print(rover.show_image(0))

