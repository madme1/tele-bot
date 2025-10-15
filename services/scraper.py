import requests
from bs4 import BeautifulSoup
from config.logger import logger

def fetch_top_ai_news(limit=5):
    url = "https://indianexpress.com/section/technology/artificial-intelligence/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='area-row')

        news_items = []
        for article in articles[:limit]:
            try:
                time_tag = article.find('time', class_='time-stamp')
                time_text = time_tag.get_text(strip=True) if time_tag else "No time found"

                headline_tag = article.find('h2', class_='list-heading')
                if headline_tag:
                    # Get headline text
                    headline_text = headline_tag.get_text(strip=True)

                    # Find the parent <a> tag of the headline to get the full article link
                    link_tag = headline_tag.find_parent('a', href=True)
                    link_url = link_tag['href'] if link_tag else "No link found"
                else:
                    headline_text = "No headline found"
                    link_url = "No link found"

                news_items.append(f"🕒 {time_text}\n📰 {headline_text}\n🔗 {link_url}")
            except Exception as e:
                logger.warning(f"Error processing article: {e}")

        return news_items

    except Exception as e:
        logger.error(f"Failed to fetch AI news: {e}")
        return []
