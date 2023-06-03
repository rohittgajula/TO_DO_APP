from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework import permissions, authentication

from .models import Tag, Task
from .serializers import TaskSerializer, TagSerializer

@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
class TaskAPI(APIView):

    def get(self, request):
        objs = Task.objects.all()
        serializer = TaskSerializer(objs, many=True)
        return Response({
            'data':serializer.data
        }, status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            }, status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        if data == {}:
            return Response('Fields are empty')
        objs = Task.objects.get(id = data['id'])
        serializer = TaskSerializer(objs, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            }, status.HTTP_202_ACCEPTED)
        return Response('Fields are empty.')
    
    def patch(self, request):
        data = request.data
        if data == {}:
            return Response('Fields are empty')
        objs = Task.objects.get(id = data['id'])
        serializer = TaskSerializer(objs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            }, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        if data == {}:
            return Response({
                'message':'id field required'}
                )
        objs = Task.objects.get(id = data['id'])
        objs.delete()
        return Response({
            'message':'Sucessfully deleated.'
            }, status.HTTP_202_ACCEPTED)

@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
class TagAPI(APIView):

    def get(self, request):
        objs = Tag.objects.all()
        print(objs)
        serializer = TagSerializer(objs, many=True)
        return Response({
            'data':serializer.data
        }, status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            }, status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        if data == {}:
            return Response({
                'message':'id field required.'
            })
        objs = Tag.objects.get(id = data['id'])
        objs.delete()
        return Response({
            'message':'Sucessfully deleated.'
        }, status.HTTP_202_ACCEPTED)
    
