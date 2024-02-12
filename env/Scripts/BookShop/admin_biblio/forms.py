from django import forms 

from store.models import Writer, Category, Book

first_name = {
    "required type" : "text",
    "class" : "form-control",
    "id" : "firstnameAuthor"
}

last_name = {
    "required type" : "text",
    "class" : "form-control",
    "id" : "lastnameAuthor"
}

name_ed = {
    "required type" : "text",
    "class" : "form-control",
    "id" : "nameEditor"
}

add_ed = {
    "required type" : "text",
    "class" : "form-control",
    "id" : "addressEditor"
}
code_ed = {
    "required type" : "number",
    "class" : "form-control",
    "id" : "codeEditor",
    "min" : "0",
    "max" : "99999999"
}

name_cat = {
    "required type" : "text",
    "class" : "form-control",
    "id" : "nameGenre"
}

name_book = {
    "required type" : "text",
    "class" : "form-control",
    "id" : "titleBook"
}

nb_page = {
    "type" : "number",
    "class" : "form-control",
    "id" : "countPageBook"
}

nb_stock = {
    "type" : "number",
    "class" : "form-control",
    "id" : "priceBook"
}

resume = {
    "class" : "form-control",
    "id" : "resumeBook"
}

cover = {
    "class" : "form-control",
    "id" : "coverBook"
}

class WriterForm(forms.ModelForm) :
    class Meta :
        model = Writer
        fields = ['name','firstname']
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
             last_name
            )
        self.fields['firstname'].widget.attrs.update(
            first_name
            )
        
        
class CategoryForm(forms.ModelForm) :
    class Meta :
        model = Category
        fields = ['name']
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
             name_cat
            )
        
class BooksForm(forms.ModelForm) :
    
    writer = forms.ModelChoiceField(queryset=Writer.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control', 'id' : 'authorBook'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control', 'id' : 'formatBook'}))
    #edition = forms.ModelChoiceField(queryset=Edition.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'id' : 'editorBook'}))
    
    class Meta : 
        model = Book
        fields = ['name', 'writer', 'category', 'stock', 'nb_page', 'description', 'coverpage']
        
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
             name_book
            )
        self.fields['stock'].widget.attrs.update(
            nb_stock           
        )
        self.fields['nb_page'].widget.attrs.update(
            nb_page          
        )
        self.fields['description'].widget.attrs.update(
            resume           
        )
        self.fields['coverpage'].widget.attrs.update(
            cover           
        )
        
    