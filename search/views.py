import requests
import html5lib
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def search(request):
    if request.method == 'POST':
        products = request.POST['search']
        url = 'https://www.flipkart.com/search?q=' + products + '&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html5lib")
        link = soup.findAll("div", {'class': '_3O0U0u'})
        product = {}

        for links in link:
            title = links.find("div", {"class": "_3wU53n"})
            title_name = title.text
            cost = links.find("div", {"class": "_2rQ-NK"})
            cost_price = cost.text
            product[title_name] = cost_price

        return render(request, "result.html", {'product': product})


