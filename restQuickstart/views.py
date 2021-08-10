from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response

from polls.models import Question
from restQuickstart.serializers import UserSerializer, GroupSerializer
from .serializers import QuestionSerializer


class UserViewSet(viewsets.ModelViewSet): #View Sets stat einzelne views zusammen zu gruppieren
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Dekoratoren sind metaprogrammierung, sie verändern/verbessern die Aktion der Funktion, welche sie dekorieren. apiview gibt hier an, dass nur auf Get geantwortet werden soll, der renderer gibt an wie Jsons gerendert werden sollen.
@api_view(('GET',)) #Gibt an worauf das View antwortet. Hier nur get, bei Post würde 405 Method not allowed zurückgegeben werden.
@renderer_classes((JSONRenderer,)) #DA MUSS EIN KOMMA HIN! Einfach nur JSONRenderer geht nicht! Da es sich um Tupel handelt. Könnte aber auch ohne Komma in [] übergeben werden.
def questionList(request): # Json Listen werden durch [] begrenzt
    #questions = Question.objects.get(pk=1)
    questions = Question.objects.all() # gibt ein Queryset zurück geht seltsamerweise auch ohne all()
    serializer = QuestionSerializer(questions, many=True) #Many muss auf False gesetzt werden oder falls alle (oder mehrere) Questions übergeben werden auf True.
    return Response(serializer.data)
