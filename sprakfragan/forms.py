from django import forms
from .models import FrFragasvar, Nyckelord, FrFragasvarMyisam, DateTest, AreInlagg, AreArende, DateTest2, FrFragasvarTest1


class FrFragasvarForm(forms.ModelForm):

    class Meta:
        model = FrFragasvar
        fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar', 'idgammalt']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(FrFragasvarForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(FrFragasvarForm, self).is_valid()

    def full_clean(self):
        return super(FrFragasvarForm, self).full_clean()

    def clean_idfr_fragasvar(self):
        idfr_fragasvar = self.cleaned_data.get("idfr_fragasvar", None)
        return idfr_fragasvar

    def clean_fraga(self):
        fraga = self.cleaned_data.get("fraga", None)
        return fraga

    def clean_svar(self):
        svar = self.cleaned_data.get("svar", None)
        return svar

    def clean_skapad_av(self):
        skapad_av = self.cleaned_data.get("skapad_av", None)
        return skapad_av

    def clean_skapad_datum(self):
        skapad_datum = self.cleaned_data.get("skapad_datum", None)
        return skapad_datum

    def clean_uppdat_av(self):
        uppdat_av = self.cleaned_data.get("uppdat_av", None)
        return uppdat_av

    def clean_uppdat_datum(self):
        uppdat_datum = self.cleaned_data.get("uppdat_datum", None)
        return uppdat_datum

    def clean_senaste_granskning(self):
        senaste_granskning = self.cleaned_data.get("senaste_granskning", None)
        return senaste_granskning

    def clean_hallbarhet(self):
        hallbarhet = self.cleaned_data.get("hallbarhet", None)
        return hallbarhet

    def clean_redaktor(self):
        redaktor = self.cleaned_data.get("redaktor", None)
        return redaktor

    def clean_publicerad_webb(self):
        publicerad_webb = self.cleaned_data.get("publicerad_webb", None)
        return publicerad_webb

    def clean_publicerad_app(self):
        publicerad_app = self.cleaned_data.get("publicerad_app", None)
        return publicerad_app

    def clean_publicerad_spraktidning(self):
        publicerad_spraktidning = self.cleaned_data.get("publicerad_spraktidning", None)
        return publicerad_spraktidning

    def clean_kommentar(self):
        kommentar = self.cleaned_data.get("kommentar", None)
        return kommentar

    def clean_idgammalt(self):
        idgammalt = self.cleaned_data.get("idgammalt", None)
        return idgammalt

    def clean(self):
        return super(FrFragasvarForm, self).clean()

    def validate_unique(self):
        return super(FrFragasvarForm, self).validate_unique()

    def save(self, commit=True):
        return super(FrFragasvarForm, self).save(commit)


