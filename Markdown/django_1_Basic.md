[venv 생성하기]
conda create --name {이름} python={버전}
conda create --name py38-django python=3.8



[venv 활성화]
conda activate py38-django



[django 설치]
pip install Django



[빈 프로젝트 만들기]
django-admin startproject [trydjango](https://youtu.be/F5mRW0jo-U4)
현재 위치한 폴더에 직접 프로젝트를 만드는 경우 -> trydjango .



[디장고 서버 열기]
cd trydjango
[python manage.py runserver](https://code.visualstudio.com/docs/python/tutorial-django)



[settings.py]

```python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = False
```



[초기 마이그레이션]
[python manage.py migrate]([https://tibetsandfox.tistory.com/24])

- 실제 DB에 변경사항을 적용하는 명령어
- 마이그레이션을 적용하는 명령어



[초기 슈퍼유저 생성]
python manage.py createsuperuser







# App Products



[App 생성]
python manage.py startapp products



[모델 만들기] [docs](https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types)
[products/models.py]

```python
class Product(models.Model):
    title =         models.TextField()
    description =   models.TextField()
    price =         models.TextField()
```



[trydjango\trydjango\settings.py]

```python
INSTALLED_APPS = [
	...,
    
    'products',
]
```



[DB 반영]
python manage.py makemigrations
python manage.py migrate

> 0001_initial... OK



[모델 편집]
[[products/models.py]](https://youtu.be/F5mRW0jo-U4?t=2407)

```python
class Product(models.Model):
    title =         models.TextField()
    description =   models.TextField()
    price =         models.TextField()
    summary =       models.TextField()  # default?
```

```python
class Product(models.Model):
    title =         models.TextField()
    description =   models.TextField()
    price =         models.TextField()
    summary =       models.TextField(default='this is cool!')
```



[DB 반영]
python manage.py makemigrations
python manage.py migrate

> 0002_product_summary... OK



[products/admin.py]

```python
from .models import Product
admin.site.register(Product)
```



[파이썬 쉘에서 Product objects 생성해보기]
python manage.py shell

```python
>>> from products.models import Product
>>> Product.objects
<django.db.models.manager.Manager object at 0x000001A24B93C4C0>

>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>]>

>>> Product.objects.create(title='New product', description='another one', price='19312', summary='sweet')
<Product: Product object (2)>
    
>>> Product.objects.create(title='New product?', description='another one?', price='19321', summary='sweet?')
<Product: Product object (3)>
    
>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>]>
```



[DB랑 마이그레이션 초기화]
db.sqlite3
products/migrations/000*
{}/{}/\_pycache\_
-> 삭제



python manage.py makemigrations
{} {} migrate
{} {} createsuperuser



[다시 추가]
python manage.py shell

```python
>>> from products.models import Product
>>> Product.objects.all()
<QuerySet []>

>>> Product.objects.create(title='Newer title', price=239.99, summary='Awesome sauce')
<Product: Product object (1)>
    
>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>]>
```



[모델 편집]
[products/models.py]

```python
class Product(models.Model):
    title =         models.CharField(max_length=120)
    description =   models.TextField(blank=True, null=True)
    price =         models.DecimalField(decimal_places=2, max_digits=10000)
    summary =       models.TextField()
    featured =      models.BooleanField()  # null=True, default=True
```



python manage.py makemigrations

```css
It is impossible to add a non-nullable field 'featured' to product without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt

>>> True
Migrations for 'products':
  products\migrations\0002_product_featured.py
    - Add field featured to product
```



- 마이그레이션 이후 생성된 py
	products\migrations\0002_product_featured.py

```python
class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]

```



python manage.py migrate

> Applying products.0002_product_featured... OK



[products\models.py]

```python
class Product(models.Model):
    title =         models.CharField(max_length=120)
    description =   models.TextField(blank=True, null=True)
    price =         models.DecimalField(decimal_places=2, max_digits=10000)
    summary =       models.TextField(blank=True, null=False)
    featured =      models.BooleanField() # null(True), default(True)
```

- python manage.py makemigrations
	- Migrations for 'products':
		  products\migrations\0003_alter_product_summary.py
		    - Alter field summary on product

- python manage.py migrate
	- Operations to perform:
		  Apply all migrations: admin, auth, contenttypes, products, sessions
		Running migrations:
		  Applying products.0003_alter_product_summary... OK



```
models.TextField(blank=True, null=True)
```

blank(True): 필수 항목입니다.
blank(False):



[products\models.py]

```python
class Product(models.Model):
    title =         models.CharField(max_length=120)
    description =   models.TextField(blank=True, null=True)
    price =         models.DecimalField(decimal_places=2, max_digits=10000)
    summary =       models.TextField(blank=False, null=False)
    featured =      models.BooleanField()
```

python manage.py makemigrations
python manage.py migrate

>Applying products.0004_alter_product_summary... OK







# App Pages



[앱 생성]
python manage.py startapp pages



[pages 추가]
[trydjango\trydjango\settings.py]

```python
INSTALLED_APPS = [
  'pages',
  'products',
]
```







[pages home 추가]
[pages/views.py]

```python
def home_view(*args, **kwargs):
    html = "<h1>Hello World</h1>"  # string of HTML code
    return HttpResponse(html)
```



[trydjango\trydjango\urls.py]

```python
# ...
from pages import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
]
```

http://127.0.0.1:8000/



from pages import views -> from pages.views

```python
from pages.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]
```







[pages contact 추가하기]
[pages\views.py]

```python
def home_view(*args, **kwargs):
    html = "<h1>Hello World</h1>"  # string of HTML code
    return HttpResponse(html)

def contact_view(*args, **kwargs):
    html = "<h1>Contact Page</h1>"
    return HttpResponse(html)
```



[urls.py]

```python
from pages.views import home_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
```

https://satir.tistory.com/184







[pages about, contact 추가]
[pages\views.py]

```python
def home_view(*args, **kwargs):
    html = "<h1>Hello World</h1>"  # string of HTML code
    return HttpResponse(html)

def contact_view(*args, **kwargs):
    html = "<h1>Contact Page</h1>"
    return HttpResponse(html)

def about_view(*args, **kwargs):
    html = "<h1>About Page</h1>"
    return HttpResponse(html)

def social_view(*args, **kwargs):
    html = "<h1>Social Page</h1>"
    return HttpResponse(html)
```



[urls.py]

```python
from pages.views import home_view, contact_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]

```

https://youtu.be/F5mRW0jo-U4?t=4054



[args 확인하기]
[trydjango\pages\views.py]

```python
def home_view(*args, **kwargs):
    print(f'args: {args}, kwargs: {kwargs}')
    html = "<h1>Hello World</h1>"  # string of HTML code
    return HttpResponse(html)
```

```css
args: (<WSGIRequest: GET '/'>,), kwargs: {}
[07:29:49] "GET / HTTP/1.1" 200 20
```



```python
def home_view(request, *args, **kwargs):
    print(f'request: {request}, args: {args}, kwargs: {kwargs}')
    html = "<h1>Hello World</h1>"  # string of HTML code
    return HttpResponse(html)
```

```css
request: <WSGIRequest: GET '/'>, args: (), kwargs: {}
[07:30:50] "GET / HTTP/1.1" 200 20
```



```python
def home_view(request, *args, **kwargs):
    print(f'request: {request.user}, args: {args}, kwargs: {kwargs}')
    html = "<h1>Hello World</h1>"  # string of HTML code
    return HttpResponse(html)
```

```css
request: admin, args: (), kwargs: {}
[07:31:37] "GET / HTTP/1.1" 200 20


[07:31:58] "GET /admin/logout/ HTTP/1.1" 200 1532
request: AnonymousUser, args: (), kwargs: {}
[07:32:26] "GET / HTTP/1.1" 200 20


[07:33:17] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[07:33:17] "GET /admin/ HTTP/1.1" 200 4952
request: admin, args: (), kwargs: {}
[07:33:22] "GET / HTTP/1.1" 200 20
```







# Templates



[pages\views.py]

```python
def home_view(request, *args, **kwargs):
    print(f'request: {request.user}, args: {args}, kwargs: {kwargs}')
    # html = "<h1>Hello World</h1>"  # string of HTML code
    # return HttpResponse(html)
    return render(request, 'home.html', {})
```



[templates\home.html]

```html
<h1>Hello World</h1>
<p>This is a tempalte</p>
```



[trydjango\settings.py]

```python
TEMPLATES = [
    {
        # ...
        'DIRS': ['Z:\\doc\\trydjango\\templates'],
        # ...
    },
]
# [07:34:07] "GET / HTTP/1.1" 200 46
```

```python
TEMPLATES = [
    {
        # ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # ...
    },
]
# [07:34:20] "GET / HTTP/1.1" 200 46
```











[templates\about.html]  # 생성
[templates\contact.html]  # 생성
[pages\views.py]
about, contact → render 변경

```python
def home_view(request, *args, **kwargs):
    print(f'request: {request.user}, args: {args}, kwargs: {kwargs}')
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

# [07:35:00] "GET /contact/ HTTP/1.1" 200 42
# [07:35:02] "GET /about/ HTTP/1.1" 200 40
```







[templates\home.html]
django request 객체

```django
<h1>Hello World</h1>
{{request.user}}<br>
{{request.user.is_authenticated}}
<p>This is a tempalte</p>
```







[templates\base.html]
block, endblock, extends

```django
<!doctype html>
<html>
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    {% block content %}
    replace me
    {% endblock %}
</body>
</html>
```



[templates\home.html]

```django
{% extends 'base.html' %}

{% block content %}
    <h1>Hello World</h1>
    {{request.user}}<br>
    {{request.user.is_authenticated}}
    <p>This is a tempalte</p>
{% endblock %}
```

```html
<!-- home -->
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    <h1>Hello World</h1>
    admin<br>
    True
    <p>This is a tempalte</p>
</body>
```



[templates\about.html]

```django
{% extends 'base.html' %}
<h1>About</h1>
<p>This is a tempalte</p>
```

```html
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    replace me
</body>
```



```django
{% extends 'base.html' %}
{% block content %}
    <h1>About</h1>
    <p>This is a tempalte</p>
{% endblock content %}
```

```html
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    <h1>About</h1>
    <p>This is a tempalte</p>
</body>
```



[templates\contact.html]

```django
{% extends 'base.html' %}
{% block content %}
    <h1>Contact</h1>
    <p>This is a tempalte</p>
{% endblock content %}
```











[navbar]
[templates\base.html]
content → content_main 변경

```django
<!doctype html>
<html>
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    <h1>This is a navbar</h1>
    {% block content_main %}
    replace me
    {% endblock %}
</body>
</html>
```



[home]

```django
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    <h1>This is a navbar</h1>
    replace me
</body>
```







[templates\base.html]
block content, content_main

```django
<!doctype html>
<html>
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    <h1>This is a navbar</h1>
    {% block content %}
    content!
    {% endblock %}
    {% block content_main %}
    content_main!
    {% endblock %}
</body>
</html>
```



[about]
about에 content_main이 없어서 'content_main!'이 스크립트에 반영됨

```html
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    <h1>This is a navbar</h1>
    <h1>About</h1>
    <p>This is a tempalte</p>
    content_main!
</body>
```











[navbar.html 생성]
[templates\navbar.html]

```html
<nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
```



[templates\base.html]

```django
<!doctype html>
<html>
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    {% include 'navbar.html' %}

    {% block content %}
    replace me
    {% endblock %}
</body>
</html>
```



[about]

```html
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
    <h1>About</h1>
    <p>This is a tempalte</p>
</body>
```











# Rendering Context in a Template



[pages\views.py]
my_context

```python
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123
    }
    return render(request, 'about.html', my_context)
```



[templates\about.html]

```django
{% extends 'base.html' %}
{% block content %}
<h1>About</h1>
<p>This is a tempalte</p>

<p>
my_text: {{my_text}}<br>
my_number: {{my_number}}
</p>
{% endblock content %}
```



[about body]

```html
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
<h1>About</h1>
<p>This is a tempalte</p>
<p>
my_text: This is about us<br>
my_number: 123
</p>
</body>
```



[templates\about.html]
my_list

```python
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4242, 12313]
    }
    return render(request, 'about.html', my_context)
```



[about body p]

```
<p>
my_text: This is about us<br>
my_number: 123<br>
my_list: [123, 4242, 12313]
</p>
```







# For Loop in a Template



[templates\about.html]

```django
<ul>
{% for item in my_list %}
    <li>{{item}}</li>
{% endfor %}
</ul>
```

```html
<ul>
    <li>123</li>
    <li>4242</li>
    <li>12313</li>
</ul>
```


forloop.counter

```django
<ul>
{% for item in my_list %}
    <li>{{forloop.counter}} - {{item}}</li>
{% endfor %}
</ul>
```

```html
<ul>
    <li>1 - 123</li>
    <li>2 - 4242</li>
    <li>3 - 12313</li>
</ul>
```







[pages\views.py]
"my_list": [123, 4242, 12313, 'Abc']

```python
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4242, 12313, 'Abc']  # append 'Abc'
    }
    return render(request, 'about.html', my_context)
```



[about]

```html
<ul>
    <li>1 - 123</li>
    <li>2 - 4242</li>
    <li>3 - 12313</li>
    <li>4 - Abc</li>
</ul>
```







# Using Conditions in a Template



[pages\views.py]
"my_list": [2424, 4231, 312, 'Abc']

```python
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [2424, 4231, 312, 'Abc']
    }
    return render(request, 'about.html', my_context)
```



[templates\about.html]
if, else, [add](https://youtu.be/F5mRW0jo-U4?t=6110)

```django
<ul>
{% for item in my_list %}
    {% if item == 312 %}
        <li>{{forloop.counter}} - {{item|add:21}}</li>
    {% else %}
        <li>{{forloop.counter}} - {{item}}</li>
    {% endif %}
{% endfor %}
</ul>
```

```html
<ul>
        <li>1 - 2424</li>
        <li>2 - 4231</li>
        <li>3 - 333</li>
        <li>4 - Abc</li>
</ul>
```


elif

```django
<ul>
{% for item in my_list %}
    {% if item == 312 %}
        <li>{{forloop.counter}} - {{item|add:21}}</li>
    {% elif item == 'Abc' %}
        <li>This is not the network</li>
    {% else %}
        <li>{{forloop.counter}} - {{item}}</li>
    {% endif %}
{% endfor %}
</ul>
```

```html
<ul>
        <li>1 - 2424</li>
        <li>2 - 4231</li>
        <li>3 - 333</li>
        <li>This is not the network</li>
</ul>
```







# [Template Tags and Filters](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)

https://youtu.be/F5mRW0jo-U4?t=6161



[templates\about.html]
cycle

```django
<ul>
{% for item in my_list %}
    cycle: {% cycle 1 2 3 %}
    {% if item == 312 %}
        <li>{{forloop.counter}} - {{item|add:21}}</li>
    {% elif item == 'Abc' %}
        <li>This is not the network</li>
    {% else %}
        <li>{{forloop.counter}} - {{item}}</li>
    {% endif %}
{% endfor %}
</ul>
```

```html
<ul>
    cycle: 1
        <li>1 - 2424</li>
    cycle: 2
        <li>2 - 4231</li>
    cycle: 3
        <li>3 - 333</li>
    cycle: 1
        <li>This is not the network</li>
</ul>
```







[pages\views.py]
title

```python
def about_view(request, *args, **kwargs):
    my_context = {
        "title": "abc this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [2424, 4231, 312, 'Abc']
    }
    return render(request, 'about.html', my_context)
```



[templates\about.html]
capfirst

```django
<h1>{{title|capfirst}}</h1>
```

```html
<h1>Abc this is about us</h1>
```


upper
upper 쓸 때는 capfirst 없어도 됨

```django
<h1>{{title|capfirst|upper}}</h1>
```

```html
<h1>ABC THIS IS ABOUT US</h1>
```


title

```django
<h1>{{title|title}}</h1>
```

```html
<h1>Abc This Is About Us</h1>
```







[pages\views.py]
my_html

```python
def about_view(request, *args, **kwargs):
    my_context = {
        "title": "abc this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [2424, 4231, 312, 'Abc'],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, 'about.html', my_context)
```



[templates\about.html]

```django
{{my_html}}
```

```html
&lt;h1&gt;Hello World&lt;/h1&gt;
```


safe

```django
{{my_html|safe}}
```

```html
<h1>Hello World</h1>
```


striptags

```django
{{my_html|striptags}}
```

```html
Hello World
```


slugify

```django
{{my_html|slugify}}
```

```html
h1hello-worldh1
```



striptags|slugify

```django
{{my_html|striptags|slugify}}
```

```html
hello-world
```







## Render Data from the Database with a Model



python mange.py shell

```python
>>> Product.objects.all()    
<QuerySet [<Product: Product object (1)>]>
>>> Product.objects.get(id=1)
<Product: Product object (1)>
>>> obj = Product.objects.get(id=1)
>>> dir(obj)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'description', 'featured', 'from_db', 'full_clean', 'get_deferred_fields', 'id', 'objects', 'pk', 'prepare_database_save', 'price', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'summary', 'title', 'unique_error_message', 'validate_unique']
>>> obj.title 
'New Product'
```

Product(id, title, description, price, summary, featured)







[products\views.py]

```python
from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description
    }
    return render(request, 'product/detail.html', context)
```



[templates\product\detail.html]
templates에서 product 폴더 생성
product에서 detail.html 생성

```django
{% extends 'base.html' %}
{% block content %}
<h1>Detail HTML</h1>
{% endblock content %}
```



[trydjango\urls.py]
urls.urlpatterns - views.product_detail_view(request) - render('product/detail.html')

```python
from products.views import product_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('product/', product_detail_view),
    path('admin/', admin.site.urls),
]
```



[product]

```html
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
<h1>Detail HTML</h1>
</body>
```



[templates\product\detail.html]

```django
{% extends 'base.html' %}
{% block content %}
<h1>{{title}}</h1>
<p>{{description}}</p>
{% endblock content %}
```

```html
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
<h1>New Product</h1>
<p>description!</p>
</body>
```



[templates\product\detail.html]
if, else
/admin/products/product/1/change/
product id(1) description = ''

```django
{% extends 'base.html' %}
{% block content %}
<h1>{{title}}</h1>
<p>{% if description %}{{description}}{% else %}Description Coming Soon{% endif %}<p>
{% endblock content %}
```

```html
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
<h1>New Product</h1>
<p>Description Coming Soon</p>
</body>
```



[templates\product\detail.html]
description != None and description != ''

```django
{% extends 'base.html' %}
{% block content %}
<h1>{{title}}</h1>
<p>{% if description != None and description != '' %}{{description}}{% else %}Description Coming Soon{% endif %}</p>
{% endblock content %}
```

```html
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
<h1>New Product</h1>
<p>Description Coming Soon</p>
</body>
```







[products\views.py]

```python
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', context)
```



[templates\product\detail.html]

```django
{% extends 'base.html' %}
{% block content %}
<h1>{{object.title}}</h1>
<p>{% if object.description != None and object.description != '' %}{{object.description}}{% else %}Description Coming Soon{% endif %}</p>
{{object.price}}
{% endblock content %}
```

```html
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
<h1>New Product</h1>
<p>Description Coming Soon</p>
239.99
</body>
```







# How Django Templates Load with Apps

https://youtu.be/F5mRW0jo-U4?t=7196



[products\templates\products\product_detail.html]
templates 폴더 생성
products 폴더 생성
product_detail.html 생성하고
templates\product\detail.html 파일 내용 참고하기

```django
{% extends 'base.html' %}
{% block content %}
<h1>{{object.title}}</h1>
<p>{% if object.description != None and object.description != '' %}{{object.description}}{% else %}Description Coming Soon{% endif %}</p>
{{object.price}}
{% endblock content %}
```



[products\templates\products\product_detail.html]
수정

```django
{% extends 'base.html' %}
{% block content %}
<h1>In App template: {{object.title}}</h1>
<p>{% if object.description != None and object.description != '' %}{{object.description}}{% else %}Description Coming Soon{% endif %}</p>
{{object.price}}
{% endblock content %}
```



[products\views.py]

```python
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products/detail.html', context)
```



[오류]

```css
django.template.exceptions.TemplateDoesNotExist: products/detail.html   
[08:35:25] "GET /product/ HTTP/1.1" 500 80491
```

product -> products 폴더명은 잘 변경했지만
해당 html은 products 폴더에 없으므로
render template_name 아규먼트를 'products\product_detail.html' 로 변경해 줘야 함



[products\views.py]
'products\product_detail.html'로 변경

```python
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
```

```html
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
<h1>In App template: New Product</h1>
<p>Description Coming Soon</p>
239.99
</body>
```







[templates\product\detail.html]
product -> products 변경
detail.html -> product_detail.html 변경



[templates\products\product_detail.html]
http://127.0.0.1:8000/product/
products\templates\products\product_detail.html (x)
templates\products\product_detail.html (o)
products\templates\ 보다는 templates\ 폴더가 더 가까워서 그런 것 같음

```html
<body>
    <nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>
<h1>New Product</h1>
<p>Description Coming Soon</p>
239.99
</body>
```

templates\products\product_detail.html 삭제
templates\products 삭제







# Django Model Forms



[products\forms.py]

```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
```



[products\views.py]

```python
from django.shortcuts import render
from .models import Product
from .forms import ProductForm  # new import

# Create your views here.
def product_create_view(request):  # new function
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
```



[products\templates\products\product_create.html]
product_create.html 생성

```django
{% extends 'base.html' %}
{% block content %}
<form>
    {{form.as_p}}
    <input type='submit' value='Save'/>
</form>
{% endblock content %}
```



[trydjango\urls.py]

```python
from pages.views import home_view, contact_view, about_view
from products.views import product_detail_view, product_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('create/', product_create_view),  # new path
    path('product/', product_detail_view),
    path('admin/', admin.site.urls),
]
```



[create/]

```html
<form>
    <p>
    <label for="id_title">Title:</label>
    <input type="text" name="title" maxlength="120" required="" id="id_title">
  </p>
  <p>
    <label for="id_description">Description:</label>
    <textarea name="description" cols="40" rows="10" id="id_description"></textarea>
  </p>
  <p>
    <label for="id_price">Price:</label>
    <input type="number" name="price" step="0.01" required="" id="id_price">
  </p>
    <input type="submit" value="Save">
</form>
```

http://127.0.0.1:8000/create/?title=New+Product&description=This+is+awesome&price=123.12






[products\templates\products\product_create.html]
method(post), csrf_token

```django
{% extends 'base.html' %}
{% block content %}
<form method='post'> {% csrf_token %}
    {{form.as_p}}
    <input type='submit' value='Save'/>
</form>
{% endblock content %}
```

```css
django.db.utils.IntegrityError: NOT NULL constraint failed: products_product.featured
"POST /create/ HTTP/1.1" 500 150857
```



[products\models.py]

```python
class Product(models.Model):
    title =         models.CharField(max_length=120)
    description =   models.TextField(blank=True, null=True)
    price =         models.DecimalField(decimal_places=2, max_digits=10000)
    summary =       models.TextField(blank=False, null=False)
    featured =      models.BooleanField(default=False)
```

python manage.py makemigrations
python manage.py migrate 

>Applying products.0005_alter_product_featured... OK



[127.0.0.1:8000/create/]

```css
"POST /create/ HTTP/1.1" 200 928
```



[products\views.py]
submit 이후에 값이 남아있는 것을
form = ProductForm() 으로 리셋

```python
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # reset

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)
```







# Raw HTML Form



[products\templates\products\product_create.html]

```django
{% extends 'base.html' %}
{% block content %}

<form method='post'>
    <input type='text' name='title' placeholder='Your title' />
    <input type='submit' value='Save'/>
</form>

{% endblock content %}
```



[products\views.py]

```python
def product_create_view(request):
    context = {}
    return render(request, 'products/product_create.html', context)
```

```css
"GET /create/ HTTP/1.1" 200 373
Forbidden (CSRF token missing.): /create/
"POST /create/ HTTP/1.1" 403 2531
```







[products\templates\products\product_create.html]
post → get

```django
<form method='get'>
    <input type='text' name='title' placeholder='Your title' />
    <input type='submit' value='Save'/>
</form>
```

```css
"GET /create/ HTTP/1.1" 200 372
"GET /create/?title=abc HTTP/1.1" 200 372
```



get

```django
<form>
    <input type='text' name='title' placeholder='Your title' />
    <input type='submit' value='Save'/>
</form>
```

```css
"GET /create/ HTTP/1.1" 200 359
"GET /create/?title=abc HTTP/1.1" 200 359
```



search

```django
<form action='/search/' method='GET'>
    <input type='text' name='title' placeholder='Your title' />
    <input type='submit' value='Save'/>
</form>
```

```css
"GET /create/ HTTP/1.1" 200 390
Not Found: /search/
"GET /search/?title=abc HTTP/1.1" 404 2653
```



google search

```django
<form action='http://www.google.com/search' method='GET'>
    <input type='text' name='q' placeholder='Your search' />
    <input type='submit' value='Save'/>
</form>
```

```css
"GET /create/ HTTP/1.1" 200 407
```

https://www.google.com/search?q=abc



post, csrf_token

```django
<form action='.' method='POST'> {% csrf_token %}
    <input type='text' name='title' placeholder='Your Title' />
    <input type='submit' value='Save'/>
</form>
```

```css
"GET /create/ HTTP/1.1" 200 506
"POST /create/ HTTP/1.1" 200 506
```

csrf_token 값이  없을 경우 → "POST /create/ HTTP/1.1" 403







[products\views.py]

```python
def product_create_view(request):
    print(request.GET)
    print(request.POST)
    context = {}
    return render(request, 'products/product_create.html', context)
```



http://127.0.0.1:8000/create/?title=abc

```css
<QueryDict: {'title': ['abc']}>
<QueryDict: {}>
"GET /create/?title=abc HTTP/1.1" 200 506
```



http://127.0.0.1:8000/create/
submit으로 전송

```css
<QueryDict: {}>
<QueryDict: {'csrfmiddlewaretoken': ['63EaMkiP8iBSo9AkWK6ABlQ6yH2NlUBXOiu2sIRHLcHiawRoPyvC6eIZnDR1YTCq'], 'title': ['abc']}>
"POST /create/ HTTP/1.1" 200 506
```







[products\views.py]

```python
def product_create_view(request):
    print(request.GET.get('title'))
    print(request.POST)
    context = {}
    return render(request, 'products/product_create.html', context)
```

```css
None
<QueryDict: {'csrfmiddlewaretoken': ['yb4yPciTlZnwade0NfAiN83KcU7fYe26gqUqvARLYTtWWAv4G3Zki1VD1QWtBd3z'], 'title': ['abc']}>
"POST /create/ HTTP/1.1" 200 506

abc
<QueryDict: {}>
"GET /create/?title=abc HTTP/1.1" 200 506
```



```python
def product_create_view(request):
    # print(request.GET)
    # print(request.POST)
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
    context = {}
    return render(request, 'products/product_create.html', context)
```

```css
abc
"POST /create/ HTTP/1.1" 200 506
```







# Pure Django Form



[products\views.py]
새로 구성된 것을 작성하기 위해서 일부만 남기고 지움

```python
def product_create_view(request):
    context = {}
    return render(request, 'products/product_create.html', context)
```



[products\forms.py]
https://docs.djangoproject.com/en/4.0/ref/forms/fields/
RawProductForm 클래스 추가

```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

class RawProductForm(forms.Form): # new
    title =         forms.CharField()
    description =   forms.CharField()
    price =         forms.DecimalField()
```



[products\views.py]
DB에 반영되는 기능이 없기 때문에 submit을 시도해도 에러는 없지만 저장되지 않음

```python
def product_create_view(request):
    my_form = RawProductForm()
    context = {
        'form': my_form
    }
    return render(request, 'products/product_create.html', context)
```



[products\templates\products\product_create.html]
form.as_p

```django
<form action='.' method='POST'> {% csrf_token %}
    {{form.as_p}}
    <input type='submit' value='Save'/>
</form>
```

```html
<form action="." method="POST"> <input type="hidden" name="csrfmiddlewaretoken" value="MEdVHuGl0dpigS6qdZtzorv0TZYVp1zpuT3NnSfdD7vI2fnu6NSBTknTIVN920AS">
    <p>
    <label for="id_title">Title:</label>
    <input type="text" name="title" required="" id="id_title">
  </p>
  <p>
    <label for="id_description">Description:</label>
    <input type="text" name="description" required="" id="id_description">
  </p>
  <p>
    <label for="id_price">Price:</label>
    <input type="number" name="price" step="any" required="" id="id_price">
  </p>
    <input type="submit" value="Save">
</form>
```



form.as_ul

```django
<form action='.' method='POST'> {% csrf_token %}
    {{form.as_ul}}
    <input type='submit' value='Save'/>
</form>
```

```html
<form action="." method="POST"> <input type="hidden" name="csrfmiddlewaretoken" value="QjeVDEnzXYOfXGaJDGC7Za6XMs9TUyIqyy4Nj2WrASUFJ3rNwu19u3YQBoY7xxJT">
    <li>
    <label for="id_title">Title:</label>
    <input type="text" name="title" required="" id="id_title">
  </li>
  <li>
    <label for="id_description">Description:</label>
    <input type="text" name="description" required="" id="id_description">
  </li>
  <li>
    <label for="id_price">Price:</label>
    <input type="number" name="price" step="any" required="" id="id_price">
  </li>
    <input type="submit" value="Save">
</form>
```







[products\views.py]

- form method POST
- RawProductForm(request.POST)
	- /create/ 처음 접속했을 때
		request.POST에 요소가 없기 때문에 '필수 항목입니다.' 가 바로 출력이 됨

submit 했던 값들이 input 에 다시 들어감

```python
def product_create_view(request):
    my_form = RawProductForm(request.POST)
    context = {
        'form': my_form
    }
    return render(request, 'products/product_create.html', context)
```



if request.method == 'POST'

```python
def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
    context = {
        'form': my_form
    }
    return render(request, 'products/product_create.html', context)
```



my_form.cleaned_data
my_form.errors

```python
def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, 'products/product_create.html', context)
```



submit

```css
{'title': 'title is awesome', 'description': 'ㅇ0ㅇ', 'price': Decimal('4.99')}
"POST /create/ HTTP/1.1" 200 942
```



required를 개발자모드로 강제로 제거하고 error(description) 출력함

```css
<ul class="errorlist"><li>description<ul class="errorlist"><li>필수 항목입니다.</li></ul></li></ul>
"POST /create/ HTTP/1.1" 200 985
```







[products\views.py]

```python
def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, 'products/product_create.html', context)
```

```css
TypeError: create() takes 1 positional argument but 2 were given
"POST /create/ HTTP/1.1" 500 71954
```



**my_form.cleaned_data

```python
def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, 'products/product_create.html', context)
```

```css
{'title': 'hello world', 'description': 'description!', 'price': Decimal('99.99')}
"POST /create/ HTTP/1.1" 200 943
```







# [Form Widgets](https://youtu.be/F5mRW0jo-U4?t=9375)



[products\forms.py]

```python
class RawProductForm(forms.Form):
    title =         forms.CharField(label='')
    description =   forms.CharField(required=False)
    price =         forms.DecimalField(initial=199.99)
```

![form_widgets_1](.\images\form_widgets_1.PNG)

```css
{'title': 'title', 'description': '', 'price': Decimal('199.99')}
"POST /create/ HTTP/1.1" 200 872
```



[products\forms.py]

```python
class RawProductForm(forms.Form):
    title =         forms.CharField(label='')
    description =   forms.CharField(required=False, widget=forms.Textarea)
    price =         forms.DecimalField(initial=199.99)
```

![](.\images\form_widgets_2.PNG)



[products\forms.py]

```python
class RawProductForm(forms.Form):
    title =         forms.CharField(label='')
    description =   forms.CharField(required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "rows": 20
                            }
                        )
                    )
    price =         forms.DecimalField(initial=199.99)
```

![](.\images\form_widgets_3.PNG)

```html
<textarea name="description" cols="40" rows="20" class="new-class-name two" id="id_description"></textarea>
```







[products\forms.py]

```python
class RawProductForm(forms.Form):
    title =         forms.CharField(label='')
    description =   forms.CharField(required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "rows": 10,
                                "cols": 10
                            }
                        )
                    )
    price =         forms.DecimalField(initial=199.99)
```

![](.\images\form_widgets_4.PNG)



[products\forms.py]

```python
class RawProductForm(forms.Form):
    title =         forms.CharField(label='')
    description =   forms.CharField(required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "id": "my-id-for-textareas",
                                "rows": 10,
                                "cols": 10
                            }
                        )
                    )
    price =         forms.DecimalField(initial=199.99)
```

```html
<textarea name="description" cols="10" rows="10" class="new-class-name two" id="my-id-for-textareas"></textarea>
```



[products\forms.py]

```python
class RawProductForm(forms.Form):
    title =         forms.CharField(label='',
                        widget=forms.TextInput(
                            attrs={"placeholder": "Your title"}
                        )
                    )
    description =   forms.CharField(required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "id": "my-id-for-textareas",
                                "rows": 10,
                                "cols": 10
                            }
                        )
                    )
    price =         forms.DecimalField(initial=199.99)
```

![](.\images\form_widgets_5.PNG)



[products\forms.py]

```python
class RawProductForm(forms.Form):
    title =         forms.CharField(label='',
                        widget=forms.TextInput(
                            attrs={"placeholder": "Your title"}
                        )
                    )
    description =   forms.CharField(required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "placeholder": "Your description",
                                "id": "my-id-for-textareas",
                                "rows": 10,
                                "cols": 10
                            }
                        )
                    )
    price =         forms.DecimalField(initial=199.99)
```

![](.\images\form_widgets_6.PNG)







# Form Validation Methods



[products\forms.py]

```python
class ProductForm(forms.ModelForm):
    title = forms.CharField(
                label='',
                widget=forms.TextInput(
                    attrs={"placeholder": "Your title"}
                )
            ) # new

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
```



[products\views.py]

```python
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

# "POST /create/ HTTP/1.1" 200 892
```







[products\forms.py]
RawProductForm 참고하기

```python
class ProductForm(forms.ModelForm):
    title =         forms.CharField(
                        label='',
                        widget=forms.TextInput(
                            attrs={"placeholder": "Your title"}
                        )
                    )

    description =   forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "placeholder": "Your description",
                                "id": "my-id-for-textareas",
                                "rows": 10,
                                "cols": 10
                            }
                        )
                    )

    price =         forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if '2022' in title:
            return title
        else:
            raise forms.ValidationError('This is not a valid title!!!')
```

![](.\images\FormValidationMethods1.PNG)



```python
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not '2022' in title:
            raise forms.ValidationError('This is not a valid title')
        if not 'news' in title:
            raise forms.ValidationError('This is not a valid title')
        return title
```

'news', '2022' 문자열을 포함하지 않으면 raise!

![](.\images\FormValidationMethods2.PNG)







EmailField

```python
class ProductForm(forms.ModelForm):
    title =         forms.CharField(
                        label='',
                        widget=forms.TextInput(
                            attrs={"placeholder": "Your title"}
                        )
                    )

    email =         forms.EmailField()

    description =   forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "placeholder": "Your description",
                                "id": "my-id-for-textareas",
                                "rows": 10,
                                "cols": 10
                            }
                        )
                    )

    price =         forms.DecimalField(initial=199.99)

    class Meta:  # ModelForm
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not '2022' in title:
            raise forms.ValidationError('This is not a valid title')
        if not 'news' in title:
            raise forms.ValidationError('This is not a valid title')
        return title

    def clean_email(self, *args, **kwargs):
        email: str = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('This is not a valid email')
        return email
```

![](.\images\FormValidationMethods3.PNG)







# Initial Values for Forms



[products\views.py]

```python
def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title :3"
    }

    form = RawProductForm(
        request.POST or None,
        initial=initial_data
    )

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)
```


[trydjango\urls.py]

```python
from products.views import render_initial_data

urlpatterns = [
    path('', home_view, name='home'),
    path('initial/', render_initial_data),
    path('admin/', admin.site.urls),
]
```

![](.\images\InitialValuesforForms1.PNG)



[products\views.py]

```python
def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title :3"
    }

    obj = Product.objects.get(id=1)

    form = ProductForm(
        request.POST or None,
        initial=initial_data,
        instance=obj
    )

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)
```

![](.\images\InitialValuesforForms2.PNG)



[products\views.py]

```python
def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title :3"
    }

    obj = Product.objects.get(id=1)

    form = ProductForm(
        request.POST or None,
        # initial=initial_data,
        instance=obj
    )

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)
```

![](.\images\InitialValuesforForms3.PNG)







[Update]
[products\views.py]

```python
def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title :3"
    }

    obj = Product.objects.get(id=1)

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
```



[products\forms.py]

```python
    def clean_title(self, *args, **kwargs):
        title: str = self.cleaned_data.get('title')
        # if not '2022' in title:
        #     raise forms.ValidationError('This is not a valid title')
        # if not 'news' in title:
        #     raise forms.ValidationError('This is not a valid title')
        return title

    def clean_email(self, *args, **kwargs):
        email: str = self.cleaned_data.get('email')
        # if not email.endswith('edu'):
        #     raise forms.ValidationError('This is not a valid email')
        return email
```



submit
![4](.\images\InitialValuesforForms4-1.PNG)



"POST /initial/ HTTP/1.1" 200 1149
![4](.\images\InitialValuesforForms4-2.PNG)







# Dynamic URL Routing



[products\views.py]
(request) → (request, id)

```python
from .models import Product

def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
```



[trydjango\urls.py]
\<int:id\>

```python
from products.views import dynamic_lookup_view

urlpatterns = [
    path('products/<int:id>/', dynamic_lookup_view, name='product'),
]

# "GET /products/1/ HTTP/1.1" 200 292
```

\<int:my_id\> 일 경우, dynamic_lookup_view의 파라미터를 my_id로 변경







# Handle DoesNotExist



[products\views.py]

```python
from django.shortcuts import render, get_object_or_404
from .models import Product

def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
```

```css
변경 전: "GET /products/15/ HTTP/1.1" 500 75230
변경 후: "GET /products/15/ HTTP/1.1" 404 2326
```



[products\views.py]

```python
from django.http import Http404
from django.shortcuts import render
from .models import Product

def dynamic_lookup_view(request, my_id):
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
```

```css
"GET /products/15/ HTTP/1.1" 404 2256
```









# Delete and Confirm



[products\views.py]

```python
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Product

def product_delete_view(request, obj_id):
    obj = get_object_or_404(Product, id=obj_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)

def dynamic_lookup_view(request, obj_id):
    obj = get_object_or_404(Product, id=obj_id)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)

```



[products\templates\products\product_delete.html]

```django
{% extends 'base.html' %}
{% block content %}
<form action='.' method='POST'> {% csrf_token %}
    <h1>Do you want to delete the product "{{object.title}}"?</h1>
    <p><input type='submit' value='Yes' /> <a href='../'>Cancel</a></p>
</form>
{% endblock content %}
```



[trydjango\urls.py]

```python
from products.views import dynamic_lookup_view, product_delete_view

urlpatterns = [
    path('products/<int:obj_id>/delete/', product_delete_view, name='product-delete'),
    path('products/<int:obj_id>/', dynamic_lookup_view, name='product'),
]
```

```css
"GET /products/1/ HTTP/1.1" 200 292
"GET /products/1/delete HTTP/1.1" 301 0
"GET /products/1/delete/ HTTP/1.1" 200 532
"POST /products/1/delete/ HTTP/1.1" 302 0
Not Found: /products/1/
"GET /products/1/ HTTP/1.1" 404 2482
```







# View of a List of Database objects

https://youtu.be/F5mRW0jo-U4?t=10703



[products\views.py]

```python
from django.shortcuts import render
from .models import Product

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)
```



[products\templates\products\product_list.html]

```django
{% extends 'base.html' %}
{% block content %}
{{object_list}}

{% for instance in object_list %}
    <p>{{instance.id}} - {{instance.title}}</p>
{% endfor %}

{% endblock content %}
```



[trydjango\urls.py]
product_list_view

```python
urlpatterns = [
    path('products/', product_list_view, name='product-list'),
    path('products/<int:obj_id>/delete/', product_delete_view, name='product-delete'),
    path('products/<int:obj_id>/', dynamic_lookup_view, name='product'),
]
```

![](.\images\ViewofaListofDatabaseobjects1.PNG)







# Dynamic Linking of URLs



[products\templates\products\product_list.html]
Dynamic Linking - Before

```django
{% extends 'base.html' %}
{% block content %}

{% for instance in object_list %}
    <p>{{instance.id}} - <a href='/products/{{instance.id}}'>{{instance.title}}</a></p>
{% endfor %}

{% endblock content %}
```

![](.\images\DynamicLinkingofURLs1.PNG)







[pages\models.py]

```python
class Product(models.Model):
    title =         models.CharField(max_length=120)
    description =   models.TextField(blank=True, null=True)
    price =         models.DecimalField(decimal_places=2, max_digits=10000)
    summary =       models.TextField(blank=False, null=False)
    featured =      models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'/products/{self.id}'
```



[products\templates\products\product_list.html]
Dynamic Linking - After

```django
{% extends 'base.html' %}
{% block content %}

{% for instance in object_list %}
    <p>{{instance.id}} - <a href='{{instance.get_absolute_url}}'>{{instance.title}}</a></p>
{% endfor %}

{% endblock content %}
```







# Django URLs Reverse



[products\models.py]

```python
    def get_absolute_url(self):
        # return f'/products/{self.id}'
        return reverse('product-detail', kwargs={'obj_id': self.id})
```



[trydjango\urls.py]
'products/\<int:obj_id\>/' → 'p/\<int:obj_id\>/'
reverse 하는 김에 route 인자 변경

```python
urlpatterns = [
	#
    path('p/<int:obj_id>/', dynamic_lookup_view, name='product-detail'),
    #
]
```

```css
"GET /products/ HTTP/1.1" 200 650
"GET /p/2/ HTTP/1.1" 200 314
"GET /p/10/ HTTP/1.1" 200 308
```







# In App URLs and Namespacing

https://youtu.be/F5mRW0jo-U4?t=10991



[products\views.py]

```python
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Product
from .forms import ProductForm

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
```



[trydjango\urls.py]
'product-detail' → 'products/\<int:obj_id\>/'

```python
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view
from products.views import (
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_list_view,
    product_update_view,
)

urlpatterns = [
    path('products/', product_list_view, name='product-list'),
    path('products/create/', product_create_view, name='product-create'),
    path('products/<int:obj_id>/', product_detail_view, name='product-detail'),
    path('products/<int:obj_id>/update/', product_update_view, name='product-update'),
    path('products/<int:obj_id>/delete/', product_delete_view, name='product-delete'),

    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
```



[trydjango\urls.py]
'product-detail' → 'about/\<int:obj_id\>/'

```python
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view
from products.views import (
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_list_view,
    product_update_view,
)

urlpatterns = [
    path('products/', product_list_view, name='product-list'),
    path('products/create/', product_create_view, name='product-create'),
    path('products/<int:obj_id>/', product_detail_view, name='product-detail'),
    path('products/<int:obj_id>/update/', product_update_view, name='product-update'),
    path('products/<int:obj_id>/delete/', product_delete_view, name='product-delete'),

    path('', home_view, name='home'),
    path('about/<int:obj_id>/', about_view, name='product-detail'),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
```











[새로운 urls]
[products\urls.py]

```python
from django.urls import path
from products.views import (
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_list_view,
    product_update_view,
)

urlpatterns = [
    path('products/', product_list_view, name='product-list'),
    path('products/create/', product_create_view, name='product-create'),
    path('products/<int:obj_id>/', product_detail_view, name='product-detail'),
    path('products/<int:obj_id>/update/', product_update_view, name='product-update'),
    path('products/<int:obj_id>/delete/', product_delete_view, name='product-delete'),
]
```



[trydjango\urls.py]
products에 새로운 urls가 생겼으니 메인 urls에 include 할 것

```python
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pages.views import home_view, contact_view, about_view
# from products.views import (
#     product_create_view,
#     product_detail_view,
#     product_delete_view,
#     product_list_view,
#     product_update_view,
# )

urlpatterns = [
    # path('blog/', include('blog.urls')),
    path('products/', include('products.urls')),
    
    path('', home_view, name='home'),
    path('about/<int:obj_id>/', about_view, name='product-detail'),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
```


products urls를 수정해야 함

```css
"GET /products/ HTTP/1.1" 404 3492
"GET /products/products HTTP/1.1" 301 0
"GET /products/products/ HTTP/1.1" 200 574
```







[products\urls.py]
about?

```python
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:obj_id>/', product_detail_view, name='product-detail'),
    path('<int:obj_id>/update/', product_update_view, name='product-update'),
    path('<int:obj_id>/delete/', product_delete_view, name='product-delete'),
]
```

```css
"GET /products/ HTTP/1.1" 200 574
"GET /about/2/ HTTP/1.1" 200 618
```



[products\urls.py]
app_name

```python
app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:obj_id>/', product_detail_view, name='product-detail'),
    path('<int:obj_id>/update/', product_update_view, name='product-update'),
    path('<int:obj_id>/delete/', product_delete_view, name='product-delete'),
]
```



[products\models.py]
'product-detail' → 'products:product-detail'

```python
    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'obj_id': self.id})
```

```css
"GET /products/ HTTP/1.1" 200 595
"GET /products/2/ HTTP/1.1" 200 291
```







# Class Based Views - ListView



```css
1. Create a New App named Blog
2. Add 'Blog' to your Django project
3. Create a Model named Article
4. Run Migrations
5. Create a ModelForm for Article
6. Create 'article_list.html' & 'article_detail.html' Template
7. Add Article Model to the Admin
8. Save a new Article object in the admin
Confused? Start here: https://kirr.co/9ypik6
```

```css
tree

#blog (1, 2)
	#migrations (4)
	#templates
		#articles
			-article_list.html (6)
			-article_detail.html (6)
	-models.py (3)
	-forms.py (5)
	-admin.py (7)

http://127.0.0.1:8000/admin/blog/article/ (8)
```





#### 1. Create a New App named Blog

```cmd
\trydjango>python manage.py startapp blog
```





#### 2. Add 'Blog' to your Django project

```cmd
\trydjango>dir
<DIR>    blog
<DIR>    pages
<DIR>    products
<DIR>    templates
<DIR>    trydjango
...
```





#### 3. Create a Model named Article

[blog\models.py]

```python
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)
```



[trydjango\settings.py]

```python
INSTALLED_APPS = [
    #
    'blog',
    'pages',
    'products',
]
```





#### 4. Run Migrations

```cmd
\trydjango>python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Article
    
\trydjango>python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, products, sessions
Running migrations:
  Applying blog.0001_initial... OK
```





#### 5. Create a ModelForm for Article

[blog\forms.py]
fields를 field라고 선언하면 runserver 진행 중에 raise가 일어나니 주의할 것

```python
from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]
```





#### 6. Create 'article_list.html' & 'article_detail.html' Template

products\templates\products 참고하기



[blog\templates\articles\article_list.html]

```django
{% extends 'base.html' %}
{% block content %}
{% for instance in object_list %}
    <p>{{instance.id}} - <a href='./{{instance.id}}'>{{instance.title}}</a></p>
{% endfor %}
{% endblock content %}
```



[blog\templates\articles\article_detail.html]
title, content, active

```django
{% extends 'base.html' %}
{% block content %}
<h1>{{object.title}}</h1>
<p>{{object.content}}</p>
<p>{{object.active}}</p>
{% endblock content %}
```





#### 7. Add Article Model to the Admin

```python
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```





#### 8. Save a new Article object in the admin

http://127.0.0.1:8000/admin/blog/article/

```css
[09:03:27] "GET /admin/blog/article/add/ HTTP/1.1" 200 7225
[09:03:27] "GET /admin/jsi18n/ HTTP/1.1" 200 8911

[09:03:45] "POST /admin/blog/article/add/ HTTP/1.1" 302 0
[09:03:45] "GET /admin/blog/article/ HTTP/1.1" 200 7070
```







[blog\views.py]
ArticleListView 객체만 만들고 urls.py 편집하기

```python
from django.shortcuts import render

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.all()
```



[blog\urls.py]

```python
from django.urls import path
from .views import (
    ArticleListView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
]
```



[trydjango\urls.py]
include('blog.urls')

```python
urlpatterns = [
    path('blog/', include('blog.urls')),
    path('products/', include('products.urls')),

    path('', home_view, name='home'),
    path('about/<int:obj_id>/', about_view, name='product-detail'),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
```

```css
django.template.exceptions.TemplateDoesNotExist: blog/article_list.html
"GET /blog/ HTTP/1.1" 500 81061
```







[blog\views.py]

```python
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html
```

```css
"GET /blog/ HTTP/1.1" 200 286
```







# Class Based Views - DetailView



[blog\views.py]
클래스 이름, 상속 클래스, 템플렛 이름만 변경하고 urls.py로 이동하기

```python
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()
```



[blog\urls.py]

```python
from .views import (
    ArticleDetailView,
    ArticleListView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    
    # path('', product_list_view, name='product-list'),
    # path('create/', product_create_view, name='product-create'),
    # path('<int:obj_id>/', product_detail_view, name='product-detail'),
    # path('<int:obj_id>/update/', product_update_view, name='product-update'),
    # path('<int:obj_id>/delete/', product_delete_view, name='product-delete'),
]
```



[blog\templates\articles\article_detail.html]
html 다시 확인하기

```django
{% extends 'base.html' %}
{% block content %}
<h1>{{object.title}}</h1>
<p>{{object.content}}</p>
<p>{{object.active}}</p>
{% endblock content %}
```

```css
"GET /blog/ HTTP/1.1" 200 286
"GET /blog/1/ HTTP/1.1" 200 289
```



[blog\views.py]
template_name 주석처리하고 접속해보기

```python
class ArticleDetailView(DetailView):
    # template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()
```

```css
django.template.exceptions.TemplateDoesNotExist: blog/article_detail.html
"GET /blog/1/ HTTP/1.1" 500 81132
```



[blog\urls.py]
int:pk → int:id

```python
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
]
```

```css
"GET /blog HTTP/1.1" 301 0
"GET /blog/ HTTP/1.1" 200 286

Internal Server Error: /blog/1/
AttributeError: Generic detail view ArticleDetailView must be called with either an object pk or a slug 
in the URLconf.
"GET /blog/1/ HTTP/1.1" 500 80666
```

```python
class Article(models.Model):
    # id(pk)
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)
```



[blog\urls.py]
int:slug

```python
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
```

```css
django.core.exceptions.FieldError: Cannot resolve keyword 'slug' into field. Choices are: active, content, id, title
"GET /blog/1/ HTTP/1.1" 500 119365
```







[blog\urls.py]
int:pk

```python
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
```



[blog\views.py]

```python
class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        obj_id = self.kwargs.get('pk')
        return get_object_or_404(Article, id=obj_id)
```

```css
"GET /blog/ HTTP/1.1" 200 289
"GET /blog/1/ HTTP/1.1" 200 289
"GET /blog/2 HTTP/1.1" 301 0
Not Found: /blog/2/
"GET /blog/2/ HTTP/1.1" 404 2566, No Article matches the given query.
```







# Class Based Views - CreateView



[blog\views.py]
클래스 이름. 상속 클래스. 템플렛 이름만 변경하고 html, urls 작성하기

```python
from .forms import ArticleModelForm

# Create your views here.
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
```



[blog\templates\articles\article_create.html]
참조: products\templates\products\product_create.html

```django
{% extends 'base.html' %}
{% block content %}

<form action='.' method='POST'> {% csrf_token %}
    {{form.as_p}}
    <input type='submit' value='Save'/>
</form>

{% endblock content %}
```



[blog\urls.py]

```python
from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),

    # path('', product_list_view, name='product-list'),
    # path('create/', product_create_view, name='product-create'),
    # path('<int:obj_id>/', product_detail_view, name='product-detail'),
    # path('<int:obj_id>/update/', product_update_view, name='product-update'),
    # path('<int:obj_id>/delete/', product_delete_view, name='product-delete'),
]
```

```css
django.core.exceptions.ImproperlyConfigured: Using ModelFormMixin (base class of ArticleCreateView) without the 'fields' attribute is prohibited.
[22/Jan/2022 07:31:05] "GET /blog/create/ HTTP/1.1" 500 92956
```



[blog\views.py]

```python
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
```

```css
"GET /blog/create/ HTTP/1.1" 200 890
```



```python
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
```

```css
django.core.exceptions.ImproperlyConfigured: No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
"POST /blog/create/ HTTP/1.1" 500 102766
```



[blog\models.py]

```python
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
```

```css
"GET /blog/create/ HTTP/1.1" 200 890

{'title': '20220122', 'content': '0821', 'active': True}
"POST /blog/create/ HTTP/1.1" 302 0
"GET /blog/3/ HTTP/1.1" 200 280
```







# UpdateView



[blog\views.py]

```python
class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
        
    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=obj_id)
```



[blog\urls.py]

```python
from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
]
```

```css
"GET /blog/3/ HTTP/1.1" 200 280

"GET /blog/3/update HTTP/1.1" 301 0
"GET /blog/3/update/ HTTP/1.1" 200 911

{'title': '20220122', 'content': '0832', 'active': True}
"POST /blog/3/update/ HTTP/1.1" 302 0
"GET /blog/3/ HTTP/1.1" 200 280
```







# DeleteView



[blog\views.py]
get_success_url 없을 때: [500 Internal Server Error](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/500)

```python
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=obj_id)
```



[blog\urls.py]

```python
from .views import (
    ArticleDeleteView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')
]
```

```css
"GET /blog/2/delete HTTP/1.1" 301 0
"GET /blog/2/delete/ HTTP/1.1" 200 530

Internal Server Error: /blog/2/delete/
django.core.exceptions.ImproperlyConfigured: No URL to redirect to. Provide a success_url.
"POST /blog/2/delete/ HTTP/1.1" 500 85028
```







[blog\views.py]
get_success_url 있을 때: [200 OK](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/200)

```python
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    # success_url = '/blog/'

    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=obj_id)

    def get_success_url(self) -> str:
        # return reverse('blog(app_name):list-view(name)')
        return reverse('articles:article-list')
```

```css
"GET /blog/2/delete/ HTTP/1.1" 200 530

"POST /blog/2/delete/ HTTP/1.1" 302 0
"GET /blog/ HTTP/1.1" 200 332
```

