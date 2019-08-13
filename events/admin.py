from khayyam import JalaliDate
from datetime import datetime
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date.widgets import AdminJalaliDateWidget

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db import models
from django.contrib.admin.widgets import AdminTimeWidget
from django import forms

from .models import Event
from utils.admin import BaseAdmin

class EventForm(forms.ModelForm):

    date = forms.DateField(initial="", widget=AdminJalaliDateWidget, validators=[], input_formats=['%Y-%m-%d'])
    time = forms.TimeField(initial="19:00", widget=AdminTimeWidget)

    class Meta:
        model = Event
        exclude = []

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        if 'date' in self.initial:
            self.initial['date'] = JalaliDate(self.initial['date'])

    def clean(self):
        value = self.data['date'] 
        if len(value) > 0:
            j_year = value.split('-')[0]
            j_month = value.split('-')[1]
            j_day = value.split('-')[2]
            self.cleaned_data['date'] = JalaliDate(year=j_year, month=j_month, day=j_day).todate()

        return self.cleaned_data

class EventAdmin(ModelAdminJalaliMixin, BaseAdmin):
    form=EventForm
    list_display = ('id', 'img', 'jalali_date', 'title', 'created')
    list_editable = ()

    def get_queryset(self, request):
        return Event.objects.order_by('-date')

    def img(self, obj):
        if obj.image:
            return mark_safe("<img width=50 height=50 src={}>".format(obj.image_url))
        else:
            return "No Image"
    
    def img_url(self, obj):
        return mark_safe("<a href={}>دانلود</>".format(obj.image_url))
    
    img.short_description = 'عکس'
    img_url.short_description = 'دانلود عکس'

admin.site.register(Event, EventAdmin)