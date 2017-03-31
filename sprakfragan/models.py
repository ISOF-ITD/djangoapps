# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AreArende(models.Model):
    idare_arende = models.AutoField(primary_key=True)
    intressant_frageladan = models.TextField(blank=True, null=True)  # This field type is a guess.
    intressant_publ_skrift = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.IntegerField()
    idtilldelad = models.IntegerField(blank=True, null=True)
    tidsstampel = models.DateTimeField()
    namn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'are_arende'


class AreInlagg(models.Model):
    idare_inlagg = models.AutoField(primary_key=True)
    rubrik = models.TextField()
    text = models.TextField(blank=True, null=True)
    regdatum = models.DateField()
    tidsstampel = models.DateTimeField()
    are_arende_idare_arende = models.ForeignKey(AreArende, models.DO_NOTHING, db_column='are_arende_idare_arende')
    are_medium_idare_medium = models.IntegerField()
    are_inlaggstyp_idare_inlaggstyp = models.IntegerField()
    anvandare_idanvandare = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'are_inlagg'


class DateTest(models.Model):
    idare_arende = models.AutoField(primary_key=True)
    idtilldelad = models.IntegerField(blank=True, null=True)
    tidsstampel = models.DateTimeField()
    namn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'date_test'


class DateTest2(models.Model):
    idare_arende = models.AutoField(primary_key=True)
    idtilldelad = models.IntegerField(blank=True, null=True)
    tidsstampel = models.DateTimeField()
    namn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'date_test2'


class FrFragasvar(models.Model):
    idfr_fragasvar = models.AutoField(primary_key=True)
    fraga = models.TextField()
    svar = models.TextField()
    skapad_av = models.CharField(max_length=45, blank=True, null=True)
    skapad_datum = models.DateTimeField(blank=True, null=True)
    uppdat_av = models.CharField(max_length=45, blank=True, null=True)
    uppdat_datum = models.DateTimeField(blank=True, null=True)
    senaste_granskning = models.DateField(blank=True, null=True)
    hallbarhet = models.IntegerField(blank=True, null=True)
    redaktor = models.CharField(max_length=255, blank=True, null=True)
    publicerad_webb = models.DateField(blank=True, null=True)
    publicerad_app = models.DateField(blank=True, null=True)
    publicerad_spraktidning = models.DateField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    idgammalt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_fragasvar'


class FrFragasvarMyisam(models.Model):
    idfr_fragasvar = models.IntegerField()
    fraga = models.TextField()
    svar = models.TextField()
    skapad_av = models.CharField(max_length=45, blank=True, null=True)
    skapad_datum = models.DateTimeField(blank=True, null=True)
    uppdat_av = models.CharField(max_length=45, blank=True, null=True)
    uppdat_datum = models.DateTimeField(blank=True, null=True)
    senaste_granskning = models.DateField(blank=True, null=True)
    hallbarhet = models.IntegerField(blank=True, null=True)
    redaktor = models.CharField(max_length=255, blank=True, null=True)
    publicerad_webb = models.DateField(blank=True, null=True)
    publicerad_app = models.DateField(blank=True, null=True)
    publicerad_spraktidning = models.DateField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_fragasvar_myisam'


class FrFragasvarTest1(models.Model):
    idfr_fragasvar = models.IntegerField()
    fraga = models.TextField()
    svar = models.TextField()
    skapad_av = models.CharField(max_length=45, blank=True, null=True)
    skapad_datum = models.DateTimeField(blank=True, null=True)
    uppdat_av = models.CharField(max_length=45, blank=True, null=True)
    uppdat_datum = models.DateTimeField(blank=True, null=True)
    senaste_granskning = models.DateField(blank=True, null=True)
    hallbarhet = models.IntegerField(blank=True, null=True)
    redaktor = models.CharField(max_length=255, blank=True, null=True)
    publicerad_webb = models.DateField(blank=True, null=True)
    publicerad_app = models.DateField(blank=True, null=True)
    publicerad_spraktidning = models.DateField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_fragasvar_test1'


class Nyckelord(models.Model):
    idnyckelord = models.AutoField(primary_key=True)
    ord_uttryck = models.CharField(max_length=255, blank=True, null=True)
    felaktig_form = models.CharField(max_length=255, blank=True, null=True)
    icke_grundform = models.CharField(max_length=255, blank=True, null=True)
    ordbildningskommentar = models.TextField(blank=True, null=True)
    bojningskommentar = models.TextField(blank=True, null=True)
    betydelsekommentar = models.TextField(blank=True, null=True)
    stavningskommentar = models.TextField(blank=True, null=True)
    ovrig_kommentar = models.TextField(blank=True, null=True)
    idgammalt = models.IntegerField(blank=True, null=True)
    skapad_av = models.CharField(max_length=45, blank=True, null=True)
    skapad_datum = models.DateTimeField(blank=True, null=True)
    uppdat_av = models.CharField(max_length=45, blank=True, null=True)
    uppdat_datum = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nyckelord'
