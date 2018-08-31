from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^hello_apiview',views.HelloAPIView.as_view()),
]
