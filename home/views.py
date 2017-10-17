# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json

# from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from home.models import *
from cart.forms import CartAddProductForm
# Create your views here.

def index(request):
    categories= Categories.objects.all()
    products = Product.objects.filter(cate_id=1)

    context ={
        'categories':categories,
        'products': products
    }

    return render(request,"home/index.html",context)

def categories (request,cate_id):
    categories = Categories.objects.filter()
    products= Product.objects.filter(cate_id=cate_id)[:6]

    context={
        'categories': categories,
        'products': products
    }
    return render(request,"home/index.html",context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, product_id=id,
                                         slug=slug,
                                         available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'home/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def search(request):
    key =  request.GET.get('names', None)
    name=[]
    image=[]
    products=Product.objects.filter(product_name__contains=key)
    for product in products:
        name.append(product.product_name)
        image.append(product.product_image)
    # print result
    results=json.dumps({
        'name':name,
        'image':image
    })
    print name
    # json_data=json.dumps(results)
    # result_serialize=serializers.serialize('json', results)
    return HttpResponse(results, content_type='application/json')
