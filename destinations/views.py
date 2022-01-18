from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import callData

class ListingsAPIView(APIView):
	@staticmethod
	def post(request):
		q = request.data.get('q')
		page_size = request.data.get('page_size')
		context = {}
		if callData(page_size, q):
			context["success"] = True
			context["message"] = "Data has been saved successfully"
		else:
			context["success"] = False
			context["message"] = "Some error occurred"				
		return Response(context)