class NyckelordForm(forms.ModelForm):

    class Meta:
        model = Nyckelord
        fields = ['idnyckelord', 'ord_uttryck', 'felaktig_form', 'icke_grundform', 'ordbildningskommentar', 'bojningskommentar', 'betydelsekommentar', 'stavningskommentar', 'ovrig_kommentar', 'idgammalt', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(NyckelordForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(NyckelordForm, self).is_valid()

    def full_clean(self):
        return super(NyckelordForm, self).full_clean()

    def clean_idnyckelord(self):
        idnyckelord = self.cleaned_data.get("idnyckelord", None)
        return idnyckelord

    def clean_ord_uttryck(self):
        ord_uttryck = self.cleaned_data.get("ord_uttryck", None)
        return ord_uttryck

    def clean_felaktig_form(self):
        felaktig_form = self.cleaned_data.get("felaktig_form", None)
        return felaktig_form

    def clean_icke_grundform(self):
        icke_grundform = self.cleaned_data.get("icke_grundform", None)
        return icke_grundform

    def clean_ordbildningskommentar(self):
        ordbildningskommentar = self.cleaned_data.get("ordbildningskommentar", None)
        return ordbildningskommentar

    def clean_bojningskommentar(self):
        bojningskommentar = self.cleaned_data.get("bojningskommentar", None)
        return bojningskommentar

    def clean_betydelsekommentar(self):
        betydelsekommentar = self.cleaned_data.get("betydelsekommentar", None)
        return betydelsekommentar

    def clean_stavningskommentar(self):
        stavningskommentar = self.cleaned_data.get("stavningskommentar", None)
        return stavningskommentar

    def clean_ovrig_kommentar(self):
        ovrig_kommentar = self.cleaned_data.get("ovrig_kommentar", None)
        return ovrig_kommentar

    def clean_idgammalt(self):
        idgammalt = self.cleaned_data.get("idgammalt", None)
        return idgammalt

    def clean_skapad_av(self):
        skapad_av = self.cleaned_data.get("skapad_av", None)
        return skapad_av

    def clean_skapad_datum(self):
        skapad_datum = self.cleaned_data.get("skapad_datum", None)
        return skapad_datum

    def clean_uppdat_av(self):
        uppdat_av = self.cleaned_data.get("uppdat_av", None)
        return uppdat_av

    def clean_uppdat_datum(self):
        uppdat_datum = self.cleaned_data.get("uppdat_datum", None)
        return uppdat_datum

    def clean(self):
        return super(NyckelordForm, self).clean()

    def validate_unique(self):
        return super(NyckelordForm, self).validate_unique()

    def save(self, commit=True):
        return super(NyckelordForm, self).save(commit)


class FrFragasvarMyisamForm(forms.ModelForm):

    class Meta:
        model = FrFragasvarMyisam
        fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(FrFragasvarMyisamForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(FrFragasvarMyisamForm, self).is_valid()

    def full_clean(self):
        return super(FrFragasvarMyisamForm, self).full_clean()

    def clean_idfr_fragasvar(self):
        idfr_fragasvar = self.cleaned_data.get("idfr_fragasvar", None)
        return idfr_fragasvar

    def clean_fraga(self):
        fraga = self.cleaned_data.get("fraga", None)
        return fraga

    def clean_svar(self):
        svar = self.cleaned_data.get("svar", None)
        return svar

    def clean_skapad_av(self):
        skapad_av = self.cleaned_data.get("skapad_av", None)
        return skapad_av

    def clean_skapad_datum(self):
        skapad_datum = self.cleaned_data.get("skapad_datum", None)
        return skapad_datum

    def clean_uppdat_av(self):
        uppdat_av = self.cleaned_data.get("uppdat_av", None)
        return uppdat_av

    def clean_uppdat_datum(self):
        uppdat_datum = self.cleaned_data.get("uppdat_datum", None)
        return uppdat_datum

    def clean_senaste_granskning(self):
        senaste_granskning = self.cleaned_data.get("senaste_granskning", None)
        return senaste_granskning

    def clean_hallbarhet(self):
        hallbarhet = self.cleaned_data.get("hallbarhet", None)
        return hallbarhet

    def clean_redaktor(self):
        redaktor = self.cleaned_data.get("redaktor", None)
        return redaktor

    def clean_publicerad_webb(self):
        publicerad_webb = self.cleaned_data.get("publicerad_webb", None)
        return publicerad_webb

    def clean_publicerad_app(self):
        publicerad_app = self.cleaned_data.get("publicerad_app", None)
        return publicerad_app

    def clean_publicerad_spraktidning(self):
        publicerad_spraktidning = self.cleaned_data.get("publicerad_spraktidning", None)
        return publicerad_spraktidning

    def clean_kommentar(self):
        kommentar = self.cleaned_data.get("kommentar", None)
        return kommentar

    def clean(self):
        return super(FrFragasvarMyisamForm, self).clean()

    def validate_unique(self):
        return super(FrFragasvarMyisamForm, self).validate_unique()

    def save(self, commit=True):
        return super(FrFragasvarMyisamForm, self).save(commit)


class DateTestForm(forms.ModelForm):

    class Meta:
        model = DateTest
        fields = ['idare_arende', 'idtilldelad', 'tidsstampel', 'namn']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DateTestForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DateTestForm, self).is_valid()

    def full_clean(self):
        return super(DateTestForm, self).full_clean()

    def clean_idare_arende(self):
        idare_arende = self.cleaned_data.get("idare_arende", None)
        return idare_arende

    def clean_idtilldelad(self):
        idtilldelad = self.cleaned_data.get("idtilldelad", None)
        return idtilldelad

    def clean_tidsstampel(self):
        tidsstampel = self.cleaned_data.get("tidsstampel", None)
        return tidsstampel

    def clean_namn(self):
        namn = self.cleaned_data.get("namn", None)
        return namn

    def clean(self):
        return super(DateTestForm, self).clean()

    def validate_unique(self):
        return super(DateTestForm, self).validate_unique()

    def save(self, commit=True):
        return super(DateTestForm, self).save(commit)


class AreInlaggForm(forms.ModelForm):

    class Meta:
        model = AreInlagg
        fields = ['idare_inlagg', 'rubrik', 'text', 'regdatum', 'tidsstampel', 'are_arende_idare_arende', 'are_medium_idare_medium', 'are_inlaggstyp_idare_inlaggstyp', 'anvandare_idanvandare']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AreInlaggForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AreInlaggForm, self).is_valid()

    def full_clean(self):
        return super(AreInlaggForm, self).full_clean()

    def clean_idare_inlagg(self):
        idare_inlagg = self.cleaned_data.get("idare_inlagg", None)
        return idare_inlagg

    def clean_rubrik(self):
        rubrik = self.cleaned_data.get("rubrik", None)
        return rubrik

    def clean_text(self):
        text = self.cleaned_data.get("text", None)
        return text

    def clean_regdatum(self):
        regdatum = self.cleaned_data.get("regdatum", None)
        return regdatum

    def clean_tidsstampel(self):
        tidsstampel = self.cleaned_data.get("tidsstampel", None)
        return tidsstampel

    def clean_are_arende_idare_arende(self):
        are_arende_idare_arende = self.cleaned_data.get("are_arende_idare_arende", None)
        return are_arende_idare_arende

    def clean_are_medium_idare_medium(self):
        are_medium_idare_medium = self.cleaned_data.get("are_medium_idare_medium", None)
        return are_medium_idare_medium

    def clean_are_inlaggstyp_idare_inlaggstyp(self):
        are_inlaggstyp_idare_inlaggstyp = self.cleaned_data.get("are_inlaggstyp_idare_inlaggstyp", None)
        return are_inlaggstyp_idare_inlaggstyp

    def clean_anvandare_idanvandare(self):
        anvandare_idanvandare = self.cleaned_data.get("anvandare_idanvandare", None)
        return anvandare_idanvandare

    def clean(self):
        return super(AreInlaggForm, self).clean()

    def validate_unique(self):
        return super(AreInlaggForm, self).validate_unique()

    def save(self, commit=True):
        return super(AreInlaggForm, self).save(commit)


class AreArendeForm(forms.ModelForm):

    class Meta:
        model = AreArende
        fields = ['idare_arende', 'intressant_frageladan', 'intressant_publ_skrift', 'status', 'idtilldelad', 'tidsstampel', 'namn']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AreArendeForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AreArendeForm, self).is_valid()

    def full_clean(self):
        return super(AreArendeForm, self).full_clean()

    def clean_idare_arende(self):
        idare_arende = self.cleaned_data.get("idare_arende", None)
        return idare_arende

    def clean_intressant_frageladan(self):
        intressant_frageladan = self.cleaned_data.get("intressant_frageladan", None)
        return intressant_frageladan

    def clean_intressant_publ_skrift(self):
        intressant_publ_skrift = self.cleaned_data.get("intressant_publ_skrift", None)
        return intressant_publ_skrift

    def clean_status(self):
        status = self.cleaned_data.get("status", None)
        return status

    def clean_idtilldelad(self):
        idtilldelad = self.cleaned_data.get("idtilldelad", None)
        return idtilldelad

    def clean_tidsstampel(self):
        tidsstampel = self.cleaned_data.get("tidsstampel", None)
        return tidsstampel

    def clean_namn(self):
        namn = self.cleaned_data.get("namn", None)
        return namn

    def clean(self):
        return super(AreArendeForm, self).clean()

    def validate_unique(self):
        return super(AreArendeForm, self).validate_unique()

    def save(self, commit=True):
        return super(AreArendeForm, self).save(commit)


