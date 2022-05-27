from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_books/', views.all_books, name='all_books'),
    path('book/<int:book_id>/', views.book_detail, name='book'),
    path('review/<int:book_id>/', views.book_review, name='review'),
]
