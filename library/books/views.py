from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

from books.models import Book
def viewbooks(request):
    k=Book.objects.all()
    context={'book':k}
    return render(request,'view.html',context)


def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p= request.POST['p']
        pa= request.POST['pa']
        l= request.POST['l']
        c= request.FILES['c']
        pd= request.FILES['pd']
        b=Book.objects.create(title=t,author=a,price=p,pages=pa,languages=l,cover=c,pdf=pd)
        b.save()
        return redirect('/view')
    return render(request,'add.html')


def viewdetails(request,p):
    k=Book.objects.get(id=p)
    context={'book':k}

    return render(request,'viewdetails.html',context)


def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return redirect('books:view')

def edit(request,p):
    k=Book.objects.get(id=p)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.pages=request.POST['pa']
        k.languages=request.POST['l']
        if(request.FILES.get('c')==None):
            k.save()
        else:
            k.cover=request.FILES.get('c')

        if (request.FILES.get('pd')==None):
            k.save()
        else:
            k.pdf=request.FILES.get('pd')
        k.save()
        return redirect('books:view')
    context={'book':k}
    return render(request,'edit.html',context)

