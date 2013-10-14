
# -*- encoding: utf-8 -*-

from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import Http404, HttpResponse
from time import strftime
from forms import MisionForm
from models import mision
from django.shortcuts import render_to_response
import json
import socket

def runBsc(request):
    t=get_template('base.html')
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    html= t.render(Context({'maintitle':'BSC GPA', 'title':'Resultados','subtitle':'Perspectiva Financiera','month':date["month"], 'year':date["year"],'currentpage':'status'}))
    return HttpResponse(html)

def addKpi(request):
    t=get_template('base.html')
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    html= t.render(Context({'maintitle':'BSC GPA', 'title':'Ingreso Indicadores','subtitle':'Perspectiva Financiera','month':date["month"], 'year':date["year"], 'currentpage':'add'}))
    return HttpResponse(html)

def viewMision(request):
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    form=MisionForm()
    data={'maintitle':'BSC GPA', 'title':'Configuración','subtitle':'Misión Empresarial','month':date["month"], 'year':date["year"], 'currentpage':'conf', 'form':form}
    csrfContext = RequestContext(request, data)
#    return render_to_response('mision.html', {'maintitle':'BSC GPA', 'title':'Configuración','subtitle':'Misión Empresarial','month':date["month"], 'year':date["year"], 'currentpage':'conf', 'form':form})
    return render_to_response('mision.html', data, csrfContext)

def addMision(request):
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    if request.is_ajax() and request.POST:
        form=MisionForm(request.POST)
        if form.is_valid():
            form.save()
            data={'message':'Correcto'}
        else:
            data={'message':'Error'}
        return HttpResponse(json.dumps(data),content_type='application/json')
    else:
        raise Http404
  

def addPerspective(request):
    t=get_template('ingreso_perspectivas.html')
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    html= t.render(Context({'maintitle':'BSC GPA', 'title':'Configuración','subtitle':'Perspectivas','month':date["month"], 'year':date["year"], 'currentpage':'conf'}))
    
    return HttpResponse(html)    
