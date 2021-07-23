from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MobilList.as_view()),
    path('<int:pk>', views.MobilDetail.as_view()),
]