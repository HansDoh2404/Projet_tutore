from django.urls import path
from . import views

app_name = 'admin_biblio'

urlpatterns = [
    path('', views.index, name="index"),
    path('author/', views.author, name="author"),
    path('authors/', views.authors, name="authors"),
    path('book/<int:bookid>', views.book, name="book"),
    path('books/', views.books, name="books"),
    path('editor/', views.editor, name="editor"),
    path('editors/', views.editors, name="editors"),
    path('formats/', views.formats, name="formats"),
    path('genres/', views.genres, name="genres"),
    path('valid/<str:bookid>/<str:userid>', views.book_valid, name='book_valid'),
    path('reviews/', views.reviews, name="reviews"),
]
