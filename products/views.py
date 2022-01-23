from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# from django.http import Http404

# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def product_update_view(request, obj_id):  # id=id
    obj = get_object_or_404(Product, id=obj_id)  # id=id

    form = ProductForm(
        request.POST or None,
        instance=obj
    )

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)

def product_detail_view(request, obj_id):
    obj = Product.objects.get(id=obj_id)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)

def product_delete_view(request, obj_id):
    obj = get_object_or_404(Product, id=obj_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)

# def dynamic_lookup_view(request, obj_id):
#     # obj = Product.objects.get(id=my_id)
#     obj = get_object_or_404(Product, id=obj_id)
#     context = {
#         'object': obj
#     }
#     return render(request, 'products/product_detail.html', context)

# def render_initial_data(request):
#     initial_data = {
#         'title': "My this awesome title :3"
#     }

#     obj = Product.objects.get(id=1)

#     form = ProductForm(
#         request.POST or None,
#         instance=obj
#     )

#     if form.is_valid():
#         form.save()

#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)

# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         print(title)
#     context = {}
#     return render(request, 'products/product_create.html', context)

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'object': obj
#     }
#     return render(request, 'products/product_detail.html', context)
