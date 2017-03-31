from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Nyckelord
from ..forms import NyckelordForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class NyckelordListView(ListView):
    model = Nyckelord
    template_name = "sprakfragan/nyckelord_list.html"
    paginate_by = 20
    context_object_name = "nyckelord_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(NyckelordListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NyckelordListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NyckelordListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(NyckelordListView, self).get_queryset()

    def get_allow_empty(self):
        return super(NyckelordListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(NyckelordListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(NyckelordListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(NyckelordListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(NyckelordListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(NyckelordListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(NyckelordListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NyckelordListView, self).get_template_names()


class NyckelordDetailView(DetailView):
    model = Nyckelord
    template_name = "sprakfragan/nyckelord_detail.html"
    context_object_name = "nyckelord"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(NyckelordDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NyckelordDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NyckelordDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NyckelordDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(NyckelordDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(NyckelordDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(NyckelordDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NyckelordDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NyckelordDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NyckelordDetailView, self).get_template_names()


class NyckelordCreateView(CreateView):
    model = Nyckelord
    form_class = NyckelordForm
    # fields = ['idnyckelord', 'ord_uttryck', 'felaktig_form', 'icke_grundform', 'ordbildningskommentar', 'bojningskommentar', 'betydelsekommentar', 'stavningskommentar', 'ovrig_kommentar', 'idgammalt', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum']
    template_name = "sprakfragan/nyckelord_create.html"
    success_url = reverse_lazy("nyckelord_list")

    def __init__(self, **kwargs):
        return super(NyckelordCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(NyckelordCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NyckelordCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(NyckelordCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(NyckelordCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(NyckelordCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(NyckelordCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(NyckelordCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(NyckelordCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(NyckelordCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(NyckelordCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(NyckelordCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NyckelordCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("nyckelord_detail", args=(self.object.pk,))


class NyckelordUpdateView(UpdateView):
    model = Nyckelord
    form_class = NyckelordForm
    # fields = ['idnyckelord', 'ord_uttryck', 'felaktig_form', 'icke_grundform', 'ordbildningskommentar', 'bojningskommentar', 'betydelsekommentar', 'stavningskommentar', 'ovrig_kommentar', 'idgammalt', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum']
    template_name = "sprakfragan/nyckelord_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "nyckelord"

    def __init__(self, **kwargs):
        return super(NyckelordUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NyckelordUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(NyckelordUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(NyckelordUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NyckelordUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(NyckelordUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(NyckelordUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(NyckelordUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(NyckelordUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(NyckelordUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(NyckelordUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(NyckelordUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(NyckelordUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(NyckelordUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NyckelordUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NyckelordUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NyckelordUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("nyckelord_detail", args=(self.object.pk,))


class NyckelordDeleteView(DeleteView):
    model = Nyckelord
    template_name = "sprakfragan/nyckelord_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "nyckelord"

    def __init__(self, **kwargs):
        return super(NyckelordDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(NyckelordDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(NyckelordDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(NyckelordDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(NyckelordDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(NyckelordDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(NyckelordDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(NyckelordDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(NyckelordDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(NyckelordDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(NyckelordDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("nyckelord_list")
