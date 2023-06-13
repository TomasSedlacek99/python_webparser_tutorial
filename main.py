from urllib.request import urlopen
from bs4 import  BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/profiles"
page = browser.get(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")
for link in links:
    link_url = url + link["href"]
    print(link_url)

