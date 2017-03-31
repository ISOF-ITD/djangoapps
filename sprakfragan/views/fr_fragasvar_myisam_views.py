from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import FrFragasvarMyisam
from ..forms import FrFragasvarMyisamForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class FrFragasvarMyisamListView(ListView):
    model = FrFragasvarMyisam
    template_name = "sprakfragan/fr_fragasvar_myisam_list.html"
    paginate_by = 20
    context_object_name = "fr_fragasvar_myisam_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(FrFragasvarMyisamListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarMyisamListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(FrFragasvarMyisamListView, self).get_queryset()

    def get_allow_empty(self):
        return super(FrFragasvarMyisamListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(FrFragasvarMyisamListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(FrFragasvarMyisamListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(FrFragasvarMyisamListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(FrFragasvarMyisamListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(FrFragasvarMyisamListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarMyisamListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarMyisamListView, self).get_template_names()


class FrFragasvarMyisamDetailView(DetailView):
    model = FrFragasvarMyisam
    template_name = "sprakfragan/fr_fragasvar_myisam_detail.html"
    context_object_name = "fr_fragasvar_myisam"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(FrFragasvarMyisamDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarMyisamDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarMyisamDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarMyisamDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarMyisamDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarMyisamDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarMyisamDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarMyisamDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarMyisamDetailView, self).get_template_names()


class FrFragasvarMyisamCreateView(CreateView):
    model = FrFragasvarMyisam
    form_class = FrFragasvarMyisamForm
    # fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar']
    template_name = "sprakfragan/fr_fragasvar_myisam_create.html"
    success_url = reverse_lazy("fr_fragasvar_myisam_list")

    def __init__(self, **kwargs):
        return super(FrFragasvarMyisamCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(FrFragasvarMyisamCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FrFragasvarMyisamCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FrFragasvarMyisamCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FrFragasvarMyisamCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(FrFragasvarMyisamCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FrFragasvarMyisamCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarMyisamCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarMyisamCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarMyisamCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_myisam_detail", args=(self.object.pk,))


class FrFragasvarMyisamUpdateView(UpdateView):
    model = FrFragasvarMyisam
    form_class = FrFragasvarMyisamForm
    # fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar']
    template_name = "sprakfragan/fr_fragasvar_myisam_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "fr_fragasvar_myisam"

    def __init__(self, **kwargs):
        return super(FrFragasvarMyisamUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarMyisamUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarMyisamUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarMyisamUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarMyisamUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(FrFragasvarMyisamUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FrFragasvarMyisamUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FrFragasvarMyisamUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FrFragasvarMyisamUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(FrFragasvarMyisamUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FrFragasvarMyisamUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarMyisamUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarMyisamUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarMyisamUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarMyisamUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_myisam_detail", args=(self.object.pk,))


class FrFragasvarMyisamDeleteView(DeleteView):
    model = FrFragasvarMyisam
    template_name = "sprakfragan/fr_fragasvar_myisam_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "fr_fragasvar_myisam"

    def __init__(self, **kwargs):
        return super(FrFragasvarMyisamDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FrFragasvarMyisamDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(FrFragasvarMyisamDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FrFragasvarMyisamDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(FrFragasvarMyisamDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(FrFragasvarMyisamDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FrFragasvarMyisamDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FrFragasvarMyisamDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FrFragasvarMyisamDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FrFragasvarMyisamDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("fr_fragasvar_myisam_list")
