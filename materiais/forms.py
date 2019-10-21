from django import forms 
from .models import Post, Material

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'url',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'url': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material 
        fields = ('autor', 'titulo', 'desc' , 'paginas', 'videos', 'url')
        widgets = {
            'autor' : forms.TextInput(attrs={'class':'form-control mb-3'}),
            'titulo' : forms.TextInput(attrs={'class':'form-control mb-3'}),
            'desc' : forms.TextInput(attrs={'class':'form-control mb-3'}),
            'paginas':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'videos':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'url':forms.TextInput(attrs={'class':'form-control mb-3'}),
        }