# -*- coding: utf-8 -*- 
'''
Created on 2012-12-28

@author: qhw
'''

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def test(request):
  user = auth.authenticate(username='qhw', password='1920521')
  if user is not None:
    return HttpResponse("success")
    
  if request.user.is_authenticated():
    
    if "test" in request.session:
      return HttpResponse(request.session["test"])
    else:
      request.session["test"] = "qhw"
      return HttpResponse("hello")
  else:
    return HttpResponse("not")

#登陆
def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

#登出
def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")
