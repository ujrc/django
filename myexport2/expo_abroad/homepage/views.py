from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
	template_name='homepage/index.html'
	

# def main(request):
# 	return render(request,'homepage/main.html',{})
