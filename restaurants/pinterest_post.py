import base64
import json
import requests
import os

class Pinterest:
    @staticmethod
    def get_access_token(token_name):
        access_token = os.getenv('PWD') + '/access_tokens.sh'
        f = open(access_token, 'r+')
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()

        return 'Not found'

    def __init__(self):
        self.access_token = Pinterest.get_access_token('PINTEREST_ACCESS_TOKEN')


# write your code below
    def publish_photo_msg(self, message, image_url):        
        URL=" https://api.pinterest.com/v1/pins/?access_token="+self.access_token
        PARAMS={
            "board":"arishh2/qeatsboard",
            "note":message,
            "image_url":image_url
        }

        r=requests.post(url=URL,params=PARAMS)
        print(str(r.json()))
        
if __name__ == '__main__':
    pinterest= Pinterest()
    
    image_url = 'https://assetsds.cdnedge.bluemix.net/sites/default/files/styles/very_big_1/public/feature/images/ice_cream_1.jpg'
    message='Finally published pin !'
    pinterest.publish_photo_msg(message, image_url)

