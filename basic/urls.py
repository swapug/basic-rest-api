from django.urls import path
from basic import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
