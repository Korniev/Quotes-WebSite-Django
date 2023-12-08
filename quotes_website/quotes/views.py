from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm
from .utils import get_mongo_db
from .models import Author, Quote


# Create your views here.


def main(request, page=1):
    db = get_mongo_db()
    quotes = db.quotes.find().sort("created_at", -1)
    per_page = 10
    paginator = Paginator(list(quotes), per_page=per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


@login_required
def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            # Зберігаємо автора в базі даних Django
            new_author = author_form.save()

            # Додавання цитати
            quote_text = author_form.cleaned_data['quote']
            if quote_text:
                # Створення нової цитати зі збереженим автором
                new_quote = Quote(quote=quote_text, author=new_author)
                new_quote.save()
                # Додавання тегів до цитати
                for tag in author_form.cleaned_data['tags']:
                    new_quote.tags.add(tag)
                new_quote.save()

                # Тут додаємо автора та цитату в MongoDB
                db = get_mongo_db()
                author_data = {
                    'fullname': new_author.fullname,
                    'born_date': new_author.born_date,
                    'born_location': new_author.born_location,
                    'description': new_author.description
                }
                db.authors.insert_one(author_data)
                db.quotes.insert_one({'quote': quote_text, 'author': author_data})

            return redirect('quotes:root')
    else:
        author_form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': author_form})


