from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from websitesscraper_app.models import links


# Create your views here.
def home(request):
    if request.method=='POST':
        link_new=request.POST.get('page','')
        urls = requests.get(link_new)
        # urls = requests.get("http://www.google.com")
        beautysoup = BeautifulSoup(urls.text, 'html.parser')
    # address = []
        for link in beautysoup.find_all('a'):
        #address.append(link.get('href'))
            li_address=link.get('href')
            li_name=link.string
            links.objects.create(address=li_address,string_name=li_name)
        return HttpResponseRedirect('/')
    else:
        data_values = links.objects.all()

    return render(request, 'home.html', {'data_values': data_values})

