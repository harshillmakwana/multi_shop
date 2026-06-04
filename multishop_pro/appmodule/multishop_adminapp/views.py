from django.shortcuts import render ,redirect
from django.http import HttpResponse
from appmodule.multishop_adminapp import forms, models
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def myname(request):
    return HttpResponse("this is admin application")

@login_required(login_url='login_view')
def index_view1(request):
    return render(request,'admin_app/index.html')

@login_required(login_url='login_view')
def charts_view1(request):
    return render(request,'admin_app/chartjs.html')

@login_required(login_url='login_view')
def basic_elemrnta_view(request):
    return render(request,'admin_app/basic_elements.html')

@login_required(login_url='login_view')
def basic_table_view(request):
    return render(request,'admin_app/basic-table.html')

@login_required(login_url='login_view')
def blank_page_view(request):
    return render(request,'admin_app/blank-page.html')

@login_required(login_url='login_view')
def button_view(request):
    return render(request,'admin_app/buttons.html')

@login_required(login_url='login_view')
def dropdowns_view(request):
    return render(request,'admin_app/dropdowns.html')

@login_required(login_url='login_view')
def error_404_view(request):
    return render(request,'admin_app/error-404.html')

@login_required(login_url='login_view')
def error_500_view(request):
    return render(request,'admin_app/error-500.html')

@login_required(login_url='login_view')
def font_awesome_view(request):
    return render(request,'admin_app/font-awesome.html')

@login_required(login_url='login_view')
def login_view1(request):
    return render(request,'admin_app/login.html')

@login_required(login_url='login_view')
def register_view1(request):
    return render(request,'admin_app/register.html')

@login_required(login_url='login_view')
def typography_view(request):
    return render(request,'admin_app/typography.html')


#CRUD opration
@login_required(login_url='login_view')
def create_category(request):
    if request.method == 'POST':
        form = forms.category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_category')
        else:
            print(form.errors)
    return render(request,'admin_app/create_categoty1.html')

@login_required(login_url='login_view')        
def list_category(request):
    cate = models.category.objects.all()
    context = {'cate':cate}
    return render(request,'admin_app/list_category1.html',context)


def delete_category(request,id):
    del_cat = models.category.objects.get(id=id)
    del_cat.delete()
    return redirect('list_category')

def update_category(request, id):
    up_cate = models.category.objects.get(id=id)
    if request.method == 'POST':
        form = forms.category_form(request.POST,instance=up_cate)
        if form.is_valid():
            form.save()
            messages.success(request,"Category updated success!")
            return redirect('list_category')
        else:
            print(form.errors)
    context = {'up_cate': up_cate}
    return render(request,'admin_app/update_category1.html',context)


@login_required(login_url='login_view')
def create_category_sub(request):
    cat_main = models.category.objects.all()
    if request.method == 'POST':
        form = forms.category_sub_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(list_category_sub)
        else:
            print(form.errors)
    context = {'cat_main':cat_main}
    return render(request,'admin_app/create_categoty2.html',context)

@login_required(login_url='login_view')
def list_category_sub(request):
    cate2 = models.category_sbu.objects.all()
    context = {'cate2':cate2}
    return render(request,'admin_app/list_category2.html',context)

def delete_category_sub(request,id):
    del_cat2 = models.category_sbu.objects.get(id=id)
    del_cat2.delete()
    return redirect('list_category_sub')

def update_category_sub(request, id):
    cat_main = models.category.objects.all()
    upda_cate = models.category_sbu.objects.get(id=id)
    if request.method == 'POST':
        form = forms.category_sub_form(request.POST,instance=upda_cate)
        if form.is_valid():
            form.save()
            messages.success(request,"Category updated success!")
            return redirect('list_category_sub')
        else:
            print(form.errors)
    context = {'upda_cate': upda_cate,'cat_main':cat_main}
    return render(request,'admin_app/update_category2.html',context)


@login_required(login_url='login_view')
def create_category_sub_sub(request):
    cat_main1 = models.category.objects.all()
    cat_main2 = models.category_sbu.objects.all()
    if request.method == 'POST':
        form = forms.category_sub_sub_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_category_sub_sub)
        else:
            print(form.errors)
    context = {'cat_main1':cat_main1,'cat_main2':cat_main2}
    return render(request,'admin_app/create_categoty3.html',context)

@login_required(login_url='login_view')
def list_category_sub_sub(request):
    cate3 = models.category_sub_sub.objects.all()
    context = {'cate3':cate3}
    return render(request,'admin_app/list_category3.html',context)

def delete_category_sub_sub(request,id):
    del_cat2 = models.category_sub_sub.objects.get(id=id)
    del_cat2.delete()
    return redirect('list_category_sub_sub')
  
def update_category_sub_sub(request, id):
    cat_main1 = models.category.objects.all()
    cat_main2 = models.category_sbu.objects.all()
    upda_cate = models.category_sub_sub.objects.get(id=id)
    if request.method == 'POST':
        form = forms.category_sub_sub_form(request.POST,instance=upda_cate)
        if form.is_valid():
            form.save()
            messages.success(request,"Category updated success!")
            return redirect('list_category_sub_sub')
        else:
            print(form.errors)
    context = {'upda_cate': upda_cate,'cat_main1':cat_main1,'cat_main2':cat_main2}
    return render(request,'admin_app/update_category3.html',context)


@login_required(login_url='login_view')
def create_product(request):
    cat_main1 = models.category.objects.all()
    cat_main2 = models.category_sbu.objects.all()
    cat_main3 = models.category_sub_sub.objects.all()
    if request.method == 'POST':
        form = forms.product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(list_product)
        else:
            print(form.errors)
    context = {'cat_main1':cat_main1,'cat_main2':cat_main2,'cat_main3':cat_main3}
    return render(request,'admin_app/create_product.html',context)

@login_required(login_url='login_view')
def list_product(request):
    pro = models.product.objects.all()
    context = {'pro':pro}
    return render(request,'admin_app/list_product.html',context)  

def delete_product(request,id):
    del_pro = models.product.objects.get(id=id)
    del_pro.delete()
    return redirect(list_product)

def update_product(request,id):
    cat_main1 = models.category.objects.all()
    cat_main2 = models.category_sbu.objects.all()
    cat_main3 = models.category_sub_sub.objects.all()
    up_pro = models.product.objects.get(id=id)
    if request.method == 'POST':
        form = forms.product_form(request.POST,request.FILES,instance=up_pro)
        if form.is_valid():
            form.save()
            messages.success(request,"Product updated success!")
            return redirect(list_product)
        else:
            print(form.errors)
    context = {'up_pro':up_pro,'cat_main1':cat_main1,'cat_main2':cat_main2,'cat_main3':cat_main3}
    return render(request,'admin_app/update_product.html',context)            




