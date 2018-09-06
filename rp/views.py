from django.shortcuts import render#_to_respose
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.
def rp(request):
	return HttpResponseRedirect('http://pls.redirect-me.xyz/?/ru/?partner=p23676p3132805p8160')
