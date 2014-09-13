from django.shortcuts import render
from od_api.models import modes, odPairs
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context, loader
# Create your views here.
def ODView(request):
    ''' Effort report by person,project, then task. Modify the ORM query to return the needed data'''
    obg = (request.GET.get('obg'))
    mode = (request.GET.get('mode'))
    maxdist = (request.GET.get('maxdist'))
    maxtime = (request.GET.get('maxtime'))

    if obg == None:
        #Can't allow this
        obg = '060376039001' # Assigning Default
    
    modeo = None
    try:
        int(mode)
        modeo = modes.objects.get(pk=mode)
    except:
        try:
            modeo = modes.objects.get(name=mode)
        except:
            pass
    
    if modeo == None:
        modeo = modes.objects.get(pk=1) # Assigning a default
           
  
    if maxdist == None and maxtime == None:
        # You really don't want to do this...
        odrecs = odPairs.objects.filter(origin=obg).filter(mode=modeo)
    elif maxdist == None:
        odrecs = odPairs.objects.filter(origin=obg).filter(mode=modeo).filter(ttime__lte=maxtime).order_by('ttime')
    elif maxtime == None:
        odrecs = odPairs.objects.filter(origin=obg).filter(mode=modeo).filter(tdist__lte=maxdist).order_by('tdist')
    else:
        odrecs = odPairs.objects.filter(origin=obg).filter(mode=modeo).filter(ttime__lte=maxtime).filter(tdist__lte=maxdist).order_by('ttime','tdist')
        
    numrecs = odrecs.count()
        
    t = loader.get_template('odrecs.html')
    c = RequestContext(request,{'odrecs': odrecs,'obg':obg,'mode':modeo,'maxdist':maxdist,'maxtime':maxtime, 'numrecs':numrecs})
    return HttpResponse(t.render(c))