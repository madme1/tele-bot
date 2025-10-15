import requests
from bs4 import BeautifulSoup
from config.logger import logger

def fetch_latest_indianexpress_news(limit=5):
    url = "https://indianexpress.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        latest_news_div = soup.find('div', id='HP_LATEST_NEWS')
        if not latest_news_div:
            logger.warning("Latest news section not found")
            return []

        articles = latest_news_div.find_all('div', class_='other-article')

        news_items = []
        for article in articles[:limit]:
            try:
                headline_tag = article.find('h3')
                if headline_tag:
                    link_tag = headline_tag.find('a', href=True)
                    headline_text = link_tag.get_text(strip=True) if link_tag else "No headline found"
                    link_url = link_tag['href'] if link_tag else "No link found"

                    # Make link absolute if needed
                    if link_url.startswith("//"):
                        link_url = "https:" + link_url
                    elif link_url.startswith("/"):
                        link_url = "https://indianexpress.com" + link_url

                    news_items.append(f"📰 {headline_text}\n🔗 {link_url}")
                else:
                    logger.warning("No headline tag found in article")
            except Exception as e:
                logger.warning(f"Error processing article: {e}")

        return news_items

    except Exception as e:
        logger.error(f"Failed to fetch latest Indian Express news: {e}")
        return []
