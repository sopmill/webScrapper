"""
Module: downloader.py

SOLID Principle: Single Responsibility Principle (SRP)
- Including SRP allows for eaiser maintainability, readability, and flexability. You can easily modify functionality of this module.  
Description:
This module is responsible for downloading content from URLs.

Input:
- URL: The URL from which content will be downloaded.

Output:
- Downloaded HTML content.
"""

import os
import requests
from module_2 import scrapper as mod2

def download_content(url):
    """
    Function to download the content of a URL.

    Input:
    - url: The URL from which content will be downloaded.

    Output:
    - Downloaded HTML content.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to download {url}")
            return None
    except Exception as e:
        print(f"Error occurred while downloading {url}: {str(e)}")
        return None

def process_and_save_content(html_content):
    """
    Function to process downloaded HTML content and save the processed content to a file.

    Input:
    - html_content: HTML content of the webpage.
    """
    article_text = mod2.scrape_article(html_content)
    if article_text:
        save_article(article_text)

def save_article(content):
    """
    Function to save the processed article content to a file.

    Input:
    - content: Processed article text.
    """
    if not os.path.exists('processed'):
        os.makedirs('processed')
    
    file_name = f"article_{len(os.listdir('processed')) + 1}.txt"
    with open(os.path.join('processed', file_name), 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Article saved to {file_name}")
