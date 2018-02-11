from django.test import TestCase
from django.utils import timezone
# Create your tests here.
from .models import Course

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title = 'python regular expressions',
            description = 'learn to write python  regular expressions',
        )
        now = timezone.now()
        self.assertLess(course.created_at,now)
