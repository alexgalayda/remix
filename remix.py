from PIL import Image
from transformers import pipeline
from diffusers import StableDiffusionImg2ImgPipeline

from utils import read_image, IMG_TO_TEXT, IMG_TO_IMG


class Remix:
    def __init__(self, device: str='cuda'):
        self.image_to_text = pipeline("image-to-text", model=IMG_TO_TEXT)
        self.device = device
        self.image_to_image = StableDiffusionImg2ImgPipeline.from_pretrained(IMG_TO_IMG)
        self.image_to_image = self.image_to_image.to(self.device)

    def __call__(self, name1: str, name2: str) -> Image:
        image_major = read_image(name1)
        image_minor = read_image(name2)
        prompt = self.get_prompt(img_context=image_major, img_style=image_minor)
        init_image = image_major.resize((768, 512))
        image = self.image_to_image(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images[0]        
        return image

    def get_prompt(self, img_context: Image, img_style: Image) -> str:
        context = self.image_to_text(img_context)[0]['generated_text']
        style = self.image_to_text(img_style)[0]['generated_text']
        return f'context: {context}, style: {style}'
