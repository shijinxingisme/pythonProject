import json
import base64

import requests


def submit_post(url: str, data: dict):
    """
    Submit a POST request to the given URL with the given data.
    """
    return requests.post(url, data=json.dumps(data))


def save_encoded_image(b64_image: str, output_path: str):
    """
    Save the given image to the given output path.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))


if __name__ == '__main__':
    txt2img_url = 'http://8.140.21.51:7860/sdapi/v1/txt2img'
    data = {'prompt': 'Nikon RAW photo,8 k,Fujifilm XT3,masterpiece, best quality, realistic, photorealistic,ultra detailed,1girl,solo, close up portrait, standing, fashionable and trendy atmosphere, walk-in closet, designer clothing and accessories, saika1, <lora:saika___v3:1>'}
    response = submit_post(txt2img_url, data)
    save_encoded_image(response.json()['images'][0], 'dmeinv.png')