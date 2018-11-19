
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.urls import path
from . import views
from . import CCA

urlpatterns = [
    url(r'^$', views.home),
]

urlpatterns = [
    url(r'^$', views.home),
                  # ex: /polls/
                  path('', views.index, name='index'),
                  # ex: /polls/5/
                path('<str:question_id>/chatview/', CCA.get_flightresults, name='get_flightresults'),
                  # ex: /polls/5/results/
                  path('<str:question_id>/results/', views.results, name='results'),
                  # ex: /polls/5/vote/
                  path('<str:question_id>/vote/', views.vote, name='vote')
              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)