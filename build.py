import os
import markdown
import bs4
from bs4 import BeautifulSoup

with open("content.md", "r") as file:
    md = file.read()
    md_html = markdown.markdown(md)

with open("index.html", "r+") as file:
    soup = BeautifulSoup(file, "html.parser")
    md_soup = BeautifulSoup(md_html, "html.parser")    

    main = soup.find(string=lambda text: type(text) == bs4.element.Comment)
    main.parent.append(md_soup)

    file.seek(0)
    file.truncate(0)
    file.write(soup.prettify())