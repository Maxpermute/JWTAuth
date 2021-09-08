from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		content = {'message': 'Hello, GeeksforGeeks'}
		return Response(content)



def index(request):
    return HttpResponse("my frist blogweb django project")


def home(request):
    return HttpResponse("my 2nd folder django project")