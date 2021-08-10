from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/
    # path('', views.index, name='index'), #path(route,view,kwargs,name) last two are optional. if pattern matches it calls the specified view function with an HttpRequest object.
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'), # ruft entsprechend views.vote(question_id=<int:question_id>) auf da int:question_id, dies gibt den entsprechend benannten parameter an
]