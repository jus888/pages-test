#!/usr/bin/python3

import os
import markdown
import bs4
from bs4 import BeautifulSoup

with open("content.md", "r") as file:
    text = file.read()
    md = markdown.Markdown(extensions = ['meta'])    
    md_html = md.convert(text)
    meta = md.Meta
    print(meta['items'])

with open("index.html", "r+") as file:
    soup = BeautifulSoup(file, "html.parser")
    md_soup = BeautifulSoup(md_html, "html.parser")    

    comments = soup.find_all(string=lambda text: type(text) == bs4.element.Comment)
    for comment in comments:
        comment_string = comment.string.strip()
        parent = comment.parent
        parent.clear()        

        if comment_string == "Main":
            parent.append(md_soup)

        elif comment_string == "Title":
            parent.append(f"{meta['title'][0]}")

    file.seek(0)
    file.truncate(0)
    file.write(soup.prettify())