from django.shortcuts import render
from django.http import JsonResponse
from .tasks import long_running_task
# Create your views here.

def index(request):
    delay = request.GET.get('delay',2)
    long_running_task.delay(delay)
    return JsonResponse(
        data={"message":"This takes long"}
    )