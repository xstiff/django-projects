from django import forms
from .models import Expense, SortBy



class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'date')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['date'].required = False

class SortbyForm(forms.ModelForm):
    class Meta:
        model = SortBy
        fields = ('dropdown',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dropdown'].required = False
        # self.fields['date'].required = False
