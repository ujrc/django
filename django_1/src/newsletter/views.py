from django.shortcuts import render
from .forms import SignUpForm, ContactForm
# Create your views here.
def home(request):
	title="Welcome"
	# if request.user.is_authenticated():
	# 	title="My title %s" %(request.user) 

	#Add form
	# if request.POST:
	# 	print(request.POST)
	form =SignUpForm(request.POST or None)
	context={
	'title':title,
	'form':form,
	}
	if form.is_valid():
		# form.save()
		# print(request.POST['email']) # This is not good  don't save data through request

		instance=form.save(commit=False)
		full_name=form.cleaned_data.get('full_name')
		if not full_name:
			full_name="My name"
		instance.full_name=full_name
		instance.save()
		# print(instance.email)
		# print(instance.full_name)
		context={
		'title':'Thank you for joining us',
		}
	return render(request,'newsletter/home.html',context)

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		email=form.cleaned_data.get('email')
		message=form.cleaned_data['message']
		full_name=form.cleaned_data['full_name']
		# print (email,full_name,message)
		# print(form.cleaned_data)
		for key in form.cleaned_data:
			# print (key)
			print(form.cleaned_data[key])
			print(form.cleaned_data.get(key))
	context={
	'form':form,
	}
	template='newsletter/forms.html'

	return render(request,template,context)