from django.urls import path
from rest_framework import routers
from .import views

router= routers.DefaultRouter(trailing_slash=False)
router.register('employees', views.EmployeeViewset, basename='employees')


urlpatterns = router.urls