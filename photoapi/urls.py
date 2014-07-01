
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings
from photoapi import views
import photoapi.views
urlpatterns = patterns('',
    
    url(r'^register/$', views.ClientRegistration),
    
    url(r'^login/$', views.LoginRequest),
    url(r'^logout/$', views.LogoutRequest),
    url(r'^profile/$', views.Profile, name='profile'),
    #url(r'^upload/$', views.UploadPhoto),
    #url(r'^showall/$', views.PhotoList),
    url(r'^userphoto/$', login_required(photoapi.views.UserPhotoView.as_view()), name='user-photo'),
    url(r'^new/$', login_required(photoapi.views.PhotoAddView.as_view()), name='photo-new',),
    url(r'^edit/(?P<pk>\d+)/$', login_required(photoapi.views.UpdatePhotoView.as_view()), name='photo-edit',),
    url(r'^delete/(?P<pk>\d+)/$', login_required(photoapi.views.DeletePhotoView.as_view()), name='photo-delete',),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

