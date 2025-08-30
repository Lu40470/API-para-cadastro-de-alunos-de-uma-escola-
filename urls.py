from django.urls import path, include
from .views import cursoAPIView, cursosAPIView,AvaliaçãoAPIView,AvaliaçõesAPIView,CursoViewSet,AvaliaçãoViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos',CursoViewSet)
router.register('avaliações',AvaliaçãoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

"""urlpatterns = [
path('cursos/', cursosAPIView.as_view(),name = 'cursos'), 
path('cursos/<int:pk>/', cursoAPIView.as_view(),name = 'curso'),
path('cursos/<int:cursos_pk>/avaliações', AvaliaçõesAPIView.as_view(),name = 'curso_avaliações'),
path('cursos/<int:cursos_pk>/avaliações/<int:avaliação_pk>', AvaliaçãoAPIView.as_view(),name = 'curso_avaliação'),
path('avaliações/', AvaliaçõesAPIView.as_view(), name='avaliações')
, path('avaliações/<int:avaliação_pk>/', AvaliaçãoAPIView.as_view(), name = 'avaliação')] """