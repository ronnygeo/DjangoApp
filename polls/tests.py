import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question, Choice
from django.core.urlresolvers import reverse

# Create your tests here.
class QuestionMethodTests(TestCase):

    def test_was_published_today(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_q = Question(pub_date=time)

        self.assertNotEqual(future_q.pub_date, timezone.now())

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date=time)

class QuestionViewTests(TestCase):
    def test_index_view_with_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['questions'], [])