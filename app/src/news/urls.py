from django.urls import path
from .views import news_list, add_news, read_news, add_comment


urlpatterns = [
    path('', news_list, name='news_list'),
    path('add/', add_news, name='add_news'),
    path('<int:news_id>/', read_news, name='read_news'),
    path('<int:news_id>/add_comment/', add_comment, name="add_comment")
]
