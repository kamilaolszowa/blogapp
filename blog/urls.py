from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from pprint import pprint

admin.site.site_header = 'Blog Admin'
router = SimpleRouter()
router.register('posts', views.PostViewSet),
router.register('bloggers', views.BloggerViewSet)

urlpatterns = urlpatterns = router.urls
