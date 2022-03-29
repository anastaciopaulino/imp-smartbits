from attr import fields
from django import forms

from .models import Subscription


class SubscriptionCreateForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'email', '_class', 'course')
        model = Subscription
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Nome'
        self.fields['name'].required = True
        self.fields['name'].widget.attrs['class'] = 'form-control'
        
        self.fields['email'].label = 'E-mail'
        self.fields['email'].required = True
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['_class'].label = 'Classe'
        self.fields['_class'].required = True
        self.fields['_class'].widget.attrs['class'] = 'form-control'
        

        self.fields['course'].label = 'Curso'
        self.fields['course'].required = True
        self.fields['course'].widget.attrs['class'] = 'form-control'