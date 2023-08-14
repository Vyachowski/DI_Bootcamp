from django.shortcuts import render
from .serializers import ReportSerial
from django.views.decorators.csrf import csrf_exempt
from .models import Report
from django.http import JsonResponse
# Create your views here.


@csrf_exempt
def report_view(request):
    if request.method == 'GET':
        reports = Report.objects.all()
        serializer = ReportSerial(reports, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = request.POST
        print(data)