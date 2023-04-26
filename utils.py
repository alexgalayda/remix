from pathlib import Path
from PIL import Image


__all__ = ['read_image', 'IMG_TO_TEXT', 'IMG_TO_IMG']

def read_image(name: str|Path) -> Image:
    name = Path(name).absolute()
    image = Image.open(name).convert("RGB")
    return image

image_to_text_weight = [
    'nlpconnect/vit-gpt2-image-captioning',
    'Salesforce/blip-image-captioning-base',
    'Salesforce/blip-image-captioning-large',
]

text_to_image_weight = [
    'CompVis/stable-diffusion-v1-4',
    'runwayml/stable-diffusion-v1-5',
    'stabilityai/stable-diffusion-2-base',
    'stabilityai/stable-diffusion-2',
    'stabilityai/stable-diffusion-2-1-base',
    'stabilityai/stable-diffusion-2-1',
]

IMG_TO_TEXT = image_to_text_weight[-1]

IMG_TO_IMG = text_to_image_weight[-1]
