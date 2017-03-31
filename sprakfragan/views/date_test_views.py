from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DateTest
from ..forms import DateTestForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DateTestListView(ListView):
    model = DateTest
    template_name = "sprakfragan/date_test_list.html"
    paginate_by = 20
    context_object_name = "date_test_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DateTestListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DateTestListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DateTestListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DateTestListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DateTestListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DateTestListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DateTestListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DateTestListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DateTestListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DateTestListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DateTestListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTestListView, self).get_template_names()


class DateTestDetailView(DetailView):
    model = DateTest
    template_name = "sprakfragan/date_test_detail.html"
    context_object_name = "date_test"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DateTestDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DateTestDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DateTestDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DateTestDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DateTestDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DateTestDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DateTestDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DateTestDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DateTestDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTestDetailView, self).get_template_names()


class DateTestCreateView(CreateView):
    model = DateTest
    form_class = DateTestForm
    # fields = ['idare_arende', 'idtilldelad', 'tidsstampel', 'namn']
    template_name = "sprakfragan/date_test_create.html"
    success_url = reverse_lazy("date_test_list")

    def __init__(self, **kwargs):
        return super(DateTestCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DateTestCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DateTestCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DateTestCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DateTestCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DateTestCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DateTestCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DateTestCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DateTestCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DateTestCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DateTestCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DateTestCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTestCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("date_test_detail", args=(self.object.pk,))


class DateTestUpdateView(UpdateView):
    model = DateTest
    form_class = DateTestForm
    # fields = ['idare_arende', 'idtilldelad', 'tidsstampel', 'namn']
    template_name = "sprakfragan/date_test_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "date_test"

    def __init__(self, **kwargs):
        return super(DateTestUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DateTestUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DateTestUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DateTestUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DateTestUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DateTestUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DateTestUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DateTestUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DateTestUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DateTestUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DateTestUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DateTestUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DateTestUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DateTestUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DateTestUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DateTestUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTestUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("date_test_detail", args=(self.object.pk,))


class DateTestDeleteView(DeleteView):
    model = DateTest
    template_name = "sprakfragan/date_test_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "date_test"

    def __init__(self, **kwargs):
        return super(DateTestDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DateTestDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DateTestDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DateTestDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DateTestDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DateTestDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DateTestDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DateTestDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DateTestDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DateTestDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DateTestDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("date_test_list")
