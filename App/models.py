from django.db import models

# Create your models here.

class home(models.Model):
    slide_title_h2 = models.CharField(max_length=1000)
    slide_title_p = models.CharField(max_length=1000)
    zoom_img = models.ImageField(upload_to='home_page_img/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
    
class about(models.Model):
    about_img=models.ImageField(upload_to='about_img/',blank=True,null=True)
    about_h2 = models.CharField(max_length=1000)
    about_p =models.CharField(max_length=10000)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
class why_choose(models.Model):
    why_choose_img = models.ImageField(upload_to='why_choose_img/' ,blank=True,null=True)
    why_choose_h2 = models.CharField(max_length=1000)
    why_choose_p = models.CharField(max_length=10000)
    created_at=models.DateTimeField(auto_now_add=True)
    
class why_choose_lists(models.Model):
    lists =models.CharField(max_length=400)
    created_at=models.DateTimeField(auto_now_add=True)
    


class home_img_holder(models.Model):
    img_holder1 = models.ImageField(upload_to='img_holder/' ,blank=True,null=True)
    img_holder2 = models.ImageField(upload_to='img_holder/' ,blank=True,null=True)
    img_holder3 = models.ImageField(upload_to='img_holder/' ,blank=True,null=True)
    img_holder4 = models.ImageField(upload_to='img_holder/' ,blank=True,null=True)
    img_holder5 = models.ImageField(upload_to='img_holder/' ,blank=True,null=True)
    img_holder6 = models.ImageField(upload_to='img_holder/' ,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    

class Home_page_gallery(models.Model):
    home_gallery = models.ImageField(upload_to='home_page_gallery/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    


class gallery(models.Model):
    gallery_page=models.ImageField(upload_to='gallery/',blank=True,null=True)




   
    
class Price_card(models.Model):
    basic_plan = models.IntegerField()
    premium_plan = models.IntegerField()
    luxery_plan = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    



class testimonial(models.Model):
    testimonial_paragraph = models.CharField(max_length=1000)
    testimonial_img = models.ImageField(upload_to='testimonial_img/',blank=True,null=True)
    testimonial_name = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    
class blogs(models.Model):
    blog_img=models.ImageField(upload_to='blog_img/',blank=True,null=True)
    blog_author=models.CharField(max_length=100)
    blog_heading=models.CharField(max_length=400)
    blog_p1 =models.CharField(max_length=2000)
    blog_qutous = models.CharField(max_length=2000)
    blog_p2=models.CharField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
    
    
class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField() 
    number_of_guests = models.CharField(max_length=50) 
    package = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    budget_range = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event_type}"