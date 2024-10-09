from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import taskViewSet
from . import views

router = DefaultRouter()
router.register(r'task', taskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('registro/', views.SignUP.as_view(), name="SignUP")
] 


