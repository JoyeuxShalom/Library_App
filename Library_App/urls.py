from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('issue_book/', views.issue_book, name='issue_book'),
]
