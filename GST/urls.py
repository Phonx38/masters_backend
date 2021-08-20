from django.urls import path
from . import views

urlpatterns = [
    path("gstinfo/", views.GSTList.as_view()),
    path("gstinfo/<str:pk>", views.GSTDetail.as_view()),
]
