from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AreInlagg
from ..forms import AreInlaggForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AreInlaggListView(ListView):
    model = AreInlagg
    template_name = "sprakfragan/are_inlagg_list.html"
    paginate_by = 20
    context_object_name = "are_inlagg_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AreInlaggListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AreInlaggListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AreInlaggListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AreInlaggListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AreInlaggListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AreInlaggListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AreInlaggListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AreInlaggListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AreInlaggListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AreInlaggListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AreInlaggListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreInlaggListView, self).get_template_names()


class AreInlaggDetailView(DetailView):
    model = AreInlagg
    template_name = "sprakfragan/are_inlagg_detail.html"
    context_object_name = "are_inlagg"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AreInlaggDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AreInlaggDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AreInlaggDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AreInlaggDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AreInlaggDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AreInlaggDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AreInlaggDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AreInlaggDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AreInlaggDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreInlaggDetailView, self).get_template_names()


class AreInlaggCreateView(CreateView):
    model = AreInlagg
    form_class = AreInlaggForm
    # fields = ['idare_inlagg', 'rubrik', 'text', 'regdatum', 'tidsstampel', 'are_arende_idare_arende', 'are_medium_idare_medium', 'are_inlaggstyp_idare_inlaggstyp', 'anvandare_idanvandare']
    template_name = "sprakfragan/are_inlagg_create.html"
    success_url = reverse_lazy("are_inlagg_list")

    def __init__(self, **kwargs):
        return super(AreInlaggCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AreInlaggCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AreInlaggCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AreInlaggCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AreInlaggCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AreInlaggCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AreInlaggCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AreInlaggCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AreInlaggCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AreInlaggCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AreInlaggCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AreInlaggCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreInlaggCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("are_inlagg_detail", args=(self.object.pk,))


class AreInlaggUpdateView(UpdateView):
    model = AreInlagg
    form_class = AreInlaggForm
    # fields = ['idare_inlagg', 'rubrik', 'text', 'regdatum', 'tidsstampel', 'are_arende_idare_arende', 'are_medium_idare_medium', 'are_inlaggstyp_idare_inlaggstyp', 'anvandare_idanvandare']
    template_name = "sprakfragan/are_inlagg_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "are_inlagg"

    def __init__(self, **kwargs):
        return super(AreInlaggUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AreInlaggUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AreInlaggUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AreInlaggUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AreInlaggUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AreInlaggUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AreInlaggUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AreInlaggUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AreInlaggUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AreInlaggUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AreInlaggUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AreInlaggUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AreInlaggUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AreInlaggUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AreInlaggUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AreInlaggUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreInlaggUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("are_inlagg_detail", args=(self.object.pk,))


class AreInlaggDeleteView(DeleteView):
    model = AreInlagg
    template_name = "sprakfragan/are_inlagg_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "are_inlagg"

    def __init__(self, **kwargs):
        return super(AreInlaggDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AreInlaggDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AreInlaggDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AreInlaggDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AreInlaggDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AreInlaggDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AreInlaggDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AreInlaggDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AreInlaggDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AreInlaggDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreInlaggDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("are_inlagg_list")
