from django.urls import path
from . import views

urlpatterns = [
    path('', views.typingmaster_home),
    path('start', views.test_page),
    path('collect', views.collect_results),
    path('results', views.test_results),
    path('halloffame', views.hall_of_fame),
    path('logout', views.logout)
]