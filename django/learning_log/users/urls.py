from django.urls import path, include

app_name = 'users'
urlpatterns = [
	#include djando default auth urls
	path('', include('django.contrib.auth.urls')),
]