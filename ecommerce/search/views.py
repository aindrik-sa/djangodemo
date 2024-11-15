from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def search_products(request):
    p=None
    query=" "
    if(request.method=="POST"):
        query=request.POST['q'] #reads the query value
        print(query)
        if query:
            p=Product.objects.filter(Q(name__icontains=query))  #filter the records matching with the query
    context={'pro':p,'query':query}
    return render(request,'search.html',context)