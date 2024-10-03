from django.urls import path, include
from rest_framework import routers

from todo.views import ToDoViewSet


router = routers.DefaultRouter()
router.register(r'todo', ToDoViewSet)


urlpatterns = [
    path('', include(router.urls))
]
