#1.Parsing RSS Feeds
import feedparser

def parse_rss_feed(rss_url):
    feed = feedparser.parse(rss_url)
    urls = [entry.link for entry in feed.entries]
    return urls

#2.Extracting Article Information using newspaper3k
from newspaper import Article

def scrape_article(url):
    article = Article(url)
    article.download()
    article.parse()
    
    article_info = {
        'title': article.title,
        'author': article.authors,
        'publish_date': article.publish_date,
        'content': article.text
    }
    return article_info

#3.Combining the Parsing and Scraping Functions
def scrape_rss_articles(rss_url):
    # Parse RSS feed and get article URLs
    article_urls = parse_rss_feed(rss_url)
    
    # Scrape each article and store information
    articles_info = []
    for url in article_urls:
        try:
            article_info = scrape_article(url)
            articles_info.append(article_info)
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
    
    return articles_info


#4.Test with Multiple RSS Feeds
rss_feeds = [
    'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'https://feeds.bbci.co.uk/news/world/rss.xml',
]

for rss_feed in rss_feeds:
    articles = scrape_rss_articles(rss_feed)
    for article in articles:
        print(article)
