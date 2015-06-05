#!/usr/bin/python
import  sys
from rtputils.hyperic.cli.funcs import *
from django.shortcuts import render_to_response
from rtputils.hyperic.cli.htmlmap import loginstr
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

def logout(request):
  try:
    del request.session['user_id']
    del request.session['logged_in']
  except:
    pass
  return redirect(index) 


def login(request, user):
  request.session['user_id'] = user.id
  request.session['logged_in'] = True
  return initialpage(request)

  
def initialpage(request):
  t = request.REQUEST.copy()
  return render_to_response('index.html', {} , mimetype='text/html') 

def todict(dct):
  temp = {}
  for key,value in dct.items():
    if isinstance(value, list):
      value = value[0]
    else:
      value = value
    temp.update({str(key):str(value)})
  return temp 
 

@csrf_exempt
def applogic (request):
  if request.method == 'GET' and 'actionName' not in request.GET:
    input = request.GET['searchValue']
    if input:
      (type, obj) = check_dict(input)
      if type == 'justoutput':
        return HttpResponse(html(obj), content_type="text/plain")
      elif type == 'callfunction':
        (rtype, rdata) = obj({})
        response =  HttpResponse(rdata,  content_type=type)
	return response
    else:
      response =  HttpResponse("",  content_type="text/plain")
      return response
  elif request.method == 'POST':
    dct =  todict(request.POST.copy())
    actionName=dct['actionName'] 
    del dct['actionName']
    (type, obj) = check_dict(actionName)
    (rtype, rdata) = obj(dct)
    print (rtype, rdata)
    response =  HttpResponse(rdata,  content_type=rtype)
    return response
  else:
    response =  HttpResponse("Error..",  content_type="text/plain")
    return response
    
@csrf_exempt
def index(request):
  if 'logged_in' in request.session:
    return initialpage(request)
  elif request.method == 'POST':
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    request.user = user
    if user:
      if user.is_active:
        return login(request, user)
      else:
        return HttpResponse('<strong>User not active</strong>', 'text/html')
    else:
      return HttpResponse('<strong>Invalid username and/or password</strong>', 'text/html')
  elif request.method == 'GET':
    return HttpResponse('<strong>%s</strong>' % loginstr, 'text/html')
