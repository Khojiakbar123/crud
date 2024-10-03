from django.urls import path

from book_api.views import book_list, book_detail

urlpatterns = [
    path('',book_list),
    path('<int:pk>/',book_detail)
]