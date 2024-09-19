from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.db import transaction
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# Model bject - Single Student Data
def student_detail(requ,est, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Query Set - All stduent data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    

def student_api(request):
    if request.method == 'GET':
        # Check if an ID is passed as a query parameter (for GET requests)
        id = request.GET.get('id', None)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)  # Get a single student
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except Student.DoesNotExist:
                return HttpResponse('Student not found', status=404)
        
        # If no ID, return all students
        stu = Student.objects.all()  # Get all students
        serializer = StudentSerializer(stu, many=True)  # many=True for list of students
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == "POST":
        # Use transaction.atomic() to ensure rollback in case of failure
        with transaction.atomic():
            try:
                json_data = request.body
                stream = io.BytesIO(json_data)
                pythondata = JSONParser().parse(stream)
                serializer = StudentSerializer(data=pythondata)
                if serializer.is_valid():
                    serializer.save()  # Save the student data
                    res = {'msg': "Data Created"}
                    json_data = JSONRenderer().render(res)
                    return HttpResponse(json_data, content_type='application/json', status=201)
                else:
                    json_data = JSONRenderer().render(serializer.errors)
                    return HttpResponse(json_data, content_type='application/json', status=400)
            except Exception as e:
                # If any error occurs, the transaction will be rolled back automatically
                return JsonResponse({'error': str(e)}, status=400)
    
    return HttpResponse("Invalid request method", status=405)

