# Create your views here.
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import Http404, HttpResponse

def loadTable(request):
    t=get_template('base.html')
    html= t.render(Context({'title':'BSC GPA'}))
    return HttpResponse(html)