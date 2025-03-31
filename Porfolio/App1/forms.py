from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):  # Changed from Portfolio to PortfolioForm , model class and form class shouldn't be same
    class Meta:
        model = Portfolio
        fields = '__all__'