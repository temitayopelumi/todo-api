from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Tasks

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    taskss = Tasks.objects.all()
    serializers = TaskSerializers(taskss, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def taskDetail(request, pk):
    taskss = Tasks.objects.get(id=pk)
    serializers = TaskSerializers(taskss, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = TaskSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task =Tasks.objects.get(id=pk)
    serializers = TaskSerializers(instance=task, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task =Tasks.objects.get(id=pk)
    task.delete()
    
    return Response('item succefully deleted')