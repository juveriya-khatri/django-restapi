from .models import Student
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer


class StudentList(APIView):
	def get(self, request, format=None):
		students = Student.objects.all().order_by('id')
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = StudentSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)


class StudentDetail(APIView):
	def get_object(self, pk):
		try:
			return Student.objects.get(id=pk)
		except Student.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		students =self.get_object(pk)
		serializer = StudentSerializer(students, many=False)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		student = self.get_object(pk)
		serializer = StudentSerializer(instance=student, data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		student = self.get_object(pk)
		student.delete()

		return Response('Item Deleted!')
