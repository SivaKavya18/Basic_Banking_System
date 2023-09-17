from django.shortcuts import render,HttpResponse
from .models import customers,history
from django.http import HttpResponseRedirect
from django.utils.timezone import localtime
import datetime

# Create your views here.
def home(request):
    return render(request,'home.html')
def all_customers(request):
    customer_det=customers.objects.all()
    return render(request,'all_customers.html',{'customer':customer_det})
def search(request):
    search_val=request.GET['search_val']
    customer_det=customers.objects.all()
    def fun(customer_n):
        if search_val.lower() in customer_n.name.lower():
            return True 
        else:
            return False
    customer_det=list(filter(fun,customer_det))
    return render(request,'all_customers.html',{'customer':customer_det})
def customer(request,id):
    customer_det=customers.objects.get(id=id)
    customer_all=customers.objects.all()
    def rem_id(val):
        if (val.id)!=id:
            return True 
        else:
            return False
    customer_all=list(filter(rem_id,customer_all))
    return render(request,'customer.html',{'customer':customer_det,'customer_all':customer_all})
def transfer(request,id1,id2):
    customer1=customers.objects.get(id=id1)
    customer2=customers.objects.get(id=id2)
    return render(request,'transfer.html',{'customer1':customer1,'customer2':customer2})
def tran(request,id1,id2):
    transfer_val=int(request.GET['transferval'])
    customer1=customers.objects.get(id=id1)
    customer2=customers.objects.get(id=id2)
    customer1.current_balance=customer1.current_balance-transfer_val
    customer2.current_balance=customer2.current_balance+transfer_val
    s=''
    if request.GET:
        if (customer1.current_balance<0 or transfer_val<0):
            s='Transfer Unsuccessful'
        else:
            customer1.save()
            customer2.save()
            history.objects.create(sender=customer1.name,reciever=customer2.name,amount=transfer_val,date_transfer=datetime.datetime.now())
            s='Transfer Successful'
    return render(request,'transfer.html',{'result':s,'customer1':customer1,'customer2':customer2})
def main(request):
    return HttpResponseRedirect('/home')
def transfer_history(request):
    tr_hs=history.objects.all()
    return render(request,'transfer_history.html',{'history':tr_hs})
def about_us(request):
    return render(request,'about_us.html')
