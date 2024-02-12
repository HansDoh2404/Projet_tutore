from django.shortcuts import render, redirect, get_object_or_404
from .forms import WriterForm, CategoryForm, BooksForm
from django.contrib.auth.models import User
from store.models import Category, Book, History

import datetime
import time
import locale

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
# Create your views here.

def index(request):
    notif_list = History.objects.all()
    context = {
       "notif_list" : notif_list
    }
    return render(request, 'admin_biblio/index.html', context)

def author(request):
    return render(request, 'admin_biblio/author.html')

def authors(request):
    form = WriterForm()
    context = {'form' : form}
    if request.method == 'POST' :
        form = WriterForm(request.POST)
        form.save()
    return render(request, 'admin_biblio/authors.html', context = context)

def book(request, bookid):
    book = Book.objects.get(id = bookid)
    context = {
        'book' : book
    }
    return render(request, 'admin_biblio/book.html', context = context)

def books(request):
    all_book = Book.objects.all()
    form = BooksForm()
    context = {'form' : form, 'all_book' : all_book}
    if request.method == 'POST' :
        form = BooksForm(request.POST, request.FILES)
        form.save() 
    return render(request, 'admin_biblio/books.html', context = context)

def editor(request):
    return render(request, 'admin_biblio/editor.html')

def editors(request):
    return render(request, 'admin_biblio/editors.html', context = context)

def formats(request):
    return render(request, 'admin_biblio/formats.html')

def genres(request):
    form = CategoryForm()
    context = {'form' : form}
    cat = Category.objects.create(name=form.fields['name'])
    cat.save()
    return render(request, 'admin_biblio/genres.html', context = context)

def reviews(request):
    return render(request, 'admin_biblio/reviews.html')

def book_valid(request, bookid, userid):
    b = get_object_or_404(Book, name=bookid)
    u = User.objects.get(username=userid)
    h = get_object_or_404(History, book_id=b.id, user_id = u.id)
    h.status = 'Accepté'
    h.created = datetime.datetime.now()
    h.updated = h.created + datetime.timedelta(days=15)
    h.save()
    return render(request, 'admin_biblio/index.html')