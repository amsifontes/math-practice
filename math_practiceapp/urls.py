from django.urls import path
from . import views

urlpatterns = [
    # ex: /math_practiceapp/
    path('', views.index, name='index'),
    # ex: /math_practiceapp/5
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /math_practiceapp/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /math_practiceapp/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
