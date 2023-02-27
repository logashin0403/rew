from django.urls import path
from .views import add_message, grounds_list


urlpatterns = [
    path('<str:sport_type>/', grounds_list, name='grounds_list'),
    path('<str:sport_type>/<int:ground_id>/add_message/', add_message, name="add_message"),

]