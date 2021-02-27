from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Setting(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    title=models.CharField(max_length=(33))
    keywords=models.CharField(max_length=(264))
    description=models.CharField(max_length=(264))
    company=models.CharField(blank=True,max_length=(100))
    address=models.CharField(blank=True,max_length=(100))
    fax=models.CharField(blank=True,max_length=(100))
    email=models.CharField(blank=True,max_length=(100))
    smtpserver=models.CharField(blank=True,max_length=(100))
    smtpemail=models.CharField(blank=True,max_length=(100))
    smtppassword=models.CharField(blank=True,max_length=(100))
    smtpport=models.CharField(blank=True,max_length=(100))
    icon=models.ImageField(blank=True,upload_to='images/')
    facebook=models.CharField(blank=True,max_length=(100))
    instagram=models.CharField(blank=True,max_length=(100))
    twitter=models.CharField(blank=True,max_length=(100))
    youtube=models.CharField(blank=True,max_length=(100))
    aboutus=RichTextUploadingField(blank=True)
    contact=RichTextUploadingField(blank=True)
    references=RichTextUploadingField(blank=True)
    status=models.CharField(max_length=(10),choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactMessages(models.Model):
    STATUS=(
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed'),
    )
    name=models.CharField(blank=True,max_length=(33))
    email=models.EmailField(blank=True,max_length=(64))
    subject=models.CharField(blank=True,max_length=(264))
    message=models.CharField(blank=True,max_length=(264))
    status=models.CharField(max_length=(10),choices=STATUS,default='New')
    ip=models.CharField(blank=True,max_length=(264))
    note=models.CharField(blank=True,max_length=(264))
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
from django.forms import ModelForm, TextInput, Textarea
class ContactForm(ModelForm):
    class Meta:
        model=ContactMessages
        fields=['name','email','subject','message']
        widgets={
            'name':TextInput(attrs={'class':'input','placeholder':'Name'}),
            'email':TextInput(attrs={'class':'input','placeholder':'Email'}),
            'subject':TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'message':Textarea(attrs={'class':'input','placeholder':'Your Message','rows':'5'}),
        }
