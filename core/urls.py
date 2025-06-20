from django.urls import path
from core.views import course_list

urlpatterns = [
  path('courses/', course_list, name='course_list'),
]