from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import FrFragasvarTest1
from ..forms import FrFragasvarTest1Form
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class FrFragasvarTest1ListView(ListView):
    model = FrFragasvarTest1
    template_name = "sprakfragan/fr_fragasvar_test1_list.html"
    paginate_by = 20
    context_object_name = "fr_fragasvar_test1_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(FrFragasvarTest1ListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarTest1ListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarTest1ListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(FrFragasvarTest1ListView, self).get_queryset()

    def get_allow_empty(self):
        return super(FrFragasvarTest1ListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(FrFragasvarTest1ListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(FrFragasvarTest1ListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(FrFragasvarTest1ListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(FrFragasvarTest1ListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(FrFragasvarTest1ListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarTest1ListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarTest1ListView, self).get_template_names()


class FrFragasvarTest1DetailView(DetailView):
    model = FrFragasvarTest1
    template_name = "sprakfragan/fr_fragasvar_test1_detail.html"
    context_object_name = "fr_fragasvar_test1"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(FrFragasvarTest1DetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarTest1DetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarTest1DetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarTest1DetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarTest1DetailView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarTest1DetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarTest1DetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarTest1DetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarTest1DetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarTest1DetailView, self).get_template_names()


class FrFragasvarTest1CreateView(CreateView):
    model = FrFragasvarTest1
    form_class = FrFragasvarTest1Form
    # fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar']
    template_name = "sprakfragan/fr_fragasvar_test1_create.html"
    success_url = reverse_lazy("fr_fragasvar_test1_list")

    def __init__(self, **kwargs):
        return super(FrFragasvarTest1CreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(FrFragasvarTest1CreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarTest1CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarTest1CreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(FrFragasvarTest1CreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FrFragasvarTest1CreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FrFragasvarTest1CreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FrFragasvarTest1CreateView, self).get_initial()

    def form_invalid(self, form):
        return super(FrFragasvarTest1CreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FrFragasvarTest1CreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarTest1CreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarTest1CreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarTest1CreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_test1_detail", args=(self.object.pk,))


class FrFragasvarTest1UpdateView(UpdateView):
    model = FrFragasvarTest1
    form_class = FrFragasvarTest1Form
    # fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar']
    template_name = "sprakfragan/fr_fragasvar_test1_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "fr_fragasvar_test1"

    def __init__(self, **kwargs):
        return super(FrFragasvarTest1UpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarTest1UpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarTest1UpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarTest1UpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarTest1UpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarTest1UpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarTest1UpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(FrFragasvarTest1UpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FrFragasvarTest1UpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FrFragasvarTest1UpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FrFragasvarTest1UpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(FrFragasvarTest1UpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FrFragasvarTest1UpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarTest1UpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarTest1UpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarTest1UpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarTest1UpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_test1_detail", args=(self.object.pk,))


class FrFragasvarTest1DeleteView(DeleteView):
    model = FrFragasvarTest1
    template_name = "sprakfragan/fr_fragasvar_test1_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "fr_fragasvar_test1"

    def __init__(self, **kwargs):
        return super(FrFragasvarTest1DeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarTest1DeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarTest1DeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(FrFragasvarTest1DeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarTest1DeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarTest1DeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarTest1DeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarTest1DeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarTest1DeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarTest1DeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarTest1DeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_test1_list")
