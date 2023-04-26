#!/usr/bin/python3

import argparse
from remix import Remix


parser = argparse.ArgumentParser(prog='Renix',
    description='Mix two images: python3 run.py /path/to/image1.jpg /path/to/image2.jpg',
    epilog='Send me an offer, please))')
 
parser.add_argument('images', type=str, nargs='*',
    default=['assets/lord_of_the_rings_meme.jpg', 'assets/mike_wazowski_meme.jpg'],
    help='list of /path/to/image.jpg')


if __name__ == "__main__":
    args = parser.parse_args()
    assert len(args.images) == 2, args.images
    remix = Remix(device='cuda')
    image = remix(*args.images)
    image.save(f'mixed.jpg')
