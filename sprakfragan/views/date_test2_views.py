from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DateTest2
from ..forms import DateTest2Form
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DateTest2ListView(ListView):
    model = DateTest2
    template_name = "sprakfragan/date_test2_list.html"
    paginate_by = 20
    context_object_name = "date_test2_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DateTest2ListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DateTest2ListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DateTest2ListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DateTest2ListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DateTest2ListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DateTest2ListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DateTest2ListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DateTest2ListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DateTest2ListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DateTest2ListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DateTest2ListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTest2ListView, self).get_template_names()


class DateTest2DetailView(DetailView):
    model = DateTest2
    template_name = "sprakfragan/date_test2_detail.html"
    context_object_name = "date_test2"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DateTest2DetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DateTest2DetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DateTest2DetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DateTest2DetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DateTest2DetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DateTest2DetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DateTest2DetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DateTest2DetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DateTest2DetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTest2DetailView, self).get_template_names()


class DateTest2CreateView(CreateView):
    model = DateTest2
    form_class = DateTest2Form
    # fields = ['idare_arende', 'idtilldelad', 'tidsstampel', 'namn']
    template_name = "sprakfragan/date_test2_create.html"
    success_url = reverse_lazy("date_test2_list")

    def __init__(self, **kwargs):
        return super(DateTest2CreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DateTest2CreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DateTest2CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DateTest2CreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DateTest2CreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DateTest2CreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DateTest2CreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DateTest2CreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DateTest2CreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DateTest2CreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DateTest2CreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DateTest2CreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTest2CreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("date_test2_detail", args=(self.object.pk,))


class DateTest2UpdateView(UpdateView):
    model = DateTest2
    form_class = DateTest2Form
    # fields = ['idare_arende', 'idtilldelad', 'tidsstampel', 'namn']
    template_name = "sprakfragan/date_test2_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "date_test2"

    def __init__(self, **kwargs):
        return super(DateTest2UpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DateTest2UpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DateTest2UpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DateTest2UpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DateTest2UpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DateTest2UpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DateTest2UpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DateTest2UpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DateTest2UpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DateTest2UpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DateTest2UpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DateTest2UpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DateTest2UpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DateTest2UpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DateTest2UpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DateTest2UpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTest2UpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("date_test2_detail", args=(self.object.pk,))


class DateTest2DeleteView(DeleteView):
    model = DateTest2
    template_name = "sprakfragan/date_test2_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "date_test2"

    def __init__(self, **kwargs):
        return super(DateTest2DeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DateTest2DeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DateTest2DeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DateTest2DeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DateTest2DeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DateTest2DeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DateTest2DeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DateTest2DeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DateTest2DeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DateTest2DeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTest2DeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("date_test2_list")
