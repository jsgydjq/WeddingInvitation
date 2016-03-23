#coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import model_to_dict
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render_to_response('index_xiong.html',{'app': 'I am a test view'},
    	context_instance=RequestContext(request))


def index(request):
    return render_to_response('web_index.html',{'app': 'I am a test view'},
        context_instance=RequestContext(request))

def impress(request):
    return render_to_response('web_impress.html',{'app': 'I am a test view'},
    context_instance=RequestContext(request))
