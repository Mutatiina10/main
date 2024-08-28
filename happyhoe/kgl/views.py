from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
#accessing our models so we can get content from them
from kgl.models import *   #it means from Grocery _app, in the models.py file, import all
#borrowing decorators from django to restrict access to our pages
from django.contrib.auth.decorators import login_required
#importing a response to delete
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import SaleForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from .filters import StockFilter
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CreditSale, Product, Branch
from .forms import CreditSaleForm


# Create your views here.
def index(request):
    items = Stock.objects.all().order_by('-id')
    return render(request,'Grocery_app/index2.html', {'items': items})


@login_required
def home(request):
    products = Stock.objects.all().order_by('-id') #we're creating a variable called stock, arranged by their orders called ids
    #applying filters to a query set
    product_filters = StockFilter(request.GET, queryset=products)
    products = product_filters.qs
    return render(request, 'Grocery_app/home.html', {'products': products, 'product_filters': product_filters})

@login_required
def product_detail(request,product_id):
    product = Stock.objects.get(id = product_id)
    return render(request,'kgl/product_detail.html',{'product':product})

@login_required
def delete_detail(request,product_id):
    product = Stock.objects.get(id = product_id)
    product.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required
def issue_item(request,pk):
    #accessing all objects from the stock model
    issued_item = Stock.objects.get(id=pk)
    #accessing our form
    sales_form = SaleForm(request.POST)
    #receiving fata from the form and saving it in the model
    if request.method == 'POST':
    #checking whether the form is valid
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_cost
            new_sale.save()
            #keep track of stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()


            return redirect('receipt')
    return render(request,'Grocery_app/issue_item.html', {'sales_form': sales_form})

@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'Grocery_app/receipt.html', {'sales': sales})

@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'Grocery_app/receipt_detail.html', {'receipt': receipt})


class LogoutView(LogoutView):
    def get(self,request):
        logout(request)
        return redirect(login)
    

def LoginView(LoginView):
     pass
        