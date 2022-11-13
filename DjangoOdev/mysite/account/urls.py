from django.urls import path
from . import views
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/home
#http://127.0.0.1:8000/enaccount
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/


urlpatterns = [

    path("", views.home),
    path("home", views.home),
    path("enaccount", views.enaccount)



    ]