from django.shortcuts import render,redirect,HttpResponse
from .models import Inventory,Contact,Sale
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from math import ceil
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
	# products = Product.objects.all()
	# print(products)
	# n = len(products)
	# nSlides = n//4 + ceil((n/4)-(n//4))

	allProds = []
	catprods = Inventory.objects.values('category', 'id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prod = Inventory.objects.filter(category=cat)
		n = len(prod)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		allProds.append([prod, range(1, nSlides), nSlides])

	# params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
	# allProds = [[products, range(1, nSlides), nSlides],
	#             [products, range(1, nSlides), nSlides]]
	params = {'allProds':allProds}
	return render(request, 'shop/index.html', params)



def searchMatch(query, item):
	'''return true only if query matches the item'''
	if query in item.desc.lower() or query in item.name.lower() or query in item.category.lower():
		return True
	else:
		return False



def search(request):
	query = request.GET.get('search')
	allProds = []
	catprods = Inventory.objects.values('category', 'id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prodtemp = Inventory.objects.filter(category=cat)
		prod = [item for item in prodtemp if searchMatch(query, item)]

		n = len(prod)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		if len(prod) != 0:
			allProds.append([prod, range(1, nSlides), nSlides])
	params = {'allProds': allProds, "msg": ""}
	if len(allProds) == 0 or len(query)<4:
		params = {'msg': "Please make sure to enter relevant search query"}
	return render(request, 'shop/search.html', params)


def about(request):
	return render(request, 'shop/about.html')



def contact(request):
	if request.method=="POST":
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		phone = request.POST.get('phone', '')
		desc = request.POST.get('desc', '')
		contact = Contact(name=name, email=email, phone=phone, desc=desc)
		contact.save()
		messages.success(request,"Thank you for contacting with us, we will revert back to you soon.")
		return redirect("ShopHome")

	return render(request, 'shop/contact.html')



def productView(request, myid):
	# Fetch the product using the id
	product = Inventory.objects.filter(id=myid)


	return render(request, 'shop/productView.html', {'product':product[0]})




@login_required(login_url='handleLogin')
def checkout(request):
	if request.method=="POST":
		items_json = request.POST.get('itemsJson', '')
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		address = request.POST.get('address1', '') 
		city = request.POST.get('city', '')
		state = request.POST.get('state', '')
		zip_code = request.POST.get('zip_code', '')
		phone = request.POST.get('phone', '')
		total= request.POST.get('total', '')
		order = Sale(items_json=items_json,name=name, email=email, address=address, city=city,
					   state=state, zip_code=zip_code, phone=phone,total=total)
		order.save()
		thank = True
		id = order.order_id
		return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
	return render(request, 'shop/checkout.html')


def handleSignup(request):
	if request.method== "POST":
		#Get the post parameters
		username =request.POST['username']
		fname =request.POST['fname']
		lname =request.POST['lname']
		email =request.POST['email']
		pass1 =request.POST['pass1']
		pass2 =request.POST['pass2']

		#checks for erroneous inputs

		if len(username)>10:
			messages.error(request,"username must be under 10 characters")
			return redirect("ShopHome")

		if pass1 != pass2:
			messages.error(request,"The passwords do not match")
			return redirect("ShopHome")


		#create the user
		

		myuser= User.objects.create_user(username,email,pass1)
		myuser.first_name =fname
		myuser.last_name =lname
		myuser.save()
		messages.success(request,"Your Lloyds Bakery Account Has Been Succesfully Created, Please Login To Continue")
		return redirect("ShopHome")

	else:
		return HttpResponse('404 - Not Found')


def handleLogin(request):
	if request.method== "POST":
		#Get the post parameters
		loginusername =request.POST['loginusername']
		loginpassword =request.POST['loginpassword']	


		user =auth.authenticate(username=loginusername,password=loginpassword)

		if user is not None:
			auth.login(request,user)
			messages.success(request,"Succesfully logged In")
			return redirect("ShopHome")

		else:
			messages.error(request,"Invalid Credentials")
			return redirect("ShopHome")

	messages.error(request,"Please Signup Or Login to Continue")
	return redirect("ShopHome")


def handleLogout(request):
		logout(request)
		messages.success(request,"Succesfully logged Out")
		return redirect("ShopHome")







