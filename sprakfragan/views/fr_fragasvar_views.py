from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import FrFragasvar
from ..forms import FrFragasvarForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class FrFragasvarListView(ListView):
    model = FrFragasvar
    template_name = "sprakfragan/fr_fragasvar_list.html"
    paginate_by = 20
    context_object_name = "fr_fragasvar_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(FrFragasvarListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(FrFragasvarListView, self).get_queryset()

    def get_allow_empty(self):
        return super(FrFragasvarListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(FrFragasvarListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(FrFragasvarListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(FrFragasvarListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(FrFragasvarListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(FrFragasvarListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarListView, self).get_template_names()


class FrFragasvarDetailView(DetailView):
    model = FrFragasvar
    template_name = "sprakfragan/fr_fragasvar_detail.html"
    context_object_name = "fr_fragasvar"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(FrFragasvarDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarDetailView, self).get_template_names()


class FrFragasvarCreateView(CreateView):
    model = FrFragasvar
    form_class = FrFragasvarForm
    # fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar', 'idgammalt']
    template_name = "sprakfragan/fr_fragasvar_create.html"
    success_url = reverse_lazy("fr_fragasvar_list")

    def __init__(self, **kwargs):
        return super(FrFragasvarCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(FrFragasvarCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(FrFragasvarCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FrFragasvarCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FrFragasvarCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FrFragasvarCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(FrFragasvarCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FrFragasvarCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_detail", args=(self.object.pk,))


class FrFragasvarUpdateView(UpdateView):
    model = FrFragasvar
    form_class = FrFragasvarForm
    # fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar', 'idgammalt']
    template_name = "sprakfragan/fr_fragasvar_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "fr_fragasvar"

    def __init__(self, **kwargs):
        return super(FrFragasvarUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(FrFragasvarUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FrFragasvarUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FrFragasvarUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FrFragasvarUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(FrFragasvarUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FrFragasvarUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_detail", args=(self.object.pk,))


class FrFragasvarDeleteView(DeleteView):
    model = FrFragasvar
    template_name = "sprakfragan/fr_fragasvar_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "fr_fragasvar"

    def __init__(self, **kwargs):
        return super(FrFragasvarDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(FrFragasvarDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_list")
