from django.urls import path, include
from .views import UserViewSet , customUserRegister ,custom_user_login
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
   
    path('', include(router.urls)),
    path('users/register',view = customUserRegister,  name='user_register'),
    path('users/login',view = custom_user_login, name='custom_user_login'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)