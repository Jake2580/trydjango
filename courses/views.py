from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Course
from .forms import CourseModelForm


class CourseObjectMixin:
    model = Course

    def get_object(self):
        id = self.kwargs.get('id')  # from CourseDeleteView.get_object()

        if id is None:
            return None

        obj = get_object_or_404(self.model, id=id)  # Course → self.model
        return obj


class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'

    # GET Method
    def get(self, request, id=None):  # (self, request, id=None, *args, **kwargs)
        context = dict()
        obj = self.get_object()

        if obj is not None:
            context['object'] = obj

        return render(request, self.template_name, context)

    # POST Method
    def post(self, request, id=None):  # (self, request, id=None, *args, **kwargs)
        context = dict()
        obj = self.get_object()

        if obj is not None:
            # obj.delete()
            print(f'CourseDeleteView.post: 안돼! {id}번 Course 삭제하지마!')
            # context['object'] = None
            return redirect('/courses/')

        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'

    # GET Method
    def get(self, request, id=None, *args, **kwargs):
        context = dict()
        obj = self.get_object()

        if obj is not None:
            form = CourseModelForm(request.GET or None, instance=obj)
            if form.is_valid():
                form.save()

            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)

    # POST Method
    def post(self, request, id=None, *args, **kwargs):
        context = dict()
        obj = self.get_object()

        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()

            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()

        context = {'form': form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'

    def get_queryset(self):
        return Course.objects.all()

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


""" class MyListView(CourseListView):
    queryset = Course.objects.filter(id=1)
    pass """


# BASE VIEW CLASS = VIEW
class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'  # DetailView

    # GET Method
    def get(self, request, id=None, *args, **kwargs):
        context = dict(object=self.get_object())
        return render(request, self.template_name, context)

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})

    pass


""" class CourseView(View):
    template_name = 'about.html'
    def get(self, request, *args, **kwargs):
        # GET Methods
        return render(request, self.template_name, {})  # new_obj = CourseView()

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {}) """

# HTTP Methods
""" def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {}) """
