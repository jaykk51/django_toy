from django import forms

class ClubSearchForm(forms.Form):
    search_word = forms.CharField(label='검색어를 입력하세요 ')
