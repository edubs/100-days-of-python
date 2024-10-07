import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    a_tag = article_tag.find('a')
    text = article_tag.getText()
    article_texts.append(text)
    link = a_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts[article_upvotes.index(max(article_upvotes))])
print(article_links[article_upvotes.index(max(article_upvotes))])
print(article_upvotes[article_upvotes.index(max(article_upvotes))])

print(article_upvotes.index(max(article_upvotes)))

# for span in titleline_spans:
#     a_tag = span.find("a")
#     print(a_tag.getText())

# import lxml # (if the html parser isn't working)

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
#
# # get the text from all anchor tags
# for tag in all_anchor_tags:
#     print(tag.getText())
#
# # get hrefs from all ancho tags
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.get("class"))

# # find the first instance matching css selector a tag inside p tag
# company_url = soup.select_one(selector="p a")
# print(company_url)
# print(soup.select_one("#name"))
# # get objects with a class of heading (css selector)
# print(soup.select(".heading"))