class DateTest2Form(forms.ModelForm):

    class Meta:
        model = DateTest2
        fields = ['idare_arende', 'idtilldelad', 'tidsstampel', 'namn']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DateTest2Form, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DateTest2Form, self).is_valid()

    def full_clean(self):
        return super(DateTest2Form, self).full_clean()

    def clean_idare_arende(self):
        idare_arende = self.cleaned_data.get("idare_arende", None)
        return idare_arende

    def clean_idtilldelad(self):
        idtilldelad = self.cleaned_data.get("idtilldelad", None)
        return idtilldelad

    def clean_tidsstampel(self):
        tidsstampel = self.cleaned_data.get("tidsstampel", None)
        return tidsstampel

    def clean_namn(self):
        namn = self.cleaned_data.get("namn", None)
        return namn

    def clean(self):
        return super(DateTest2Form, self).clean()

    def validate_unique(self):
        return super(DateTest2Form, self).validate_unique()

    def save(self, commit=True):
        return super(DateTest2Form, self).save(commit)


class FrFragasvarTest1Form(forms.ModelForm):

    class Meta:
        model = FrFragasvarTest1
        fields = ['idfr_fragasvar', 'fraga', 'svar', 'skapad_av', 'skapad_datum', 'uppdat_av', 'uppdat_datum', 'senaste_granskning', 'hallbarhet', 'redaktor', 'publicerad_webb', 'publicerad_app', 'publicerad_spraktidning', 'kommentar']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(FrFragasvarTest1Form, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(FrFragasvarTest1Form, self).is_valid()

    def full_clean(self):
        return super(FrFragasvarTest1Form, self).full_clean()

    def clean_idfr_fragasvar(self):
        idfr_fragasvar = self.cleaned_data.get("idfr_fragasvar", None)
        return idfr_fragasvar

    def clean_fraga(self):
        fraga = self.cleaned_data.get("fraga", None)
        return fraga

    def clean_svar(self):
        svar = self.cleaned_data.get("svar", None)
        return svar

    def clean_skapad_av(self):
        skapad_av = self.cleaned_data.get("skapad_av", None)
        return skapad_av

    def clean_skapad_datum(self):
        skapad_datum = self.cleaned_data.get("skapad_datum", None)
        return skapad_datum

    def clean_uppdat_av(self):
        uppdat_av = self.cleaned_data.get("uppdat_av", None)
        return uppdat_av

    def clean_uppdat_datum(self):
        uppdat_datum = self.cleaned_data.get("uppdat_datum", None)
        return uppdat_datum

    def clean_senaste_granskning(self):
        senaste_granskning = self.cleaned_data.get("senaste_granskning", None)
        return senaste_granskning

    def clean_hallbarhet(self):
        hallbarhet = self.cleaned_data.get("hallbarhet", None)
        return hallbarhet

    def clean_redaktor(self):
        redaktor = self.cleaned_data.get("redaktor", None)
        return redaktor

    def clean_publicerad_webb(self):
        publicerad_webb = self.cleaned_data.get("publicerad_webb", None)
        return publicerad_webb

    def clean_publicerad_app(self):
        publicerad_app = self.cleaned_data.get("publicerad_app", None)
        return publicerad_app

    def clean_publicerad_spraktidning(self):
        publicerad_spraktidning = self.cleaned_data.get("publicerad_spraktidning", None)
        return publicerad_spraktidning

    def clean_kommentar(self):
        kommentar = self.cleaned_data.get("kommentar", None)
        return kommentar

    def clean(self):
        return super(FrFragasvarTest1Form, self).clean()

    def validate_unique(self):
        return super(FrFragasvarTest1Form, self).validate_unique()

    def save(self, commit=True):
        return super(FrFragasvarTest1Form, self).save(commit)

