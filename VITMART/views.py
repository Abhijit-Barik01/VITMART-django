from django.shortcuts import render
from store.models import Product
def home(request):
	products=Product.objects.all().filter(is_available=True) #dynamically finding all product
	context={'products':products,} #creating dictionary
	return render(request,'home.html',context) #passing the data
