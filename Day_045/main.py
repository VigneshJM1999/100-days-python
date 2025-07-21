from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
title_spans = soup.find_all("span", class_="titleline")
anchor_tags = [span.find("a") for span in title_spans]
article_text = [anchor.get_text() for anchor in anchor_tags]
article_link = [anchor.get("href") for anchor in anchor_tags]
article_upvote_tag = soup.find_all("span", class_="score")
article_upvote = [int(article.get_text().split()[0]) for article in article_upvote_tag]

print(f"{article_text}\n{article_link}\n{article_upvote}")
