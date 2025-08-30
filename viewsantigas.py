from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import cursosSerializer, avaliaçõesSerializer
from .models    import cursos, avaliações

class cursosAPIView(APIView):
    def get(self,request): 
        cursos_1 = cursos.objects.all()
        serializer = cursosSerializer(cursos_1, many = True)
        return Response(serializer.data)
    
    def post(self,request): 
        serializer = cursosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AvaliaçõesAPIView(APIView): 
    def get(self,request):
        avaliacao = avaliações.objects.all()
        serializer = avaliaçõesSerializer(avaliacao,many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = avaliaçõesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)