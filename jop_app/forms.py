from django import forms
from .models import Jop_Applier, Jop


class Jop_ApplierForm(forms.ModelForm):

    class Meta:
        model = Jop_Applier
        fields = ("name", "email", "website", "cv", "cover_letter")


class AddJopForm(forms.ModelForm):

    class Meta:
        model = Jop
        fields = '__all__'
        # becuase this field will be assigned when save()
        exclude = ('slug', 'owner')
