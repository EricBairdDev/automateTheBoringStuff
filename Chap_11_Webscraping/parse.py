import requests
import os
from bs4 import BeautifulSoup

# Make a directory for the images, if one does not already exist
if not os.path.exists('xkcd'):
    os.makedirs('xkcd')

# Start with the first comic
url = 'https://xkcd.com/1'

while not url.endswith('#'):
    # Download the page
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        # Download the image
        print(f'Downloading image {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()

        # Save the image to ./xkcd
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # Get the Prev button's url
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')

print('Done.')
