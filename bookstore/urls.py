from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('items/', BookListCreateView.as_view(), name='book-list-create'),
    path('items/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
