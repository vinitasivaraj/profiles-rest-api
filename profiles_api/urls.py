from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('helloViewset',views.HelloViewset,basename='helloViewset'),
router.register('profile',views.UserProfileviewset)


urlpatterns = [
    path("hello/",views.HelooApi.as_view()),
    path('login/',views.UserloginApiView.as_view()),
    path('',include(router.urls)),
]