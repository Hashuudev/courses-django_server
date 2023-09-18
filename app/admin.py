  
from django.contrib import admin
from app.models import Courses,CoursesDetails,Playlist,Comments
from django.contrib.auth.models import User,Group

# Remove Group and User Table in Admin Panel
# admin.site.unregister(User)
# admin.site.unregister(Group)


# View DB Table in Admin Panel
admin.site.register(Courses)
admin.site.register(CoursesDetails)
admin.site.register(Playlist)
admin.site.register(Comments)
# ----------------------------------
# @admin.register(MyTableName)
# class MyTableName(admin.ModelAdmin):
#     list_display =  ['id','name']
        