from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=15) 

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()    

    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()
    
    def update_category(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

class Profile(models.Model):
   
    name = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    about_us = models.CharField(max_length=300, blank=True)
    profile_pic = models.ImageField(upload_to='pics/')
    phone= models.CharField(max_length=30, null=True)
    email_address= models.CharField(max_length=30, null=True)
    open_hours = models.CharField(max_length=30, null=True)
    closing_hours = models.CharField(max_length=30, null=True)
    days = models.CharField(max_length=30, null=True)
    pay_through= models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

class Image(models.Model):
    image = models.ImageField(upload_to = 'pics/')
    name = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    description =models.CharField(max_length=100, blank=True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)       

    @classmethod
    def all_pics(cls):
        pics = cls.objects.all()
        return pics 

    

    @classmethod
    def pic_categories(cls):
        pics = cls.objects.order_by('category')
        return pics 

    @classmethod
    def get_pic(cls, id):
        pic = cls.objects.get(id=id)
        return pic

    @classmethod
    def search_by_category(cls, search_input):
        images = cls.objects.filter(category__name__icontains=search_input)
        return images        

    class Meta:
        ordering = ['name']

class Project(models.Model):
    first_name = models.CharField(max_length = 30,null = True)
    last_name = models.CharField(max_length = 30,null = True)
    location = models.CharField(max_length = 30,null = True)
    road_number = models.CharField(max_length = 30,null = True)
    house_number = models.CharField(max_length = 30,null = True)
    choice = models.CharField(max_length = 30,null = True)
    name = models.CharField(max_length = 30,null = True)
    size = models.CharField(max_length = 30,null = True)
    
    

    def __str__(self):
        return self.title