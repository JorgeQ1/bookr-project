from django.contrib import admin

class BookrAdminSite(admin.AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr Administration'
    index_title = 'Bookr site admin'
    logout_template = 'reviews/logged_out.html'