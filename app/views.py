from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request): 
     context ={}
     return render(request, "index.html", context)

def cart(request): 
     context ={}
     return render(request, "cart.html", context)

def checkout(request): 
     context ={}
     return render(request, "checkout.html", context)

def shop_grid(request): 
     context ={}
     return render(request, "shop-grid.html", context)

def contact(request): 
     context ={}
     return render(request, "contact.html", context)