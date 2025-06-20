from django.shortcuts import render
from core.models import Course

def course_list(request):
  courses = Course.objects.all()
  return render(request, 'course_list.html', {'course': courses})

# Create your views here.
