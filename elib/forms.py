from django import forms
# from . models import BorrowRecord

# class BorrowForm(forms.ModelForm):
#     class Meta:
#         model = BorrowRecord
#         fields = ['user', 'book', 'return_date']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)