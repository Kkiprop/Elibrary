from django.contrib import admin
from . models import Customer,Books,Genre,Cart,CartItem

admin.site.register(Customer)
# admin.site.register(Books)
# admin.site.register(BorrowRecord)
admin.site.register(Genre)
admin.site.register(Cart)
# admin.site.register(CartItem)

class BooksAdmin(admin.ModelAdmin):

    list_display = ("title", "author",'genre','price','availability')

    actions = ["mark_as_available", "mark_as_unavailable"]

    def mark_as_available(self, request, queryset):
        queryset.update(availability=True)
    
    def mark_as_unavailable(self, request, queryset):
        queryset.update(availability=False)
    
    # def mark_as_completed(self, request, queryset):
    #     queryset.update(completed=True)

admin.site.register(Books, BooksAdmin)

class CartItemAdmin(admin.ModelAdmin):

    list_display = ("book", "quantity",)

    # actions = ["mark_as_confirmed", "mark_as_active", "mark_as_completed"]

    # def mark_as_confirmed(self, request, queryset):
    #     queryset.update(confirmed=True)
    
    # def mark_as_active(self, request, queryset):
    #     queryset.update(active=True)
    
    # def mark_as_completed(self, request, queryset):
    #     queryset.update(completed=True)

admin.site.register(CartItem, CartItemAdmin)


# class CustomerAdmin(admin.ModelAdmin):

#     list_display = ("User")

#     # actions = ["mark_as_confirmed", "mark_as_active", "mark_as_completed"]

#     # def mark_as_confirmed(self, request, queryset):
#     #     queryset.update(confirmed=True)
    
#     # def mark_as_active(self, request, queryset):
#     #     queryset.update(active=True)
    
#     # def mark_as_completed(self, request, queryset):
#     #     queryset.update(completed=True)

# admin.site.register(Customer, CustomerAdmin)