from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'account', views.AccountView)
router.register(r'images', views.ImageView,basename='Image')
router.register(r'thumbnail', views.ThumbnailView,basename='Thumbnail')
#router.register(r'account', views.AccountView)
#router.register(r'account', views.AccountView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]