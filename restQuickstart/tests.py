from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory

# Create your tests here.
from polls.models import Question
from restQuickstart.views import questionList

currentTime = timezone.now()

class RestTests(TestCase):



    @classmethod
    def setUpTestData(cls): #cls ist das selbe wie self. Wird manchmal bei Class methoden genutzt
        global currentTime
        question = Question.objects.create(question_text="TestFrage", pub_date=currentTime)
        question.save()

    def testApi(self):
        global currentTime
        factory = APIRequestFactory()
        request = factory.get('/api/questions/')
        response = questionList(request)
        self.assertEqual(response.status_code, 200)
        data = response.data
        response.render()
        print(response.content.decode()) # Eckige Klammern unten, weil es als Liste zurückgegeben wird.
        self.assertJSONEqual(response.content.decode(),[{'id':1,"question_text":"TestFrage","pub_date":"%s" % currentTime.astimezone(tz=timezone.get_current_timezone()).isoformat()}])
        #self.assertEqual(set(data.keys()), set(['id', 'question_text', 'pub_date']))
