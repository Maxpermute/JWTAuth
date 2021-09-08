
from django.contrib import admin
from django.urls import path, include
from . import views # . -> pwd, views.py(import)
# from rest_fromwork.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

# router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path("", include('users.urls')),
    #path("", include('chat.urls')),
    # path("", include('To_Do.urls')),
    # path("", views.index),  # "" -> domain
    # path("home/", views.home),    #path(url, func_name)
    # path("", include('users.urls')),

]
