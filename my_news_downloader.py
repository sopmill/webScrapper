import requests
from bs4 import BeautifulSoup
import os

# Function to download the content of a URL
def download_content(url):
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

# Function to scrape the news article content from HTML
def scrape_article(html_content):
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


# Main function to process each URL from the text file
def process_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            url = line.strip()
            html_content = download_content(url)
            if html_content:
                article_text = scrape_article(html_content)
                if article_text:
                    save_article(article_text)

# Function to save the scraped article content to a file
def save_article(content):
    if not os.path.exists('articles'):
        os.makedirs('articles')
    
    file_name = f"article_{len(os.listdir('articles')) + 1}.txt"
    with open(os.path.join('articles', file_name), 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Article saved to {file_name}")

# Main function
def main():
    file_path = 'page.txt'
    process_urls_from_file(file_path)

if __name__ == "__main__":
    main()
