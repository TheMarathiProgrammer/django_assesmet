from django.urls import path
from .views import BooksListView,CreateBooks,UpdateBook,DeleteBook,RegisterUser,LoginUser
from rest_framework.authtoken import views as auth
urlpatterns = [
    path('',BooksListView.as_view()),
    path('create_book/',CreateBooks.as_view()),
    path('update_book/<int:id>',UpdateBook.as_view()),
    path('delete_book/<int:id>',DeleteBook.as_view()),
    path('register_user/',RegisterUser.as_view()),
    path('login_user/',LoginUser.as_view()),
]