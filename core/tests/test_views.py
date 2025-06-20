from django.test import TestCase
from django.urls import reverse
from core.models import Course
from django.contrib.auth.models import User

class CourseViewTest(TestCase):

    def setUp(self):
        # Menyiapkan data untuk pengujian
        Course.objects.create(name="Django for Beginners", description="Learn Django from Scratch", price=100)
        Course.objects.create(name="Advanced Django", description="Deep Dive into Django", price=200)

    def test_course_list_view(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response, 'course_list.html')
        self.assertContains(response, "Django for Beginners")
        self.assertContains(response, "Advanced Django")
