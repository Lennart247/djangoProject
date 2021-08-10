from django.urls import include, path
from rest_framework import routers
from restQuickstart import views

router = routers.DefaultRouter() #Irgendwie cooler für die Views
router.register(r'users', views.UserViewSet) # r' wird für raw Strings benutzt. See Python Reference for String literals
router.register(r'groups', views.GroupViewSet)
#router.register(r'questions', views.questionList, basename='questions')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('questions/', views.questionList, name='questionList'),
    path('api-auth/', include('rest_framework.urls', namespace='sub_rest_framework')) # Wenns auskommentiert wird ist es Unique sonst nicht
]