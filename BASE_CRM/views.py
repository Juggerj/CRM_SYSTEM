from django.shortcuts import render
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import JsonResponse
from BASE_CRM.models import *


@csrf_exempt
def index(request):

    deals = Deals.objects.filter()

    return render_to_response('index.html', locals())




