from django.shortcuts import render,redirect
from .models import pi

def index(request):
	return render(request,'index.html')

def register(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("payment")
	return render(request,"register.html")

def bregister(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("backend")
	return render(request,"bregister.html")

def fregister(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("fullstack")
	return render(request,"fregister.html")

def DSregister(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("DSA")
	return render(request,"DSregister.html")

def Dregister(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("Django")
	return render(request,"Dregister.html")

def Mregister(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("machine")
	return render(request,"Mregister.html")

def Gregister(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("graphic")
	return render(request,"Gregister.html")

def Wregister(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("web")
	return render(request,"Wregister.html")

def Myregister(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["password"]
		mobile=request.POST["mobile"]
		course=request.POST["course"]
		ob=pi.objects.create(name=name,email=email,password=password,mobile=mobile,course=course)
		ob.save()
		return redirect("mysql")
	return render(request,"Myregister.html")

def login(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("payment")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")	

def blogin(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("backend")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")		
def flogin(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("fullstack")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")		
def Wlogin(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("web")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")		
def Glogin(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("graphic")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")		
def Mylogin(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("mysql")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")		
def Mlogin(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("machine")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")		
def DSlogin(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("DSA")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")		
def Dlogin(request):
	if request.method=="POST":
		email=request.POST['email']
		pwd=request.POST['password']
		try:
			ob=pi.objects.get(email=email,password=pwd)
			request.session["uid"]=ob.name
			return redirect("Django")

		except Exception as e:
			return render(request,'Login.html',{'output':e})
	return render(request,"Login.html")		



def payment(request):
	return render(request,"payment.html")

def backend(request):
	return render(request,"backend.html")

def Django(request):
	return render(request,"Django.html")
def DSA(request):
	return render(request,"DSA.html")

def fullstack(request):
	return render(request,"fullstack.html")

def graphic(request):
	return render(request,"graphic.html")

def machine(request):
	return render(request,"machine.html")

def mysql(request):
	return render(request,"mysql.html")

def web(request):
	return render(request,"web.html")								