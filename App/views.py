from django.shortcuts import render
from .models import home,about,why_choose,why_choose_lists,home_img_holder,Home_page_gallery,Price_card,testimonial,blogs,ContactInquiry,gallery


from django.contrib import messages
from django.shortcuts import redirect

import datetime

# Create your views here.


# homepage

def Homepage(request):
    context = {
        'Home': home.objects.first(),
        'About': about.objects.first(),
        'Why_Choose': why_choose.objects.first(),
        'Why_Choose_list': why_choose_lists.objects.all().order_by('-created_at'),
        'Home_img_holder': home_img_holder.objects.all().order_by('-created_at'),
        'Home_Gallery': Home_page_gallery.objects.all().order_by('-created_at'),
        'Pricing': Price_card.objects.first(),
        'Testimonial': testimonial.objects.all().order_by('-created_at'),
    }
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_str = request.POST.get('date')
        number_of_guests = request.POST.get('number_of_guests')
        package = request.POST.get('package')
        event_type = request.POST.get('event_type')
        budget_range = request.POST.get('budget_range')

        # Convert date string to date object
        try:
            event_date = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
        except:
            event_date = None

        ContactInquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=event_date,
            number_of_guests=number_of_guests,
            package=package,
            event_type=event_type,
            budget_range=budget_range
        )
        messages.success(request, "Thank you! Your inquiry has been submitted.")
        return redirect('thanks')
    
    return render(request, 'index.html', context)


#2. about Page
def About(request):
    context = {
        'About': about.objects.first(),
        'Why_Choose': why_choose.objects.first(),
        'Home_Gallery': Home_page_gallery.objects.all().order_by('-created_at'),
        'Testimonial': testimonial.objects.all().order_by('-created_at'),
    }
    return render(request,'about.html',context)


# 3.Our service
def Services(request):
    return render(request,'service.html')




# 4.why choose us
def Why_Choose_Us(request):
    context = {
        'Why_Choose': why_choose.objects.first(),
        'Why_Choose_list': why_choose_lists.objects.all().order_by('-created_at'),
        'Home_img_holder': home_img_holder.objects.all().order_by('-created_at'),
        'Pricing': Price_card.objects.first(),
        'Testimonial': testimonial.objects.all().order_by('-created_at'),
    }
    return render(request,'why_choose_us.html',context)



# 5.pricing
def Pricing(request):
    context = {
        'Home_img_holder': home_img_holder.objects.all().order_by('-created_at'),
        'Pricing': Price_card.objects.first(),
        'Testimonial': testimonial.objects.all().order_by('-created_at'),
    }
    return render(request,'pricing.html',context)
    


# 6.Gallery
def Gallery(request):
    Testimonial=testimonial.objects.all().order_by('-created_at')
    Gallery=gallery.objects.all()
    return render(request,'gallery.html',{'gallery':Gallery , 'Testimonial':Testimonial})


# 7.Blog
def Blog(request):
    blog = blogs.objects.all().order_by('-created_at')
    return render(request,'blog-single-fullwidth.html',{'blogs':blog})


# 8.thanks
def Thanks(request):
    return render(request,'thankyou.html')



# 9.contact page
def Contact(request):
       # contact form
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_str = request.POST.get('date')
        number_of_guests = request.POST.get('number_of_guests')
        package = request.POST.get('package')
        event_type = request.POST.get('event_type')
        budget_range = request.POST.get('budget_range')

        # Convert date string to date object
        try:
            event_date = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
        except:
            event_date = None

        ContactInquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=event_date,
            number_of_guests=number_of_guests,
            package=package,
            event_type=event_type,
            budget_range=budget_range
        )
        messages.success(request, "Thank you! Your inquiry has been submitted.")
        return redirect('thanks')
    return render(request,'contact.html')