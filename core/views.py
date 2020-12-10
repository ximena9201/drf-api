from django.shortcuts import render
from django.http import JsonResponse

#third party import
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
from .models import Post


#this view returns the data as a Json payload
# def test_view(request):
#     data = {
#         'name': 'jonh',
#         'age' : 23
#     } 
#     return JsonResponse(data)

class TestView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
 #Return data for multiple instances       
 # serializer = PostSerializer(qs, many=True)

  #Return data for one instance
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.daa)
        return Response(serializer.errors)