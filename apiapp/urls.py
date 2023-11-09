from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apiapp import views
from rest_framework.authtoken import views as auth_views


#Creating the default router
router = DefaultRouter()

# Register BookViewSet with Router
router.register('bookapi', views.BookViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
]


