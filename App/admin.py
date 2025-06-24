from django.contrib import admin


from App.models import home , about , why_choose , why_choose_lists, home_img_holder, Home_page_gallery, Price_card ,testimonial,blogs,ContactInquiry,gallery
# Register your models here.

admin.site.register(home)

admin.site.register(about)

admin.site.register(why_choose)

admin.site.register(why_choose_lists)

admin.site.register(home_img_holder)

admin.site.register(Home_page_gallery)

admin.site.register(Price_card)

admin.site.register(testimonial)

admin.site.register(blogs)

admin.site.register(gallery)



@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone', 'date',
        'number_of_guests', 'package',
        'event_type', 'budget_range', 'created_at'
    )
    list_filter = ('event_type', 'budget_range', 'date')
    search_fields = ('name', 'email', 'phone')
    ordering = ('-created_at',)