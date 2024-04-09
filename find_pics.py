import os
import requests
from bs4 import BeautifulSoup
import re
import time

def download_image(url, folder_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder_path, os.path.basename(url)), 'wb') as f:
                f.write(response.content)
                print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url} - Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to download: {url} - Exception: {str(e)}")

def scrape_pinterest_images(board_url, download_path):
    try:
        response = requests.get(board_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all pins on the board
        pins = soup.find_all('img', {'class': 'hCL kVc L4E MIw'})

        # Extract image URLs from the pins
        for pin in pins:
            image_url = pin['src']
            download_image(image_url, download_path)
            time.sleep(1)  # Add a small delay to avoid overloading the server

    except Exception as e:
        print(f"Failed to scrape Pinterest board: {str(e)}")

if __name__ == "__main__":
    # URL of the Pinterest board to scrape
    pinterest_board_url = "https://www.pinterest.com/bungalow8omaha/mens-fashion-inspiration/"
    
    # Directory to save downloaded images
    download_directory = "pinterest_images"

    # Create the download directory if it doesn't exist
    os.makedirs(download_directory, exist_ok=True)

    # Scrape images from Pinterest board
    scrape_pinterest_images(pinterest_board_url, download_directory)
