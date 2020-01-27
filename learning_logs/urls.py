from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^topics/$', views.topics, name='topics'),
    #Strona szczegółowa dotycząca pojedynczego tematu.
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Strona przeznaczona do dodawania nowego tematu
    path(r'^new_topic/$', views.new_topic, name='new_topic'),
]