from django.shortcuts import render
from .utils import get_mongo_db
# Create your views here.


def main(request):
    db = get_mongo_db()
    quotes = db.quotes.find()
    return render(request, 'quotes/index.html', context={'quotes': quotes})
