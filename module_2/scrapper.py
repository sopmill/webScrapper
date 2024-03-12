"""
Module: scrapper.py

SOLID Principle: Single Responsibility Principle (SRP)
- The single responsibility of this module is to download content from a URL. Because this is the function, it makes maintenance and reusability easier. 

Description:
This module contains functions to scrape article content from HTML using BeautifulSoup.

Input:
HTML content.

Output:
- Processed article text.
"""

from bs4 import BeautifulSoup

def scrape_article(html_content):
    """
    Function to scrape the news article content from HTML.

    Input:
    - html_content: HTML content of the webpage.

    Output:
    - Processed article text.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        article_body = soup.find('div', class_='article__content')
        if article_body:
            article_content = article_body.get_text()
            return article_content
        else:
            print("Unable to find article content on the page.")
            return None
    except Exception as e:
        print(f"Error occurred while scraping the article: {str(e)}")
        return None
