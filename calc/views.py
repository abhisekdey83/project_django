from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'home.html',{'name':'Abhisek'})

def add(request):
	pname = request.GET['pname']
	price = int(request.GET['price'])
	qty = int(request.GET['qty'])
	tp = price*qty
	return render(request,"result.html",{"pname":pname,"price":price,"qty":qty,"tp":tp})