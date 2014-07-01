# Create your views herei.
import os
import json
from PIL import Image
from json import load
from django.http import HttpResponseRedirect 
from rest_framework.views import APIView
from rest_framework.response import Response          
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from photoapi.forms import RegistrationForm, LoginForm, UserProfileForm, PhotoForm
from photoapi.models import UserProfile, UserPhoto 
from django.contrib.auth import authenticate, login, logout
from photoapi.serializers import ImagesSerializer

def ClientRegistration(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
	form = RegistrationForm(data = request.POST)
        form_two = UserProfileForm(request.POST, request.FILES)

        if request.method == 'POST':
                
                if form.is_valid() and form_two.is_valid():
                        user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
                        user.save()

			profile = form_two.save(commit=False)
            		profile.user = user
			
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
           		if 'picture' in request.FILES:
                        	profile.picture = form_two.cleaned_data['picture']
			profile.save()
                        return HttpResponseRedirect('/profile/')
                else:
                        return render_to_response('photoapi/register.html', {'form': form, 'form_two': form_two}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show them a blank registration form '''
                form = RegistrationForm()
                context = {'form': form,
                           'form_two': form_two}
                return render_to_response('photoapi/register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        client = authenticate(username=username, password=password)
                        if client is not None:
                                login(request, client)
                                return HttpResponseRedirect('/profile/')
                        else:
                                return render_to_response('photoapi/login.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('photoapi/login.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('photoapi/login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/photoapi/login/')

@login_required
def Profile(request):
        if not request.user.is_authenticated():
                return HrttpResponseRedirect('/photoapi/login/')
	PhotoFrom = PhotoForm(request.POST, request.FILES)
        client = request.user.get_profile
	context = {'client': client, 'form': PhotoForm}
	photo_form =PhotoForm(request.POST, request.FILES)
	if request.method == 'POST' and 'image' in request.FILES:
		if photo_form.is_valid():
			photos = photo_form.save(commit=False)
			photos.user_id = request.user
			photos.image = request.FILES['image']
			photos.save()
	snippets = UserPhoto.objects.filter(user_id_id=request.user.id)
	if request.method == 'DELETE':
        	snippet.delete()
	if snippets:
		context = {'client': client, 'form': PhotoForm, 'data': snippets}


        return render_to_response('photoapi/profile.html', context, context_instance=RequestContext(request))

@login_required
def DeletePhoto(request):
	

def UploadPhoto(request):
        if not request.user.is_authenticated():
                return HrttpResponseRedirect('/photoapi/login/')
	current_user = request.user
    	print current_user.id
        photo_form =PhotoForm(request.POST, request.FILES)

	if request.method == 'POST' and 'image' in request.FILES:
		if photo_form.is_valid():
			photos = photo_form.save(commit=False)
			photos.user_id = request.user
			photos.image = request.FILES['image']
			photos.save()
			
			return render_to_response('photoapi/profile.html', context, context_instance=RequestContext(request))

def PhotoList(request):
	snippets = UserPhoto.objects.all()
	context = {'data': snippets}
	return render_to_response('photoapi/list_all.html', context, context_instance = RequestContext(request))


