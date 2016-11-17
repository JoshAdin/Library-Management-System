from django.contrib import admin
from lipapp.models import Book, Dvd, Libuser, Libitem
import datetime


class BookInline(admin.TabularInline):
    model = Book  # This shows all fields of Book.
    fields = [('title', 'author'), 'duedate', ]   # Customizes to show only certain fields
    extra = 0


class DvdInline(admin.TabularInline):
    model = Dvd
    fields = ['title', 'maker', 'duration', 'pubyr', 'rating', 'checked_out', 'duedate', ]
    extra = 0

def listpageF(obj):
    return (obj.first_name)
listpageF.short_description = 'First Name'

def listpageL(obj):
    return ( obj.last_name)
listpageL.short_description = 'Last Name'

def listpageP(obj):
    return (obj.phone)
listpageP.short_description = 'Phone Number'


class LibuserAdmin(admin.ModelAdmin):
    fields = [('username'), ('first_name', 'last_name')]
    inlines = [BookInline, DvdInline]

def listpageT(obj):
    return (obj.title)
listpageT.short_description = 'Title'


def renew(modeladmin, request, queryset):
    for item in queryset:
        if item.checked_out == True:
            queryset.update(duedate = item.duedate + datetime.timedelta(days = 21))
renew.short_description = " Renew"


class BookAdmin(admin.ModelAdmin):
    fields = [('title', 'author', 'pubyr'), ('checked_out', 'itemtype', 'user', 'duedate'), 'category']
    list_display = (listpageT, 'overdue', 'borrower')
    # list_display = ('title', 'overdue','borrower')
    list_filter = ('duedate', 'user', 'author', 'pubyr')
    search_fields = ('title', 'author', 'pubyr',)
    actions = [renew]

    def borrower(self, obj=None):
        if obj.checked_out == True:
            return obj.user  # Returns the user who has borrowed this book
        else:
            return ''


class DvdAdmin(admin.ModelAdmin):
    fields = [('title', 'maker', 'pubyr'), ('checked_out', 'itemtype', 'duedate'), 'rating', ]
    list_display = (listpageT,'title', 'rating', 'borrower')
    list_filter = ('duedate', 'rating', 'user', 'maker', 'pubyr')
    search_fields = ('title', 'maker', 'pubyr',)
    actions = [renew]

    def borrower(self, obj=None):
        if obj.checked_out == True:
            return obj.user  # Returns the user who has borrowed this Dvd
        else:
            return ''


# Register your models here.

# admin.site.register(Book)
admin.site.register(Book, BookAdmin)

# admin.site.register(Dvd)
admin.site.register(Dvd, DvdAdmin)

# admin.site.register(Libuser)
admin.site.register(Libuser, LibuserAdmin)
