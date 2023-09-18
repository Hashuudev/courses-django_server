
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Courses(models.Model):   
    thumbnail = models.ImageField(max_length=255)
    title = models.CharField(max_length=255)
    min_description = models.CharField(max_length=255)
    

    class Meta:  
        db_table = "Courses"
    def __str__(self):
        return self.title
    

class Playlist(models.Model):   
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    thumbnail = models.ImageField(max_length=255)
    title = models.CharField(max_length=255)
    min_description = models.CharField(max_length=255)

    class Meta:  
        db_table = "Playlist"
    def __str__(self):
        return self.title
class CoursesDetails(models.Model):   
    courses = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video_link = models.CharField(max_length=1000)
    description = HTMLField()

    class Meta:  
        db_table = "CoursesDetails"
    # def __str__(self):
    #     return self.description


class Comments(models.Model):   
    commentid = models.ForeignKey(CoursesDetails, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=1000)
    timestamp = models.DateField(auto_now=True)

    class Meta:  
        db_table = "Comments"
    def __str__(self):
        return self.comments


    
        
        