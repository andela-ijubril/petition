from django.conf.urls import url
from petition import views

urlpatterns = [
    url(r'petitions/$', views.PetitionList.as_view()),
    # url(r'^', include('petition.urls')),
]


