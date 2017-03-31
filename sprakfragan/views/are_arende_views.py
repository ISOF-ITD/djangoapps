from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AreArende
from ..forms import AreArendeForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AreArendeListView(ListView):
    model = AreArende
    template_name = "sprakfragan/are_arende_list.html"
    paginate_by = 20
    context_object_name = "are_arende_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AreArendeListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AreArendeListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AreArendeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AreArendeListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AreArendeListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AreArendeListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AreArendeListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AreArendeListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AreArendeListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AreArendeListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AreArendeListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreArendeListView, self).get_template_names()


class AreArendeDetailView(DetailView):
    model = AreArende
    template_name = "sprakfragan/are_arende_detail.html"
    context_object_name = "are_arende"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AreArendeDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AreArendeDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AreArendeDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AreArendeDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AreArendeDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AreArendeDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AreArendeDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AreArendeDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AreArendeDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreArendeDetailView, self).get_template_names()


class AreArendeCreateView(CreateView):
    model = AreArende
    form_class = AreArendeForm
    # fields = ['idare_arende', 'intressant_frageladan', 'intressant_publ_skrift', 'status', 'idtilldelad', 'tidsstampel', 'namn']
    template_name = "sprakfragan/are_arende_create.html"
    success_url = reverse_lazy("are_arende_list")

    def __init__(self, **kwargs):
        return super(AreArendeCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AreArendeCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AreArendeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AreArendeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AreArendeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AreArendeCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AreArendeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AreArendeCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AreArendeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AreArendeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AreArendeCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AreArendeCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreArendeCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("are_arende_detail", args=(self.object.pk,))


class AreArendeUpdateView(UpdateView):
    model = AreArende
    form_class = AreArendeForm
    # fields = ['idare_arende', 'intressant_frageladan', 'intressant_publ_skrift', 'status', 'idtilldelad', 'tidsstampel', 'namn']
    template_name = "sprakfragan/are_arende_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "are_arende"

    def __init__(self, **kwargs):
        return super(AreArendeUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AreArendeUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AreArendeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AreArendeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AreArendeUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AreArendeUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AreArendeUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AreArendeUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AreArendeUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AreArendeUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AreArendeUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AreArendeUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AreArendeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AreArendeUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AreArendeUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AreArendeUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreArendeUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("are_arende_detail", args=(self.object.pk,))


class AreArendeDeleteView(DeleteView):
    model = AreArende
    template_name = "sprakfragan/are_arende_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "are_arende"

    def __init__(self, **kwargs):
        return super(AreArendeDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AreArendeDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AreArendeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AreArendeDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AreArendeDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AreArendeDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AreArendeDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AreArendeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AreArendeDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AreArendeDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AreArendeDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("are_arende_list")
