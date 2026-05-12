from django.contrib import admin
from .models import Student, Document

admin.site.site_header = "Панель управления EduCRM"
admin.site.site_title = "Администрирование EduCRM"
admin.site.index_title = "Добро пожаловать в систему"


admin.site.register(Student)
admin.site.register(Document)
