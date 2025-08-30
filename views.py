from .serializers import cursosSerializer, avaliaçõesSerializer
from .models    import cursos, avaliações
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework import viewsets, mixins, generics, permissions
from rest_framework.pagination import PageNumberPagination
from .permission import ehsuperuser


class cursosAPIView(generics.ListAPIView):
    queryset = cursos.objects.all()
    serializer_class = cursosSerializer
    
class cursoAPIView(generics.RetrieveAPIView):
    queryset = cursos.objects.all()
    serializer_class = cursosSerializer

class AvaliaçõesAPIView(generics.ListAPIView): 
    queryset = avaliações.objects.all()
    serializer_class = avaliaçõesSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()

class AvaliaçãoAPIView(generics.RetrieveAPIView):
    queryset = avaliações.objects.all()
    serializer_class = avaliaçõesSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),cursos_id = self.kwargs.get('cursos_pk'), pk = self.kwargs.get('avaliação_pk'))
        return get_object_or_404(self.get_queryset(),pk = self.kwargs.get('avaliação_pk'))

#======= API V2 ===========
class Avaliaçõespagination(PageNumberPagination):
    page_size = 1

#permissions 
#permission_class = (permissions.DjangoModelPermissions)
permission_class = (ehsuperuser,permissions.DjangoModelPermissions)

class CursoViewSet(viewsets.ModelViewSet): 
    queryset = cursos.objects.all()
    serializer_class = cursosSerializer

    @action(detail=True, methods=['get'])
    def avaliações(self, request, pk=None):
        qs = avaliações.objects.filter(curso_id=pk)
        paginator = Avaliaçõespagination()
        page = paginator.paginate_queryset(qs, request)
        
        if page is not None:
            serializer = avaliaçõesSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = avaliaçõesSerializer(qs, many=True)
        return Response(serializer.data)
class AvaliaçãoViewSet(mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = avaliações.objects.all()
    serializer_class = avaliaçõesSerializer