# Remix
Analog Midjourney Remix

## Usage

Run
```
python3 run.py /home/username/image1.jpg /home/username/image2.jpg
```

Or in docker

```
docker build -t remix/torch -f Dockerfile .
docker run --rm -it --gpus all --name remix remix/torch
```

## Research

Of all the possible approaches, those based on stable diffusion were chosen, as they are the most relevant.

Let's take two pictures for testing.

![test_image1](assets/lord_of_the_rings_meme.jpg)
![test_image2](assets/mike_wazowski_meme.jpg )

### Image To Image

In the beginning, we tested a [solution](https://github.com/justinpinkney/stable-diffusion) that directly blends the image.
The result is funny, but not satisfactory.
Replacing encoders and varying ways to add context to the diffusion model did not work.

![img2img_result](assets/gollum.jpg)

### Swap text encoder to image encoder

The next attempt was to replace the encoder in the variator.

```
from diffusers import StableDiffusionImageVariationPipeline as SDIV
from diffusers import StableDiffusionImg2ImgPipeline as SDI2I

SDI2I._encode_prompt -> SDIV._encode_image

```
Despite all efforts, various attempts to substitute visual embedding instead of text embedding have failed.
It was not possible to create even meaningful images

### Img To Text + Text To Image

In the end, it was decided to use an already well-trained [Img2Img Stable Diffusion](https://huggingface.co/docs/diffusers/main/en/api/pipelines/stable_diffusion/img2img).
And generate prompt from images using Image To Text [Transformers](https://huggingface.co/tasks/image-to-text)

![img2text2img_result](assets/mixed.jpg)

The result is satisfactory. Further improvement requires more computing power and more time.

