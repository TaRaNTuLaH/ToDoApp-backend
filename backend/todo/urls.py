from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from todo import todos


router = routers.SimpleRouter(trailing_slash=False)
router.register(r"todos", todos.TodoViewSet, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
