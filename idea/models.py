import random
import string
from django.db import models

from utils.models import BaseModel

education_choices = [
    ('diploma', 'دیپلم'),
    ('bachelour', 'کارشناسی'),
    ('master', 'کارشناسی ارشد'),
    ('doc', 'دکتری'),
    ('post-doc', 'پسادکترا'),
]

state_choices = [
    ('submit', 'ثبت اولیه'),
    ('rejected', 'رد شده'),
    ('rejected-incomplete', 'رد شده-نقص اطلاعات'),
    ('under-review', 'ارزیابی علمی'),
    ('submit', 'ثبت اولیه'),
    ('tk', 'تکمیل کاربرگ‌ها'),
    ('dfkk', 'داوری فنی کسب و کار'),
    ('bka', 'برگزاری کارگروه ارزیابی'),
    ('tndsp', 'طرح نتایج در شورای پذیرش'),
    ('de', 'دریافت اعتبار'),
]

def code_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Idea(BaseModel):
    user = models.ForeignKey("users.Member", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    service_location = models.CharField(max_length=100, default='', blank=True, null=True)
    education_degree = models.CharField(max_length=100, default='diploma', blank=True, null=True, choices=education_choices)
    education_field = models.CharField(max_length=100, default='', blank=True, null=True)
    phone_number = models.CharField(max_length=100, default='', blank=True, null=True)
    internet_address = models.CharField(max_length=200, default='', blank=True, null=True)
    physical_address = models.TextField(default='', blank=True, null=True)

    title = models.CharField(max_length=100, default='', blank=True, null=True)
    body = models.TextField(default='', null=True, blank=True)
    category = models.CharField(max_length=100, default='', blank=True, null=True)

    state = models.CharField(max_length=100, default='submit', choices=state_choices)
    state_text = models.CharField(max_length=100, default='', blank=True, null=True)

    code = models.CharField(max_length=10, default=code_generator)
