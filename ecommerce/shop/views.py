from django.shortcuts import render,redirect
from shop.models import Categories
from shop.models import Product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def categories(request):
    c=Categories.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)
def products(request,p):
    c=Categories.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context={'cat':c,'product':p}
    return render(request,'products.html',context)

def product_details(request,p):
    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,'details.html',context)

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
            return redirect('shop:categories')
        else:
            return HttpResponse("passwords are not same")
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)

        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            return HttpResponse("invalid credentials")


    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect("shop:login")


def addcategories(request):
    if(request.method=="POST"):
        n=request.POST['n']
        i=request.FILES['i']
        d=request.POST['d']
        c=Categories.objects.create(name=n,image=i,description=d)
        c.save()

        return redirect('shop:categories')



    return render(request,'addcategories.html')




def addproducts(request):
    if(request.method=="POST"):
        n=request.POST['n']
        i=request.FILES['i']
        d=request.POST['d']
        s=request.POST['s']
        p=request.POST['p']
        c=request.POST['c']
        cat=Categories.objects.get(name=c)
        p=Product.objects.create(name=n,image=i,description=d,stock=s,price=p,category=cat)
        p.save()
        return redirect('/')




    return render(request,'addproducts.html')



def addstock(request,p):
    product=Product.objects.get(id=p)


    if(request.method=="POST"):
        product.stock=request.POST['s']
        product.save()
        return redirect('shop:product_details',p)


    context={'pro':product}
    return render(request,'addstock.html',context)


