from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.ProfileFeedItemViewSet)

urlpatterns=[
    url(r'^hello_apiview',views.HelloAPIView.as_view()),
    url(r'',include(router.urls)),
]
